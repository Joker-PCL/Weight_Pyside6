import os
import json
import logging

from ui_weight_10inch import Ui_MainWindow
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QGroupBox,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QSpacerItem,
    QSizePolicy,
    QGridLayout,
)
from PySide6.QtCore import QCoreApplication, QTimer, Signal, Slot, Qt, QSize
from PySide6.QtGui import QMovie, QFont, QCursor, QIcon, QPixmap
from datetime import datetime, timedelta

from src.Alert import Alert
from src.api.File import File
from src.api.Server import Server
from src.api.RFID import Rfid

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
PRODUCT_IMG_FOLDER = os.path.join(PARENT_DIR, "product")

_LOGGER = logging.getLogger()
_LOGGER.setLevel(logging.DEBUG)
_FILE_HANDLER = logging.FileHandler(LOGGING_FILE, encoding="utf-8")
_FILE_HANDLER.setLevel(logging.DEBUG)
_FORMATTER = logging.Formatter(
    "%(asctime)s %(levelname)s: %(message)s", datefmt="%d-%m-%Y %H:%M:%S"
)
_FILE_HANDLER.setFormatter(_FORMATTER)
_LOGGER.addHandler(_FILE_HANDLER)

_OFFLINE_CHECK_TIME = 15  # min ตั้งค่าเวลากำหนดให้เป็นข้อมูล Offline
_WEIGHING_DATA_FILE_CHECK_TIME = 5000  # millisec ระยะเวลาตรวจสอบไฟล์ข้อมูลการชั่ง
_SCREEN_SERVER_TIMEOUT1 = 30  # sec พักหน้าจอ
_SCREEN_SERVER_TIMEOUT2 = 10  # sec พักหน้าจอ
_SAMMARY_TIMEOUT = 180  # sec กำหนดเวลาแสดงหน้า summary


