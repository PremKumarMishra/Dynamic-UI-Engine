from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(639,390)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv) #"QT_AUTO_SCREEN_SCALE_FACTOR 1"
    win = window()
    win.show()
    app.exec()