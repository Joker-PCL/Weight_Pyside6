# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'weightIPC.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)
import resource_rc
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(38, 38, 38);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(1024, 600))
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.screen_page = QWidget(self.centralwidget)
        self.screen_page.setObjectName(u"screen_page")
        self.verticalLayout_5 = QVBoxLayout(self.screen_page)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 0, 9, 0)
        self.widget = QWidget(self.screen_page)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 55))
        self.widget.setStyleSheet(u"background-color: rgb(100, 100, 100);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 5, 10, 5)
        self.frame_28 = QFrame(self.widget)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setEnabled(True)
        self.frame_28.setMinimumSize(QSize(0, 0))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 75, 0)
        self.menu = QPushButton(self.frame_28)
        self.menu.setObjectName(u"menu")
        font = QFont()
        font.setPointSize(9)
        self.menu.setFont(font)
        self.menu.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/assets/icon/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/assets/icon/menu_open.png", QSize(), QIcon.Normal, QIcon.On)
        self.menu.setIcon(icon)
        self.menu.setIconSize(QSize(40, 40))
        self.menu.setCheckable(True)
        self.menu.setAutoExclusive(True)

        self.horizontalLayout_6.addWidget(self.menu)


        self.horizontalLayout.addWidget(self.frame_28)

        self.horizontalSpacer_5 = QSpacerItem(92, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.title = QLabel(self.widget)
        self.title.setObjectName(u"title")
        font1 = QFont()
        font1.setFamilies([u"Kanit"])
        font1.setPointSize(22)
        font1.setBold(True)
        self.title.setFont(font1)
        self.title.setStyleSheet(u"")
        self.title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.title)

        self.current_tabletID = QLabel(self.widget)
        self.current_tabletID.setObjectName(u"current_tabletID")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_tabletID.sizePolicy().hasHeightForWidth())
        self.current_tabletID.setSizePolicy(sizePolicy)
        self.current_tabletID.setFont(font1)
        self.current_tabletID.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.current_tabletID)

        self.horizontalSpacer_4 = QSpacerItem(75, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.wifi_signal = QLabel(self.widget)
        self.wifi_signal.setObjectName(u"wifi_signal")
        self.wifi_signal.setMaximumSize(QSize(30, 30))
        self.wifi_signal.setPixmap(QPixmap(u":/assets/icon/no-wifi.png"))
        self.wifi_signal.setScaledContents(True)

        self.horizontalLayout.addWidget(self.wifi_signal)

        self.datetime_group_2 = QGroupBox(self.widget)
        self.datetime_group_2.setObjectName(u"datetime_group_2")
        font2 = QFont()
        font2.setPointSize(11)
        self.datetime_group_2.setFont(font2)
        self.datetime_group_2.setAlignment(Qt.AlignCenter)
        self.datetime_group = QVBoxLayout(self.datetime_group_2)
        self.datetime_group.setSpacing(0)
        self.datetime_group.setObjectName(u"datetime_group")
        self.datetime_group.setContentsMargins(0, 5, 0, 5)
        self.time_bar = QLabel(self.datetime_group_2)
        self.time_bar.setObjectName(u"time_bar")
        self.time_bar.setMaximumSize(QSize(100, 12))
        font3 = QFont()
        font3.setFamilies([u"Kanit"])
        font3.setPointSize(13)
        font3.setBold(False)
        self.time_bar.setFont(font3)
        self.time_bar.setAlignment(Qt.AlignCenter)

        self.datetime_group.addWidget(self.time_bar)

        self.date_bar = QLabel(self.datetime_group_2)
        self.date_bar.setObjectName(u"date_bar")
        self.date_bar.setMaximumSize(QSize(120, 12))
        self.date_bar.setFont(font3)
        self.date_bar.setAlignment(Qt.AlignCenter)

        self.datetime_group.addWidget(self.date_bar)


        self.horizontalLayout.addWidget(self.datetime_group_2)


        self.verticalLayout_5.addWidget(self.widget)

        self.stackedWidget = QStackedWidget(self.screen_page)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setLayoutDirection(Qt.LeftToRight)
        self.stackedWidget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QGroupBox {\n"
"	border: none;\n"
"}\n"
"\n"
"#summary_weight_label_1, #summary_weight_label_2, #summary_average_label,  #summary_percent_label {\n"
"	background-color: rgb(80, 80, 80);\n"
"	border-top-left-radius: 15px;\n"
"	border-top-right-radius: 15px;\n"
"}")
        self.process_page = QWidget()
        self.process_page.setObjectName(u"process_page")
        self.horizontalLayout_61 = QHBoxLayout(self.process_page)
        self.horizontalLayout_61.setSpacing(0)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.process_main_frame = QFrame(self.process_page)
        self.process_main_frame.setObjectName(u"process_main_frame")
        self.process_main_frame.setFrameShape(QFrame.StyledPanel)
        self.process_main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.process_main_frame)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.process_frame = QFrame(self.process_main_frame)
        self.process_frame.setObjectName(u"process_frame")
        self.process_frame.setFrameShape(QFrame.StyledPanel)
        self.process_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.process_frame)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.process_img_frame = QFrame(self.process_frame)
        self.process_img_frame.setObjectName(u"process_img_frame")
        self.process_img_frame.setFrameShape(QFrame.StyledPanel)
        self.process_img_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.process_img_frame)
        self.horizontalLayout_62.setSpacing(0)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(164, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_62.addItem(self.horizontalSpacer_2)

        self.process_img = QLabel(self.process_img_frame)
        self.process_img.setObjectName(u"process_img")
        self.process_img.setMinimumSize(QSize(350, 350))
        self.process_img.setMaximumSize(QSize(300, 300))
        self.process_img.setPixmap(QPixmap(u":/assets/gif/connecting.gif"))
        self.process_img.setScaledContents(True)
        self.process_img.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_62.addWidget(self.process_img)

        self.horizontalSpacer_3 = QSpacerItem(163, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_62.addItem(self.horizontalSpacer_3)


        self.verticalLayout_32.addWidget(self.process_img_frame)

        self.process_label_line_1 = QLabel(self.process_frame)
        self.process_label_line_1.setObjectName(u"process_label_line_1")
        self.process_label_line_1.setMinimumSize(QSize(0, 30))
        self.process_label_line_1.setMaximumSize(QSize(16777215, 30))
        font4 = QFont()
        font4.setFamilies([u"Kanit"])
        font4.setPointSize(25)
        self.process_label_line_1.setFont(font4)
        self.process_label_line_1.setStyleSheet(u"color: rgb(128, 128, 128);")
        self.process_label_line_1.setFrameShape(QFrame.NoFrame)
        self.process_label_line_1.setFrameShadow(QFrame.Plain)
        self.process_label_line_1.setLineWidth(1)
        self.process_label_line_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.process_label_line_1)

        self.process_label_line_2 = QLabel(self.process_frame)
        self.process_label_line_2.setObjectName(u"process_label_line_2")
        self.process_label_line_2.setMinimumSize(QSize(0, 30))
        self.process_label_line_2.setMaximumSize(QSize(16777215, 30))
        font5 = QFont()
        font5.setFamilies([u"Kanit"])
        font5.setPointSize(18)
        self.process_label_line_2.setFont(font5)
        self.process_label_line_2.setStyleSheet(u"color: rgb(128, 128, 128);")
        self.process_label_line_2.setFrameShape(QFrame.NoFrame)
        self.process_label_line_2.setFrameShadow(QFrame.Plain)
        self.process_label_line_2.setLineWidth(1)
        self.process_label_line_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.process_label_line_2)

        self.process_label_line_3 = QLabel(self.process_frame)
        self.process_label_line_3.setObjectName(u"process_label_line_3")
        self.process_label_line_3.setMinimumSize(QSize(0, 30))
        self.process_label_line_3.setMaximumSize(QSize(16777215, 30))
        self.process_label_line_3.setFont(font5)
        self.process_label_line_3.setStyleSheet(u"color: rgb(128, 128, 128);")
        self.process_label_line_3.setFrameShape(QFrame.NoFrame)
        self.process_label_line_3.setFrameShadow(QFrame.Plain)
        self.process_label_line_3.setLineWidth(1)
        self.process_label_line_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.process_label_line_3)

        self.process_label_line_4 = QLabel(self.process_frame)
        self.process_label_line_4.setObjectName(u"process_label_line_4")
        self.process_label_line_4.setMinimumSize(QSize(0, 30))
        self.process_label_line_4.setMaximumSize(QSize(16777215, 30))
        font6 = QFont()
        font6.setFamilies([u"Kanit"])
        font6.setPointSize(14)
        self.process_label_line_4.setFont(font6)
        self.process_label_line_4.setStyleSheet(u"color: rgb(128, 128, 128);")
        self.process_label_line_4.setFrameShape(QFrame.NoFrame)
        self.process_label_line_4.setFrameShadow(QFrame.Plain)
        self.process_label_line_4.setLineWidth(1)
        self.process_label_line_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.process_label_line_4)


        self.verticalLayout_33.addWidget(self.process_frame)


        self.horizontalLayout_61.addWidget(self.process_main_frame)

        self.stackedWidget.addWidget(self.process_page)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.verticalLayout_15 = QVBoxLayout(self.home_page)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.login_frame = QFrame(self.home_page)
        self.login_frame.setObjectName(u"login_frame")
        self.login_frame.setToolTipDuration(0)
        self.verticalLayout_7 = QVBoxLayout(self.login_frame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 20)
        self.login_title = QFrame(self.login_frame)
        self.login_title.setObjectName(u"login_title")
        self.login_title.setMaximumSize(QSize(16777215, 80))
        self.login_title.setFrameShape(QFrame.StyledPanel)
        self.login_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.login_title)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(30, 0, 30, 0)
        self.rfid_alert = QLabel(self.login_title)
        self.rfid_alert.setObjectName(u"rfid_alert")
        self.rfid_alert.setMaximumSize(QSize(16777215, 50))
        self.rfid_alert.setFont(font4)
        self.rfid_alert.setStyleSheet(u"background-color: rgb(52, 157, 77);\n"
"border-radius: 15px;")
        self.rfid_alert.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.rfid_alert)


        self.verticalLayout_7.addWidget(self.login_title)

        self.scale_frame = QFrame(self.login_frame)
        self.scale_frame.setObjectName(u"scale_frame")
        self.horizontalLayout_5 = QHBoxLayout(self.scale_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 50, -1, 0)
        self.scale_img = QLabel(self.scale_frame)
        self.scale_img.setObjectName(u"scale_img")
        self.scale_img.setMaximumSize(QSize(300, 300))
        self.scale_img.setPixmap(QPixmap(u":/assets/images/scale.png"))
        self.scale_img.setScaledContents(True)
        self.scale_img.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.scale_img)


        self.verticalLayout_7.addWidget(self.scale_frame)

        self.rfid_frame = QFrame(self.login_frame)
        self.rfid_frame.setObjectName(u"rfid_frame")
        self.rfid_frame.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_4 = QHBoxLayout(self.rfid_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.rfid = QLabel(self.rfid_frame)
        self.rfid.setObjectName(u"rfid")
        self.rfid.setMaximumSize(QSize(370, 60))
        font7 = QFont()
        font7.setFamilies([u"Kanit"])
        font7.setPointSize(35)
        font7.setBold(True)
        self.rfid.setFont(font7)
        self.rfid.setStyleSheet(u"QLabel {\n"
"	color: rgb(100, 100, 100);\n"
"	border: solid;\n"
"	border-color: rgb(100, 100, 100);\n"
"	border-width: 3px;\n"
"	border-radius: 8px;\n"
"}")
        self.rfid.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.rfid)


        self.verticalLayout_7.addWidget(self.rfid_frame)


        self.verticalLayout_15.addWidget(self.login_frame)

        self.stackedWidget.addWidget(self.home_page)
        self.machine_page = QWidget()
        self.machine_page.setObjectName(u"machine_page")
        self.machine_page.setStyleSheet(u"QGroupBox {\n"
"	border: none;\n"
"}")
        self.verticalLayout_12 = QVBoxLayout(self.machine_page)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.machine_main_group = QGroupBox(self.machine_page)
        self.machine_main_group.setObjectName(u"machine_main_group")
        self.verticalLayout_13 = QVBoxLayout(self.machine_main_group)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(20, 0, 20, 0)
        self.machine_title_groupBox = QGroupBox(self.machine_main_group)
        self.machine_title_groupBox.setObjectName(u"machine_title_groupBox")
        self.machine_title_groupBox.setMinimumSize(QSize(0, 80))
        self.machine_title_groupBox.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_11 = QHBoxLayout(self.machine_title_groupBox)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(30, 0, 30, 0)
        self.machine_title = QLabel(self.machine_title_groupBox)
        self.machine_title.setObjectName(u"machine_title")
        self.machine_title.setMaximumSize(QSize(16777215, 60))
        self.machine_title.setFont(font4)
        self.machine_title.setStyleSheet(u"background-color: rgb(52, 157, 77);\n"
"border-radius: 15px;\n"
"padding-top: 8px;\n"
"padding-bottom: 8px;")
        self.machine_title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.machine_title)


        self.verticalLayout_13.addWidget(self.machine_title_groupBox)

        self.scrollArea_2 = QScrollArea(self.machine_main_group)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"QScrollArea {\n"