class WeightIPC(QMainWindow, Ui_MainWindow):
    def __init__(self, token, credentials, settings, balancePort):
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
        self.current_page = self.process_page
        self.switchToPage(self.current_page)
        self.home_1.clicked.connect(lambda: self.switchToPage(self.current_page))
        self.home_2.clicked.connect(lambda: self.switchToPage(self.current_page))

        self.manual_1.clicked.connect(lambda: self.switchToPage(self.manual_page))
        self.manual_2.clicked.connect(lambda: self.switchToPage(self.manual_page))

        self.develops_1.clicked.connect(lambda: self.switchToPage(self.develops_page))
        self.develops_2.clicked.connect(lambda: self.switchToPage(self.develops_page))

        self.button_machine_confirm.clicked.connect(self.selectedTablet)

        self.weighing_start_page = self.characteristics_page
        self.start_weighing.clicked.connect(lambda: self.switchToPage(self.weighing_start_page))
        
        # ไฟล์ข้อมูลการตั้งค่า
        self.settingsFile = File(self.settings)

        # ไฟล์ข้อมูลการชั่งน้ำหนัก
        self.WEIGHING_DATA_FILE = File(WEIGHING_DATA_FILE)

        # ไฟล์ข้อมูลรายชื่อ
        self.USER_DATA_FILE = File(USER_DATA_FILE)

        # ไฟล์ข้อมูลการตั้งค่าการชั่งน้ำหนัก
        self.SETTING_DATA_FILE = File(SETTING_DATA_FILE)

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
        self.findLabels(self)   # ค้นหา label ทั้งหมด

        movie = QMovie(GIF_FILE)
        self.process_img.setMovie(movie)
        movie.start()

        # ความหนาของเม็ดยา
        self.GetTabletNumber = TabletNumber(self)

        ##########################  characteristics ##########################
        self.characteristics_nomal.clicked.connect(lambda: self.characteristics("ปกติ"))
        self.characteristics_abnomal.clicked.connect(
            lambda: self.characteristics("ผิดปกติ")
        )

        ##########################  develops page   ##########################
        self.machine_page_view.clicked.connect(
            lambda: self.switchToPage(self.machine_page)
        )
        self.weighing_settings_page_view.clicked.connect(
            lambda: self.switchToPage(self.weighing_settings_page)
        )
        self.characteristics_page_view.clicked.connect(
            lambda: self.switchToPage(self.characteristics_page)
        )
        self.weighing_page_view.clicked.connect(
            lambda: self.switchToPage(self.weighing_page)
        )

    def manual_video_player(self):
        if not hasattr(self, "videoPlayer"):
            self.button_video_play.clicked.disconnect(self.manual_video_player)
            self.videoPlayer = VideoPlayer(self.manual_video, MANUAL_VIDEO_FILE)
            self.button_video_play.clicked.connect(self.videoPlayer.media.play)
            self.button_video_pause.clicked.connect(self.videoPlayer.media.pause)
            self.button_video_stop.clicked.connect(self.videoPlayer.media.stop)

    def findLabels(self, widget, mode: str = "get"):
        """
        ค้นหา QLabel ทั้งหมดที่อยู่ใน widget และดำเนินการตามโหมดที่ระบุ

        Parameters:
            widget (WidgetType): วิดเจ็ตที่ต้องการค้นหา QLabel ในนั้น
            mode (str, optional): โหมดการดำเนินการ ค่าเริ่มต้นคือ "get".
                โหมดที่เป็นไปได้:
                    - "get": ดึง QLabel ที่เกี่ยวข้องกับวิดเจ็ต
                    - "reset": รีเซ็ต QLabel สำหรับวิดเจ็ต
        """
        for child in widget.children():
            if isinstance(child, QLabel):
                if mode == "get":
                    self.initialLabel[child.objectName()] = child.text()
                    self.initialStyle[child.objectName()] = child.styleSheet()
                elif mode == "reset":
                    child.setText(self.initialLabel[child.objectName()])
                    child.setStyleSheet(self.initialStyle[child.objectName()])
            else:
                self.findLabels(child, mode)

    def clearSettingsData(self):
        print("Clear settings data!")
        _LOGGER.warning(f"Clear settings data by {self.PACKING_DATA['Operator']}")
        self.SETTING_DATA_FILE.delete_key(self.tabletID)
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
            print("Updated user data file complete")
        else:
            print("Updated user data file not complete")

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

        print(f"RFID: {rfid_text}")
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
            self.Operator.setText(f"{userData['usernameTH']} ({userData['role']})")
            self.RFID_SCAN = False

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

    def createWeighingWidget(self):
        gridLayout = QGridLayout(self.summary_weighing_widget)
        gridLayout.setObjectName("weighing_gridLayout")
        gridLayout.setVerticalSpacing(15)
        font = QFont()
        font.setFamilies(["Kanit"])
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)

        max_columns = 5
        max_length = 50
        for i in range(0, max_length):
            number = i + 1
            row = (i) // max_columns
            col = (i) % max_columns

            weight_summary_group = QGroupBox(self.summary_weighing_widget)
            weight_summary_group.setObjectName(f"weighing_group_{number}")
            weight_summary_group.setMinimumSize(QSize(0, 0))
            weight_summary_group.setMaximumSize(QSize(180, 50))
            weight_summary_group.setStyleSheet("color: rgb(255, 255, 255);")
            horizontalLayout_1 = QHBoxLayout(weight_summary_group)
            horizontalLayout_1.setSpacing(0)
            horizontalLayout_1.setObjectName(f"horizontalLayout_{number}")
            horizontalLayout_1.setContentsMargins(0, 0, 0, 0)

            weight_summary_title = QLabel(weight_summary_group)
            weight_summary_title.setObjectName(f"weighing_title_{number}")
            weight_summary_title.setMinimumSize(QSize(40, 0))
            weight_summary_title.setMaximumSize(QSize(16777215, 16777215))
            weight_summary_title.setText(f"เม็ดที่ {number}")
            weight_summary_title.setFont(font)
            weight_summary_title.setStyleSheet(
                "background-color: #0059fe;\n"
                "border-top-left-radius: 8px;\n"
                "border-bottom-left-radius: 8px;"
            )
            weight_summary_title.setAlignment(Qt.AlignCenter)

            horizontalLayout_1.addWidget(weight_summary_title)

            weight_summary_frame = QFrame(weight_summary_group)
            weight_summary_frame.setObjectName(f"weighing_frame_{number}")
            weight_summary_frame.setFont(font)
            weight_summary_frame.setStyleSheet(
                "border: solid;\n"
                "border-width: 1px;\n"
                "border-color: rgb(121, 121, 121);\n"
                "border-top-right-radius: 8px;\n"
                "border-bottom-right-radius: 8px;"
            )
            weight_summary_frame.setFrameShape(QFrame.StyledPanel)
            weight_summary_frame.setFrameShadow(QFrame.Raised)
            horizontalLayout_2 = QHBoxLayout(weight_summary_frame)
            horizontalLayout_2.setObjectName(f"horizontalLayout_0{number}")
            weight_summary = QLabel(weight_summary_frame)
            weight_summary.setObjectName(f"weighing_{number}")
            weight_summary.setText("XX.XXX")
            weight_summary.setFont(font)
            weight_summary.setStyleSheet("border: none;\n" "color: rgb(72, 72, 72);")
            weight_summary.setAlignment(Qt.AlignCenter)

            horizontalLayout_2.addWidget(weight_summary)
            horizontalLayout_1.addWidget(weight_summary_frame)
            gridLayout.addWidget(weight_summary_group, row, col, 1, 1)

        verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )
        gridLayout.addItem(verticalSpacer, (max_length) // max_columns, 0, 1, 1)

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

        self.getTabletList.getData(self.mainSpreadsheetId, self.TabletListRange)

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
                    currunt_tabletList.append(child.title().replace("เครื่องตอก ", ""))

            settings = self.settingsFile.read()
            gridLayout = QGridLayout(self.machineScrollAreaWidget)
            gridLayout.setObjectName("machine_gridLayout")
            gridLayout.setVerticalSpacing(20)
            gridLayout.setHorizontalSpacing(30)
            font = QFont()
            font.setFamilies(["Kanit"])
            font.setPointSize(12)
            font.setBold(True)

            max_rows = 2
            self.tabletID = None
            for index, tabletID in enumerate(
                sorted([tablet["tabletID"] for tablet in settings["TabletList"]])
            ):
                if not tabletID in currunt_tabletList:
                    row = (index) % max_rows
                    col = (index) // max_rows

                    _tablet = TabletList(self, tabletID)
                    _tablet.tabletID.connect(self._selectedTablet)
                    gridLayout.addWidget(_tablet.qbox, row, col, 1, 1)

    selectedTabletResult = Signal()
    def selectTabletStart(self):
        self.current_page = self.machine_page
        self.switchToPage(self.current_page)

    def selectedTablet(self):
        if self.tabletID:
            self.button_machine_confirm.setDisabled(True)
            self.button_machine_confirm.setText("กำลังโหลดข้อมูล...")
            self.selectedTabletResult.emit()
        else:
            self.Machine_alert.alert("กรุณาเลือกเครื่องตอกจากรายการ")

    @Slot(QGroupBox)
    def _selectedTablet(self, widget: QGroupBox):
        widget_title = widget.title().replace("เครื่องตอก ", "")
        if self.tabletID != widget_title:
            self.tabletID = widget_title
            self.current_tabletID.setText(f"( {self.tabletID} )")
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
                "percentWeightVariation": result[7][0],  # % ช่วงน้ำหนักเบี่ยงเบนที่ยอมรับ
                # ช่วงน้ำหนักเฉลี่ยที่ยอมรับ (Min.)
                "meanWeightAvgMin": result[8][0],
                # ช่วงน้ำหนักเฉลี่ยที่ยอมรับ (Max.)
                "meanWeightAvgMax": result[9][0],
                "meanWeightInhouseMin": result[10][0],  # ช่วงน้ำหนักเบี่ยงเบนที่ยอมรับ(Min.)
                "meanWeightInhouseMax": result[11][0],  # ช่วงน้ำหนักเบี่ยงเบนที่ยอมรับ(Max.)
                "meanWeightRegMin": result[12][0],  # ช่วงน้ำหนักเบี่ยงเบนที่ยอมรับ(Min.)
                "meanWeightRegMax": result[13][0],  # ช่วงน้ำหนักเบี่ยงเบนที่ยอมรับ(Max.)
                "meanWeightRegMax": result[14][0],  # ตั้งค่าน้ำหนักโดย
                "prepared": result[15][0],  # ตรวจสอบการตั้งค่าโดย
                "approved": result[16][0],  # ตรวจสอบการตั้งค่าโดย
            }

            self.SETTING_DATA_FILE.update(self.tabletID, settings)

        else:
            self.updateSettingsData_alert.alert("เกิดข้อผิดพลาดในการอัพเดท!")
        
        dataSettings = self.SETTING_DATA_FILE.read()
        if dataSettings:
            _dataSettings = dataSettings[self.tabletID]
            productName = _dataSettings["productName"]  # ชื่อยา
            lot = _dataSettings["lot"]  # เลขที่ผลิต
            balanceID = _dataSettings["balanceID"]  # เครื่องชั่ง
            tabletID = _dataSettings["tabletID"]  # เครื่องตอก
            numberPunches = _dataSettings["numberPunches"]  # น้ำหนักตามทฤษฎี
            # เปอร์เซ็นเบี่ยงเบน
            numberTablets = _dataSettings["numberTablets"]
            meanWeight = _dataSettings["meanWeight"]  # ช่วงน้ำหนัก 10 เม็ด(Min.)
            percentWeightVariation = _dataSettings["percentWeightVariation"]  # ช่วงน้ำหนัก 10 เม็ด(Max.)
            meanWeightAvgMin = _dataSettings["meanWeightAvgMin"]  # ช่วงน้ำหนัก 10 เม็ด(Min.)
            meanWeightAvgMax = _dataSettings["meanWeightAvgMax"]  # ช่วงน้ำหนัก 10 เม็ด(Max.)
            # ช่วงน้ำหนักเบี่ยงเบนที่กฎหมายยอมรับ (Min.)
            meanWeightInhouseMin = _dataSettings["meanWeightInhouseMin"]
            # ช่วงน้ำหนักเบี่ยงเบนที่กฎหมายยอมรับ (Max.)
            meanWeightInhouseMax = _dataSettings["meanWeightInhouseMax"]
            meanWeightRegMin = _dataSettings["meanWeightRegMin"]  # ค่าความหนา(Min.)
            meanWeightRegMax = _dataSettings["meanWeightRegMax"]  # ค่าความหนา(Max.)
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
                f"{meanWeightAvgMin} - {meanWeightAvgMax} กรัม"
            )
            self.MeanWeightInhouse.setText(
                f"{meanWeightInhouseMin} - {meanWeightInhouseMax} กรัม"
            )
            self.MeanWeightREG.setText(
                f"{meanWeightRegMin} - {meanWeightRegMax} กรัม"
            )

            # หากไม่มีข้อมูลการตั้งค่า
            if numberTablets == "XXXXX":
                self.weighing_start_page = self.numberTablets_page
            else:
                self.weighing_start_page = self.characteristics_page

            try:
                front_img = os.path.join(PRODUCT_IMG_FOLDER, productName, "UPPER.jpg")
                behind_img = os.path.join(PRODUCT_IMG_FOLDER, productName, "LOWER.jpg")
                
                # Check if files exist
                if os.path.exists(front_img) and os.path.exists(behind_img):
                    self.tablet_front_img.setPixmap(QPixmap(front_img))
                    self.tablet_behind_img.setPixmap(QPixmap(behind_img))
                else:
                    raise FileNotFoundError("One or both image files not found")

            except FileNotFoundError:
                picture_default = os.path.join(BASE_DIR, "assets", "icon", "picture_default.png")
                self.tablet_front_img.setPixmap(QPixmap(picture_default))
                self.tablet_behind_img.setPixmap(QPixmap(picture_default))
            except Exception as e:
                # Handle other exceptions
                print("An error occurred:", e)

        print("*** Update settings data complete!")
    
    
    ##########################  ป้อนจำนวนเม็ดยาที่ต้องชั่ง   ##########################
    getNumberTabletsResult = Signal(int)

    @Slot(int)
    def getNumberTablets(self, numberTablets):
        print(f"*** NumberTablets: {numberTablets}\n")
        QTimer.singleShot(500, lambda: self.getNumberTabletsResult.emit(numberTablets))

    def getNumberTabletsStart(self):
        print("*** Get number tablets...")
        self.current_page = self.numberTablets_page
        self.switchToPage(self.current_page)
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
        # self.PACKING_DATA["Characteristics"] = selected
        QTimer.singleShot(1000, lambda: self.characteristicsResult.emit())

    def characteristicsStart(self):
        print("Get characteristics data...")
        self.current_page = self.characteristics_page
        self.switchToPage(self.current_page)

    ##########################  weighing page   ##########################
    getWeighingDataResult = Signal(dict)
    hiddenBtnResult = Signal(bool)

    @Slot(dict)
    def getWeighingData(self, weighingData):
        """ดึงข้อมูลการชั่งน้ำหนัก"""

        print(f"WeighingData: {weighingData}\n")
        self.reset_weighing.setHidden(True)
        now = datetime.now()  # current date and time
        timestamp = now.strftime("%d/%m/%Y, %H:%M:%S")

        self.PACKING_DATA["Timestamp"] = timestamp
        self.PACKING_DATA["Weight"] = weighingData
        QTimer.singleShot(3000, lambda: self.getWeighingDataResult.emit(weighingData))

    @Slot(bool)
    def hiddenBtn(self, hidden):
        widget_list = [
            self.signout_1,
            self.signout_2,
            self.restart_program_1,
            self.restart_program_2,
        ]

        for w in widget_list:
            if hidden:
                w.setHidden(True)
            else:
                w.setHidden(False)

    def weighingStart(self):
        """เริ่มฟังชั่นดึงข้อมูลการชั่งน้ำหนัก"""

        print("Get weighing data...")
        self.current_page = self.weighing_page
        self.switchToPage(self.current_page)
        if not hasattr(self, "Weighing_called"):
            self.Weighing_called = False

        if not self.Weighing_called:
            self.Weighing_called = True
            self.Weighing.get.connect(self.getWeighingData)
            self.Weighing.hidden.connect(self.hiddenBtn)
        else:
            self.Weighing.weighing.clear()
            self.Weighing.isRunning()

        self.Weighing.start()

    def resetWeighing(self):
        self.findLabels(self.weight_group, mode="reset")
        self.hiddenBtn(False)
        self.Weighing.weighing.clear()

    ##########################  Send data to server   ##########################
    sendDataToServerResult = Signal(bool)

    def sendDataToServer(self):
        self.Title_alert.loading("กำลังส่งข้อมูล...", False)

        try:
            self.offline_count = 0
            weighing_data = self.WEIGHING_DATA_FILE.read()
            if weighing_data:
                print("*** Send data to server...")
                for data in weighing_data:
                    current_time = datetime.now()
                    timestamp_str = data["Timestamp"]
                    timestamp = datetime.strptime(timestamp_str, "%d/%m/%Y, %H:%M:%S")
                    if current_time - timestamp > timedelta(
                        minutes=_OFFLINE_CHECK_TIME
                    ):
                        data["Type"] = "OFFLINE"
                        self.offline_count += 1

                self.WEIGHING_DATA_FILE.write(weighing_data)
                self.Title_alert.alert_always(f"กำลังส่งข้อมูล...", False)
                self.sendDataToServer_timer.stop()

                settings = self.settingsFile.read()
                if settings:
                    self.tabletID = settings["TabletID"]
                    sheetDataId = self.findSpreadsheetID(self.tabletID)
                    rangeData = settings["Main"]["weighingDataRange"]
                    if not hasattr(self, "postDataToServer"):
                        self.postDataToServer = Server(self.token, self.credentials)
                        self.postDataToServer.get.connect(self._sendDataToServer)

                    self.postDataToServer.postData(
                        sheetDataId, rangeData, self.WEIGHING_DATA_FILE.read()
                    )
            else:
                self.sendDataToServer_timer.setInterval(_WEIGHING_DATA_FILE_CHECK_TIME)
                self.Title_alert.stop()
        except FileNotFoundError:
            print("File data not found!")
            self.Title_alert.stop()
            pass

    @Slot(bool)
    def _sendDataToServer(self, result=False):
        if result:
            self.Title_alert.success("ดำเนินการเรียบร้อยแล้ว", 3000)
            self.WEIGHING_DATA_FILE.delete()
            self.sendDataToServer_timer.start(10000)
        else:
            self.Title_alert.alert("เกิดข้อผิดพลาดในการส่งข้อมูล", 3000)
            if self.offline_count:
                QTimer.singleShot(
                    3000,
                    lambda: self.Title_alert.alert_always(
                        f"มีไฟล์ออฟไลน์อยู่ {self.offline_count} ไฟล์"
                    ),
                )
            self.sendDataToServer_timer.start(10000)

    ##########################  Weight IPC' ##########################
    def reset(self):
        if hasattr(self, "countdown_timer"):
            self.countdown_timer.stop()
        self.findLabels(self, mode="reset")
        self.run()

    def restart(self):
        """รีสตาร์ทโปรแกรม"""
        QApplication.quit()

    def exit(self):
        """ปิดโปรแกรม"""
        QApplication.quit()

    def run(self):
        print("Weight IPC is running...")
        # Valiable parameters
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
        # if not hasattr(self, "offlineDataCheck_timer"):
        #     self.sendDataToServer_timer = QTimer(self)
        #     self.sendDataToServer_timer.timeout.connect(self.sendDataToServer)
        # self.sendDataToServer_timer.start()

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
            self.characteristicsResult.connect(self.weighingStart)
            # self.successResult.connect(self.reset)
