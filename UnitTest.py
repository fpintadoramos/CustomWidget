import unittest
from PySide6 import QtWidgets

from PySide6.QtWidgets import QApplication
from CustomWidget import AnimatedButton

class NamesTestCase(unittest.TestCase):
    app = QApplication([])
    def test_buttonColor(self):
        window = AnimatedButton(100,50)
        result = window.getColor()
        self.assertEqual(result, "white")

    def test_buttonText(self):
        window = AnimatedButton(100,50)
        result = window.getText()
        self.assertEqual(result, "Button")

    def test_buttonCustomColor(self):
        window = AnimatedButton(100,50)
        window.setColor("green")
        result = window.getColor()
        self.assertEqual(result, "green")

    def test_buttonCustomText(self):
        window = AnimatedButton(100,50)
        window.setText("boton")
        result = window.getText()
        self.assertEqual(result, "boton")

if __name__ == '__main__':
    unittest.main()