"	border: solid;\n"
"	border-width: 10px;\n"
"	border-color: #61d2b4;\n"
"	border-radius: 10px;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"}")
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setWidgetResizable(True)
        self.machineScrollAreaWidget = QWidget()
        self.machineScrollAreaWidget.setObjectName(u"machineScrollAreaWidget")
        self.machineScrollAreaWidget.setGeometry(QRect(0, 0, 553, 325))
        self.scrollArea_2.setWidget(self.machineScrollAreaWidget)

        self.verticalLayout_13.addWidget(self.scrollArea_2)

        self.machine_button_group = QGroupBox(self.machine_main_group)
        self.machine_button_group.setObjectName(u"machine_button_group")
        self.machine_button_group.setMinimumSize(QSize(0, 0))
        self.machine_button_group.setMaximumSize(QSize(16777215, 70))
        self.machine_button_group.setStyleSheet(u"QPushButton {\n"
"	border-radius: 15px;\n"
"}|")
        self.horizontalLayout_9 = QHBoxLayout(self.machine_button_group)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 5, 20, -1)
        self.button_machine_confirm = QPushButton(self.machine_button_group)
        self.button_machine_confirm.setObjectName(u"button_machine_confirm")
        self.button_machine_confirm.setMinimumSize(QSize(150, 50))
        self.button_machine_confirm.setMaximumSize(QSize(250, 16777215))
        font8 = QFont()
        font8.setFamilies([u"Kanit"])
        font8.setPointSize(20)
        self.button_machine_confirm.setFont(font8)
        self.button_machine_confirm.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_machine_confirm.setStyleSheet(u"background-color:  #288fb4;")
        icon1 = QIcon()
        icon1.addFile(u":/assets/icon/confirm.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_machine_confirm.setIcon(icon1)
        self.button_machine_confirm.setIconSize(QSize(20, 20))

        self.horizontalLayout_9.addWidget(self.button_machine_confirm)


        self.verticalLayout_13.addWidget(self.machine_button_group)


        self.verticalLayout_12.addWidget(self.machine_main_group)

        self.stackedWidget.addWidget(self.machine_page)
        self.numberTablets_page = QWidget()
        self.numberTablets_page.setObjectName(u"numberTablets_page")
        self.verticalLayout_34 = QVBoxLayout(self.numberTablets_page)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.numberTablets_page)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_35 = QVBoxLayout(self.widget_2)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.widget_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 300))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.numberTablets_title_groupBox_2 = QGroupBox(self.frame_4)
        self.numberTablets_title_groupBox_2.setObjectName(u"numberTablets_title_groupBox_2")
        self.numberTablets_title_groupBox_2.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_60 = QHBoxLayout(self.numberTablets_title_groupBox_2)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(30, 0, 30, 0)
        self.numberTablets_input_title = QLabel(self.numberTablets_title_groupBox_2)
        self.numberTablets_input_title.setObjectName(u"numberTablets_input_title")
        self.numberTablets_input_title.setMaximumSize(QSize(16777215, 50))
        self.numberTablets_input_title.setFont(font4)
        self.numberTablets_input_title.setStyleSheet(u"background-color: rgb(52, 157, 77);\n"
"border-radius: 15px;")
        self.numberTablets_input_title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_60.addWidget(self.numberTablets_input_title)


        self.verticalLayout_3.addWidget(self.numberTablets_title_groupBox_2)

        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_9)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(-1, -1, -1, 20)
        self.numberTablets_val_input = QLabel(self.frame_9)
        self.numberTablets_val_input.setObjectName(u"numberTablets_val_input")
        font9 = QFont()
        font9.setFamilies([u"Kanit"])
        font9.setPointSize(50)
        font9.setBold(True)
        self.numberTablets_val_input.setFont(font9)
        self.numberTablets_val_input.setStyleSheet(u"color: rgb(100, 100, 100);\n"
"border: none;")
        self.numberTablets_val_input.setAlignment(Qt.AlignCenter)

        self.verticalLayout_38.addWidget(self.numberTablets_val_input)


        self.verticalLayout_3.addWidget(self.frame_9)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 250))
        self.frame_5.setMaximumSize(QSize(16777215, 250))
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush1 = QBrush(QColor(255, 255, 255, 128))
        brush1.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.frame_6.setPalette(palette)
        self.frame_6.setStyleSheet(u"QPushButton {\n"
"	width: 90px;\n"
"	height: 70px;\n"
"	background-color: rgb(50, 50, 50);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    font-size: 40px;\n"
"	background-color: rgb(100, 100, 100);\n"
"}")
        self.frame_6.setFrameShadow(QFrame.Plain)
        self.frame_6.setLineWidth(3)
        self.gridLayout_2 = QGridLayout(self.frame_6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.key_1 = QPushButton(self.frame_6)
        self.key_1.setObjectName(u"key_1")
        font10 = QFont()
        font10.setFamilies([u"Kanit"])
        font10.setPointSize(20)
        font10.setWeight(QFont.Medium)
        self.key_1.setFont(font10)

        self.gridLayout_2.addWidget(self.key_1, 0, 0, 1, 1)

        self.key_2 = QPushButton(self.frame_6)
        self.key_2.setObjectName(u"key_2")
        self.key_2.setFont(font10)

        self.gridLayout_2.addWidget(self.key_2, 0, 1, 1, 1)

        self.key_3 = QPushButton(self.frame_6)
        self.key_3.setObjectName(u"key_3")
        self.key_3.setFont(font10)

        self.gridLayout_2.addWidget(self.key_3, 0, 2, 1, 1)

        self.key_4 = QPushButton(self.frame_6)
        self.key_4.setObjectName(u"key_4")
        self.key_4.setFont(font10)

        self.gridLayout_2.addWidget(self.key_4, 1, 0, 1, 1)

        self.key_5 = QPushButton(self.frame_6)
        self.key_5.setObjectName(u"key_5")
        self.key_5.setFont(font10)

        self.gridLayout_2.addWidget(self.key_5, 1, 1, 1, 1)

        self.key_6 = QPushButton(self.frame_6)
        self.key_6.setObjectName(u"key_6")
        self.key_6.setFont(font10)

        self.gridLayout_2.addWidget(self.key_6, 1, 2, 1, 1)

        self.key_7 = QPushButton(self.frame_6)
        self.key_7.setObjectName(u"key_7")
        self.key_7.setFont(font10)

        self.gridLayout_2.addWidget(self.key_7, 2, 0, 1, 1)

        self.key_8 = QPushButton(self.frame_6)
        self.key_8.setObjectName(u"key_8")
        self.key_8.setFont(font10)

        self.gridLayout_2.addWidget(self.key_8, 2, 1, 1, 1)

        self.key_9 = QPushButton(self.frame_6)
        self.key_9.setObjectName(u"key_9")
        self.key_9.setFont(font10)

        self.gridLayout_2.addWidget(self.key_9, 2, 2, 1, 1)

        self.key_backspace = QPushButton(self.frame_6)
        self.key_backspace.setObjectName(u"key_backspace")
        self.key_backspace.setMinimumSize(QSize(0, 0))
        self.key_backspace.setMaximumSize(QSize(16777215, 150))
        font11 = QFont()
        font11.setPointSize(20)
        self.key_backspace.setFont(font11)
        icon2 = QIcon()
        icon2.addFile(u":/assets/keyboard/backspace.png", QSize(), QIcon.Normal, QIcon.Off)
        self.key_backspace.setIcon(icon2)
        self.key_backspace.setIconSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.key_backspace, 3, 2, 1, 1)

        self.key_0 = QPushButton(self.frame_6)
        self.key_0.setObjectName(u"key_0")
        self.key_0.setMinimumSize(QSize(0, 0))
        self.key_0.setMaximumSize(QSize(16777215, 150))
        self.key_0.setFont(font10)

        self.gridLayout_2.addWidget(self.key_0, 3, 0, 1, 2)


        self.horizontalLayout_63.addWidget(self.frame_6)

        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(50, 50, 50);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(100, 100, 100);\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_8)
        self.verticalLayout_36.setSpacing(6)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.numberTablets_img = QLabel(self.frame_8)
        self.numberTablets_img.setObjectName(u"numberTablets_img")
        self.numberTablets_img.setPixmap(QPixmap(u":/assets/icon/thickness.png"))
        self.numberTablets_img.setAlignment(Qt.AlignCenter)

        self.verticalLayout_36.addWidget(self.numberTablets_img)

        self.key_enter = QPushButton(self.frame_8)
        self.key_enter.setObjectName(u"key_enter")
        self.key_enter.setMinimumSize(QSize(0, 52))
        font12 = QFont()
        font12.setFamilies([u"Kanit"])
        font12.setPointSize(20)
        font12.setWeight(QFont.Medium)
        font12.setItalic(False)
        self.key_enter.setFont(font12)
        self.key_enter.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/assets/keyboard/enter.png", QSize(), QIcon.Normal, QIcon.Off)
        self.key_enter.setIcon(icon3)
        self.key_enter.setIconSize(QSize(30, 30))

        self.verticalLayout_36.addWidget(self.key_enter)

        self.key_cancel = QPushButton(self.frame_8)
        self.key_cancel.setObjectName(u"key_cancel")
        self.key_cancel.setMinimumSize(QSize(0, 52))
        self.key_cancel.setFont(font12)
        icon4 = QIcon()
        icon4.addFile(u":/assets/keyboard/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.key_cancel.setIcon(icon4)
        self.key_cancel.setIconSize(QSize(30, 30))

        self.verticalLayout_36.addWidget(self.key_cancel)


        self.horizontalLayout_63.addWidget(self.frame_8)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.verticalLayout_35.addWidget(self.frame_4)


        self.verticalLayout_34.addWidget(self.widget_2)

        self.stackedWidget.addWidget(self.numberTablets_page)
        self.weighing_settings_page = QWidget()
        self.weighing_settings_page.setObjectName(u"weighing_settings_page")
        self.verticalLayout_11 = QVBoxLayout(self.weighing_settings_page)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.weighing_settings_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(-1, 0, -1, -1)
        self.frame_11 = QFrame(self.frame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 80))
        self.frame_11.setMaximumSize(QSize(16777215, 80))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_57.setSpacing(10)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(5, 10, 5, 0)
        self.update_settings = QPushButton(self.frame_11)
        self.update_settings.setObjectName(u"update_settings")
        self.update_settings.setMaximumSize(QSize(350, 16777215))
        font13 = QFont()
        font13.setFamilies([u"Kanit"])
        font13.setPointSize(18)
        font13.setBold(True)
        self.update_settings.setFont(font13)
        self.update_settings.setStyleSheet(u"background-color: rgb(0, 170, 127);\n"
"border-radius: 10px;\n"
"padding-top: 8px;\n"
"padding-bottom: 8px;")

        self.horizontalLayout_57.addWidget(self.update_settings)

        self.clear_settings = QPushButton(self.frame_11)
        self.clear_settings.setObjectName(u"clear_settings")
        self.clear_settings.setMaximumSize(QSize(350, 16777215))
        self.clear_settings.setFont(font13)
        self.clear_settings.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"border-radius: 10px;\n"
