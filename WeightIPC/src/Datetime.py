from PySide6.QtWidgets import QLabel
from datetime import datetime
from PySide6.QtCore import QTimer

class ShowDateTime:
    """ แสดงวันที่, เวลา """
    def __init__(self, date_bar: QLabel, time_bar: QLabel):
        self.date_bar = date_bar
        self.time_bar = time_bar

    def print_datetime(self):
        now = datetime.now()  # current date and time
        curr_date = now.strftime("%d/%m/%Y")
        curr_time = now.strftime("%H:%M:%S")
        self.date_bar.setText(curr_date)
        self.time_bar.setText(curr_time)

    def show(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.print_datetime)
        self.timer.setInterval(1000)
        self.timer.start()

