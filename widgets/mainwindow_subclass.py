
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

        button = QPushButton("Press Me!")

        self.setCentralWidget(button)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
