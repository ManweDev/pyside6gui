
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
                                QApplication,
                                QMainWindow,
                                QListWidget,
                                QListWidgetItem,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # The parent's init function must always be called

        self.setWindowTitle("My App")

        # The QListWidget supports the selection of multiple items
        widget = QListWidget()
        widget.addItems(["One", "Two", "Three"])

        widget.currentItemChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    # The currentItemChanged event returns the actual element, while the
    # currentTextChanged event returns the string representing the element
    def index_changed(self, i: QListWidgetItem):
        print(f"Index: {i.text()}")

    def text_changed(self, s: str):
        print(f"Text: {s}")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
