from PySide6.QtWidgets import QApplication, QWidget

# Only needed for access to command line arguments
import sys

app = QApplication(sys.argv)  # If no arguments needed, use an empty list

# Create a Qt widget which will be our window
# In Qt, all top level widgets are windows, which means
# we can create a window using any widget
# Every application needs at least one window
window = QWidget()
window.show()    # Windows are hidden by default

# Start the event loop for the application
# There is only one event loop per application
app.exec()
