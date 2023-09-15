import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)
from layout_colorwidget import Color, LabelledColor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # The parent's init function must always be called

        self.setWindowTitle("My App")

        # We just need to change to a QHBoxLayout to get horizontal placement
        layout = QVBoxLayout()
        layout.addWidget(LabelledColor("red", "Red"))
        layout.addWidget(LabelledColor("green", "Green"))
        layout.addWidget(LabelledColor("blue", "Blue"))

        # We need a dummy widget to hold our layouts
        # We see borders. That is controlled by the layouts spacing, which is settable
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
