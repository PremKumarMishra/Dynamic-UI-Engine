#Window Background Image Set

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
# from PyQt5.QtGui import QPixmap, QPalette, QBrush
# from PyQt5.QtCore import Qt

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         # Set the window size
#         self.setGeometry(100, 100, 800, 600)
        
#         # Set the background image
#         self.set_background_image(r"C:\Users\Prem\Desktop\image.png")
        
#         # Add other widgets
#         label = QLabel('Hello World', self)
#         label.setStyleSheet('color: white; font-size: 24px;')

#         # Layout to center the label
#         layout = QVBoxLayout()
#         layout.addWidget(label)
#         layout.setAlignment(Qt.AlignCenter)

#         container = QWidget()
#         container.setLayout(layout)
        
#         self.setCentralWidget(container)

#     def set_background_image(self, image_path):
#         oImage = QPixmap(image_path)
#         sImage = oImage.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
#         palette = QPalette()
#         palette.setBrush(QPalette.Window, QBrush(sImage))
#         self.setPalette(palette)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     mainWindow = MainWindow()
#     mainWindow.show()
#     sys.exit(app.exec_())

#QFrame Background Image Set
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTranslator

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Using QApplication.translate for translatable strings
        hello_label = QLabel(QApplication.translate("MyWidget", "Hello, World!"))
        goodbye_label = QLabel(QApplication.translate("MyWidget", "Goodbye, World!"))

        layout.addWidget(hello_label)
        layout.addWidget(goodbye_label)

        self.setLayout(layout)
        self.setWindowTitle(QApplication.translate("MyWidget", "My Translatable App"))
        self.setGeometry(100, 100, 300, 200)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    translator = QTranslator()
    
    # Load translation file (if available)
    if translator.load("translations_fr.qm"):
        app.installTranslator(translator)
    
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
