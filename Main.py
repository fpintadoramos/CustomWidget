from PySide6.QtWidgets import QApplication, QBoxLayout, QFormLayout, QMainWindow, QVBoxLayout, QWidget
import sys

from CustomWidget import AnimatedButton

class MainWindow (QWidget):
    def __init__(self):
        super().__init__()
        self.l = QVBoxLayout(self)
        self.boton = AnimatedButton(100, 50, "Añadir", "green")
        self.boton1 = AnimatedButton(200, 50, "Eliminar", "red")
        
        self.l.addWidget(self.boton)
        self.l.addWidget(self.boton1)

        self.setLayout(self.l)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()