import sys
from PySide6.QtWidgets import QApplication
from button_placement import ButtonPlacement

app = QApplication(sys.argv)
window = ButtonPlacement()
window.show()
app.exec()
