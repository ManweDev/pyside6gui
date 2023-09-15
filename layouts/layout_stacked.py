import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QStackedLayout,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
)

from layout_colorwidget import LabelledColor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # The parent's init function must always be called

        self.setWindowTitle("My App")

        layout = QStackedLayout()
        layout.addWidget(LabelledColor("red", "1"))
        layout.addWidget(LabelledColor("green", "2"))
        layout.addWidget(LabelledColor("blue", "3"))
        layout.addWidget(LabelledColor("yellow", "4"))
        layout.setCurrentIndex(3)  # Zero-based, in widget addition order

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
