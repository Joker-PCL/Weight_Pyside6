from datetime import datetime
from PySide6.QtCore import QThread, Signal, Slot
import serial


class Weighing(QThread):
    """
    คลาสสำหรับอ่านค่าจากเครื่องชั่งน้ำหนัก \n
    โดยรับค่าจาก port rs232 และส่งค่ากลับไปยังคลาสอื่นๆ \n
    โดยส่งค่ากลับมาในรูปแบบข้อมูล float 
    """

    get = Signal(str, float)

    def __init__(
        self,
        port=None,
        baudrate=9600,
        number_tablets:int=0
    ):
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.number_tablets = int(number_tablets)

    def run(self):
        # self.serial = serial.Serial(port=self.port, baudrate=self.baudrate)
        # อ่านค่าจาก port rs232
        # currentWeight = str(random.uniform(0.155,0.165))
        weighing_number = 1
        while weighing_number <= self.number_tablets:
            try:
                # readSerial = self.serial.readline()
                currentWeight = input("Weight: ")
                # currentWeight = readSerial.decode("ascii", errors="ignore")
                currentWeight = currentWeight.replace("?", "").strip().upper()
                currentWeight = currentWeight.replace("G", "").strip()
                currentWeight = currentWeight.replace("N", "").strip()
                currentWeight = currentWeight.replace("S", "").strip()
                currentWeight = currentWeight.replace("T,", "").strip()  # AND FX
                currentWeight = currentWeight.replace("G", "").strip()  # AND FX
                currentWeight = currentWeight.replace("+", "").strip()
                weight = round(float(currentWeight), 3)

                now = datetime.now()  # current date and time
                timestamp = now.strftime("%H:%M:%S")
                self.get.emit(timestamp, weight)
                weighing_number += 1
            except Exception as e:
                continue
