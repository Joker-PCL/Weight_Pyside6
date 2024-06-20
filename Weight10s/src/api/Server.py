import logging
import pickle
import os.path
import requests
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient import errors

from PySide6.QtCore import QThread, Signal, Slot

from datetime import datetime, timedelta
from .File import File
from .LineNotify import LineNotify

_OFFLINE_CHECK_TIME = 15  # min ตั้งค่าเวลากำหนดให้เป็นข้อมูล Offline
_LOGGER = logging.getLogger(__name__)

########################## คลาสดึงข้อมูล ##########################


class GetData(QThread):
    get = Signal(object)

    def __init__(self, service, spreadsheetId=None, rangeData=None):
        super().__init__()
        self.service = service
        self.spreadsheetId = spreadsheetId
        self.rangeData = rangeData

    def run(self):
        try:
            result = (
                self.service.spreadsheets()
                .values()
                .get(spreadsheetId=self.spreadsheetId, range=self.rangeData)
                .execute()
            )

            values = result.get("values", [])
            self.get.emit(values)
        except Exception as error:
            print(error)
            self.get.emit([])


########################## คลาสส่งข้อมูล ##########################
class PostData(QThread):
    post = Signal(bool)

    def __init__(
        self,
        service,
        line_token=None,
        weight_settings: dict = {},
        spreadsheetId=None,
        remarksRange=None,
        rangeData=None,
        data=None
    ):

        super().__init__()
        self.service = service
        self.line_token = line_token
        self.spreadsheetId = spreadsheetId
        self.remarksRange = remarksRange
        self.rangeData = rangeData
        self.data = data
        self.settings = weight_settings

    def weightOutOffRanges(self, weight):
        try:
            _weight = float(weight)
            IH_MIN = self.settings['meanWeightMin']
            IH_MAX = self.settings['meanWeightMax']
            REG_MIN = self.settings['meanWeightRegMin']
            REG_MAX = self.settings['meanWeightRegMax']

            if not "XXXXX" in [IH_MIN, IH_MAX, REG_MIN, REG_MAX]:
                if _weight < REG_MIN or _weight > REG_MAX:
                    return True
                elif _weight < IH_MIN or _weight > IH_MAX:
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            return False

    def run(self):
        try:
            packing_data = []
            offline_count = 0
            offline_timestamp = None
            remarks_msg = ""
            outOffRanges_msg = ""
            char_abnormal_msg = ""

            REMARKS_ALERT = False
            LINE_ALERT = False

            for _data in self.data:
                timestamp = _data['Timestamp']
                type = _data['Type']
                weight1 = _data['Weight']['weight1']
                weight2 = _data['Weight']['weight2']
                average = None
                percentage = None
                characteristics = _data['Characteristics']
                operator = _data['Operator']
                inspactor = None
                thicknessData = _data['Thickness']

                current_time = datetime.now()
                _timestamp = datetime.strptime(timestamp, "%d/%m/%Y, %H:%M:%S")

                # ตรวจสอบการชั่งน้ำหนักออฟไลน์
                if (current_time - _timestamp) > timedelta(minutes=_OFFLINE_CHECK_TIME):
                    type = "OFFLINE"
                    offline_count += 1
                    if offline_count == 1:
                        offline_timestamp = timestamp

                if characteristics == "ผิดปกติ":
                    char_abnormal_msg += '❌พบเม็ดยาลักษณะ "ผิดปกติ"\n'
                    char_abnormal_msg += f"เวลา {timestamp}\n"
                    char_abnormal_msg += f"ผู้ปฏิบัติงาน {operator}\n"

                # ทำข้อมูลให้อยู่ในรูปแบบ array เพื่อส่งไปยัง server
                packing_cache = [
                    f"'{timestamp}",
                    type,
                    f"'{weight1:.3f}",
                    f"'{weight2:.3f}",
                    average,
                    percentage,
                    characteristics,
                    operator,
                    inspactor,
                ]

                # เพิ่มข้อมูลคสามหนา
                for i in range(1, 11):
                    thickness_value = thicknessData[f"number_{i}"]
                    if thickness_value != "-":
                        if self.settings:
                            TN_MIN = self.settings['thicknessMin']
                            TN_MAX = self.settings['thicknessMax']
                            if not "XXXXX" in [TN_MIN, TN_MAX]:
                                if float(thickness_value) < TN_MAX or float(thickness_value) > TN_MAX:
                                    outOffRanges_msg += f"เม็ดที่ {i}) {thickness_value:.3f}\n"

                        thickness_value = f"'{thickness_value}"
                                
                    packing_cache.append(thickness_value)

                packing_data.append(packing_cache)

            try:
                response = self.service.spreadsheets().values().append(
                    spreadsheetId=self.spreadsheetId,
                    range=self.rangeData,
                    body={
                        "majorDimension": "ROWS",
                        "values": packing_data
                    },
                    valueInputOption="USER_ENTERED",
                ).execute()

                # ตรวจสอบว่าการตอบกลับประสบความสำเร็จหรือไม่
                if "updates" in response:
                    _LOGGER.debug(f"Send data to server: {packing_data}")
                    self.post.emit(True)

                    message = f"\n🔰 ระบบเครื่องชั่ง 10 เม็ด \n"
                    message += f"🔰 เครื่องตอก {self.settings['tabletID']}\n"

                    if self.settings:
                        message += f"🔰 ชื่อยา {self.settings['productName']}\n"
                        message += f"🔰 Lot. {self.settings['lot']}\n"

                    # แจ้งเตือนเมื่อมีไฟล์ออฟไลน์
                    if offline_count > 0:
                        now = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
                        message += f"🔰 มีข้อมูล OFFLINE เพิ่มเข้ามาใหม่ \n"
                        message += f"❎ ขาดการเชื่อมต่อ \n"
                        message += f"{offline_timestamp}\n"
                        message += f"✅ เชื่อมต่ออีกครั้ง \n"
                        message += f"{now}\n"
                        LINE_ALERT = True

                    # แจ้งเตือนเมื่อมีน้ำหนักเม็ดยาออกนอกช่วง
                    if outOffRanges_msg:
                        message += "\n❎ น้ำหนักไม่ได้อยู่ในช่วงที่กำหนด\n"
                        message += "✅ ช่วงที่กำหนด\n"
                        message += f"IH {self.settings['meanWeightMin']}-{self.settings['meanWeightMax']}\n"
                        message += f"REG {self.settings['meanWeightRegMin']}-{self.settings['meanWeightRegMax']}\n"
                        message += "❎ น้ำหนักที่ชั่ง\n"
                        message += outOffRanges_msg
                        remarks_msg += outOffRanges_msg
                        REMARKS_ALERT = True
                        LINE_ALERT = True

                    # แจ้งเตือนเมื่อมีลักษณะเม็ดยา "ผิดปกติ"
                    if char_abnormal_msg:
                        message += char_abnormal_msg
                        remarks_msg += char_abnormal_msg
                        REMARKS_ALERT = True
                        LINE_ALERT = True

                    # แจ้งเตือนไลน์
                    if LINE_ALERT:
                        LineNotify(self.line_token, message)

                    if REMARKS_ALERT:
                        remarks_timestamp = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
                        # ส่งบันทึกค่าน้ำหนักที่ไม่ผ่านเกณฑ์
                        remarks_msg = remarks_msg.replace("❎", "")
                        remarks_msg = remarks_msg.replace("✅", "")
                        remarks_msg = remarks_msg.replace("❌", "")
                        remarks_msg = remarks_msg.replace("🔰", "")
                        response = self.service.spreadsheets().values().append(
                            spreadsheetId=self.spreadsheetId,
                            range=self.remarksRange,
                            body={
                                "majorDimension": "ROWS",
                                "values": [[remarks_timestamp, f"[แจ้งเตือนจากระบบ]\n{remarks_msg}"]]
                            },
                            valueInputOption="USER_ENTERED",
                        ).execute()

                else:
                    self.post.emit(False)

            except Exception as e:
                _LOGGER.error(f"Send data to server: {packing_data} \n {e}")
                self.post.emit(False)

        except Exception as e:
            _LOGGER.error(f"sendData_sheets: {self.data} \n {e}")
            self.post.emit(False)


