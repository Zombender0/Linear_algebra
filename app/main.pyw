import sys 
from PySide6.QtWidgets import QMainWindow, QApplication
from controller.main_controller import MainController

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.controller = MainController(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
