import pywifi
from pywifi import const
import os
import subprocess
import re
import json
import time

from PySide6.QtGui import QPixmap
from PySide6.QtCore import QThread, Signal, Slot
from ui_weight_10inch import Ui_MainWindow


class GetWiFi(QThread):
    get = Signal(str, str, str, str)

    def __init__(self, os_name):
        super().__init__()
        self.os_name = os_name

    def run(self):
        while True:
            if self.os_name == "Windows":
                try:
                    # ใช้ netsh wlan show interfaces เพื่อดึงข้อมูลเกี่ยวกับเครือข่าย WiFi
                    output1 = subprocess.check_output(
                        "netsh wlan show interfaces"
                    ).decode("utf-8")

                    # ใช้ ipconfig เพื่อดึงข้อมูล ip address
                    output_ip = subprocess.check_output(
                        "ipconfig"
                    ).decode("utf-8")
                    ip_match = re.search(r"IPv4 Address[^\n]*: (\d+\.\d+\.\d+\.\d+)", output_ip)
                    if ip_match:
                        ip = ip_match.group(1)
                    else:
                        ip = "N/A"

                    # ค้นหา SSID
                    ssid_match = re.search(r"SSID\s+: (.+)", output1)
                    if ssid_match:
                        ssid = ssid_match.group(1)
                    else:
                        ssid = "N/A"

                    # ค้นหา Signal level
                    signal_match = re.search(r"Signal\s+: (.+)%", output1)
                    if signal_match:
                        signal = signal_match.group(1)
                    else:
                        signal = "N/A"

                    # ใช้ ping google.com -n 1 เพื่อเช็คการเชื่อมต่ออินเตอร์เน็ตกับ google.com
                    try:
                        output_ping = subprocess.check_output(
                            "ping google.com -n 1"
                        ).decode("utf-8")
                        ping_match = re.search(r"Average = (.+?)ms", output_ping)
                        if ping_match:
                            ping = ping_match.group(1)
                        else:
                            ping = "N/A"

                    except Exception as e:
                        ping = "N/A"

                    self.wifi_info(ssid, ip, signal, ping)

                except subprocess.CalledProcessError:
                    print("Error fetching WiFi information.")
                    time.sleep(3)
                    self.wifi_info()

            elif self.os_name == "Linux":
                try:
                    # ใช้ iwconfig wlan0 เพื่อดึงข้อมูลเกี่ยวกับเครือข่าย WiFi
                    output_wifi = subprocess.check_output(
                        ["iwconfig", "wlan0"]
                    ).decode("utf-8")

                    # ค้นหา SSID
                    ssid_match = re.search(r'ESSID:"(.+)"', output_wifi)
                    if ssid_match:
                        ssid = ssid_match.group(1)
                    else:
                        ssid = "N/A"

                    # ใช้ ip addr เพื่อดึงข้อมูล ip address
                    output_ip = subprocess.check_output("ip addr", shell=True).decode("utf-8")
                    ip_match = re.search(r"3: wlan0:.*?\n\s+inet (\d+\.\d+\.\d+\.\d+)", output_ip, re.DOTALL)
                    if ip_match:
                        ip = ip_match.group(1)
                    else:
                        ip = "N/A"

                    # ค้นหา Signal level
                    signal_match = re.search(r"Signal level=(-\d+) dBm", output_wifi)
                    if signal_match:
                        signal = signal_match.group(1)
                    else:
                        signal = "N/A"

                    # ใช้ ping -c 1 google.com เพื่อเช็คการเชื่อมต่ออินเตอร์เน็ตกับ google.com
                    try:
                        output_ping = subprocess.check_output(
                            ["ping", "-c", "1", "google.com"]
                        ).decode("utf-8")
                        ping_match = re.search(r"time=(\d+\.?\d*) ms", output_ping)
                        if ping_match:
                            ping = ping_match.group(1)
                        else:
                            ping = "N/A"

                    except Exception as e:
                        ping = "N/A"

                    self.wifi_info(ssid, ip, signal, ping)

                    output_ip = ""

                except subprocess.CalledProcessError:
                    print("Error fetching WiFi information.")
                    self.wifi_info()
                    time.sleep(5)

            time.sleep(1)

    def wifi_info(self, ssid="N/A", ip="N/A", signal="N/A", ping="N/A"):
        self.ssid = ssid
        self.ip = ip
        self.signal = signal
        self.ping = ping
        self.get.emit(ssid, ip, signal, ping)

class WiFi(QThread):
    """การเชื่อมต่อไวไฟ"""

    def __init__(self, window: Ui_MainWindow, os_name="Windows"):
        super().__init__()
        self.signalWidget1 = window.wifi_signal
        self.signalWidget2 = window.wifi_signal_2
        self.ssidWidget = window.ssid
        self.pingWidget2 = window.ping
        self.os_name = os_name
        self.ssid = ""
        self.password = ""
        self.DISCONNECTED = 0
        self.CONNECTED = 1
        self.listener = None
        self.scaner_flag = False
        self.wifi = pywifi.PyWiFi()
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.ICON_DIR = os.path.join(self.BASE_DIR, "..", "assets", "icon")
        self.noSignal_icon = os.path.join(self.ICON_DIR, "no-wifi.png")
        self.signal1_icon = os.path.join(self.ICON_DIR, "signal1.png")
        self.signal2_icon = os.path.join(self.ICON_DIR, "signal2.png")
        self.signal3_icon = os.path.join(self.ICON_DIR, "signal3.png")
        self.signal4_icon = os.path.join(self.ICON_DIR, "signal4.png")
        self.no_internet_icon = os.path.join(self.ICON_DIR, "no_internet.png")

        self.getWiFi = GetWiFi(self.os_name)
        self.getWiFi.get.connect(self.signal_icon)
        self.getWiFi.start()
        print("Active Wifi")

    @Slot(str, str, str, str)
    def signal_icon(self, ssid, ip, signal, ping):
        self.ssid = ssid
        self.ip = ip
        self.signal = signal
        self.ping = ping

        if self.ssid == "N/A":
            signal = self.noSignal_icon
        elif self.ping == "N/A":
            signal = self.no_internet_icon
        elif self.signal == "N/A":
            signal = self.noSignal_icon
        elif self.os_name == "Windows":
            if int(self.signal) <= 25:
                signal = self.signal1_icon
            elif int(self.signal) <= 50:
                signal = self.signal2_icon
            elif int(self.signal) <= 75:
                signal = self.signal3_icon
            else:
                signal = self.signal4_icon
        elif self.os_name == "Linux":
            if int(self.signal) <= -90:
                signal = self.signal1_icon
            elif int(self.signal) <= -60:
                signal = self.signal2_icon
            elif int(self.signal) <= -30:
                signal = self.signal3_icon
            else:
                signal = self.signal4_icon

        self.signalWidget1.setPixmap(QPixmap(signal))
        self.signalWidget2.setPixmap(QPixmap(signal))
        self.ssidWidget.setText(f"SSID: {self.ssid} IP: {self.ip}")
        self.pingWidget2.setText(f"Ping: {self.ping} ms")