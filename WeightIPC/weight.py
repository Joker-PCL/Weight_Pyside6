import os
import logging

from ui_weight_10inch import Ui_MainWindow
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QGroupBox,
    QHBoxLayout,
    QFrame,
    QSpacerItem,
    QSizePolicy,
    QGridLayout,
)
from PySide6.QtCore import QTimer, Signal, Slot, Qt, QSize
from PySide6.QtGui import QMovie, QFont, QPixmap
from datetime import datetime, timedelta

from src.Alert import Alert
from src.api.File import File
from src.api.Server import Server
from src.WiFi import WiFi
from src.Datetime import ShowDateTime

from src.Weighing import Weighing
from src.TabletNumber import TabletNumber
from src.TabletList import TabletList
from src.VideoPlayer import VideoPlayer

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GIF_FILE = os.path.join(BASE_DIR, "assets", "gif", "connecting.gif")
MANUAL_VIDEO_FILE = "MANUAL.mp4"
WEIGHING_DATA_FILE = os.path.join(BASE_DIR, "database", "weighingData.json")
USER_DATA_FILE = os.path.join(BASE_DIR, "database", "usersData.json")
SETTING_DATA_FILE = os.path.join(BASE_DIR, "database", "settings.json")
LOGGING_FILE = os.path.join(BASE_DIR, "files", "polipharm.log")
PARENT_DIR = os.path.dirname(BASE_DIR)
PRODUCT_IMG_FOLDER = os.path.join(PARENT_DIR, "Product")

# Logging
_LOGGER = logging.getLogger()
_LOGGER.setLevel(logging.DEBUG)
_FILE_HANDLER = logging.FileHandler(LOGGING_FILE, encoding="utf-8")
_FILE_HANDLER.setLevel(logging.DEBUG)
_FORMATTER = logging.Formatter(
    "%(asctime)s %(levelname)s: %(message)s", datefmt="%d-%m-%Y %H:%M:%S"
)
_FILE_HANDLER.setFormatter(_FORMATTER)
_LOGGER.addHandler(_FILE_HANDLER)

# millisec ระยะเวลาตรวจสอบไฟล์ข้อมูลการชั่ง
_WEIGHING_DATA_FILE_CHECK_TIME = 30000
_SCREEN_SERVER_TIMEOUT1 = 30  # sec พักหน้าจอ
_SCREEN_SERVER_TIMEOUT2 = 10  # sec พักหน้าจอ
_WEIGHING_TIMEOUT = 180  # sec กำหนดเวลาแสดงหน้าชั่งน้ำหนัก

# โหมด Label
LABEL_GET = 1
LABEL_RESET = 2


