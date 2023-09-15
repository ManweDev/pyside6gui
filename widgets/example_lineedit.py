"""This is a richer widget than first appears"""

import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
                                QApplication,
                                QMainWindow,
                                QLineEdit,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # The parent's init function must always be called

        self.setWindowTitle("My App")

        widget = QLineEdit()
        widget.setMaxLength(12)
        widget.setPlaceholderText("Enter your phone number")
        widget.setInputMask("000-000-0000")

        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)
        widget.textEdited.connect(self.text_edited)

        self.setCentralWidget(widget)

    def return_pressed(self):
        print("Return pressed!")
        self.centralWidget().setText("BOOM!")

    def selection_changed(self):
        print(f"Selection changed! {self.centralWidget().text()}")
        #print(self.centralWidget().selectedText())


    # Called every time the text is changed
    def text_changed(self, s: str):
        print(f"Text changed: {s}")

    # Not called if text is changed by .setText()
    def text_edited(self, s):
        print(f"Text edited: {s}")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