"padding-top: 8px;\n"
"padding-bottom: 8px;")

        self.horizontalLayout_57.addWidget(self.clear_settings)


        self.verticalLayout_37.addWidget(self.frame_11)

        self.weighingSettings_Frame = QFrame(self.frame)
        self.weighingSettings_Frame.setObjectName(u"weighingSettings_Frame")
        self.weighingSettings_Frame.setStyleSheet(u"QFrame {\n"
"	border: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(100, 100, 100);\n"
"	border-radius: 15px;\n"
"	margin: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"	color: rgb(60, 60, 60);\n"
"	border: none;\n"
"	margin: 0;\n"
"}")
        self.weighingSettings_Frame.setFrameShape(QFrame.StyledPanel)
        self.weighingSettings_Frame.setFrameShadow(QFrame.Raised)
        self.Productname_Label = QLabel(self.weighingSettings_Frame)
        self.Productname_Label.setObjectName(u"Productname_Label")
        self.Productname_Label.setGeometry(QRect(50, 30, 51, 31))
        self.Productname_Label.setFont(font6)
        self.Productname = QLabel(self.weighingSettings_Frame)
        self.Productname.setObjectName(u"Productname")
        self.Productname.setGeometry(QRect(100, 30, 301, 31))
        self.Productname.setFont(font6)
        self.Productname.setIndent(-1)
        self.Lot = QLabel(self.weighingSettings_Frame)
        self.Lot.setObjectName(u"Lot")
        self.Lot.setGeometry(QRect(130, 60, 201, 31))
        self.Lot.setFont(font6)
        self.Lot_Label = QLabel(self.weighingSettings_Frame)
        self.Lot_Label.setObjectName(u"Lot_Label")
        self.Lot_Label.setGeometry(QRect(50, 60, 81, 31))
        self.Lot_Label.setFont(font6)
        self.BalanceID = QLabel(self.weighingSettings_Frame)
        self.BalanceID.setObjectName(u"BalanceID")
        self.BalanceID.setGeometry(QRect(200, 90, 211, 31))
        self.BalanceID.setFont(font6)
        self.Balance_Label = QLabel(self.weighingSettings_Frame)
        self.Balance_Label.setObjectName(u"Balance_Label")
        self.Balance_Label.setGeometry(QRect(50, 90, 141, 31))
        self.Balance_Label.setFont(font6)
        self.TabletID = QLabel(self.weighingSettings_Frame)
        self.TabletID.setObjectName(u"TabletID")
        self.TabletID.setGeometry(QRect(140, 120, 61, 31))
        self.TabletID.setFont(font6)
        self.TabletID_Label = QLabel(self.weighingSettings_Frame)
        self.TabletID_Label.setObjectName(u"TabletID_Label")
        self.TabletID_Label.setGeometry(QRect(50, 120, 91, 31))
        self.TabletID_Label.setFont(font6)
        self.WeightIpcPer_Label = QLabel(self.weighingSettings_Frame)
        self.WeightIpcPer_Label.setObjectName(u"WeightIpcPer_Label")
        self.WeightIpcPer_Label.setGeometry(QRect(50, 240, 241, 31))
        self.WeightIpcPer_Label.setFont(font6)
        self.WeightIpcPer = QLabel(self.weighingSettings_Frame)
        self.WeightIpcPer.setObjectName(u"WeightIpcPer")
        self.WeightIpcPer.setGeometry(QRect(300, 240, 101, 31))
        self.WeightIpcPer.setFont(font6)
        self.meanWeightAvgMin_Label = QLabel(self.weighingSettings_Frame)
        self.meanWeightAvgMin_Label.setObjectName(u"meanWeightAvgMin_Label")
        self.meanWeightAvgMin_Label.setGeometry(QRect(50, 270, 191, 31))
        self.meanWeightAvgMin_Label.setFont(font6)
        self.meanWeightAvgMin = QLabel(self.weighingSettings_Frame)
        self.meanWeightAvgMin.setObjectName(u"meanWeightAvgMin")
        self.meanWeightAvgMin.setGeometry(QRect(250, 270, 211, 31))
        self.meanWeightAvgMin.setFont(font6)
        self.MeanWeightREG = QLabel(self.weighingSettings_Frame)
        self.MeanWeightREG.setObjectName(u"MeanWeightREG")
        self.MeanWeightREG.setGeometry(QRect(350, 330, 201, 31))
        self.MeanWeightREG.setFont(font6)
        self.MeanWeightREG_Label = QLabel(self.weighingSettings_Frame)
        self.MeanWeightREG_Label.setObjectName(u"MeanWeightREG_Label")
        self.MeanWeightREG_Label.setGeometry(QRect(50, 330, 291, 31))
        self.MeanWeightREG_Label.setFont(font6)
        self.Operator_Label = QLabel(self.weighingSettings_Frame)
        self.Operator_Label.setObjectName(u"Operator_Label")
        self.Operator_Label.setGeometry(QRect(50, 360, 101, 31))
        self.Operator_Label.setFont(font6)
        self.Operator = QLabel(self.weighingSettings_Frame)
        self.Operator.setObjectName(u"Operator")
        self.Operator.setGeometry(QRect(150, 360, 301, 31))
        self.Operator.setFont(font6)
        self.numberPunches_Label = QLabel(self.weighingSettings_Frame)
        self.numberPunches_Label.setObjectName(u"numberPunches_Label")
        self.numberPunches_Label.setGeometry(QRect(50, 150, 91, 31))
        self.numberPunches_Label.setFont(font6)
        self.numberPunches = QLabel(self.weighingSettings_Frame)
        self.numberPunches.setObjectName(u"numberPunches")
        self.numberPunches.setGeometry(QRect(140, 150, 121, 31))
        self.numberPunches.setFont(font6)
        self.numberTablets = QLabel(self.weighingSettings_Frame)
        self.numberTablets.setObjectName(u"numberTablets")
        self.numberTablets.setGeometry(QRect(210, 180, 121, 31))
        self.numberTablets.setFont(font6)
        self.numberTablets_Label = QLabel(self.weighingSettings_Frame)
        self.numberTablets_Label.setObjectName(u"numberTablets_Label")
        self.numberTablets_Label.setGeometry(QRect(50, 180, 151, 31))
        self.numberTablets_Label.setFont(font6)
        self.meanWeight_Label = QLabel(self.weighingSettings_Frame)
        self.meanWeight_Label.setObjectName(u"meanWeight_Label")
        self.meanWeight_Label.setGeometry(QRect(50, 210, 131, 31))
        self.meanWeight_Label.setFont(font6)
        self.meanWeight = QLabel(self.weighingSettings_Frame)
        self.meanWeight.setObjectName(u"meanWeight")
        self.meanWeight.setGeometry(QRect(190, 210, 121, 31))
        self.meanWeight.setFont(font6)
        self.MeanWeightInhouse_Label = QLabel(self.weighingSettings_Frame)
        self.MeanWeightInhouse_Label.setObjectName(u"MeanWeightInhouse_Label")
        self.MeanWeightInhouse_Label.setGeometry(QRect(50, 300, 221, 31))
        self.MeanWeightInhouse_Label.setFont(font6)
        self.MeanWeightInhouse = QLabel(self.weighingSettings_Frame)
        self.MeanWeightInhouse.setObjectName(u"MeanWeightInhouse")
        self.MeanWeightInhouse.setGeometry(QRect(280, 300, 211, 31))
        self.MeanWeightInhouse.setFont(font6)

        self.verticalLayout_37.addWidget(self.weighingSettings_Frame)


        self.verticalLayout_11.addWidget(self.frame)

        self.stackedWidget.addWidget(self.weighing_settings_page)
        self.characteristics_page = QWidget()
        self.characteristics_page.setObjectName(u"characteristics_page")
        self.verticalLayout_14 = QVBoxLayout(self.characteristics_page)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.thickness_frame_2 = QFrame(self.characteristics_page)
        self.thickness_frame_2.setObjectName(u"thickness_frame_2")
        self.thickness_frame_2.setMaximumSize(QSize(16777215, 80))
        self.thickness_frame_2.setFrameShape(QFrame.StyledPanel)
        self.thickness_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.thickness_frame_2)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(30, -1, 30, -1)
        self.thickness_title_2 = QLabel(self.thickness_frame_2)
        self.thickness_title_2.setObjectName(u"thickness_title_2")
        self.thickness_title_2.setMaximumSize(QSize(16777215, 50))
        self.thickness_title_2.setFont(font4)
        self.thickness_title_2.setStyleSheet(u"background-color: rgb(52, 157, 77);\n"
"border-radius: 15px;")
        self.thickness_title_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_33.addWidget(self.thickness_title_2)


        self.verticalLayout_14.addWidget(self.thickness_frame_2)

        self.characteristics_frame = QFrame(self.characteristics_page)
        self.characteristics_frame.setObjectName(u"characteristics_frame")
        self.characteristics_frame.setStyleSheet(u"QLabel {\n"
"	border: solid;\n"
"	border-width: 2px;\n"
"	border-color: rgb(111, 105, 37);\n"
"	border-radius: 15px;\n"
"	padding: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	margin-top: 25px;\n"
"	border-radius: 15px;\n"
"}")
        self.characteristics_frame.setFrameShape(QFrame.StyledPanel)
        self.characteristics_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.characteristics_frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(20)
        self.gridLayout_4.setVerticalSpacing(15)
        self.gridLayout_4.setContentsMargins(-1, -1, -1, 30)
        self.tablet_front_img = QLabel(self.characteristics_frame)
        self.tablet_front_img.setObjectName(u"tablet_front_img")
        self.tablet_front_img.setMinimumSize(QSize(250, 250))
        self.tablet_front_img.setMaximumSize(QSize(250, 250))
        self.tablet_front_img.setPixmap(QPixmap(u":/assets/icon/picture_default.png"))
        self.tablet_front_img.setScaledContents(True)

        self.gridLayout_4.addWidget(self.tablet_front_img, 1, 0, 1, 1)

        self.characteristics_abnomal = QPushButton(self.characteristics_frame)
        self.characteristics_abnomal.setObjectName(u"characteristics_abnomal")
        self.characteristics_abnomal.setMinimumSize(QSize(120, 80))
        self.characteristics_abnomal.setFont(font8)
        self.characteristics_abnomal.setCursor(QCursor(Qt.PointingHandCursor))
        self.characteristics_abnomal.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        icon5 = QIcon()
        icon5.addFile(u":/assets/icon/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.characteristics_abnomal.setIcon(icon5)
        self.characteristics_abnomal.setIconSize(QSize(30, 30))

        self.gridLayout_4.addWidget(self.characteristics_abnomal, 2, 1, 1, 1)

        self.characteristics_nomal = QPushButton(self.characteristics_frame)
        self.characteristics_nomal.setObjectName(u"characteristics_nomal")
        self.characteristics_nomal.setMinimumSize(QSize(120, 80))
        self.characteristics_nomal.setFont(font8)
        self.characteristics_nomal.setCursor(QCursor(Qt.PointingHandCursor))
        self.characteristics_nomal.setStyleSheet(u"background-color: rgb(0, 170, 0);")
        self.characteristics_nomal.setIcon(icon1)
        self.characteristics_nomal.setIconSize(QSize(30, 30))

        self.gridLayout_4.addWidget(self.characteristics_nomal, 2, 0, 1, 1)

        self.tablet_behind_img = QLabel(self.characteristics_frame)
        self.tablet_behind_img.setObjectName(u"tablet_behind_img")
        self.tablet_behind_img.setMinimumSize(QSize(250, 250))
        self.tablet_behind_img.setMaximumSize(QSize(250, 250))
        self.tablet_behind_img.setPixmap(QPixmap(u":/assets/icon/picture_default.png"))
        self.tablet_behind_img.setScaledContents(True)

        self.gridLayout_4.addWidget(self.tablet_behind_img, 1, 1, 1, 1)

        self.tablet_front_label = QLabel(self.characteristics_frame)
        self.tablet_front_label.setObjectName(u"tablet_front_label")
        self.tablet_front_label.setMaximumSize(QSize(16777215, 50))
        font14 = QFont()
        font14.setFamilies([u"Kanit"])
        font14.setPointSize(18)
        font14.setBold(False)
        font14.setUnderline(True)
        self.tablet_front_label.setFont(font14)
        self.tablet_front_label.setStyleSheet(u"border: none;\n"
"color: rgb(80, 80, 80);")
        self.tablet_front_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.tablet_front_label, 0, 0, 1, 1)

        self.tablet_behind_label = QLabel(self.characteristics_frame)
        self.tablet_behind_label.setObjectName(u"tablet_behind_label")
        self.tablet_behind_label.setMaximumSize(QSize(16777215, 50))
        self.tablet_behind_label.setFont(font14)
        self.tablet_behind_label.setStyleSheet(u"border: none;\n"
"color: rgb(80, 80, 80);")
        self.tablet_behind_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.tablet_behind_label, 0, 1, 1, 1)


        self.verticalLayout_14.addWidget(self.characteristics_frame)

        self.stackedWidget.addWidget(self.characteristics_page)
        self.weighing_page = QWidget()
        self.weighing_page.setObjectName(u"weighing_page")
        self.weighing_page.setStyleSheet(u"QGroupBox {\n"
"	border: none\n"
"}")
        self.verticalLayout_27 = QVBoxLayout(self.weighing_page)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.weight_summary_main_group = QGroupBox(self.weighing_page)
        self.weight_summary_main_group.setObjectName(u"weight_summary_main_group")
        self.weight_summary_main_group.setMinimumSize(QSize(0, 220))
        self.weight_summary_main_group.setMaximumSize(QSize(16777215, 220))
        self.verticalLayout_9 = QVBoxLayout(self.weight_summary_main_group)
        self.verticalLayout_9.setSpacing(15)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(20, -1, 20, -1)
        self.weight_summary_title_frame = QFrame(self.weight_summary_main_group)
        self.weight_summary_title_frame.setObjectName(u"weight_summary_title_frame")
        self.weight_summary_title_frame.setMaximumSize(QSize(16777215, 60))
        self.weight_summary_title_frame.setFrameShape(QFrame.StyledPanel)
        self.weight_summary_title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.weight_summary_title_frame)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.weight_summary_title = QLabel(self.weight_summary_title_frame)
        self.weight_summary_title.setObjectName(u"weight_summary_title")
        self.weight_summary_title.setMaximumSize(QSize(16777215, 50))
        self.weight_summary_title.setFont(font4)
        self.weight_summary_title.setStyleSheet(u"background-color: rgb(52, 157, 77);\n"
"border-radius: 15px;")
        self.weight_summary_title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_34.addWidget(self.weight_summary_title)


        self.verticalLayout_9.addWidget(self.weight_summary_title_frame)

        self.weight_summary_group = QGroupBox(self.weight_summary_main_group)
        self.weight_summary_group.setObjectName(u"weight_summary_group")
        self.weight_summary_group.setMinimumSize(QSize(0, 0))
        self.weight_summary_group.setMaximumSize(QSize(16777215, 70))
        font15 = QFont()
        font15.setPointSize(5)
        self.weight_summary_group.setFont(font15)
        self.weight_summary_group.setStyleSheet(u"#summary_weight_min_1, #summary_weight_min_2, #summary_average\n"
" {\n"
"	background-color: rgb(255, 170, 0);\n"
"	border-bottom-left-radius: 15px;\n"
"	border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"#summary_weight_min_label_1, #summary_weight_min_label_2, #summary_average_label {\n"
"	background-color: rgb(80, 80, 80);\n"
"	border-top-left-radius: 15px;\n"
"	border-top-right-radius: 15px;\n"
"}")
        self.weight_summary_group.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.horizontalLayout_35 = QHBoxLayout(self.weight_summary_group)
        self.horizontalLayout_35.setSpacing(20)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.summary_weight_min_group_1 = QGroupBox(self.weight_summary_group)
        self.summary_weight_min_group_1.setObjectName(u"summary_weight_min_group_1")
        self.summary_weight_min_group_1.setLayoutDirection(Qt.LeftToRight)
        self.summary_weight_min_group_1.setStyleSheet(u"")
        self.verticalLayout_18 = QVBoxLayout(self.summary_weight_min_group_1)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.summary_weight_min_label_1 = QLabel(self.summary_weight_min_group_1)
        self.summary_weight_min_label_1.setObjectName(u"summary_weight_min_label_1")
        font16 = QFont()
        font16.setFamilies([u"Kanit"])
        font16.setPointSize(12)
        font16.setBold(True)
        self.summary_weight_min_label_1.setFont(font16)
        self.summary_weight_min_label_1.setLayoutDirection(Qt.LeftToRight)
        self.summary_weight_min_label_1.setAutoFillBackground(False)
        self.summary_weight_min_label_1.setStyleSheet(u"")
        self.summary_weight_min_label_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.summary_weight_min_label_1)

        self.summary_weight_min_1 = QLabel(self.summary_weight_min_group_1)
        self.summary_weight_min_1.setObjectName(u"summary_weight_min_1")
        self.summary_weight_min_1.setMinimumSize(QSize(0, 40))
        self.summary_weight_min_1.setMaximumSize(QSize(16777215, 40))
        font17 = QFont()
        font17.setFamilies([u"Kanit"])
        font17.setPointSize(20)
        font17.setBold(True)
        self.summary_weight_min_1.setFont(font17)
        self.summary_weight_min_1.setStyleSheet(u"")
        self.summary_weight_min_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.summary_weight_min_1)


        self.horizontalLayout_35.addWidget(self.summary_weight_min_group_1)

        self.summary_weight_min_group_2 = QGroupBox(self.weight_summary_group)
        self.summary_weight_min_group_2.setObjectName(u"summary_weight_min_group_2")
        self.summary_weight_min_group_2.setLayoutDirection(Qt.LeftToRight)
        self.summary_weight_min_group_2.setStyleSheet(u"")
        self.verticalLayout_19 = QVBoxLayout(self.summary_weight_min_group_2)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.summary_weight_min_label_2 = QLabel(self.summary_weight_min_group_2)
        self.summary_weight_min_label_2.setObjectName(u"summary_weight_min_label_2")
        self.summary_weight_min_label_2.setFont(font16)
        self.summary_weight_min_label_2.setLayoutDirection(Qt.LeftToRight)
        self.summary_weight_min_label_2.setAutoFillBackground(False)
        self.summary_weight_min_label_2.setStyleSheet(u"")
        self.summary_weight_min_label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.summary_weight_min_label_2)

        self.summary_weight_min_2 = QLabel(self.summary_weight_min_group_2)
        self.summary_weight_min_2.setObjectName(u"summary_weight_min_2")
        self.summary_weight_min_2.setMinimumSize(QSize(0, 40))
        self.summary_weight_min_2.setMaximumSize(QSize(16777215, 40))
        self.summary_weight_min_2.setFont(font17)
        self.summary_weight_min_2.setStyleSheet(u"")
        self.summary_weight_min_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.summary_weight_min_2)


        self.horizontalLayout_35.addWidget(self.summary_weight_min_group_2)

        self.average_summary_group = QGroupBox(self.weight_summary_group)
        self.average_summary_group.setObjectName(u"average_summary_group")
        self.average_summary_group.setLayoutDirection(Qt.LeftToRight)
        self.average_summary_group.setStyleSheet(u"")
        self.verticalLayout_20 = QVBoxLayout(self.average_summary_group)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.summary_average_label = QLabel(self.average_summary_group)
        self.summary_average_label.setObjectName(u"summary_average_label")
        self.summary_average_label.setFont(font16)
        self.summary_average_label.setLayoutDirection(Qt.LeftToRight)
        self.summary_average_label.setAutoFillBackground(False)
        self.summary_average_label.setStyleSheet(u"")
        self.summary_average_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.summary_average_label)

        self.summary_average = QLabel(self.average_summary_group)
        self.summary_average.setObjectName(u"summary_average")
        self.summary_average.setMinimumSize(QSize(0, 40))
        self.summary_average.setMaximumSize(QSize(16777215, 40))
        self.summary_average.setFont(font17)
        self.summary_average.setStyleSheet(u"")
        self.summary_average.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.summary_average)


        self.horizontalLayout_35.addWidget(self.average_summary_group)

        self.timeout_group = QGroupBox(self.weight_summary_group)
        self.timeout_group.setObjectName(u"timeout_group")
        self.timeout_group.setMinimumSize(QSize(0, 0))
        self.timeout_group.setMaximumSize(QSize(16777215, 70))
        font18 = QFont()
        font18.setPointSize(1)
        self.timeout_group.setFont(font18)
        self.timeout_group.setAlignment(Qt.AlignCenter)
        self.timeout_group.setCheckable(False)
        self.timeout_group.setChecked(False)
        self.verticalLayout_26 = QVBoxLayout(self.timeout_group)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.timeout_title = QLabel(self.timeout_group)
        self.timeout_title.setObjectName(u"timeout_title")
        font19 = QFont()
        font19.setFamilies([u"Kanit"])
        font19.setPointSize(11)
        self.timeout_title.setFont(font19)
        self.timeout_title.setStyleSheet(u"color: rgb(80, 80, 80);")
        self.timeout_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.timeout_title)

        self.timeout = QLabel(self.timeout_group)
        self.timeout.setObjectName(u"timeout")
        self.timeout.setFont(font7)
        self.timeout.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.timeout.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.timeout)


        self.horizontalLayout_35.addWidget(self.timeout_group)

        self.button_exit = QPushButton(self.weight_summary_group)
        self.button_exit.setObjectName(u"button_exit")
        self.button_exit.setMinimumSize(QSize(65, 65))
        self.button_exit.setMaximumSize(QSize(65, 65))
        self.button_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_exit.setStyleSheet(u"border: none;")
        icon6 = QIcon()
        icon6.addFile(u":/assets/icon/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_exit.setIcon(icon6)
        self.button_exit.setIconSize(QSize(60, 60))

        self.horizontalLayout_35.addWidget(self.button_exit)


        self.verticalLayout_9.addWidget(self.weight_summary_group)

        self.current_weight_widget = QWidget(self.weight_summary_main_group)
        self.current_weight_widget.setObjectName(u"current_weight_widget")
        self.current_weight_widget.setMinimumSize(QSize(0, 55))
        self.current_weight_widget.setStyleSheet(u"background-color: rgb(50, 50, 50);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.horizontalLayout_12 = QHBoxLayout(self.current_weight_widget)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(20, 0, 20, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer)

        self.current_weight_label = QLabel(self.current_weight_widget)
        self.current_weight_label.setObjectName(u"current_weight_label")
        self.current_weight_label.setMinimumSize(QSize(50, 50))
        self.current_weight_label.setMaximumSize(QSize(50, 50))
        self.current_weight_label.setPixmap(QPixmap(u":/assets/icon/weighing.png"))
        self.current_weight_label.setScaledContents(True)
        self.current_weight_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.current_weight_label)

        self.current_weight = QLabel(self.current_weight_widget)
        self.current_weight.setObjectName(u"current_weight")
        self.current_weight.setMinimumSize(QSize(200, 0))
        self.current_weight.setMaximumSize(QSize(200, 16777215))
        font20 = QFont()
        font20.setFamilies([u"Kanit"])
        font20.setPointSize(30)
        font20.setBold(True)
        font20.setItalic(False)
        font20.setUnderline(False)
        font20.setStrikeOut(False)
        self.current_weight.setFont(font20)
        self.current_weight.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.current_weight)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_6)


        self.verticalLayout_9.addWidget(self.current_weight_widget)


        self.verticalLayout_27.addWidget(self.weight_summary_main_group)

        self.weight_summary_main_group_2 = QGroupBox(self.weighing_page)
        self.weight_summary_main_group_2.setObjectName(u"weight_summary_main_group_2")
        self.weight_summary_main_group_2.setMinimumSize(QSize(0, 300))
        self.weight_summary_main_group_2.setAlignment(Qt.AlignCenter)
        self.verticalLayout_8 = QVBoxLayout(self.weight_summary_main_group_2)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, -1, 5, -1)
        self.scrollArea = QScrollArea(self.weight_summary_main_group_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"border: none;")
        self.scrollArea.setWidgetResizable(True)
        self.summary_weighing_widget = QWidget()
        self.summary_weighing_widget.setObjectName(u"summary_weighing_widget")
        self.summary_weighing_widget.setGeometry(QRect(0, 0, 623, 283))
        self.scrollArea.setWidget(self.summary_weighing_widget)

        self.verticalLayout_8.addWidget(self.scrollArea)


        self.verticalLayout_27.addWidget(self.weight_summary_main_group_2)

        self.stackedWidget.addWidget(self.weighing_page)
        self.manual_page = QWidget()
        self.manual_page.setObjectName(u"manual_page")
        self.verticalLayout_6 = QVBoxLayout(self.manual_page)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.manual_title_group = QFrame(self.manual_page)
        self.manual_title_group.setObjectName(u"manual_title_group")
        self.manual_title_group.setMaximumSize(QSize(16777215, 55))
        self.manual_title_group.setFrameShape(QFrame.StyledPanel)
        self.manual_title_group.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.manual_title_group)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(30, 0, 30, 0)
        self.manual_title = QLabel(self.manual_title_group)
        self.manual_title.setObjectName(u"manual_title")
        self.manual_title.setMaximumSize(QSize(16777215, 45))
        self.manual_title.setFont(font4)
        self.manual_title.setStyleSheet(u"background-color: rgb(52, 157, 77);\n"
"border-radius: 15px;")
        self.manual_title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.manual_title)


        self.verticalLayout_6.addWidget(self.manual_title_group)

        self.frame_3 = QFrame(self.manual_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_3)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(-1, 0, -1, 5)
        self.frame_12 = QFrame(self.frame_3)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(-1, 5, -1, -1)
        self.manual_video = QGroupBox(self.frame_12)
        self.manual_video.setObjectName(u"manual_video")
        self.manual_video.setStyleSheet(u"QWidget {\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: solid;\n"
"	border-width: 2px;\n"
"	border-color: rgb(111, 105, 37);\n"
"	border-radius: 15px;\n"
"	padding: 10px;\n"
"}")

        self.horizontalLayout_67.addWidget(self.manual_video)


        self.verticalLayout_28.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(16777215, 50))
        self.frame_13.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_66.setSpacing(10)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(-1, 0, -1, 0)
        self.button_video_play = QPushButton(self.frame_13)
        self.button_video_play.setObjectName(u"button_video_play")
        self.button_video_play.setMinimumSize(QSize(0, 0))
        self.button_video_play.setMaximumSize(QSize(120, 16777215))
        self.button_video_play.setFont(font8)
        self.button_video_play.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_video_play.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/assets/icon/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_video_play.setIcon(icon7)
        self.button_video_play.setIconSize(QSize(55, 55))

        self.horizontalLayout_66.addWidget(self.button_video_play)

        self.button_video_pause = QPushButton(self.frame_13)
        self.button_video_pause.setObjectName(u"button_video_pause")
        self.button_video_pause.setMinimumSize(QSize(0, 0))
        self.button_video_pause.setMaximumSize(QSize(120, 16777215))
        self.button_video_pause.setFont(font8)
        self.button_video_pause.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_video_pause.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/assets/icon/pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_video_pause.setIcon(icon8)
        self.button_video_pause.setIconSize(QSize(50, 50))

        self.horizontalLayout_66.addWidget(self.button_video_pause)

        self.button_video_stop = QPushButton(self.frame_13)
        self.button_video_stop.setObjectName(u"button_video_stop")
        self.button_video_stop.setMinimumSize(QSize(0, 0))
        self.button_video_stop.setMaximumSize(QSize(120, 16777215))
        self.button_video_stop.setFont(font8)
        self.button_video_stop.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_video_stop.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u":/assets/icon/stop-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_video_stop.setIcon(icon9)
        self.button_video_stop.setIconSize(QSize(45, 45))

        self.horizontalLayout_66.addWidget(self.button_video_stop)


        self.verticalLayout_28.addWidget(self.frame_13)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.manual_page)
        self.develops_page = QWidget()
        self.develops_page.setObjectName(u"develops_page")
        self.verticalLayout_31 = QVBoxLayout(self.develops_page)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.frame_2 = QFrame(self.develops_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QLabel {\n"
"	color: rgb(100, 100, 100);\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_2)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(-1, 5, -1, -1)
        self.widget_3 = QWidget(self.frame_2)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_65 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, -1)
        self.groupBox_6 = QGroupBox(self.widget_3)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMaximumSize(QSize(16777215, 100))
        font21 = QFont()
        font21.setFamilies([u"Kanit"])
        font21.setPointSize(14)
        font21.setBold(True)
        self.groupBox_6.setFont(font21)
        self.groupBox_6.setStyleSheet(u"QGroupBox {\n"
"	border: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(255, 170, 0);\n"
"	border-radius: 8px;\n"
"	color: #262626;\n"
"}")
        self.groupBox_6.setAlignment(Qt.AlignCenter)
        self.wifi_signal_2 = QLabel(self.groupBox_6)
        self.wifi_signal_2.setObjectName(u"wifi_signal_2")
        self.wifi_signal_2.setGeometry(QRect(20, 10, 80, 80))
        self.wifi_signal_2.setMinimumSize(QSize(80, 80))
        self.wifi_signal_2.setMaximumSize(QSize(80, 80))
        self.wifi_signal_2.setPixmap(QPixmap(u":/assets/icon/no-wifi.png"))
        self.wifi_signal_2.setScaledContents(True)
        self.ping = QLabel(self.groupBox_6)
        self.ping.setObjectName(u"ping")
        self.ping.setGeometry(QRect(120, 60, 171, 25))
        self.ping.setMinimumSize(QSize(0, 25))
        self.ping.setMaximumSize(QSize(16777215, 25))
        self.ping.setFont(font21)
        self.ping.setStyleSheet(u"color: rgb(100, 100, 100);")
        self.ssid = QLabel(self.groupBox_6)
        self.ssid.setObjectName(u"ssid")
        self.ssid.setGeometry(QRect(120, 30, 221, 25))
        self.ssid.setMinimumSize(QSize(0, 25))
        self.ssid.setMaximumSize(QSize(16777215, 25))
        self.ssid.setFont(font21)
        self.ssid.setStyleSheet(u"color: rgb(100, 100, 100);")

        self.horizontalLayout_65.addWidget(self.groupBox_6)


        self.verticalLayout_39.addWidget(self.widget_3)

        self.view_pages_group_2 = QGroupBox(self.frame_2)
        self.view_pages_group_2.setObjectName(u"view_pages_group_2")
        self.view_pages_group_2.setMinimumSize(QSize(0, 0))
        self.view_pages_group_2.setMaximumSize(QSize(16777215, 180))
        self.view_pages_group_2.setFont(font21)
        self.view_pages_group_2.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"}\n"
"\n"
"QGroupBox {\n"
"	border: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(255, 170, 0);\n"
"	border-radius: 8px;\n"
"	color: #262626;\n"
"}\n"
"\n"
"QPushButton {\n"
"	border: none;\n"
"}\n"
"")
        self.view_pages_group_2.setAlignment(Qt.AlignCenter)
        self.view_pages_group_2.setFlat(False)
        self.horizontalLayout_56 = QHBoxLayout(self.view_pages_group_2)
        self.horizontalLayout_56.setSpacing(15)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(15, 40, 15, 15)
        self.tabletList = QScrollArea(self.view_pages_group_2)
        self.tabletList.setObjectName(u"tabletList")
        self.tabletList.setMinimumSize(QSize(0, 130))
        self.tabletList.setMaximumSize(QSize(16777215, 135))
        self.tabletList.setStyleSheet(u"QGroupBox {\n"
"	min-width: 120px;\n"
"	max-width: 120px;\n"
"	min-height: 100px;\n"
"}")
        self.tabletList.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tabletList.setWidgetResizable(True)
        self.tabletListContents = QWidget()
        self.tabletListContents.setObjectName(u"tabletListContents")
        self.tabletListContents.setGeometry(QRect(0, 0, 563, 130))
        self.horizontalLayout_64 = QHBoxLayout(self.tabletListContents)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.tabletList.setWidget(self.tabletListContents)

        self.horizontalLayout_56.addWidget(self.tabletList)


        self.verticalLayout_39.addWidget(self.view_pages_group_2)


        self.verticalLayout_31.addWidget(self.frame_2)

        self.view_pages_group = QGroupBox(self.develops_page)
        self.view_pages_group.setObjectName(u"view_pages_group")
        self.view_pages_group.setMinimumSize(QSize(0, 180))
        self.view_pages_group.setMaximumSize(QSize(16777215, 180))
        self.view_pages_group.setFont(font21)
        self.view_pages_group.setStyleSheet(u"QGroupBox {\n"
"	border: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(255, 170, 0);\n"
"	border-radius: 8px;\n"
"	color: #262626;\n"
"}\n"
"\n"
"QPushButton {\n"
"	border: none;\n"
"}\n"
"")
        self.view_pages_group.setAlignment(Qt.AlignCenter)
        self.view_pages_group.setFlat(False)
        self.horizontalLayout_7 = QHBoxLayout(self.view_pages_group)
        self.horizontalLayout_7.setSpacing(15)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(15, 40, 15, 15)
        self.groupBox_2 = QGroupBox(self.view_pages_group)
        self.groupBox_2.setObjectName(u"groupBox_2")
        font22 = QFont()
        font22.setFamilies([u"Kanit"])
        font22.setPointSize(12)
        self.groupBox_2.setFont(font22)
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.verticalLayout_17 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(-1, -1, -1, 0)
        self.machine_page_view = QPushButton(self.groupBox_2)
        self.machine_page_view.setObjectName(u"machine_page_view")
        self.machine_page_view.setFont(font19)
        self.machine_page_view.setCursor(QCursor(Qt.PointingHandCursor))
        self.machine_page_view.setLayoutDirection(Qt.LeftToRight)
        self.machine_page_view.setStyleSheet(u"")
        icon10 = QIcon()
        icon10.addFile(u":/assets/icon/machine.png", QSize(), QIcon.Normal, QIcon.Off)
        self.machine_page_view.setIcon(icon10)
        self.machine_page_view.setIconSize(QSize(80, 80))
        self.machine_page_view.setAutoRepeat(False)

        self.verticalLayout_17.addWidget(self.machine_page_view)


        self.horizontalLayout_7.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.view_pages_group)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font22)
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.verticalLayout_16 = QVBoxLayout(self.groupBox)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, -1, -1, 0)
        self.weighing_settings_page_view = QPushButton(self.groupBox)
        self.weighing_settings_page_view.setObjectName(u"weighing_settings_page_view")
        self.weighing_settings_page_view.setFont(font19)
        self.weighing_settings_page_view.setCursor(QCursor(Qt.PointingHandCursor))
        self.weighing_settings_page_view.setLayoutDirection(Qt.LeftToRight)
        self.weighing_settings_page_view.setStyleSheet(u"")
        icon11 = QIcon()
        icon11.addFile(u":/assets/icon/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.weighing_settings_page_view.setIcon(icon11)
        self.weighing_settings_page_view.setIconSize(QSize(80, 80))
        self.weighing_settings_page_view.setAutoRepeat(False)

        self.verticalLayout_16.addWidget(self.weighing_settings_page_view)


        self.horizontalLayout_7.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(self.view_pages_group)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font22)
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.verticalLayout_29 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(-1, -1, -1, 0)
        self.characteristics_page_view = QPushButton(self.groupBox_3)
        self.characteristics_page_view.setObjectName(u"characteristics_page_view")
        self.characteristics_page_view.setFont(font19)
        self.characteristics_page_view.setCursor(QCursor(Qt.PointingHandCursor))
        self.characteristics_page_view.setLayoutDirection(Qt.LeftToRight)
        self.characteristics_page_view.setStyleSheet(u"")
        icon12 = QIcon()
        icon12.addFile(u":/assets/icon/characteristics.png", QSize(), QIcon.Normal, QIcon.Off)
        self.characteristics_page_view.setIcon(icon12)
        self.characteristics_page_view.setIconSize(QSize(80, 80))
        self.characteristics_page_view.setAutoRepeat(False)

        self.verticalLayout_29.addWidget(self.characteristics_page_view)


        self.horizontalLayout_7.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.view_pages_group)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setFont(font22)
        self.groupBox_4.setAlignment(Qt.AlignCenter)
        self.verticalLayout_30 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(-1, -1, -1, 0)
        self.weighing_page_view = QPushButton(self.groupBox_4)
        self.weighing_page_view.setObjectName(u"weighing_page_view")
        self.weighing_page_view.setFont(font19)
        self.weighing_page_view.setCursor(QCursor(Qt.PointingHandCursor))
        self.weighing_page_view.setLayoutDirection(Qt.LeftToRight)
        self.weighing_page_view.setStyleSheet(u"")
        icon13 = QIcon()
        icon13.addFile(u":/assets/icon/weighing.png", QSize(), QIcon.Normal, QIcon.Off)
        self.weighing_page_view.setIcon(icon13)
        self.weighing_page_view.setIconSize(QSize(80, 80))
        self.weighing_page_view.setAutoRepeat(False)

        self.verticalLayout_30.addWidget(self.weighing_page_view)


        self.horizontalLayout_7.addWidget(self.groupBox_4)


        self.verticalLayout_31.addWidget(self.view_pages_group)

        self.stackedWidget.addWidget(self.develops_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout_3.addWidget(self.screen_page, 0, 2, 1, 1)

        self.hide_sidebar = QWidget(self.centralwidget)
        self.hide_sidebar.setObjectName(u"hide_sidebar")
        self.hide_sidebar.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(0, 150, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(0, 150, 255);\n"
"	color: white;\n"
"	height: 30px;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	padding: 15px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: #f5fafe;\n"
"	color: rgb(0, 150, 255);\n"
"	font-weight: bold;\n"
"}")
        self.verticalLayout_42 = QVBoxLayout(self.hide_sidebar)
        self.verticalLayout_42.setSpacing(20)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.profile_img2 = QLabel(self.hide_sidebar)
        self.profile_img2.setObjectName(u"profile_img2")
        self.profile_img2.setMinimumSize(QSize(80, 80))
        self.profile_img2.setMaximumSize(QSize(80, 80))
        self.profile_img2.setPixmap(QPixmap(u":/assets/images/polipharm.png"))
        self.profile_img2.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.profile_img2)


        self.verticalLayout_42.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.home_2 = QPushButton(self.hide_sidebar)
        self.home_2.setObjectName(u"home_2")
        self.home_2.setMinimumSize(QSize(5, 0))
        self.home_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon14 = QIcon()
        icon14.addFile(u":/assets/icon/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_2.setIcon(icon14)
        self.home_2.setIconSize(QSize(40, 40))
        self.home_2.setCheckable(True)
        self.home_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_2)

        self.manual_2 = QPushButton(self.hide_sidebar)
        self.manual_2.setObjectName(u"manual_2")
        self.manual_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon15 = QIcon()
        icon15.addFile(u":/assets/icon/manual_1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.manual_2.setIcon(icon15)
        self.manual_2.setIconSize(QSize(40, 40))
        self.manual_2.setCheckable(True)
        self.manual_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.manual_2)

        self.develops_2 = QPushButton(self.hide_sidebar)
        self.develops_2.setObjectName(u"develops_2")
        self.develops_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon16 = QIcon()
        icon16.addFile(u":/assets/icon/developer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.develops_2.setIcon(icon16)
        self.develops_2.setIconSize(QSize(50, 50))
        self.develops_2.setCheckable(True)
        self.develops_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.develops_2)


        self.verticalLayout_42.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 297, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_42.addItem(self.verticalSpacer)

        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.signout_2 = QPushButton(self.hide_sidebar)
        self.signout_2.setObjectName(u"signout_2")
        self.signout_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon17 = QIcon()
        icon17.addFile(u":/assets/icon/logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.signout_2.setIcon(icon17)
        self.signout_2.setIconSize(QSize(50, 50))

        self.verticalLayout_40.addWidget(self.signout_2)

        self.restart_program_2 = QPushButton(self.hide_sidebar)
        self.restart_program_2.setObjectName(u"restart_program_2")
        font23 = QFont()
        font23.setFamilies([u"Kanit"])
        font23.setPointSize(12)
        font23.setStrikeOut(False)
        font23.setKerning(True)
        self.restart_program_2.setFont(font23)
        self.restart_program_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon18 = QIcon()
        icon18.addFile(u":/assets/icon/restart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restart_program_2.setIcon(icon18)
        self.restart_program_2.setIconSize(QSize(50, 50))
#if QT_CONFIG(shortcut)
        self.restart_program_2.setShortcut(u"Ctrl+S")
#endif // QT_CONFIG(shortcut)

        self.verticalLayout_40.addWidget(self.restart_program_2)


        self.verticalLayout_42.addLayout(self.verticalLayout_40)


        self.gridLayout_3.addWidget(self.hide_sidebar, 0, 0, 1, 1)

        self.show_sidebar = QWidget(self.centralwidget)
        self.show_sidebar.setObjectName(u"show_sidebar")
        self.show_sidebar.setEnabled(True)
        self.show_sidebar.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(0, 150, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: rgb(0, 150, 255);\n"
"	color: white;\n"
"	text-align: left;\n"
"	height: 30px;\n"
"	border: none;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"	padding: 15px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: #f5fafe;\n"
"	color: rgb(0, 150, 255);\n"
"	font-weight: bold;\n"
"}")
        self.verticalLayout_41 = QVBoxLayout(self.show_sidebar)
        self.verticalLayout_41.setSpacing(20)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, 0, -1)
        self.profile_img1 = QLabel(self.show_sidebar)
        self.profile_img1.setObjectName(u"profile_img1")
        self.profile_img1.setMinimumSize(QSize(80, 80))
        self.profile_img1.setMaximumSize(QSize(80, 80))
        self.profile_img1.setPixmap(QPixmap(u":/assets/images/polipharm.png"))
        self.profile_img1.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.profile_img1)

        self.label_3 = QLabel(self.show_sidebar)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font17)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_41.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.home_1 = QPushButton(self.show_sidebar)
        self.home_1.setObjectName(u"home_1")
        font24 = QFont()
        font24.setFamilies([u"Kanit"])
        font24.setPointSize(12)
        font24.setBold(False)
        self.home_1.setFont(font24)
        self.home_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_1.setIcon(icon14)
        self.home_1.setIconSize(QSize(40, 40))
        self.home_1.setCheckable(True)
        self.home_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.home_1)

        self.manual_1 = QPushButton(self.show_sidebar)
        self.manual_1.setObjectName(u"manual_1")
        self.manual_1.setFont(font22)
        self.manual_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.manual_1.setIcon(icon15)
        self.manual_1.setIconSize(QSize(40, 40))
        self.manual_1.setCheckable(True)
        self.manual_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.manual_1)

        self.develops_1 = QPushButton(self.show_sidebar)
        self.develops_1.setObjectName(u"develops_1")
        self.develops_1.setFont(font19)
        self.develops_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.develops_1.setIcon(icon16)
        self.develops_1.setIconSize(QSize(50, 50))
        self.develops_1.setCheckable(True)
        self.develops_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.develops_1)


        self.verticalLayout_41.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 297, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_41.addItem(self.verticalSpacer_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.signout_1 = QPushButton(self.show_sidebar)
        self.signout_1.setObjectName(u"signout_1")
        self.signout_1.setFont(font23)
        self.signout_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.signout_1.setIcon(icon17)
        self.signout_1.setIconSize(QSize(50, 50))
#if QT_CONFIG(shortcut)
        self.signout_1.setShortcut(u"Ctrl+S")
#endif // QT_CONFIG(shortcut)

        self.verticalLayout_4.addWidget(self.signout_1)

        self.restart_program_1 = QPushButton(self.show_sidebar)
        self.restart_program_1.setObjectName(u"restart_program_1")
        self.restart_program_1.setFont(font23)
        self.restart_program_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.restart_program_1.setIcon(icon18)
        self.restart_program_1.setIconSize(QSize(50, 50))
#if QT_CONFIG(shortcut)
        self.restart_program_1.setShortcut(u"Ctrl+S")
#endif // QT_CONFIG(shortcut)

        self.verticalLayout_4.addWidget(self.restart_program_1)


        self.verticalLayout_41.addLayout(self.verticalLayout_4)


        self.gridLayout_3.addWidget(self.show_sidebar, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menu.toggled.connect(self.show_sidebar.setVisible)
        self.menu.toggled.connect(self.hide_sidebar.setHidden)
        self.develops_2.toggled.connect(self.develops_1.setChecked)
        self.develops_1.toggled.connect(self.develops_2.setChecked)
        self.manual_1.toggled.connect(self.manual_2.setChecked)
        self.manual_2.toggled.connect(self.manual_1.setChecked)
        self.home_2.toggled.connect(self.home_1.setChecked)
        self.home_1.toggled.connect(self.home_2.setChecked)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu.setText("")
        self.title.setText(QCoreApplication.translate("MainWindow", u"\u0e23\u0e30\u0e1a\u0e1a\u0e40\u0e04\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e0a\u0e31\u0e48\u0e07\u0e2d\u0e2d\u0e19\u0e44\u0e25\u0e19\u0e4c", None))
        self.current_tabletID.setText("")
        self.wifi_signal.setText("")
        self.time_bar.setText(QCoreApplication.translate("MainWindow", u"HH:MM:SS", None))
        self.date_bar.setText(QCoreApplication.translate("MainWindow", u"DD/MM/YYYY", None))
        self.process_img.setText("")
        self.process_label_line_1.setText(QCoreApplication.translate("MainWindow", u"ONLINE WEIGHING SYSTEM", None))
        self.process_label_line_2.setText(QCoreApplication.translate("MainWindow", u"Created by Nattapon pondonko", None))
        self.process_label_line_3.setText(QCoreApplication.translate("MainWindow", u"Engineering Department", None))
        self.process_label_line_4.setText("")
        self.rfid_alert.setText(QCoreApplication.translate("MainWindow", u"\u0e41\u0e2a\u0e01\u0e19\u0e1a\u0e31\u0e15\u0e23\u0e1e\u0e19\u0e31\u0e01\u0e07\u0e32\u0e19", None))
        self.scale_img.setText("")
        self.rfid.setText(QCoreApplication.translate("MainWindow", u"XXXXXXXXXX", None))
        self.machine_title.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e40\u0e04\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e15\u0e2d\u0e01\u0e17\u0e35\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e01\u0e32\u0e23\u0e0a\u0e31\u0e48\u0e07\u0e19\u0e49\u0e33\u0e2b\u0e19\u0e31\u0e01", None))
        self.button_machine_confirm.setText(QCoreApplication.translate("MainWindow", u"\u0e22\u0e37\u0e19\u0e22\u0e31\u0e19", None))
        self.numberTablets_input_title.setText(QCoreApplication.translate("MainWindow", u"\u0e08\u0e33\u0e19\u0e27\u0e19\u0e40\u0e21\u0e47\u0e14\u0e17\u0e35\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e0a\u0e31\u0e48\u0e07", None))
        self.numberTablets_val_input.setText(QCoreApplication.translate("MainWindow", u"XXXX", None))
        self.key_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.key_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.key_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.key_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.key_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.key_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.key_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.key_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.key_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.key_backspace.setText("")
        self.key_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.numberTablets_img.setText("")
        self.key_enter.setText(QCoreApplication.translate("MainWindow", u"  \u0e22\u0e37\u0e19\u0e22\u0e31\u0e19", None))
        self.key_cancel.setText(QCoreApplication.translate("MainWindow", u"  \u0e22\u0e01\u0e40\u0e25\u0e34\u0e01", None))
        self.update_settings.setText(QCoreApplication.translate("MainWindow", u"\u0e2d\u0e31\u0e1e\u0e40\u0e14\u0e17\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e01\u0e32\u0e23\u0e15\u0e31\u0e49\u0e07\u0e04\u0e48\u0e32", None))
        self.clear_settings.setText(QCoreApplication.translate("MainWindow", u"\u0e25\u0e49\u0e32\u0e07\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e01\u0e32\u0e23\u0e15\u0e31\u0e49\u0e07\u0e04\u0e48\u0e32", None))
        self.Productname_Label.setText(QCoreApplication.translate("MainWindow", u"\u0e0a\u0e37\u0e48\u0e2d\u0e22\u0e32", None))
        self.Productname.setText(QCoreApplication.translate("MainWindow", u"XXXXXXXXXX", None))
        self.Lot.setText(QCoreApplication.translate("MainWindow", u"XXXXXXX", None))
        self.Lot_Label.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e25\u0e02\u0e17\u0e35\u0e48\u0e1c\u0e25\u0e34\u0e15", None))
        self.BalanceID.setText(QCoreApplication.translate("MainWindow", u"XXXXXXX", None))
        self.Balance_Label.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e04\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e0a\u0e31\u0e48\u0e07\u0e2b\u0e21\u0e32\u0e22\u0e40\u0e25\u0e02", None))
        self.TabletID.setText(QCoreApplication.translate("MainWindow", u"XXX", None))
        self.TabletID_Label.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e04\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e15\u0e2d\u0e01", None))
        self.WeightIpcPer_Label.setText(QCoreApplication.translate("MainWindow", u"% \u0e0a\u0e48\u0e27\u0e07\u0e19\u0e49\u0e33\u0e2b\u0e19\u0e31\u0e01\u0e40\u0e1a\u0e35\u0e48\u0e22\u0e07\u0e40\u0e1a\u0e19\u0e17\u0e35\u0e48\u0e22\u0e2d\u0e21\u0e23\u0e31\u0e1a", None))
        self.WeightIpcPer.setText(QCoreApplication.translate("MainWindow", u"XX.XXX %", None))
        self.meanWeightAvgMin_Label.setText(QCoreApplication.translate("MainWindow", u"\u0e0a\u0e48\u0e27\u0e07\u0e19\u0e49\u0e33\u0e2b\u0e19\u0e31\u0e01\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22\u0e17\u0e35\u0e48\u0e22\u0e2d\u0e21\u0e23\u0e31\u0e1a", None))
        self.meanWeightAvgMin.setText(QCoreApplication.translate("MainWindow", u"XX.XXX - XX.XXX \u0e01\u0e23\u0e31\u0e21", None))
        self.MeanWeightREG.setText(QCoreApplication.translate("MainWindow", u"XX.XXX - XX.XXX \u0e01\u0e23\u0e31\u0e21", None))
        self.MeanWeightREG_Label.setText(QCoreApplication.translate("MainWindow", u"\u0e0a\u0e48\u0e27\u0e07\u0e19\u0e49\u0e33\u0e2b\u0e19\u0e31\u0e01\u0e40\u0e1a\u0e35\u0e48\u0e22\u0e07\u0e40\u0e1a\u0e19\u0e17\u0e35\u0e48\u0e01\u0e0f\u0e2b\u0e21\u0e32\u0e22\u0e22\u0e2d\u0e21\u0e23\u0e31\u0e1a", None))
        self.Operator_Label.setText(QCoreApplication.translate("MainWindow", u"\u0e1c\u0e39\u0e49\u0e1b\u0e0f\u0e34\u0e1a\u0e31\u0e15\u0e34\u0e07\u0e32\u0e19", None))
        self.Operator.setText(QCoreApplication.translate("MainWindow", u"XXXXXXXXXX", None))
        self.numberPunches_Label.setText(QCoreApplication.translate("MainWindow", u"\u0e08\u0e33\u0e19\u0e27\u0e19\u0e2a\u0e32\u0e01", None))
        self.numberPunches.setText(QCoreApplication.translate("MainWindow", u"XXX \u0e2a\u0e32\u0e01", None))
        self.numberTablets.setText(QCoreApplication.translate("MainWindow", u"XX \u0e40\u0e21\u0e47\u0e14", None))
        self.numberTablets_Label.setText(QCoreApplication.translate("MainWindow", u"\u0e08\u0e33\u0e19\u0e27\u0e19\u0e40\u0e21\u0e47\u0e14\u0e17\u0e35\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e0a\u0e31\u0e48\u0e07", None))
        self.meanWeight_Label.setText(QCoreApplication.translate("MainWindow", u"\u0e19\u0e49\u0e33\u0e2b\u0e19\u0e31\u0e01\u0e15\u0e2d\u0e01/\u0e40\u0e21\u0e47\u0e14", None))
        self.meanWeight.setText(QCoreApplication.translate("MainWindow", u"XX.XXX \u0e01\u0e23\u0e31\u0e21", None))
        self.MeanWeightInhouse_Label.setText(QCoreApplication.translate("MainWindow", u"\u0e0a\u0e48\u0e27\u0e07\u0e19\u0e49\u0e33\u0e2b\u0e19\u0e31\u0e01\u0e40\u0e1a\u0e35\u0e48\u0e22\u0e07\u0e40\u0e1a\u0e19\u0e17\u0e35\u0e48\u0e22\u0e2d\u0e21\u0e23\u0e31\u0e1a", None))
        self.MeanWeightInhouse.setText(QCoreApplication.translate("MainWindow", u"XX.XXX - XX.XXX \u0e01\u0e23\u0e31\u0e21", None))
        self.thickness_title_2.setText(QCoreApplication.translate("MainWindow", u"\u0e25\u0e31\u0e01\u0e29\u0e13\u0e30\u0e40\u0e21\u0e47\u0e14\u0e22\u0e32", None))
        self.tablet_front_img.setText("")
        self.characteristics_abnomal.setText(QCoreApplication.translate("MainWindow", u"\u0e1c\u0e34\u0e14\u0e1b\u0e01\u0e15\u0e34", None))
        self.characteristics_nomal.setText(QCoreApplication.translate("MainWindow", u"\u0e1b\u0e01\u0e15\u0e34", None))
        self.tablet_behind_img.setText("")
        self.tablet_front_label.setText(QCoreApplication.translate("MainWindow", u"\u0e14\u0e49\u0e32\u0e19\u0e2b\u0e19\u0e49\u0e32", None))
        self.tablet_behind_label.setText(QCoreApplication.translate("MainWindow", u"\u0e14\u0e49\u0e32\u0e19\u0e2b\u0e25\u0e31\u0e07", None))
        self.weight_summary_main_group.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.weight_summary_title.setText(QCoreApplication.translate("MainWindow", u"\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e01\u0e32\u0e23\u0e0a\u0e31\u0e48\u0e07\u0e19\u0e49\u0e33\u0e2b\u0e19\u0e31\u0e01", None))
        self.summary_weight_min_label_1.setText(QCoreApplication.translate("MainWindow", u"\u0e19\u0e49\u0e33\u0e2b\u0e19\u0e31\u0e01\u0e15\u0e48\u0e33\u0e2a\u0e38\u0e14", None))
        self.summary_weight_min_1.setText(QCoreApplication.translate("MainWindow", u"XX.XXX", None))
        self.summary_weight_min_label_2.setText(QCoreApplication.translate("MainWindow", u"\u0e19\u0e49\u0e33\u0e2b\u0e19\u0e31\u0e01\u0e2a\u0e39\u0e07\u0e2a\u0e38\u0e14", None))
        self.summary_weight_min_2.setText(QCoreApplication.translate("MainWindow", u"XX.XXX", None))
        self.summary_average_label.setText(QCoreApplication.translate("MainWindow", u"\u0e19\u0e49\u0e33\u0e2b\u0e19\u0e31\u0e01\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22", None))
        self.summary_average.setText(QCoreApplication.translate("MainWindow", u"XX.XXX", None))
        self.timeout_title.setText(QCoreApplication.translate("MainWindow", u"\u0e19\u0e31\u0e1a\u0e40\u0e27\u0e25\u0e32\u0e16\u0e2d\u0e22\u0e2b\u0e25\u0e31\u0e07", None))
        self.timeout.setText(QCoreApplication.translate("MainWindow", u"180 s.", None))
        self.button_exit.setText("")
        self.current_weight_label.setText("")
        self.current_weight.setText(QCoreApplication.translate("MainWindow", u"XX.XXX", None))
        self.manual_title.setText(QCoreApplication.translate("MainWindow", u"\u0e04\u0e39\u0e48\u0e21\u0e37\u0e2d\u0e01\u0e32\u0e23\u0e43\u0e0a\u0e49\u0e07\u0e32\u0e19", None))
        self.button_video_play.setText("")
        self.button_video_pause.setText("")
        self.button_video_stop.setText("")
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u0e01\u0e32\u0e23\u0e40\u0e0a\u0e37\u0e48\u0e2d\u0e21\u0e15\u0e48\u0e2d\u0e44\u0e27\u0e44\u0e1f", None))
        self.wifi_signal_2.setText("")
        self.ping.setText(QCoreApplication.translate("MainWindow", u"Ping: 00 ms", None))
        self.ssid.setText(QCoreApplication.translate("MainWindow", u"SSID: XXXXXXXXXXX", None))
        self.view_pages_group_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0e23\u0e32\u0e22\u0e01\u0e32\u0e23\u0e40\u0e04\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e15\u0e2d\u0e01 (\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e40\u0e04\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e15\u0e2d\u0e01\u0e17\u0e35\u0e48\u0e1b\u0e0f\u0e34\u0e1a\u0e15\u0e34\u0e07\u0e32\u0e19)", None))
        self.view_pages_group.setTitle(QCoreApplication.translate("MainWindow", u"\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e14\u0e39\u0e2b\u0e19\u0e49\u0e32\u0e40\u0e21\u0e19\u0e39\u0e01\u0e32\u0e23\u0e0a\u0e31\u0e48\u0e07\u0e19\u0e49\u0e33\u0e2b\u0e19\u0e31\u0e01", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0e40\u0e04\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e15\u0e2d\u0e01", None))
        self.machine_page_view.setText("")
#if QT_CONFIG(shortcut)
        self.machine_page_view.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e01\u0e32\u0e23\u0e15\u0e31\u0e49\u0e07\u0e04\u0e48\u0e32", None))
        self.weighing_settings_page_view.setText("")
#if QT_CONFIG(shortcut)
        self.weighing_settings_page_view.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0e2b\u0e19\u0e49\u0e32\u0e25\u0e31\u0e01\u0e29\u0e13\u0e30\u0e40\u0e21\u0e47\u0e14\u0e22\u0e32", None))
        self.characteristics_page_view.setText("")
#if QT_CONFIG(shortcut)
        self.characteristics_page_view.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u0e2b\u0e19\u0e49\u0e32\u0e0a\u0e31\u0e48\u0e07\u0e19\u0e49\u0e33\u0e2b\u0e19\u0e31\u0e01", None))
        self.weighing_page_view.setText("")
#if QT_CONFIG(shortcut)
        self.weighing_page_view.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.profile_img2.setText("")
        self.home_2.setText("")
        self.manual_2.setText("")
        self.develops_2.setText("")
        self.signout_2.setText("")
        self.restart_program_2.setText("")
        self.profile_img1.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"WEIGHT V1", None))
        self.home_1.setText(QCoreApplication.translate("MainWindow", u"  \u0e2b\u0e19\u0e49\u0e32\u0e2b\u0e25\u0e31\u0e01", None))
        self.manual_1.setText(QCoreApplication.translate("MainWindow", u"  \u0e27\u0e34\u0e18\u0e35\u0e43\u0e0a\u0e49\u0e07\u0e32\u0e19", None))
        self.develops_1.setText(QCoreApplication.translate("MainWindow", u"Develops ", None))
        self.signout_1.setText(QCoreApplication.translate("MainWindow", u"  \u0e2d\u0e2d\u0e01\u0e08\u0e32\u0e01\u0e23\u0e30\u0e1a\u0e1a", None))
        self.restart_program_1.setText(QCoreApplication.translate("MainWindow", u"  \u0e23\u0e35\u0e2a\u0e15\u0e32\u0e23\u0e4c\u0e17", None))
    # retranslateUi

