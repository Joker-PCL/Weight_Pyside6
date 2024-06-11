from PySide6.QtWidgets import QPushButton, QGroupBox, QVBoxLayout, QLabel
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QCursor, QIcon
from PySide6.QtCore import QThread, QTimer, Signal, Slot, Qt, QSize


class TabletList(QThread):
    tabletID = Signal(QGroupBox)

    def __init__(self, window, tabletID):
        super().__init__()
        self.window = window
        font = QFont()
        font.setFamilies(["Kanit"])
        font.setPointSize(14)
        font.setBold(True)
        self.current_qbox = None

        self.qbox = QGroupBox()
        self.qbox.setObjectName(f"QBoxTablet{tabletID}")
        self.qbox.setMinimumSize(QSize(200, 180))
        self.qbox.setMaximumSize(QSize(200, 180))
        self.qbox.setFont(font)
        self.qbox.setAlignment(Qt.AlignCenter)
        self.qbox.setTitle(f"เครื่องตอก {tabletID}")
        self.qbox.setStyleSheet(
            """
            	border: solid;
            	border-width: 1px;
            	border-color: rgb(255, 170, 0);
            	border-radius: 8px;
            	color: #262626;
            """
        )

        vertical_layout = QVBoxLayout(self.qbox)
        vertical_layout.setObjectName(f"verticalLayout_{tabletID}")
        vertical_layout.setContentsMargins(-1, -1, -1, 0)
        vertical_layout.setSpacing(20)

        self.button = QPushButton(self.qbox)
        self.button.setObjectName(f"tablet{tabletID}")
        self.button.setCursor(QCursor(Qt.PointingHandCursor))
        self.button.setLayoutDirection(Qt.LeftToRight)
        icon = QIcon()
        icon.addFile(":/assets/icon/machine.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button.setIcon(icon)
        self.button.setIconSize(QSize(130, 130))
        self.button.setAutoRepeat(False)
        self.button.setStyleSheet("border: none;")

        vertical_layout.addWidget(self.button)
        self.button.clicked.connect(lambda: self.setCurrentTablet(self.qbox))

    def setCurrentTablet(self, qbox: QGroupBox):
        self.tabletID.emit(qbox)

        # self.current_tabletID_1.setText(f"({tabletID})")
        # self.current_tabletID_2.setText(tabletID)
        # settings = self.settingsFile.read()
        # settings["TabletID"] = tabletID
        # self.settingsFile.write(settings)
