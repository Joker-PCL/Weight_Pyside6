import sys
import os

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from weight import WeightIPC

##################################### ตั้งค่า ######################################
#################################################################################
OS_NAME = "Windows"  # ตั้งค่าระบบปฏิบัติการ
BALANCE_PORT_WINDOWS = "COM6"  # พอร์ต RS232 ** Windows("COM6")
BALANCE_PORT_LINUX = "/dev/ttyUSB0"  # พอร์ต RS232 ** Linux("/dev/ttyUSB0")
#################################################################################
#################################################################################

if OS_NAME == "Windows":
    os.environ["QT_MEDIA_BACKEND"] = "windows"
    # os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"
    BALANCE_PORT = BALANCE_PORT_WINDOWS
elif OS_NAME == "Linux":
    os.environ["QT_MEDIA_BACKEND"] = "gstreamer"
    BALANCE_PORT = BALANCE_PORT_LINUX

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STYLE = os.path.join(BASE_DIR, "style.qss")
ICON = os.path.join(BASE_DIR, "assets", "images", "scale.png")

TOKEN = os.path.join(BASE_DIR, "files", "token.pickle")
CREDENTIALS = os.path.join(BASE_DIR, "files", "credentials.json")
SETTINGS = os.path.join(BASE_DIR, "files", "settings.json")


def main():
    app = QApplication(sys.argv)

    with open(STYLE, "r") as file:
        _style = file.read()
        app.setStyleSheet(_style)

    # เลือกจอที่สอง
    screens = app.screens()
    second_screen = screens[1]

    # สร้างหน้าต่างหลัก
    window = WeightIPC(OS_NAME, TOKEN, CREDENTIALS, SETTINGS, BALANCE_PORT)
    window.resize(1280, 800)
    # window.resize(1024, 600)
    window.move(0, 0)
    window.setWindowIcon(QIcon(ICON))
    window.setWindowTitle("Weight IPC'")
    window.setWindowFlags(
        Qt.FramelessWindowHint | Qt.WindowTitleHint | Qt.WindowStaysOnTopHint
    )
    window.setGeometry(second_screen.availableGeometry())  # ให้หน้าต่างเต็มจอ
    window.showFullScreen()
    # window.show()

    # sounds_folder = os.path.join(BASE_DIR, "sounds")
    # file = 'sound1.mp3'
    # test_sounds = PlaySound(sounds_folder)
    # test_sounds.play_all()

    window.run()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