class Server(QThread):
    print("*** Server is running...")
    get = Signal(object)
    post = Signal(bool)

    def __init__(self, token=None, credentials=None, weight_settings_file: File = None, line_token=None):
        super().__init__()
        self.token = token
        self.credentials = credentials
        self.scopes = ['https://www.googleapis.com/auth/spreadsheets']
        self.WEIGHT_SETTING_FLIE = weight_settings_file
        self.line_token = line_token

    def connection(self):
        try:
            creds = None
            if os.path.exists(self.token):
                with open(self.token, "rb") as token:
                    creds = pickle.load(token)
            # If there are no (valid) credentials available, let the user log in.
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        self.credentials, self.scopes
                    )
                    creds = flow.run_local_server(port=0)
                # Save the credentials for the next run
                with open(self.token, "wb") as token:
                    pickle.dump(creds, token)

            service = build("sheets", "v4", credentials=creds)
            return service

        except Exception as error:
            print(error)
            return None

    ##########################  ดึงข้อมูลจาก server  ##########################
    def getData(self, sheetDataId, settingDataRange):
        """
        อ่านข้อมูลจาก server \n
        รับค่า spreadsheetId และ range มาเป็น string เพื่อใช้ในการอ่านข้อมูลจาก server
        """
        try:
            service = self.connection()
            if not hasattr(self, "_getData_"):
                self._getData_ = GetData(
                    service, sheetDataId, settingDataRange)
                self._getData_.get.connect(self._getData)
            self._getData_.start()
        except Exception as error:
            print(error)
            self.get.emit([])

    @Slot(object)
    def _getData(self, result):
        if hasattr(self, "_getData_"):
            if self._getData_.isRunning():
                self._getData_.quit()
                self._getData_.wait()

            del self._getData_
            self.get.emit(result)

    ##########################  ส่งข้อมูลไปยัง server  ##########################
    def postData(self, sheetDataId, remarksRange, rangeData, data):
        """
        ส่งข้อมูลไปยัง server \n
        รับค่า spreadsheetId และ range มาเป็น string \n
        และ data มาเป็น object เพื่อใช้ในการส่งข้อมูลไปยัง server
        """

        try:
            service = self.connection()
            weight_settings = self.WEIGHT_SETTING_FLIE.read()
            if not hasattr(self, "_postData_"):
                self._postData_ = PostData(
                    service,
                    self.line_token,
                    weight_settings,
                    sheetDataId,
                    remarksRange,
                    rangeData,
                    data,
                )
                self._postData_.post.connect(self._postData)
            self._postData_.start()
        except Exception as error:
            print(error)
            self.post.emit(False)

    @Slot(bool)
    def _postData(self, result):
        if hasattr(self, "_postData_"):
            if self._postData_.isRunning():
                self._postData_.quit()
                self._postData_.wait()

            del self._postData_
            self.post.emit(result)
