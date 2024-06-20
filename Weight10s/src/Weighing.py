from PySide6.QtCore import QThread, Signal, Slot
import serial


class Weighing(QThread):
    """
    คลาสสำหรับอ่านค่าจากเครื่องชั่งน้ำหนัก \n
    โดยรับค่าจาก port rs232 และส่งค่ากลับไปยังคลาสอื่นๆ \n
    โดยส่งค่ากลับมาในรูปแบบข้อมูล dict ดังนี้    \n
    { \n
        "weight1": 0.000, \n
        "weight2": 0.000, \n
        "average": 0.000 \n
    } \n
    """

    get = Signal(object)
    hidden = Signal(bool)

    def __init__(
        self,
        port=None,
        baudrate=9600,
    ):
        super().__init__()
        self.port = port
        self.baudrate = baudrate

    def run(self):
        # self.serial = serial.Serial(port=self.port, baudrate=self.baudrate)
        self.weighing = []

        # อ่านค่าจาก port rs232
        # currentWeight = str(random.uniform(0.155,0.165))

        while len(self.weighing) < 2:
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
                self.weighing.append(weight)

                self.get.emit(self.weighing)
                self.hidden.emit(True)
            
            except Exception as e:
                continue
