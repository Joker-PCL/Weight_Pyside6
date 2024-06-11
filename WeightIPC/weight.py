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
from src.Thickness import Thickness
from src.TabletList import TabletList
from src.VideoPlayer import VideoPlayer

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GIF_FILE = os.path.join(BASE_DIR, "assets", "gif", "connecting.gif")
MANUAL_VIDEO_FILE = os.path.join(BASE_DIR, "SARAN.mp4")
WEIGHING_DATA_FILE = os.path.join(BASE_DIR, "database", "weighingData.json")
USER_DATA_FILE = os.path.join(BASE_DIR, "database", "usersData.json")
SETTING_DATA_FILE = os.path.join(BASE_DIR, "database", "settings10s.json")
LOGGING_FILE = os.path.join(BASE_DIR, "files", "polipharm.log")

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
        self.current_page = self.home_page
        self.home_1.clicked.connect(lambda: self.switchToPage(self.current_page))
        self.home_2.clicked.connect(lambda: self.switchToPage(self.current_page))

        self.manual_1.clicked.connect(lambda: self.switchToPage(self.manual_page))
        self.manual_2.clicked.connect(lambda: self.switchToPage(self.manual_page))

        self.develops_1.clicked.connect(lambda: self.switchToPage(self.develops_page))
        self.develops_2.clicked.connect(lambda: self.switchToPage(self.develops_page))

        self.button_machine_confirm.clicked.connect(self.setCurrentTabletID)

        # สร้างการแจ้งเตือนส่วนหัว
        self.Title_alert = Alert(self.title)

        # สร้างการแจ้งเตือนแสกน rfid
        self.RFID_alert = Alert(self.rfid_alert)

        # สร้างการแจ้งเตือนหน้าเลือกเครื่องตอก
        self.Machine_alert = Alert(self.machine_title)

        # สร้างการแจ้งเตือนอัพเดทข้อมูลการตั้งค่า
        self.updateSettingsData_alert = Alert(self.update_settings)
        self.show_sidebar.setHidden(True)

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

        self.createWeighingWidget()
        self.createMachineWidget()

    # เปลี่ยนหน้าต่างแสดงผล
    def switchToPage(self, page):
        self.stackedWidget.setCurrentWidget(page)

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

    current_tabletID = Signal(QGroupBox)
    def createMachineWidget(self):
        gridLayout = QGridLayout(self.machineScrollAreaWidget)
        gridLayout.setObjectName("machine_gridLayout")
        gridLayout.setVerticalSpacing(20)
        gridLayout.setHorizontalSpacing(30)
        font = QFont()
        font.setFamilies(["Kanit"])
        font.setPointSize(12)
        font.setBold(True)

        max_rows = 2
        max_length = 10
        self.current_tabletID = None
        for i in range(0, max_length):
            number = i + 1
            row = (i) % max_rows
            col = (i) // max_rows

            select_machine = TabletList(self, number)
            select_machine.tabletID.connect(self.findLabels)
            gridLayout.addWidget(select_machine.qbox, row, col, 1, 1)

    @Slot(QGroupBox)
    def findLabels(self, widget: QGroupBox):
        if self.current_tabletID != widget.title():
            self.current_tabletID = widget.title()
            initialStyle = widget.styleSheet()
            for child in self.machineScrollAreaWidget.children():
                if isinstance(child, QGroupBox):
                    if child.title() == widget.title():
                        child.setStyleSheet(
                            """
                                border: solid;
                                border-width: 1px;
                                border-color: rgb(255, 150, 0);
                                border-radius: 8px;
                                background-color: #f4f56e; 
                                color:  #58b3d3;
                            """
                        )
                    else:
                        child.setStyleSheet(initialStyle)

    def setCurrentTabletID(self):
        if not self.current_tabletID:
            self.Machine_alert.alert("กรุณาเลือกเครื่องตอกจากรายการ")
        else:
            self.button_machine_confirm.setDisabled(True)
            self.button_machine_confirm.setText("กำลังโหลดข้อมูล...")