
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtCore import QCoreApplication
class Color(QWidget):
  def __init__(self, color):
    super().__init__()
    self.setAutoFillBackground(True) 
    self.myPalette = self.palette() 
    self.myPalette.setColor(QPalette.Window, QColor(color))
    self.setPalette(self.myPalette) 

class Window(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("HO Box Layouts")
    self.layout = QHBoxLayout()
    self.layout.addWidget(Color('blue'))
    self.layout.addWidget(Color('white'))
    self.layout.addWidget(Color('red'))
    self.widget = QWidget()
    self.widget.setLayout(self.layout)
    self.setCentralWidget(self.widget)

app = QCoreApplication.instance()
if app is None:
  app = QApplication(sys.argv)
window = Window()
window.show()
app.exec_()