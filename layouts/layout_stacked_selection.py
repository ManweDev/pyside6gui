import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QStackedLayout,
)

from layout_colorwidget import LabelledColor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # The parent's init function must always be called

        self.setWindowTitle("My App")

        page_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stack_layout = QStackedLayout()

        page_layout.addLayout(self.stack_layout)
        page_layout.addLayout(button_layout)

        button = QPushButton("Red")
        button.clicked.connect(self.activate_tab_1)
        button_layout.addWidget(button)
        self.stack_layout.addWidget(LabelledColor("red", "Index 0 -> red"))

        button = QPushButton("Green")
        button.clicked.connect(self.activate_tab_2)
        button_layout.addWidget(button)
        self.stack_layout.addWidget(LabelledColor("green", "Index 1 -> green"))

        button = QPushButton("Yellow")
        button.clicked.connect(self.activate_tab_3)
        button_layout.addWidget(button)
        self.stack_layout.addWidget(LabelledColor("yellow", "Index 2 -> yellow"))

        widget = QWidget()
        widget.setLayout(page_layout)

        self.setCentralWidget(widget)

    def activate_tab_1(self):
        self.stack_layout.setCurrentIndex(0)

    def activate_tab_2(self):
        self.stack_layout.setCurrentIndex(1)

    def activate_tab_3(self):
        self.stack_layout.setCurrentIndex(2)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
