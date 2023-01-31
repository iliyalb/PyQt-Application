from PySide6.QtWidgets import QMainWindow, QPushButton


class ButtonPlacement(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MainWindow")
        button = QPushButton("OK")
        self.setCentralWidget(button)