class WeightIPC(QMainWindow, Ui_MainWindow):
    def __init__(self, os_name, token, credentials, settings, balancePort):
        """
        token = google.auth.token
        credentials = google.oauth2.credentials.Credentials
        settings = ไฟล์ตั้งค่าโปรแกรม **/files/settings.json
        balancePort = พอร์ต RS232 ** Windows("COM6"), Linux("/dev/ttyUSB0")
        """
        super().__init__()

        self.token = token
        self.credentials = credentials
        self.settings = settings
        self.balancePort = balancePort

        self.setupUi(self)
        showDateTime = ShowDateTime(self.date_bar, self.time_bar)
        showDateTime.start()
        self.WiFi = WiFi(self, os_name)
        self.WiFi.show_signal_icon()

        self.current_page = self.process_page
        self.switchToPage(self.current_page)
        self.home_1.clicked.connect(
            lambda: self.switchToPage(self.current_page))
        self.home_2.clicked.connect(
            lambda: self.switchToPage(self.current_page))

        self.manual_1.clicked.connect(
            lambda: self.switchToPage(self.manual_page))
        self.manual_2.clicked.connect(
            lambda: self.switchToPage(self.manual_page))

        self.develops_1.clicked.connect(
            lambda: self.switchToPage(self.develops_page))
        self.develops_2.clicked.connect(
            lambda: self.switchToPage(self.develops_page))

        self.signout_1.clicked.connect(self.reset)
        self.signout_2.clicked.connect(self.reset)

        self.restart_program_1.clicked.connect(self.restart)
        self.restart_program_2.clicked.connect(self.restart)

        self.button_machine_confirm.clicked.connect(self.selectedTablet)

        self.weighing_start_page = self.characteristics_page
        self.start_weighing.clicked.connect(
            lambda: self.switchToPage(self.weighing_start_page))

        self.button_exit.clicked.connect(self.reset)

        # ไฟล์ข้อมูลการตั้งค่า
        self.settingsFile = File(self.settings)

        # ไฟล์ข้อมูลการชั่งน้ำหนัก
        self.WEIGHING_DATA_FILE = File(WEIGHING_DATA_FILE)

        # ไฟล์ข้อมูลรายชื่อ
        self.USER_DATA_FILE = File(USER_DATA_FILE)

        # ไฟล์ข้อมูลการตั้งค่าการชั่งน้ำหนัก
        self.WEIGHT_SETTING_FILE = File(SETTING_DATA_FILE)

        # สร้างการแจ้งเตือนส่วนหัว
        self.Title_alert = Alert(self.title)

        # สร้างการแจ้งเตือนแสกน rfid
        self.RFID_alert = Alert(self.rfid_alert)

        # สร้างการแจ้งเตือนหน้าเลือกเครื่องตอก
        self.Machine_alert = Alert(self.machine_title)

        # สร้างการแจ้งเตือนอัพเดทข้อมูลการตั้งค่า
        self.updateSettingsData_alert = Alert(self.update_settings)
        self.show_sidebar.setHidden(True)

        self.update_settings.clicked.connect(self.updateSettingsData)
        self.clear_settings.clicked.connect(self.clearSettingsData)

        # เก็บค่า label เริ่มต้นทั้งหมด
        self.initialLabel = {}
        self.initialStyle = {}
        self.findLabels(self)  # ค้นหา label ทั้งหมด

        process_gif = QMovie(GIF_FILE)
        self.process_img.setMovie(process_gif)
        process_gif.start()
        self.button_video_play.clicked.connect(self.manual_video_player)

        # ความหนาของเม็ดยา
        self.GetTabletNumber = TabletNumber(self)

        ##########################  characteristics ##########################
        self.characteristics_nomal.clicked.connect(
            lambda: self.characteristics("ปกติ"))
        self.characteristics_abnomal.clicked.connect(
            lambda: self.characteristics("ผิดปกติ"))

        ##########################  develops page   ##########################
        self.machine_page_view.clicked.connect(
            lambda: self.switchToPage(self.machine_page))
        self.weighing_settings_page_view.clicked.connect(
            lambda: self.switchToPage(self.weighing_settings_page)
        )
        self.characteristics_page_view.clicked.connect(
            lambda: self.switchToPage(self.characteristics_page)
        )
        self.weighing_page_view.clicked.connect(
            lambda: self.switchToPage(self.weighing_page))

    def manual_video_player(self):
        if not hasattr(self, "videoPlayer"):
            self.button_video_play.clicked.disconnect(self.manual_video_player)
            self.videoPlayer = VideoPlayer(
                self.manual_video, MANUAL_VIDEO_FILE)
            self.button_video_play.clicked.connect(self.videoPlayer.media.play)
            self.button_video_pause.clicked.connect(
                self.videoPlayer.media.pause)
            self.button_video_stop.clicked.connect(self.videoPlayer.media.stop)

    def findLabels(self, widget, mode=LABEL_GET):
        """
        ค้นหา QLabel ทั้งหมดที่อยู่ใน widget และดำเนินการตามโหมดที่ระบุ

        Parameters:
            widget (WidgetType): วิดเจ็ตที่ต้องการค้นหา QLabel ในนั้น
            mode (str, optional): โหมดการดำเนินการ ค่าเริ่มต้นคือ LABEL_GET.
                โหมดที่เป็นไปได้:
                    - LABEL_GET: ดึง QLabel ที่เกี่ยวข้องกับวิดเจ็ต
                    - LABEL_RESET: รีเซ็ต QLabel สำหรับวิดเจ็ต
        """
        for child in widget.children():
            try:
                if isinstance(child, QLabel):
                    if mode == LABEL_GET:
                        self.initialLabel[child.objectName()] = child.text()
                        self.initialStyle[child.objectName()
                                          ] = child.styleSheet()
                    elif mode == LABEL_RESET:
                        child.setText(self.initialLabel[child.objectName()])
                        child.setStyleSheet(
                            self.initialStyle[child.objectName()])
                else:
                    self.findLabels(child, mode)
            except Exception as e:
                pass

    def clearSettingsData(self):
        print("*** Clear settings data!")
        _LOGGER.warning(
            f"Clear settings data by {
                self.PACKING_DATA['Operator']}"
        )
        self.WEIGHT_SETTING_FILE.delete_key(self.tabletID)
        for label_name, label_text in self.initialLabel.items():
            # ค้นหา QLabel ที่มี objectName ตรงกับ label_name
            label = self.weighingSettings_Frame.findChild(QLabel, label_name)
            if label and label.objectName() != "Operator":
                label.setText(label_text)

    # เปลี่ยนหน้าต่างแสดงผล
    def switchToPage(self, page):
        self.stackedWidget.setCurrentWidget(page)

    ##########################  อ่านไฟล์ข้อมูลการตั้งค่า   ##########################
    readSettingsFileResult = Signal()

    def readSettingsFile(self):
        print("*** Read settings file...")
        settings = self.settingsFile.read()
        if settings:
            self.mainSpreadsheetId = settings["Main"]["spreadsheetID"]
            self.userDataRange = settings["Main"]["userDataRange"]
            self.TabletListRange = settings["Main"]["TabletListRange"]
            self.settingDataRange = settings["Main"]["settingDataRange"]
            QTimer.singleShot(500, lambda: self.readSettingsFileResult.emit())

    ##########################  อัพเดทข้อมูลรายชื่อ   ##########################
    updateUsersDataResult = Signal()

    def updateUsersData(self):
        print("*** Update settings data...")
        if not hasattr(self, "getUserData"):
            self.getUserData = Server(self.token, self.credentials)
            self.getUserData.get.connect(self._updateUsersData)

        self.getUserData.getData(self.mainSpreadsheetId, self.userDataRange)

    @Slot(object)
    def _updateUsersData(self, dataUsers):
        self.updateUsersDataResult.emit()

        print("*** Update users data complete")

        def format_data(data):
            rfid = data[0]
            employeeId = data[1]
            usernameTH = data[2]
            usernameEN = data[3]
            role = data[5]

            return {
                "rfid": rfid,
                "employeeId": employeeId,
                "usernameTH": usernameTH,
                "usernameEN": usernameEN,
                "role": role,
            }

        if dataUsers:
            Lists = list(map(format_data, dataUsers))
            self.USER_DATA_FILE.write(Lists)
            print("*** Updated user data file complete")
        else:
            print("*** Updated user data file not complete")

        ##########################  screen saver page   ##########################

    screenSaverResult = Signal(int)

    @Slot(int)
    def screenSaver(self):
        """พักหน้าจอ"""
        if self.screenServerTimer > 0:
            self.screenServerTimer -= 1
            self.screenSaverResult.emit(self.screenServerTimer)
        else:
            self.home_1.setChecked(True)
            self.home_2.setChecked(True)
            self.current_page = self.process_page
            self.process_label_line_4.setText("แสกนบัตรพนักงาน...")
            self.switchToPage(self.current_page)
            self.screenServercountdown_timer.stop()  # หยุดนับถอยหลังเมื่อ timeout ถึง 0

    ##########################  login page   ##########################
    loginResult = Signal()
    rfidGetKey = Signal(str)

    @Slot(str)
    def login(self, rfid_text):
        """เข้าสู่ระบบ"""

        def rfidCheck(rfid):
            """ตรวจสอบ RFID ว่ามีในระบบหรือไม่"""
            userDataLists = self.USER_DATA_FILE.read()
            for data in userDataLists:
                if data["rfid"] == rfid:
                    return {"usernameTH": data["usernameTH"], "role": data["role"]}
            return None

        print(f"*** RFID: {rfid_text}")
        self.current_page = self.home_page
        self.switchToPage(self.current_page)
        self.screenServerTimer = _SCREEN_SERVER_TIMEOUT2
        self.rfid.setText(rfid_text)
        userData = rfidCheck(rfid_text)

        if userData:
            self.screenServercountdown_timer.stop()
            self.RFID_alert.loading("กำลังโหลดข้อมูล...")
            self.signout_1.setHidden(False)
            self.signout_2.setHidden(False)
            QTimer.singleShot(1000, lambda: self.loginResult.emit())
            self.PACKING_DATA["Operator"] = userData["usernameTH"]
            self.Operator.setText(
                f"{userData['usernameTH']} ({userData['role']})")
            self.RFID_SCAN = False

            # ประทับเวลาชั่งน้ำหนัก
            now = datetime.now()  # current date and time
            self.TIMPSTAMP = now.strftime("%d/%m/%Y, %H:%M:%S")
            _LOGGER.info(f"login: RFID {rfid_text} DETAIL {str(userData)}")

            if userData["role"] == "Admin":
                self.develops_1.setHidden(False)
                self.develops_2.setHidden(False)
                self.clear_settings.setHidden(False)
                self.restart_program_1.setHidden(False)
                self.restart_program_2.setHidden(False)
        else:
            self.screenServercountdown_timer.start(1000)
            self.RFID_alert.alert("ไม่พบ RFID ในระบบ")
            QTimer.singleShot(1500, lambda: self.rfid.setText("XXXXXXXXXX"))

    def loginStart(self):
        self.RFID_SCAN = True
        self.current_page = self.home_page
        QTimer.singleShot(2000, lambda: self.switchToPage(self.current_page))

    def keyPressEvent(self, event):
        if self.RFID_SCAN:
            key = event.text()
            if key != "\r":
                self.RFID_KEY += key

            if key == "\r":
                self.rfidGetKey.emit(self.RFID_KEY)
                self.RFID_KEY = ""

    ##########################  อัพเดทข้อมูลรายชื่อเครื่องตอก   ##########################
    updateTabletListResult = Signal()

    def updateTabletList(self):
        print("*** Update tablet list...")
        settings = self.settingsFile.read()
        if settings:
            self.mainSpreadsheetId = settings["Main"]["spreadsheetID"]
            self.userDataRange = settings["Main"]["userDataRange"]
            self.TabletListRange = settings["Main"]["TabletListRange"]
            self.settingDataRange = settings["Main"]["settingDataRange"]

        if not hasattr(self, "getTabletList"):
            self.getTabletList = Server(self.token, self.credentials)
            self.getTabletList.get.connect(self._updateTabletList)

        self.getTabletList.getData(
            self.mainSpreadsheetId, self.TabletListRange)

    @Slot(object)
    def _updateTabletList(self, tabletList):
        self.updateTabletListResult.emit()
        print("*** Update tablet list complete")

        def format_data(data):
            tabletID = data[0]
            spreadsheetUrl = data[4]
            spreadsheetID = spreadsheetUrl.split("/")[5]
            return {"tabletID": tabletID, "spreadsheetID": spreadsheetID}

        settings = self.settingsFile.read()
        if settings:
            if tabletList:
                settings["TabletList"] = list(map(format_data, tabletList))
                self.settingsFile.write(settings)

            currunt_tabletList = []
            for child in self.machineScrollAreaWidget.children():
                if isinstance(child, QGroupBox):
                    currunt_tabletList.append(
                        child.title().replace("เครื่องตอก ", ""))

            settings = self.settingsFile.read()
            if not hasattr(self, "machine_gridLayout"):
                self.machine_gridLayout = QGridLayout(
                    self.machineScrollAreaWidget)
                self.machine_gridLayout.setObjectName("machine_gridLayout")
                self.machine_gridLayout.setVerticalSpacing(20)
                self.machine_gridLayout.setHorizontalSpacing(30)

            max_rows = 2
            self.tabletID = None
            for index, tabletID in enumerate(
                sorted([tablet["tabletID"]
                       for tablet in settings["TabletList"]])
            ):
                if not tabletID in currunt_tabletList:
                    row = (index) % max_rows
                    col = (index) // max_rows

                    _tablet = TabletList(self, tabletID)
                    _tablet.tabletID.connect(self._selectedTablet)
                    self.machine_gridLayout.addWidget(
                        _tablet.qbox, row, col, 1, 1)

    selectedTabletResult = Signal()

    def selectTabletStart(self):
        self.current_page = self.machine_page
        self.switchToPage(self.current_page)

    def selectedTablet(self):
        if self.tabletID:
            self.button_machine_confirm.setDisabled(True)
            self.current_tabletID.setText(f"( {self.tabletID} )")
            self.button_machine_confirm.setText("กำลังโหลดข้อมูล...")
            self.selectedTabletResult.emit()
        else:
            self.Machine_alert.alert("กรุณาเลือกเครื่องตอกจากรายการ")

    @Slot(QGroupBox)
    def _selectedTablet(self, widget: QGroupBox):
        widget_title = widget.title().replace("เครื่องตอก ", "")
        if self.tabletID != widget_title:
            self.tabletID = widget_title
            initialStyle = widget.styleSheet()
            for child in self.machineScrollAreaWidget.children():
                if isinstance(child, QGroupBox):
                    if child.title() == widget.title():
                        child.setStyleSheet(
                            """
                                border: solid;
                                border-width: 2px;
                                border-color: rgb(255, 150, 0);
                                border-radius: 8px;
                                background-color: #f4f56e; 
                                color:  #58b3d3;
                            """
                        )
                    else:
                        child.setStyleSheet(initialStyle)

    ##########################   อัพเดทข้อมูลการตั้งค่า   ##########################
    updateSettingsDataResult = Signal()

    # ค้นหา SpreadsheetID จาก tabletID
    def findSpreadsheetID(self, tabletID):
        settings = self.settingsFile.read()
        if settings:
            self.TabletList = settings["TabletList"]

            for tablet in self.TabletList:
                if tablet["tabletID"] == tabletID:
                    return tablet["spreadsheetID"]
            return None
        else:
            return None

    def updateSettingsData(self):
        print("*** Update settings data...")
        settingsFile = self.settingsFile.read()
        if settingsFile:
            sheetDataId = self.findSpreadsheetID(self.tabletID)
            if not hasattr(self, "getSettingsData"):
                self.getSettingsData = Server(self.token, self.credentials)
                self.getSettingsData.get.connect(self._updateSettingsData)

            self.getSettingsData.getData(sheetDataId, self.settingDataRange)

    def find_image(self, base_path, extensions):
        for ext in extensions:
            file_path = f"{base_path}.{ext}"
            if os.path.exists(file_path):
                return file_path
        return None

    @Slot(object)
    def _updateSettingsData(self, result):
        self.updateSettingsDataResult.emit()
        self.current_page = self.weighing_settings_page
        self.switchToPage(self.current_page)
        self.button_machine_confirm.setDisabled(False)
        self.button_machine_confirm.setText("ยืนยัน")

        if result:
            settings = {
                "productName": result[0][0],  # ชื่อยา
                "lot": result[1][0],  # เลขที่ผลิต
                "balanceID": result[2][0],  # เครื่องชั่ง
                "tabletID": result[3][0],  # เครื่องตอก
                "numberPunches": result[4][0],  # จำนวนสาก
                "numberTablets": result[5][0],  # จำนวนเม็ดที่ต้องชั่ง
                "meanWeight": result[6][0],  # น้ำหนักตอก/เม็ด (g)
                # % ช่วงน้ำหนักเบี่ยงเบนที่ยอมรับ
                "percentWeightVariation": result[7][0],
                # ช่วงน้ำหนักเฉลี่ยที่ยอมรับ (Min.)
                "meanWeightAvgMin": result[8][0],
                # ช่วงน้ำหนักเฉลี่ยที่ยอมรับ (Max.)
                "meanWeightAvgMax": result[9][0],
                # ช่วงน้ำหนักเบี่ยงเบนที่ยอมรับ(Min.)
                "meanWeightInhouseMin": result[10][0],
                # ช่วงน้ำหนักเบี่ยงเบนที่ยอมรับ(Max.)
                "meanWeightInhouseMax": result[11][0],
                # ช่วงน้ำหนักเบี่ยงเบนที่ยอมรับ(Min.)
                "meanWeightRegMin": result[12][0],
                # ช่วงน้ำหนักเบี่ยงเบนที่ยอมรับ(Max.)
                "meanWeightRegMax": result[13][0],
                "meanWeightRegMax": result[14][0],  # ตั้งค่าน้ำหนักโดย
                "prepared": result[15][0],  # ตรวจสอบการตั้งค่าโดย
                "approved": result[16][0],  # ตรวจสอบการตั้งค่าโดย
            }

            self.WEIGHT_SETTING_FILE.update(self.tabletID, settings)

        else:
            self.updateSettingsData_alert.alert("เกิดข้อผิดพลาดในการอัพเดท!")

        dataSettings = self.WEIGHT_SETTING_FILE.read()
        if dataSettings:
            _dataSettings = dataSettings[self.tabletID]
            productName = _dataSettings["productName"]  # ชื่อยา
            lot = _dataSettings["lot"]  # เลขที่ผลิต
            balanceID = _dataSettings["balanceID"]  # เครื่องชั่ง
            tabletID = _dataSettings["tabletID"]  # เครื่องตอก
            numberPunches = _dataSettings["numberPunches"]  # น้ำหนักตามทฤษฎี
            # เปอร์เซ็นเบี่ยงเบน
            numberTablets = _dataSettings["numberTablets"]
            # ช่วงน้ำหนัก 10 เม็ด(Min.)
            meanWeight = _dataSettings["meanWeight"]
            percentWeightVariation = _dataSettings[
                "percentWeightVariation"
            ]  # ช่วงน้ำหนัก 10 เม็ด(Max.)
            # ช่วงน้ำหนัก 10 เม็ด(Min.)
            meanWeightAvgMin = _dataSettings["meanWeightAvgMin"]
            # ช่วงน้ำหนัก 10 เม็ด(Max.)
            meanWeightAvgMax = _dataSettings["meanWeightAvgMax"]
            # ช่วงน้ำหนักเบี่ยงเบนที่กฎหมายยอมรับ (Min.)
            meanWeightInhouseMin = _dataSettings["meanWeightInhouseMin"]
            # ช่วงน้ำหนักเบี่ยงเบนที่กฎหมายยอมรับ (Max.)
            meanWeightInhouseMax = _dataSettings["meanWeightInhouseMax"]
            # ค่าความหนา(Min.)
            meanWeightRegMin = _dataSettings["meanWeightRegMin"]
            # ค่าความหนา(Max.)
            meanWeightRegMax = _dataSettings["meanWeightRegMax"]
            prepared = _dataSettings["prepared"]  # ตั้งค่าน้ำหนักโดย
            approved = _dataSettings["approved"]  # ตรวจสอบการตั้งค่าโดย

            self.Productname.setText(productName)
            self.Lot.setText(lot)
            self.BalanceID.setText(balanceID)
            self.TabletID.setText(tabletID)
            self.numberPunches.setText(f"{numberPunches} สาก")
            self.numberTablets.setText(f"{numberTablets} เม็ด")
            self.meanWeight.setText(f"{meanWeight} กรัม")
            self.WeightIpcPer.setText(percentWeightVariation)
            self.meanWeightAvg.setText(
                f"{meanWeightAvgMin} - {meanWeightAvgMax} กรัม")
            self.MeanWeightInhouse.setText(
                f"{meanWeightInhouseMin} - {meanWeightInhouseMax} กรัม")
            self.MeanWeightREG.setText(
                f"{meanWeightRegMin} - {meanWeightRegMax} กรัม")

            # หากไม่มีข้อมูลการตั้งค่า
            if numberTablets == "XXXXX":
                self.weighing_start_page = self.numberTablets_page
            else:
                self.NUMBER_TABLET = numberTablets
                self.weighing_start_page = self.characteristics_page

            try:
                front_img_base = os.path.join(
                    PRODUCT_IMG_FOLDER, productName.upper(), "UPPER")
                front_img = self.find_image(front_img_base, ["jpg", "png"])

                behind_img_base = os.path.join(
                    PRODUCT_IMG_FOLDER, productName.upper(), "LOWER")
                behind_img = self.find_image(behind_img_base, ["jpg", "png"])

                # Check if files exist
                if os.path.exists(front_img) and os.path.exists(behind_img):
                    self.tablet_front_img.setPixmap(QPixmap(front_img))
                    self.tablet_behind_img.setPixmap(QPixmap(behind_img))
                else:
                    raise FileNotFoundError(
                        "One or both image files not found")

            except FileNotFoundError:
                print("*** Images file not found")
                picture_default = os.path.join(
                    BASE_DIR, "assets", "icon", "picture_default.png")
                self.tablet_front_img.setPixmap(QPixmap(picture_default))
                self.tablet_behind_img.setPixmap(QPixmap(picture_default))
            except Exception as e:
                # Handle other exceptions
                print("*** An error occurred:", e)

        print("*** Update settings data complete!")

    ##########################  ป้อนจำนวนเม็ดยาที่ต้องชั่ง   ##########################
    getNumberTabletsResult = Signal(int)

    @Slot(int)
    def getNumberTablets(self, numberTablets):
        print(f"*** NumberTablets: {numberTablets}\n")
        self.NUMBER_TABLET = numberTablets
        QTimer.singleShot(
            500, lambda: self.getNumberTabletsResult.emit(numberTablets))

    def getNumberTabletsStart(self):
        print("*** Get number tablets...")
        self.current_page = self.numberTablets_page
        self.switchToPage(self.current_page)
        self.GetTabletNumber.current_value = ""
        if not hasattr(self, "GetNumberTablets_called"):
            self.GetThickness_called = False

        if not self.GetThickness_called:
            self.GetThickness_called = True
            self.GetTabletNumber.get.connect(self.getNumberTablets)

    ##########################  characteristics page   ##########################
    characteristicsResult = Signal()

    # เลือกลักษณะเม็ดยา
    def characteristics(self, selected):
        print(f"** Characteristics: {selected}")
        self.PACKING_DATA["Characteristics"] = selected
        QTimer.singleShot(1000, lambda: self.characteristicsResult.emit())

    def characteristicsStart(self):
        print("*** Get characteristics data...")
        self.current_page = self.characteristics_page
        self.switchToPage(self.current_page)

    ##########################  weighing page   ##########################
    getWeighingDataResult = Signal()

    def weightOutOffRanges(
        self, settings: dict, widget: QLabel, weight: float, color: str = "#FFFFFF", unit: str = ""
    ):
        """
        ตรวจสอบว่าช่วงน้ำหนักอยู่ในช่วงที่กฎหมายยอมรับหรือไม่ \n
        :param widget: QLabel -> widget \n
        :param weight: float -> ค่าน้ำหนัก \n
        :param color: str -> สีตัวอักษร \n
        :param unit: str -> หน่วย
        """
        IR_STYLE = f"border: none; color: {color};"
        OFR_IH_STYLE = f"border: none; color: #FB0B97;"
        OFR_REG_STYLE = f"border: none; color: #FA0B0E;"
        widget.setText(f"{weight:.3f}{unit}")

        if settings:
            IH_MIN = settings["meanWeightInhouseMin"]
            IH_MAX = settings["meanWeightInhouseMax"]
            REG_MIN = settings["meanWeightRegMin"]
            REG_MAX = settings["meanWeightRegMax"]

            if not "XXXXX" in [IH_MIN, IH_MAX, REG_MIN, REG_MAX]:
                if weight < REG_MIN and weight > REG_MAX:
                    widget.setStyleSheet(OFR_REG_STYLE)
                elif weight < IH_MIN and weight > IH_MAX:
                    widget.setStyleSheet(OFR_IH_STYLE)
                else:
                    widget.setStyleSheet(IR_STYLE)
            else:
                widget.setStyleSheet(IR_STYLE)

    def createWeighingWidget(self, settings:dict, number: int, weight: float):
        font = QFont()
        font.setFamilies(["Kanit"])
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)

        weighing_group = QGroupBox()
        weighing_group.setObjectName(f"weighing_group_{number}")
        weighing_group.setMinimumSize(QSize(0, 0))
        weighing_group.setMaximumSize(QSize(180, 50))
        weighing_group.setStyleSheet("color: rgb(255, 255, 255);")
        horizontalLayout_1 = QHBoxLayout(weighing_group)
        horizontalLayout_1.setSpacing(0)
        horizontalLayout_1.setObjectName(f"horizontalLayout_{number}")
        horizontalLayout_1.setContentsMargins(0, 0, 0, 0)

        weighing_title = QLabel(weighing_group)
        weighing_title.setObjectName(f"weighing_title_{number}")
        weighing_title.setMinimumSize(QSize(40, 0))
        weighing_title.setMaximumSize(QSize(16777215, 16777215))
        weighing_title.setText(f"เม็ดที่ {number}")
        weighing_title.setFont(font)
        weighing_title.setStyleSheet(
            "background-color: #0059fe;\n"
            "border-top-left-radius: 8px;\n"
            "border-bottom-left-radius: 8px;"
        )
        weighing_title.setAlignment(Qt.AlignCenter)

        horizontalLayout_1.addWidget(weighing_title)

        weighing_frame = QFrame(weighing_group)
        weighing_frame.setObjectName(f"weighing_frame_{number}")
        weighing_frame.setFont(font)
        weighing_frame.setStyleSheet(
            "border: solid;\n"
            "border-width: 1px;\n"
            "border-color: rgb(121, 121, 121);\n"
            "border-top-right-radius: 8px;\n"
            "border-bottom-right-radius: 8px;"
        )
        weighing_frame.setFrameShape(QFrame.StyledPanel)
        weighing_frame.setFrameShadow(QFrame.Raised)
        horizontalLayout_2 = QHBoxLayout(weighing_frame)
        horizontalLayout_2.setObjectName(f"horizontalLayout_0{number}")
        weighing = QLabel(weighing_frame)
        weighing.setObjectName(f"weighing_{number}")
        self.weightOutOffRanges(settings, weighing, weight, color="#1A1A1A")
        weighing.setFont(font)
        weighing.setAlignment(Qt.AlignCenter)

        horizontalLayout_2.addWidget(weighing)
        horizontalLayout_1.addWidget(weighing_frame)
        return weighing_group

    @Slot(str, float)
    def getWeighingData(self, timestamp, weight):
        """ดึงข้อมูลการชั่งน้ำหนัก"""

        print(f"*** WeighingData: {timestamp}, {weight}")
        self.signout_1.setHidden(True)
        self.signout_2.setHidden(True)
        self.restart_program_1.setHidden(True)
        self.restart_program_2.setHidden(True)

        self.WEIGHING_CACHE.append(weight)
        self.PACKING_DATA["Weight"].append(
            {
                "timestamp": timestamp,
                "weight": weight,
            }
        )

        dataSettings = self.WEIGHT_SETTING_FILE.read()
        settings = {}
        if dataSettings:
            settings = dataSettings[self.tabletID]

        # ค่าน้ำหนัก, ตรวจสอบค่าเฉลี่ยว่าออกนอกช่วงหรือไม่
        count = len(self.PACKING_DATA["Weight"])
        self.weightOutOffRanges(settings, self.current_weight, weight, unit=" กรัม")
        self.weightOutOffRanges(settings, self.weighing_min, min(self.WEIGHING_CACHE))
        self.weightOutOffRanges(settings, self.weighing_max, max(self.WEIGHING_CACHE))

        # ค่าเฉลี่ย
        _average_weight = sum(self.WEIGHING_CACHE)/count
        self.weighing_average.setText(f"{_average_weight:.3f}")

        # ตรวจสอบค่าเฉลี่ยว่าออกนอกช่วงหรือไม่
        if not "XXXXX" in [settings["meanWeightAvgMin"], settings["meanWeightAvgMax"]]:
            if _average_weight < settings["meanWeightAvgMin"] or _average_weight > settings["meanWeight"]:
                self.weighing_average.setStyleSheet("color: #FA0B0E;")
            else:
                self.weighing_average.setStyleSheet("color: #FFFFFF;")

        print(f"*** WeighingData: No.{count}, {weight}")

        # สร้าง widget แสดงน้ำหนักยา
        max_columns = 5
        max_length = self.NUMBER_TABLET
        row = (count - 1) // max_columns
        col = (count - 1) % max_columns

        if not hasattr(self, "weighing_gridLayout"):
            self.weighing_gridLayout = QGridLayout(self.weighing_widget_group)
            self.weighing_gridLayout.setObjectName("weighing_gridLayout")
            self.weighing_gridLayout.setVerticalSpacing(15)
            self.verticalSpacer = QSpacerItem(
                20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
            )

        self.weighing_gridLayout.addItem(
            self.verticalSpacer, (max_length) // max_columns, 0, 1, 1)
        weighing_widget = self.createWeighingWidget(settings, count, weight)
        self.weighing_gridLayout.addWidget(weighing_widget, row, col, 1, 1)
        self.timeout.setText(f"{max_length-count}")

        if count == max_length:
            print(f"*** WeighingData: Success")
            self.PACKING_DATA["Type"] = "ONLINE"
            self.MAIN_PACKING_DATA[self.TIMPSTAMP] = self.PACKING_DATA
            self.WEIGHING_DATA_FILE.update(
                self.tabletID, self.MAIN_PACKING_DATA)
            self.sendDataToServer_timer.start(100)  # ส่งข้อมูล
            QTimer.singleShot(1500, lambda: self.getWeighingDataResult.emit())

    def weighingStart(self):
        """เริ่มฟังชั่นดึงข้อมูลการชั่งน้ำหนัก"""

        print("*** Get weighing data...")
        self.PACKING_DATA["Weight"] = []
        self.WEIGHING_CACHE = []
        self.current_page = self.weighing_page
        self.switchToPage(self.current_page)
        # if not hasattr(self, "Weighing_called"):
        #     self.Weighing_called = False

        # if not self.Weighing_called:
        # self.Weighing_called = True

        self.timeout_title.setText("จำนวนเม็ดที่ต้องชั่ง")
        self.timeout.setText(f"{self.NUMBER_TABLET}")

        self.Weighing = Weighing(
            self.balancePort, number_tablets=self.NUMBER_TABLET)
        self.Weighing.get.connect(self.getWeighingData)

        self.Weighing.start()

    ##########################  countdown   ##########################
    countdownResult = Signal(int)
    successResult = Signal()

    @Slot(int)
    def updateCountdown(self):
        if self.summary_timeout >= 0:
            self.timeout.setText(f"{self.summary_timeout} s.")
            self.countdownResult.emit(self.summary_timeout)
            self.summary_timeout -= 1
        else:
            self.successResult.emit()
            self.countdown_timer.stop()  # หยุดนับถอยหลังเมื่อ timeout ถึง 0
            self.run()

    def countdownStart(self):
        self.button_exit.setHidden(False)
        self.timeout_title.setText("นับเวลาถอยหลัง")
        self.timeout.setText(f"{_WEIGHING_TIMEOUT}")
        self.summary_timeout = _WEIGHING_TIMEOUT
        if not hasattr(self, "countdown_timer"):
            self.countdown_timer = QTimer(self)
            self.countdown_timer.timeout.connect(self.updateCountdown)
        self.countdown_timer.start(1000)

    ##########################  Send data to server   ##########################
    sendDataToServerResult = Signal(bool)

    def sendDataToServer(self):
        try:
            self.file_count = 0
            weighing_data = self.WEIGHING_DATA_FILE.read()  # อ่านไฟล์ข้อมูลการชั่งน้ำหนัก

            if weighing_data:
                # อ่านข้อมูลตามหมายเลขเครื่องตอก
                for _TABLET in weighing_data:
                    _TABLET_WEIGHING_DATA = weighing_data[_TABLET]
                    self.file_count += len(_TABLET_WEIGHING_DATA)

                    # อัพเดทข้อมูลสถานะ ONLINE, OFFLINE
                    self.WEIGHING_DATA_FILE.update(
                        _TABLET, _TABLET_WEIGHING_DATA)
                    self.Title_alert.alert_always(f"กำลังส่งข้อมูล...", False)
                    self.sendDataToServer_timer.stop()

                    # อ่านข้อมูลจากไฟล์ตั้งค่า
                    settings = self.settingsFile.read()
                    if settings:
                        sheetDataId = self.findSpreadsheetID(_TABLET)
                        remarksRange = settings["Main"]["remarksRange"]
                        rangeData = settings["Main"]["weighingDataRange"]
                        line_tokens = settings["Main"]["line_token"]
                        if not hasattr(self, "postDataToServer"):
                            self.postDataToServer = Server(
                                self.token, self.credentials, self.WEIGHT_SETTING_FILE, line_tokens
                            )
                            self.postDataToServer.post.connect(
                                self._sendDataToServer)

                        print("*** Send data to server...")
                        self.postDataToServer.postData(
                            _TABLET, sheetDataId, remarksRange, rangeData, _TABLET_WEIGHING_DATA
                        )
            else:
                self.sendDataToServer_timer.setInterval(
                    _WEIGHING_DATA_FILE_CHECK_TIME)
                self.Title_alert.stop()
        except FileNotFoundError:
            print("*** File data not found!")
            self.Title_alert.stop()
            pass

    @Slot(str, bool)
    def _sendDataToServer(self, tabletID, result=False):
        if result:
            QTimer.singleShot(1000, lambda: self.Title_alert.success(
                "ดำเนินการเรียบร้อยแล้ว", 3000))
            self.WEIGHING_DATA_FILE.delete_key(tabletID)
            self.sendDataToServer_timer.start(100)
        else:
            QTimer.singleShot(2000, lambda: self.Title_alert.alert_always(
                "เกิดข้อผิดพลาดในการส่งข้อมูล"))
            if self.file_count > 0:
                QTimer.singleShot(
                    5000,
                    lambda: self.Title_alert.alert_always(
                        f"มีไฟล์ค้างอยู่ในเครื่อง {self.file_count} ไฟล์"),
                )
            self.sendDataToServer_timer.start(_WEIGHING_DATA_FILE_CHECK_TIME)

    ##########################  Weight IPC' ##########################
    def reset(self):
        # เคลียร์ widget รายการเครื่องตอก
        if hasattr(self, "machine_gridLayout"):
            while self.machine_gridLayout.count():
                item = self.machine_gridLayout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.machine_gridLayout.removeItem(item)

        # เคลียร์ widget ข้อมูลการชั่งน้ำหนักยา
        if hasattr(self, "weighing_gridLayout"):
            while self.weighing_gridLayout.count():
                item = self.weighing_gridLayout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.weighing_gridLayout.removeItem(item)

        if hasattr(self, "countdown_timer"):
            self.countdown_timer.stop()

        self.findLabels(self, mode=LABEL_RESET)
        self.run()

    def restart(self):
        """รีสตาร์ทโปรแกรม"""
        QApplication.quit()

    def exit(self):
        """ปิดโปรแกรม"""
        QApplication.quit()

    def run(self):
        print("*** Weight IPC is running...")
        # Valiable parameters
        self.MAIN_PACKING_DATA = {}
        self.PACKING_DATA = {}
        self.SEND_DATA_TO_SERVER_STATUS = True
        self.RFID_SCAN = False
        self.RFID_KEY = ""

        # พักหน้าจอ
        self.screenServerTimer = _SCREEN_SERVER_TIMEOUT1
        if not hasattr(self, "screenServercountdown_timer"):
            self.screenServercountdown_timer = QTimer(self)
            self.screenServercountdown_timer.timeout.connect(self.screenSaver)
        self.screenServercountdown_timer.start(1000)

        # ส่งข้อมูลไปบันทึกยัง sever
        if not hasattr(self, "sendDataToServer_timer"):
            self.sendDataToServer_timer = QTimer(self)
            self.sendDataToServer_timer.timeout.connect(self.sendDataToServer)
        self.sendDataToServer_timer.start(100)

        # โหลดข้อมูลหน้าแรก
        self.current_page = self.process_page
        self.switchToPage(self.current_page)
        self.process_label_line_4.setText("กำลังโหลด...")
        self.home_1.setChecked(True)
        self.home_2.setChecked(True)
        self.develops_1.setHidden(True)
        self.develops_2.setHidden(True)
        self.signout_1.setHidden(True)
        self.signout_2.setHidden(True)
        self.clear_settings.setHidden(True)
        self.restart_program_1.setHidden(False)
        self.restart_program_2.setHidden(False)
        self.button_exit.setHidden(True)

        # อัพเดทข้อมูล
        self.readSettingsFile()
        if not hasattr(self, "FirstConnect"):
            self.FirstConnect = True

        if self.FirstConnect:
            self.FirstConnect = False
            self.readSettingsFileResult.connect(self.updateUsersData)
            self.updateUsersDataResult.connect(self.loginStart)
            self.rfidGetKey.connect(self.login)
            self.loginResult.connect(self.updateTabletList)
            self.updateTabletListResult.connect(self.selectTabletStart)
            self.selectedTabletResult.connect(self.updateSettingsData)
            self.updateSettingsDataResult.connect(self.characteristicsStart)
            self.updateSettingsDataResult.connect(self.getNumberTabletsStart)
            self.getNumberTabletsResult.connect(self.characteristicsStart)
            self.characteristicsResult.connect(self.weighingStart)
            self.getWeighingDataResult.connect(self.countdownStart)
            self.successResult.connect(self.reset)
