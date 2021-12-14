
from PySide6.QtCore import QEasingCurve, QObject, QPoint, QPropertyAnimation, QSequentialAnimationGroup, QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
import sys

class AnimatedButton(QWidget):
    def __init__(self, height, width, text, color):
        super().__init__()

        self.rec = QWidget(self)
        self.rec.setStyleSheet("background-color:"+color)
        self.rec.setGeometry(0,0,height,width+10)

        self.button = QPushButton(self)
        self.button.setGeometry(0,0,height,width)
        self.button.setText(text)

        self.anim = QPropertyAnimation(self.rec, b"size")
        self.anim.setEndValue(QSize(height, width))
        self.anim.setDuration(80)

        self.anim1 = QPropertyAnimation(self.rec, b"size")
        self.anim1.setEndValue(QSize(height, width+10))
        self.anim1.setDuration(80)

        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim)
        self.anim_group.addAnimation(self.anim1)
        

        self.button.clicked.connect(self.animation)

    def animation(self):
        self.anim_group.start()


    

        
