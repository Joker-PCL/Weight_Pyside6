from PySide6.QtCore import QTimer
from PySide6.QtGui import QPixmap
import os

class ShowImage():
    def __init__(self, front_widget, behind_widget, paths):
        self.tablet_front_img = front_widget
        self.tablet_behind_img = behind_widget
        self.paths = paths
        self.image_index = 0
        
    def show(self, front_img, behind_img):
        self.tablet_front_img.setPixmap(QPixmap(front_img))
        self.tablet_behind_img.setPixmap(QPixmap(behind_img))
        