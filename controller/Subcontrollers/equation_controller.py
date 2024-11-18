from views.modified_python_files.equation_selecter_window import EquationSelecterWindow
from PySide6.QtCore import QThreadPool,Signal,QObject
from utils.runnable import TaskRunnable
from utils.equation_utils import equation_to_rich_text
from models.EquationFunctions import EquationEvaluator,EquationParser
from helpers.box_helper import warning_box



class EquationController(QObject):
    equation_accepted_signal = Signal(str)

    def __init__(self):
        super().__init__()
        self.equation = None
        self.equation_window = None
        self.thread_pool = QThreadPool()

    def set_window(self,window:EquationSelecterWindow)->None:
        if isinstance(self.equation_window,EquationSelecterWindow): 
            self.equation_window.deleteLater()
        self.equation_window = window
        self.equation_window.update_equation_signal.connect(self.equation_window.update_equation_label)
        self.equation_window.equation_line_edit.setText(self.equation)

    def connect_buttons(self):
        self.equation_window.x_to_n_button.clicked.connect(lambda: self.equation_window.connect_x_to_n_button())
        self.equation_window.e_button.clicked.connect(lambda: self.equation_window.connect_e_button())
        self.equation_window.pi_button.clicked.connect(lambda: self.equation_window.connect_pi_button())
        self.equation_window.cos_button.clicked.connect(lambda: self.equation_window.connect_cos_button())
        self.equation_window.sin_button.clicked.connect(lambda: self.equation_window.connect_sen_button())
        self.equation_window.tan_button.clicked.connect(lambda: self.equation_window.connect_tan_button())
        self.equation_window.sqrt_button.clicked.connect(lambda: self.equation_window.connect_sqrt_button())
        self.equation_window.equation_line_edit.textChanged.connect(lambda text: self.run_async_task(
            self.process_equation, text
        ))
        self.equation_window.accept_button.clicked.connect(lambda: self.connect_accept_button())
        self.equation_window.apply_button.clicked.connect(lambda: self.connect_apply_button())
        self.equation_window.cancel_button.clicked.connect(lambda: self.connect_cancel_button())

    def run_async_task(self,task,*args):
        task_runnable = TaskRunnable(task,*args)
        self.thread_pool.start(task_runnable)

    def process_equation(self, equation_text: str):
        processed_text = equation_to_rich_text(equation_text)
        self.equation_window.update_equation_signal.emit(processed_text)

    def connect_accept_button(self):
        equation = self.equation_window.equation_line_edit.text()
        parsed_equation = EquationParser(equation)
        if EquationEvaluator(parsed_equation,1) is None and equation != '':
            warning_box("Ecuación no válida")
            return
        self.equation = equation
        rich_text_equation = self.equation_window.equation_label.text()
        self.equation_accepted_signal.emit(rich_text_equation)
        self.equation_window.destroy(True)
        self.equation_window = None

    def connect_apply_button(self):
        equation = self.equation_window.equation_line_edit.text()
        parsed_equation = EquationParser(equation)
        if EquationEvaluator(parsed_equation,1) is None and equation != '':
            warning_box("Ecuación no válida")
            return
        self.equation = equation
        rich_text_equation = self.equation_window.equation_label.text()
        self.equation_accepted_signal.emit(rich_text_equation)

    def connect_cancel_button(self):
        self.equation_window.destroy(True)
        self.equation_window = None

    def open_window(self):
        self.connect_buttons()
        self.equation_window.show()

    def open_equation_selecter_window(self):
        self.open_window()
