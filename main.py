from controller.controller import MatrixController
from PySide6.QtWidgets import QMainWindow, QApplication
from sys import argv, exit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.controller = MatrixController(self)

if __name__ == '__main__':
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec())
