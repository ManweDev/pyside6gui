import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QGridLayout,
)

from layout_colorwidget import Color, LabelledColor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # The parent's init function must always be called

        self.setWindowTitle("My App")

        layout = QGridLayout()
        layout.addWidget(LabelledColor("red", "0,0"), 0, 0)
        layout.addWidget(LabelledColor("green", "1,0"), 1, 0)
        layout.addWidget(LabelledColor("blue", "1,1"), 1, 1)
        layout.addWidget(LabelledColor("purple", "2,1"), 2, 1)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
