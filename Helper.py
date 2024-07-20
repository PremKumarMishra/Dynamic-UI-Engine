from PyQt5.QtCore import QObject,QPropertyAnimation,QVariantAnimation,QAbstractAnimation,QEvent,QRect,QSize
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication
import re
import math

SCALE_FACTOR = 1

#Animation Hover Handler
class HoverHandler(QObject):
    def __init__(self, widget, animation_data):
        super().__init__(widget)
        self.widget = widget
        self.animation_data = animation_data
        self.animation = None

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.Enter:
            self.start_animation()
        elif event.type() == QEvent.Type.Leave:
            self.stop_animation()
        return super().eventFilter(obj, event)

    def start_animation(self):
        animation_type = self.animation_data.get('type')
        duration = self.animation_data.get('duration', 1000)
        # if animation_type == 'opacity':
        #     self.animation = QPropertyAnimation(self.widget, b"windowOpacity")
        #     self.animation.setStartValue(self.animation_data.get('start_value', 0.0))
        #     self.animation.setEndValue(self.animation_data.get('end_value', 1.0))
        #     self.animation.setDuration(duration)
        #     self.animation.start()
        # elif animation_type == 'position':
        #     self.animation = QPropertyAnimation(self.widget, b"geometry")
        #     start_pos = self.animation_data.get('start_value', [0, 0])
        #     end_pos = self.animation_data.get('end_value', [100, 100])
        #     start_rect = QRect(start_pos[0], start_pos[1], self.widget.width(), self.widget.height())
        #     end_rect = QRect(end_pos[0], end_pos[1], self.widget.width(), self.widget.height())
        #     self.animation.setStartValue(start_rect)
        #     self.animation.setEndValue(end_rect)
        #     self.animation.setDuration(duration)
        #     self.animation.start()
        # elif animation_type == 'size':
        #     self.animation = QPropertyAnimation(self.widget, b"size")
        #     start_size = self.animation_data.get('start_value', [0, 0])
        #     end_size = self.animation_data.get('end_value', [100, 100])
        #     start_rect = QSize(*start_size)
        #     end_rect = QSize(*end_size)
        #     self.animation.setStartValue(start_rect)
        #     self.animation.setEndValue(end_rect)
        #     self.animation.setDuration(duration)
        #     self.animation.start()
        if animation_type == 'color':
            self.animation = QVariantAnimation(self.widget)
            start_color = self.animation_data.get('start_value', [0, 0, 0, 255])
            end_color = self.animation_data.get('end_value', [255, 255, 255, 255])
            start_rect = QColor(*start_color)
            end_rect = QColor(*end_color)
            self.animation.setStartValue(start_rect)
            self.animation.setEndValue(end_rect)
            self.animation.setDuration(duration)
            self.animation.valueChanged.connect(self.applyColorAnimation)
            self.animation.start()
    
    def applyColorAnimation(self,color:QColor):
        property_name = self.animation_data.get('property', 'background')
        stylesheet = self.widget.styleSheet()

        new_style = ""
        if property_name == 'background':
            new_style = f"background-color: rgba({color.red()},{color.green()},{color.blue()},{color.alpha()});"
        elif property_name == 'border':
            new_style = f"border-color: rgba({color.red()},{color.green()},{color.blue()},{color.alpha()});"
        elif property_name == 'color':
            new_style = f"color: rgba({color.red()},{color.green()},{color.blue()},{color.alpha()});"

        # Find existing style for the property and replace it
        if f"{property_name}-color:" in stylesheet:
            stylesheet = re.sub(f"{property_name}-color:.*?;", new_style, stylesheet)
        elif f"{property_name}:" in stylesheet:
            stylesheet = re.sub(f"{property_name}:.*?;", new_style, stylesheet)
        else:
            stylesheet += new_style

        self.widget.setStyleSheet(stylesheet)

    def stop_animation(self):
        if self.animation:
            self.animation.setDirection(QAbstractAnimation.Direction.Backward)
            self.animation.start()


#Calculate Scaling Factor
def calculateScaleFactor(base_width:int, base_height:int):
    global SCALE_FACTOR
    primaryScreen = QApplication.primaryScreen()
    target_width = primaryScreen.size().width()
    target_height = primaryScreen.size().height()
    width_scale = target_width / base_width
    height_scale = target_height / base_height
    SCALE_FACTOR = math.sqrt(width_scale * height_scale)

    del primaryScreen
    del target_width
    del target_height
    del width_scale
    del height_scale 
    print(SCALE_FACTOR)
