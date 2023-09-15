
import sys

from PySide6.QtWidgets import (
                                QApplication,
                                QMainWindow,
                                QComboBox,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # The parent's init function must always be called

        self.setWindowTitle("My App")

        widget = QComboBox()
        widget.addItems(["One", "Two", "Three"])
        # To make the combobox editable with .setEditable(True)
        widget.setEditable(True)
        # How the insertion is handled is controlled by insertion policy
        widget.setInsertPolicy(QComboBox.InsertPolicy.InsertAtTop)
        # The number of items can also be controlled. Then the text can still
        # be changed but is not added to the combobox
        widget.setMaxCount(5)

        widget.currentIndexChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    def index_changed(self, i: int):
        print(f"Combobox index: {i}")

    def text_changed(self, s: str):
        print(f"Combobox text: {s}")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
