import sys 
import os 

PYTHONPATH = 'algebra_path'
directory_path = os.getenv(PYTHONPATH)

if directory_path:
    sys.path.append(directory_path)
else:
    current_path = os.path.abspath(__file__)
    dir_path = os.path.dirname(current_path)
    parent_path = os.path.dirname(dir_path)
    sys.path.append(parent_path)

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
    exit(app.exec())



