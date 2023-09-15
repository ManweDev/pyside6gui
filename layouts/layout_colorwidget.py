from PySide6.QtCore import Qt

from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout


class Color(QWidget):
    def __init__(self, color: str):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


class LabelledColor(Color):
    def __init__(self, color: str, text: str):
        super().__init__(color)

        # Create the label and set it to display the row and column
        label = QLabel(text)

        # Change the font to 30 points
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)

        # Lay out our label in the center of the widget
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        # And display it
        self.setLayout(layout)
