import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
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
    self.layout = QVBoxLayout()
    self.layout.addWidget(Color('black'))
    self.layout.addWidget(Color('red'))
    self.layout.addWidget(Color('yellow'))
    self.widget = QWidget()
    self.widget.setLayout(self.layout)
    self.setCentralWidget(self.widget)

app = QCoreApplication.instance()
if app is None:
  app = QApplication(sys.argv)
window = Window()
window.show()
app.exec_()