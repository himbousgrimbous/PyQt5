import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
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
        self.setWindowTitle("Grid Layouts")
        self.layout = QGridLayout()

        for x in range(4):
            for y in range(4):
                
                if x%2==0:
                    if y%2==0:
                        self.layout.addWidget(Color('Black'),x,y)
                    else:
                        self.layout.addWidget(Color("White"),x,y)
            
                else:
                    if y%2!=0:
                        self.layout.addWidget(Color('Black'),x,y)
                    else:
                        self.layout.addWidget(Color('White'),x,y)
                    
        
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

app = QCoreApplication.instance()
if app is None:
    app = QApplication(sys.argv)
window = Window()
window.show()
app.exec_()
                