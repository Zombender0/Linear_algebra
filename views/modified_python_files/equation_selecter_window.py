from views.generated_python_files.ui_equation_selecter_window import Ui_insert_equation_dialog as GeneratedEquationDialog
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Slot,Signal

def set_cursor_position_parenthesis(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        self:EquationSelecterWindow = args[0]
        self.equation_line_edit.setFocus()
        self.equation_line_edit.setCursorPosition(len(self.equation_line_edit.text())-1)
        return result
    return wrapper

class EquationSelecterWindow(QDialog,GeneratedEquationDialog):
    update_equation_signal = Signal(str)
    
    def __init__(self,parent:QDialog=None):
        super().__init__(parent)
        self.setupUi(self)

    def setupUi(self, insert_equation_dialog):
        super().setupUi(insert_equation_dialog)
        self.equation_line_edit.setClearButtonEnabled(True)
        self.setWindowTitle('Ingresar ecuación')

    @Slot()
    @set_cursor_position_parenthesis
    def connect_x_to_n_button(self):
        self.equation_line_edit.insert('**()')
    @Slot()
    def connect_e_button(self):
        self.equation_line_edit.insert('e')
    @Slot()
    def connect_pi_button(self):
        self.equation_line_edit.insert('π')
    @Slot()
    @set_cursor_position_parenthesis
    def connect_cos_button(self):
        self.equation_line_edit.insert('cos()')
    @Slot()
    @set_cursor_position_parenthesis
    def connect_sen_button(self):
        self.equation_line_edit.insert('sen()')
    @Slot()
    @set_cursor_position_parenthesis
    def connect_tan_button(self):
        self.equation_line_edit.insert('tan()')
    @Slot()
    @set_cursor_position_parenthesis
    def connect_sqrt_button(self):
        self.equation_line_edit.insert('√()')

    @Slot(str)
    def update_equation_label(self,label_rich_text:str):
        self.equation_label.setText(label_rich_text)



