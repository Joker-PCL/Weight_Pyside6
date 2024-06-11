from PySide6.QtWidgets import QPushButton, QGroupBox, QVBoxLayout
from PySide6.QtGui import QFont, QCursor, QIcon
from PySide6.QtCore import QThread, QTimer, Signal, Slot, Qt, QSize

class TabletList(QThread):
    tabletID = Signal(QGroupBox)

    def __init__(self, tabletID):
        super().__init__()
        font = QFont()
        font.setFamilies([u"Kanit"])
        font.setPointSize(16)

        self.qbox = QGroupBox()
        self.qbox.setObjectName(f"QBoxTablet{tabletID}")
        self.qbox.setFont(font)
        self.qbox.setMinimumSize(QSize(250, 0))
        self.qbox.setAlignment(Qt.AlignCenter)
        self.qbox.setTitle(f"เครื่องตอก {tabletID}")
        vertical_layout = QVBoxLayout(self.qbox)
        vertical_layout.setObjectName(f"verticalLayout_{tabletID}")
        vertical_layout.setContentsMargins(-1, -1, -1, 0)
        vertical_layout.setSpacing(20)

        self.button = QPushButton(self.qbox)
        self.button.setObjectName(f"tablet{tabletID}")
        self.button.setCursor(QCursor(Qt.PointingHandCursor))
        self.button.setLayoutDirection(Qt.LeftToRight)
        icon14 = QIcon()
        icon14.addFile(u":/assets/icon/machine.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button.setIcon(icon14)
        self.button.setIconSize(QSize(150, 150))
        self.button.setAutoRepeat(False)
        
        vertical_layout.addWidget(self.button)
        self.button.clicked.connect(lambda: self.setCurrentTablet(self.qbox))

    def setCurrentTablet(self, qbox: QGroupBox):
        self.tabletID.emit(qbox)
                