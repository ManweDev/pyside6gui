import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
                                QApplication,
                                QMainWindow,
)
from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # The parent's init function must always be called

        self.setWindowTitle("My App")

        widget = Color("red")

        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
