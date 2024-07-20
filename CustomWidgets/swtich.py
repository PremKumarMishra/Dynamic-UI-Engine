from PyQt5.QtCore import Qt, QSize, QPropertyAnimation, pyqtProperty,pyqtSignal
from PyQt5.QtGui import QPainter, QColor, QBrush,QPalette
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QSizePolicy
import re


class QSwitch(QWidget):
    toggled = pyqtSignal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self._checked = False
        self._handle_position = 3
        self._handle_radius = self.height() - 6
        self.animation = QPropertyAnimation(self, b"handlePosition")
        self.animation.setDuration(200)

        self._bg_color = QColor(200, 200, 200)
        self._checked_bg_color = QColor(0, 150, 0)
        self._handle_color = QColor(255, 255, 255)

        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.setMinimumSize(60, 30)
        self.setMouseTracking(True)

    def sizeHint(self):
        return QSize(60, 30)

    def minimumSizeHint(self):
        return QSize(60, 30)

    @pyqtProperty(int)
    def handlePosition(self):
        return self._handle_position

    @handlePosition.setter
    def handlePosition(self, pos):
        self._handle_position = pos
        self.update()

    def animate(self):
        if self._checked:
            self.animation.setEndValue(self.width() - self._handle_radius - 3)
        else:
            self.animation.setEndValue(3)
        self.animation.start()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw background
        painter.setBrush(QBrush(self._checked_bg_color if self._checked else self._bg_color))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(0, 0, self.width(), self.height(), self.height() // 2, self.height() // 2)

        # Draw handle
        painter.setBrush(QBrush(self._handle_color))
        painter.drawEllipse(self._handle_position, 3, self._handle_radius, self._handle_radius)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._checked = not self._checked
            self.animate()
            self.update()
            self.toggled.emit()
    
    def isChecked(self):
        return self._checked
    
    def setChecked(self,value):
        self._checked = value
        self.animate()
        self.update()
        self.toggled.emit()

    def setFixedSize(self, width, height):
        super().setFixedSize(width, height)
        self._handle_radius = height - 6
        self.update()
    
    def setFixedWidth(self,width):
        super().setFixedWidth(width)
        self.update()
    
    def setFixedHeight(self, height):
        super().setFixedHeight(height)
        self._handle_radius = height - 6
        self.update()

    def setMinimumSize(self, width, height):
        super().setMinimumSize(width, height)
        self._handle_radius = height - 6
        self.update()

    def setMaximumSize(self, width, height):
        super().setMaximumSize(width, height)
        self._handle_radius = height - 6
        self.update()

    def setStyleSheet(self, style):
        super().setStyleSheet(style)
        parsedStylesheet = self._parseStylesheet(style)
        if 'QSwitch' in parsedStylesheet:
            if 'background' in parsedStylesheet['QSwitch']:
                self._bg_color = QColor(parsedStylesheet['QSwitch']['background'])
            elif 'background-color' in parsedStylesheet['QSwitch']:
                self._bg_color = QColor(parsedStylesheet['QSwitch']['background-color'])
        
        if 'QSwitch::handle' in parsedStylesheet:
            if 'background' in parsedStylesheet['QSwitch::handle']:
                self._handle_color = QColor(parsedStylesheet['QSwitch::handle']['background'])
            elif 'background-color' in parsedStylesheet['QSwitch::handle']:
                self._handle_color = QColor(parsedStylesheet['QSwitch::handle']['background-color'])
        
        if 'QSwitch::checked' in parsedStylesheet:
            if 'background' in parsedStylesheet['QSwitch::checked']:
                self._checked_bg_color = QColor(parsedStylesheet['QSwitch::checked']['background'])
            elif 'background-color' in parsedStylesheet['QSwitch::checked']:
                self._checked_bg_color = QColor(parsedStylesheet['QSwitch::checked']['background-color'])
        
        self.update()

    @staticmethod
    def _parseStylesheet(stylesheet):
        """
        Parses a Qt stylesheet string into a dictionary.
        """
        style_dict = {}
        selector_pattern = re.compile(r'([^\{]+)\{([^\}]+)\}')
        property_pattern = re.compile(r'([^:]+):([^;]+);')

        for selector_match in selector_pattern.finditer(stylesheet):
            selector = selector_match.group(1).strip()
            properties = selector_match.group(2).strip()
            if selector not in style_dict:
                style_dict[selector] = {}
            
            for property_match in property_pattern.finditer(properties):
                prop = property_match.group(1).strip()
                value = property_match.group(2).strip()
                style_dict[selector][prop] = value

        return style_dict

