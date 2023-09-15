
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
                                QApplication,
                                QMainWindow,
                                QCheckBox,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # The parent's init function must always be called

        self.setWindowTitle("My App")

        widget = QCheckBox("This is a checkbox")

        # For tristate, use Qt.CheckState.PartiallyChecked
        # or .setTristate(True)
        widget.setCheckState(Qt.CheckState.Checked)

        widget.stateChanged.connect(self.show_state)

        self.setCentralWidget(widget)

    def show_state(self, s):
        print(Qt.CheckState(s) == Qt.CheckState.Checked)
        print(Qt.CheckState(s))


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
