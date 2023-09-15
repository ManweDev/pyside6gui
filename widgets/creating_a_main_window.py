from PySide6.QtWidgets import QApplication, QMainWindow

import sys

app = QApplication(sys.argv)

# A QMainWindow is a pre-made window which provides a lot of
# standard window features including toolbars, menus,
# a statusbar, dockable widgets and more.
window = QMainWindow()
window.show()

app.exec()