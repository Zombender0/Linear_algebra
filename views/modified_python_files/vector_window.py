from views.generated_python_files.ui_vector_window import Ui_main_widget as Generated_VectorWindow
from PySide6.QtWidgets import (QHBoxLayout, QLabel,QListWidget, QPushButton,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,QTextEdit,
    QWidget)
from PySide6.QtCore import Slot
from helpers.matrix_helper import *
from copy import deepcopy
class VectorWindow(QWidget,Generated_VectorWindow):
    def __init__(self,matrix:list[list]):
        super.__init__()
        self.matrix_instance = deepcopy(matrix)
        self.setupUi()
    
    def setupUi(self, main_widget):
        super().setupUi(main_widget)
    