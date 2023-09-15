import sys

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QToolBar,
    QWidgetAction,
    QStatusBar,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # The parent's init function must always be called

        self.setWindowTitle("My App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(24, 24))
        toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.addToolBar(toolbar)

        button_action = QWidgetAction(self)
        button_action.setIcon(QIcon("icons/layers-alignment-center.png"))
        button_action.setText("Save")
        button_action.setStatusTip("Does not really save anything. Hey!")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)

        toolbar.addAction(button_action)

        self.setStatusBar(QStatusBar(self))

        self.setCentralWidget(label)

    def onMyToolBarButtonClick(self, s: str):
        print("CLICK", s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
