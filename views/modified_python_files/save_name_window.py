from views.generated_python_files.ui_save_name_window import Ui_save_dialog as GeneratedSavedDialog
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Slot,Signal

class SaveNameWindow(QDialog,GeneratedSavedDialog):  

    def __init__(self,parent:QDialog=None,mode:str=None):
        super().__init__(parent)
        self.mode = mode
        self.setupUi(self,self.mode)
    
    def setupUi(self, save_dialog,mode):
        super().setupUi(save_dialog)
        if mode == 'Matriz':
            self.main_line_edit.setPlaceholderText('Ingrese nombre de la matriz a guardar: ')
            self.label.setText('Ingresar nombre de matriz')
        else:
            self.main_line_edit.setPlaceholderText('Ingrese nombre de la ecuacion a guardar: ')
            self.label.setText('Ingresar nombre de la ecuacion')
    