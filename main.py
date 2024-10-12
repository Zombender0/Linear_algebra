from controller.main_controller import MainController
from PySide6.QtWidgets import QMainWindow, QApplication
from sys import argv, exit

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.controller = MainController(self)

if __name__ == '__main__':
    app = QApplication(argv)
    window = MainApp()
    window.show()
    exit(app.exec())
