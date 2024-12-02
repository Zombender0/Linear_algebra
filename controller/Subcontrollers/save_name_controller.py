from views.modified_python_files.save_name_window import SaveNameWindow
from PySide6.QtCore import QThreadPool,Signal,QObject,Slot
from configparser import ConfigParser
from helpers.box_helper import warning_box,information_box

class SaveController(QObject):
    name_matrix_signal = Signal(str)
    name_equation_signal = Signal(str)
    def __init__(self,config:ConfigParser):
        super().__init__()
        self.config = config
        self.save_window = None
        
    def set_window(self,window:SaveNameWindow):
        if isinstance(self.save_window,SaveNameWindow): 
            self.save_window.deleteLater()
        self.save_window = window

    def connect_buttons(self):
        self.save_window.accept_button.clicked.connect(self.accept_matrix_button if self.save_window.mode == 'Matriz' else self.accept_equation_button)
        self.save_window.cancel_button.clicked.connect(self.cancel_button)

    @Slot()
    def accept_matrix_button(self):
        matrix_list = self.config.sections()
        matrix_list = [section.split('MATRICES.')[1] for section in matrix_list if section.startswith('MATRICES.')]
        matrix_name = self.save_window.main_line_edit.text()
        if matrix_name in matrix_list:
            warning_box('La matriz ingresada ya existe dentro del sistema')
            return None
        self.name_matrix_signal.emit(matrix_name)
        self.save_window.destroy(True)

    def accept_equation_button(self):
        equation_list = self.config.sections()
        equation_list = [section.split('ECUACIONES.')[1] for section in equation_list if section.startswith('ECUACIONES.')]
        equation_name = self.save_window.main_line_edit.text()
        if equation_name in equation_list:
            warning_box('La ecuacion ingresada ya existe dentro del sistema')
            return None
        self.name_equation_signal.emit(equation_name)
        self.save_window.destroy(True)

    @Slot()
    def cancel_button(self):
        self.save_window.destroy(True)
        
    def open_window(self):
        self.connect_buttons()
        self.save_window.show()

    def open_save_window(self):
        self.open_window()