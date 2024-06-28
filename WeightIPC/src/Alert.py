from PySide6.QtCore import QTimer
from PySide6.QtCore import QThread, Signal
from gpiozero import Buzzer
from time import sleep

class Alert():
    def __init__(self, widget):
        self.widget = widget
        self.initial_text = self.widget.text()
        self.initial_style = self.widget.styleSheet()

    def alert(self, message: str = "", timeout: int = 1500, style: bool = True):
        """
        เก็บค่า style ใหม่ \n
        message = ข้อความแจ้งเตือน \n
        timeout = เวลาในการแสดงข้อความแจ้งเตือน เริ่มต้น 1500 ms. \n
        style = เป็น bool เพื่อกำหนดว่าจะใช้ส่วนของคุณสมบัติ background-color, padding หรือไม่
        """

        self.widget.setText(message)
        # เพิ่มส่วนของคุณสมบัติ border-radius และเก็บค่า style ใหม่
        if style:
            new_style = f"{self.initial_style} background-color: rgb(255, 17, 17); padding: 0px 20px;"
            self.widget.setStyleSheet(new_style)
        else:
            self.widget.setStyleSheet(self.initial_style)

        QTimer.singleShot(timeout, lambda: self.widget.setText(self.initial_text))
        QTimer.singleShot(timeout, lambda: self.widget.setStyleSheet(self.initial_style))
        
    def alert_always(self, message: str = "", style: bool = True):
        """
        เก็บค่า style ใหม่ \n
        message = ข้อความแจ้งเตือน \n
        style = เป็น bool เพื่อกำหนดว่าจะใช้ส่วนของคุณสมบัติ background-color, padding หรือไม่
        """
                
        self.widget.setText(message)
        # เพิ่มส่วนของคุณสมบัติ border-radius และเก็บค่า style ใหม่
        if style:
            new_style = f"{self.initial_style} background-color: rgb(255, 17, 17); padding: 0px 20px;"
            self.widget.setStyleSheet(new_style)
        else:
            self.widget.setStyleSheet(self.initial_style)

    def success(self, message: str = "", timeout: int = 1500, style: bool = True):
        """
        เก็บค่า style ใหม่ \n
        message = ข้อความแจ้งเตือน \n
        timeout = เวลาในการแสดงข้อความแจ้งเตือน เริ่มต้น 1500 ms. \n
        style = เป็น bool เพื่อกำหนดว่าจะใช้ส่วนของคุณสมบัติ background-color, padding หรือไม่
        """

        self.widget.setText(message)
        # เพิ่มส่วนของคุณสมบัติ border-radius และเก็บค่า style ใหม่
        if style:
            new_style = f"{self.initial_style} background-color: rgb(0, 170, 127); padding: 0px 20px;"
            self.widget.setStyleSheet(new_style)
        else:
            self.widget.setStyleSheet(self.initial_style)
            
        QTimer.singleShot(timeout, lambda: self.widget.setText(self.initial_text))
        QTimer.singleShot(timeout, lambda: self.widget.setStyleSheet(self.initial_style))

    def loading(self, message: str = "", style: bool = True):
        """
        เก็บค่า style ใหม่ \n
        message = ข้อความแจ้งเตือน \n
        style = เป็น bool เพื่อกำหนดว่าจะใช้ส่วนของคุณสมบัติ background-color หรือไม่
        """

        self.widget.setText(message)
        if style:
            new_style = f"{self.initial_style} background-color: rgb(0, 170, 127);"
            self.widget.setStyleSheet(new_style)
        else:
            self.widget.setStyleSheet(self.initial_style)

    def stop(self):
        self.widget.setText(self.initial_text)
        self.widget.setStyleSheet(self.initial_style)

class BuzzerAlert(QThread):
    running = Signal()

    def __init__(self, buzzer_pin, rounds:int=1, duration:int=1):
        super().__init__()
        self.rounds = rounds
        self.duration = duration
        self.BUZZER = Buzzer(buzzer_pin)

    def run(self):
        while self.rounds:
            self.BUZZER.on()
            sleep(self.duration)
            self.BUZZER.off()
            sleep(self.duration)
            self.rounds -= 1

        self.running.emit()

class BUZZER(QThread):
    def __init__(self, os_name, buzzer_pin):
        """
        os_name = "Linux" หรือ "Windows" \n
        buzzer_pin = ขา GPIO ที่ต้องการใช้งานเสียงแจ้งเตือน \n
        """
        super().__init__()
        self.os_name = os_name
        self.buzzer_pin = buzzer_pin
        self.queue = []
        
    def alert(self, duration:int=0.5, rounds:int=1):
        """
        เปิดเสียงแจ้งเตือน
        rounds = จำนวนครั้งที่ต้องการให้เสียงแจ้งเตือน \n
        duration = เวลาที่ต้องการให้เสียงแจ้งเตือน \n
        """
        if self.os_name == "Linux":
            if not hasattr(self, "buzzer"):
                self.buzzer = BuzzerAlert(self.buzzer_pin, rounds, duration)
                self.buzzer.running.connect(self._alert)
                self.buzzer.start()
            else:
                self.queue.append([rounds, duration])
        else:
            self.buzzer = None

    def _alert(self):
        self.buzzer.quit()
        self.buzzer.wait()
        del self.buzzer
        if self.queue:
            rounds = self.queue[0][0]
            duration = self.queue[0][1]
            self.buzzer = BuzzerAlert(self.buzzer_pin, rounds, duration)
            self.buzzer.running.connect(self._alert)
            self.buzzer.start()
            self.queue.pop()