from PySide6.QtCore import QThread, Signal, Slot
from src.Alert import Alert

class TabletNumber(QThread):
    get = Signal(int)

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.current_value = ""
        self.max_range = 3 # max range
        
        ##########################   Keyboard   ##########################
        self.window.key_1.clicked.connect(lambda: self.read_key("1"))
        self.window.key_2.clicked.connect(lambda: self.read_key("2"))
        self.window.key_3.clicked.connect(lambda: self.read_key("3"))
        self.window.key_4.clicked.connect(lambda: self.read_key("4"))
        self.window.key_5.clicked.connect(lambda: self.read_key("5"))
        self.window.key_6.clicked.connect(lambda: self.read_key("6"))
        self.window.key_7.clicked.connect(lambda: self.read_key("7"))
        self.window.key_8.clicked.connect(lambda: self.read_key("8"))
        self.window.key_9.clicked.connect(lambda: self.read_key("9"))
        self.window.key_0.clicked.connect(lambda: self.read_key("0"))
        self.window.key_backspace.clicked.connect(lambda: self.read_key("backspace"))
        self.window.key_enter.clicked.connect(lambda: self.read_key("enter"))
        
        ##########################   NumberTablets   ##########################
        self.numberTablets_alert = Alert(self.window.numberTablets_input_title)
        self.numberTablets_alert_input = Alert(self.window.numberTablets_val_input)
        self.numberTablets_val_input = self.window.numberTablets_val_input

        self.initial_text = self.window.numberTablets_val_input.text()
        
    # อ่านข้อมูลจาก widgets keyboard 
    @Slot(int)
    def read_key(self, key: str):
        if key == "enter":
            value = self.current_value
            if value:
                try:
                    self.get.emit(int(value))
                except ValueError:
                    self.numberTablets_alert.alert("ข้อมูลไม่ถูกต้อง")
            else:
                self.numberTablets_alert.alert("กรุณากรอกข้อมูลให้ครบ")
        elif key == "backspace":
            if len(self.current_value) > 0:
                self.current_value = self.current_value[:-1]
                self.numberTablets_val_input.setText(f"{self.current_value} เม็ด")
                if len(self.current_value) == 0:
                    self.numberTablets_val_input.setText("XXXX")        
        else:
            if len(self.current_value) < self.max_range:
                self.current_value += key
                self.numberTablets_val_input.setText(f"{self.current_value} เม็ด")
