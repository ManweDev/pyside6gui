
import sys

from PySide6.QtWidgets import (
                                QApplication,
                                QMainWindow,
                                QPushButton,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # The parent's init function must always be called

        self.setWindowTitle("My App")

        # We could also use .setFixedSize(minWidth, minHeight)
        self.setMinimumSize(400, 300)  # minWidth, minHeight
        self.setMaximumSize(600, 500)  # maxWidth, maxHeight

        # We need to keep a reference to this widget to be able to
        # access it in our slot.
        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        self.button_is_checked = True
        self.button.released.connect(self.the_button_was_released)

        self.setCentralWidget(self.button)

    # The released event does not send the checked state, so we need to access it
    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()
        print("Checked?", self.button_is_checked)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
