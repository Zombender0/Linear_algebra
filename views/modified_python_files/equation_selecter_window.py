from views.generated_python_files.ui_equation_selecter_window import Ui_insert_equation_dialog as GeneratedEquationDialog
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Slot,Signal

def set_cursor_position_parenthesis(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        self:EquationSelecterWindow = args[0]
        self.equation_line_edit.setFocus()
        self.equation_line_edit.setCursorPosition(self.equation_line_edit.cursorPosition()-1)
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

    @Slot()
    @set_cursor_position_parenthesis
    def connect_exp_button(self):
        self.equation_line_edit.insert('exp()')

    @Slot()
    @set_cursor_position_parenthesis
    def connect_ln_button(self):
        self.equation_line_edit.insert('ln()')
    
    @Slot()
    @set_cursor_position_parenthesis
    def connect_log_button(self):
        self.equation_line_edit.insert('log()')
    
    @Slot()
    def connect_open_parentheses_button(self):
        self.equation_line_edit.insert('(')
    @Slot()
    def connect_closed_parentheses_button(self):
        self.equation_line_edit.insert(')')
    @Slot()
    def connect_one_button(self):
        self.equation_line_edit.insert('1')
    @Slot()
    def connect_two_button(self):
        self.equation_line_edit.insert('2')
    @Slot()
    def connect_three_button(self):
        self.equation_line_edit.insert('3')
    @Slot()
    def connect_four_button(self):
        self.equation_line_edit.insert('4')
    @Slot()
    def connect_five_button(self):
        self.equation_line_edit.insert('5')
    @Slot()
    def connect_six_button(self):
        self.equation_line_edit.insert('6')
    @Slot()
    def connect_seven_button(self):
        self.equation_line_edit.insert('7')
    @Slot()
    def connect_eight_button(self):
        self.equation_line_edit.insert('8')
    @Slot()
    def connect_nine_button(self):
        self.equation_line_edit.insert('9')
    @Slot()
    def connect_zero_button(self):
        self.equation_line_edit.insert('0')
    @Slot()
    def connect_ce_button(self):
        self.equation_line_edit.backspace()
    @Slot()
    def connect_point_button(self):
        self.equation_line_edit.insert('.')
    @Slot()
    def connect_add_button(self):
        self.equation_line_edit.insert('+')
    @Slot()
    def connect_substract_button(self):
        self.equation_line_edit.insert('-')
    @Slot()
    def connect_multiply_button(self):
        self.equation_line_edit.insert('*')
    @Slot()
    def connect_divide_button(self):
        self.equation_line_edit.insert('/')

    @Slot()
    def connect_back_position(self):
        self.equation_line_edit.setFocus()
        self.equation_line_edit.setCursorPosition(self.equation_line_edit.cursorPosition()-1)
    @Slot()
    def connect_next_position_button(self):
        self.equation_line_edit.setFocus()
        self.equation_line_edit.setCursorPosition(self.equation_line_edit.cursorPosition()+1)
    @Slot(str)
    def update_equation_label(self,label_rich_text:str):
        self.equation_label.setText(label_rich_text)


