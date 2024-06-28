import logging
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient import errors

from PySide6.QtCore import QThread, Signal, Slot

from datetime import datetime, timedelta
from .File import File
from .LineNotify import LineNotify

_LOGGER = logging.getLogger(__name__)
_OFFLINE_CHECK_TIME = 15  # min ตั้งค่าเวลากำหนดให้เป็นข้อมูล Offline


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
    post = Signal(str, bool)

    def __init__(
        self,
        service,
        line_token=None,
        tabletID=None,
        weight_settings: dict = {},
        spreadsheetId=None,
        remarksRange=None,
        rangeData=None,
        data=None,
    ):
        super().__init__()
        self.service = service
        self.line_token = line_token
        self.tabletID = tabletID
        self.weight_settings = weight_settings
        self.spreadsheetId = spreadsheetId
        self.remarksRange = remarksRange
        self.rangeData = rangeData
        self.data = data
        self.settings = None
        if self.tabletID in self.weight_settings:
            self.settings = self.weight_settings[self.tabletID]

    def weightOutOffRanges(self, weight):
        try:
            _weight = float(weight)
            IH_MIN = self.settings["meanWeightInhouseMin"]
            IH_MAX = self.settings["meanWeightInhouseMax"]
            REG_MIN = self.settings["meanWeightRegMin"]
            REG_MAX = self.settings["meanWeightRegMax"]

            if not "XXXXX" in [IH_MIN, IH_MAX, REG_MIN, REG_MAX]:
                if _weight < float(REG_MIN) or _weight > float(REG_MAX):
                    return True
                elif _weight < float(IH_MIN) or _weight > float(IH_MAX):
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
            weightOutOffRanges_msg = ""
            char_abnormal_msg = ""

            REMARKS_ALERT = False
            LINE_ALERT = False

            for timestamp in self.data:
                _data = self.data[timestamp]
                type = _data["Type"]
                characteristics = _data["Characteristics"]
                operator = _data["Operator"]
                weighing = _data["Weight"]

                current_time = datetime.now()
                _timestamp = datetime.strptime(timestamp, "%d/%m/%Y, %H:%M:%S")

                # ตรวจสอบการชั่งน้ำหนักออฟไลน์
                if (current_time - _timestamp) > timedelta(minutes=_OFFLINE_CHECK_TIME):
                    type = "OFFLINE"
                    offline_count += 1
                    if offline_count == 1:
                        offline_timestamp = timestamp

                if characteristics == "ผิดปกติ":
                    char_abnormal_msg += '\n❌พบเม็ดยาลักษณะ "ผิดปกติ"\n'

                packing_row1 = [
                    f"'{timestamp}",
                    operator,
                    type,
                    characteristics,
                    "Timestamp",
                ]

                packing_row2 = [
                    None,
                    None,
                    None,
                    None,
                    "Weight",
                ]

                weight_cache = []
                for i, weight in enumerate(weighing):
                    _weight = weight['weight']
                    weight_cache.append(float(_weight))
                    packing_row1.append(f"'{weight['timestamp']}")
                    packing_row2.append(f"'{_weight:.3f}")
                    if self.settings:
                        if self.weightOutOffRanges(_weight):
                            weightOutOffRanges_msg += f"เม็ดที่ {i+1}) {_weight:.3f} กรัม\n"

                AVG_MIN = self.settings["meanWeightAvgMin"]
                AVG_MAX = self.settings["meanWeightAvgMax"]
                average = sum(weight_cache) / len(weight_cache)
                if average < float(AVG_MIN) or average > float(AVG_MAX):
                    weightOutOffRanges_msg += f"ค่าเฉลี่ย {average:.3f} กรัม\n"

            packing_data.append(packing_row1)
            packing_data.append(packing_row2)

            try:
                response = self.service.spreadsheets().values().append(
                    spreadsheetId=self.spreadsheetId,
                    range=self.rangeData,
                    body={"majorDimension": "ROWS", "values": packing_data},
                    valueInputOption="USER_ENTERED",
                ).execute()

                # ตรวจสอบว่าการตอบกลับประสบความสำเร็จหรือไม่
                if "updates" in response:
                    _LOGGER.debug(f"Send data to server: {packing_data}")
                    self.post.emit(self.tabletID, True)

                    message = f"\n🔰 ระบบเครื่องชั่ง IPC \n"
                    message += f"🔰 เครื่องตอก {self.tabletID}\n"

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
                    if weightOutOffRanges_msg:
                        weight_header_msg = "\n❎ น้ำหนักไม่ได้อยู่ในช่วงที่กำหนด\n"
                        message += weight_header_msg
                        message += "✅ ช่วงที่กำหนด\n"
                        message += f"AVG {self.settings['meanWeightAvgMin']}-{self.settings['meanWeightAvgMax']} กรัม\n"
                        message += f"IH {self.settings['meanWeightInhouseMin']}-{self.settings['meanWeightInhouseMax']} กรัม\n"
                        message += f"REG {self.settings['meanWeightRegMin']}-{self.settings['meanWeightRegMax']} กรัม\n"
                        message += "❎ น้ำหนักที่ชั่ง\n"
                        message += weightOutOffRanges_msg
                        remarks_msg += weight_header_msg
                        remarks_msg += weightOutOffRanges_msg
                        REMARKS_ALERT = True
                        LINE_ALERT = True

                    # แจ้งเตือนเมื่อมีลักษณะเม็ดยา "ผิดปกติ"
                    if char_abnormal_msg:
                        message += char_abnormal_msg
                        remarks_msg += char_abnormal_msg
                        REMARKS_ALERT = True
                        LINE_ALERT = True
                    
                    # เพิ่มแจ้งเตือนผู้ปฏิบัติงาน
                    timestamp_msg = f"⌚ {timestamp}\n"
                    operator_msg = f"ผู้ปฏิบัติงาน {operator}\n"
                    message += timestamp_msg
                    message += operator_msg
                    remarks_msg += timestamp_msg
                    remarks_msg += operator_msg

                    # แจ้งเตือนไลน์
                    if LINE_ALERT:
                        LineNotify(self.line_token, message)

                    if REMARKS_ALERT:
                        remarks_timestamp = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
                        # ส่งบันทึกค่าน้ำหนักที่ไม่ผ่านเกณฑ์
                        remarks_msg = remarks_msg.replace("❎ ", "")
                        remarks_msg = remarks_msg.replace("✅ ", "")
                        remarks_msg = remarks_msg.replace("❌ ", "")
                        remarks_msg = remarks_msg.replace("🔰 ", "")
                        remarks_msg = remarks_msg.replace("⌚", "เวลา")
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
                    self.post.emit(self.tabletID, False)

            except Exception as e:
                _LOGGER.error(f"Send data to server: {packing_data} \n {e}")
                self.post.emit(self.tabletID, False)

        except Exception as e:
            _LOGGER.error(f"sendData_sheets: {self.data} \n {e}")
            self.post.emit(self.tabletID, False)


class Server(QThread):
    """
    คลาสสำหรับเชื่อมต่อกับ server
    โดยรับค่าจากตัวแปร token และ credentials
    และ Settings Files

    """

    print("*** Server is running...")
    get = Signal(object)
    post = Signal(str, bool)

    def __init__(
        self, token=None, credentials=None, weight_settings_file: File = None, line_tokens=None
    ):
        super().__init__()
        self.token = token
        self.credentials = credentials
        self.scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        self.WEIGHT_SETTING_FLIE = weight_settings_file
        self.line_tokens = line_tokens

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
                        self.credentials, self.scopes)
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
            self._getData_.quit()
            self._getData_.wait()
            del self._getData_
            self.get.emit(result)

    ##########################  ส่งข้อมูลไปยัง server  ##########################
    def postData(self, tabletID, sheetDataId, remarksRange, rangeData, data):
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
                    self.line_tokens,
                    tabletID,
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
            self.post.emit(tabletID, False)

    @Slot(str, bool)
    def _postData(self, tabletID, result):
        if hasattr(self, "_postData_"):
            self._postData_.quit()
            self._postData_.wait()
            del self._postData_
            self.post.emit(tabletID, result)
