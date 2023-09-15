"""Example of having widgets change each other."""

import sys

from PySide6.QtWidgets import (
                                QApplication, QMainWindow,
                                QLabel, QLineEdit,
                                QVBoxLayout, QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # The parent's init function must always be called

        self.setWindowTitle("My App")

        self.label = QLabel()
        self.input = QLineEdit()

        # To connect the input to the label, both widgets have to be defined
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
