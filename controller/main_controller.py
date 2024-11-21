from PySide6.QtCore import Slot,QObject,QSize
from PySide6.QtWidgets import QMainWindow

from helpers.box_helper import *
from helpers.matrix_helper import *
from helpers.validation_helper import float_parser
from helpers.animation_helper import animate_side_bar
from constants.ui_constants import MAX_WIDTH
from views.modified_python_files.main_window import MainWindow 
from views.modified_python_files.solution_window import SolutionWindow
from views.modified_python_files.vector_window import VectorWindow
from views.modified_python_files.equation_selecter_window import EquationSelecterWindow

from controller.subcontrollers.solution_controller import SolutionController
from controller.subcontrollers.vector_controller import VectorController
from controller.subcontrollers.equation_controller import EquationController

from models.GaussJordan import GaussJordan
from models.GaussMethod import GaussMethod
from models.CramersRule import CramersRule
from models.InvertibleMatrix import InvertibleMatrix
from models.CramersRule import CramersRule
from models.InvertibleMatrix import InvertibleMatrix
from models.BisectionMethod import BisectionMethod
from models.NewtonRaphson import NewthonRaphson
from models.FalsePositionMethod import FalsePositionMethod
from models.SecantMethod import SecantMethod
from models.EquationFunctions import EquationParser

class MainController(QObject):
    def __init__(self,window:QMainWindow):
        super().__init__()
        self.main_window = MainWindow(window)
        self.solution_controller = SolutionController()
        self.vector_controller = VectorController()
        self.equation_controller = EquationController()
        self.equation_controller.equation_accepted_signal.connect(self.change_equation)
        self.connect_main_window_buttons()
        
    def connect_main_window_buttons(self):
        #UI
        self.main_window.matrix_tab_button.clicked.connect(lambda: self.main_window.main_stacked_widget.setCurrentIndex(0))
        self.main_window.equation_tab_button.clicked.connect(lambda: self.main_window.main_stacked_widget.setCurrentIndex(1)) 
        self.main_window.expand_button.clicked.connect(lambda: animate_side_bar(self.main_window.sub_side_bar,QSize(32,MAX_WIDTH),QSize(150,MAX_WIDTH)))
        #MATRIX
        self.main_window.table_update_button.clicked.connect(lambda: self.update_matrix_size())
        self.main_window.table_fill_0_button.clicked.connect(lambda: self.main_window.fill_matrix_0())
        self.main_window.table_clean_matrix_button.clicked.connect(lambda: self.main_window.clean_matrix())
        self.main_window.table_random_matrix_button.clicked.connect(lambda: self.main_window.random_matrix())
        self.main_window.table_solve_matrix_button.clicked.connect(lambda: self.solution_tab())
        self.main_window.table_transposition_button.clicked.connect(lambda: self.transpose_matrix())
        self.main_window.table_adjust_size_button.clicked.connect(lambda: self.main_window.adjust_matrix())
        self.main_window.table_import_from_csv_button.clicked.connect(lambda: self.main_window.import_matrix_from_csv())
        self.main_window.table_invert_button.clicked.connect(lambda: self.open_inverted_matrix_window())
        self.main_window.table_determinant_button.clicked.connect(lambda: self.open_determinant_window())
        self.main_window.table_vector_button.clicked.connect(lambda: self.open_vector_window())
        self.main_window.table_resize_checkbox.checkStateChanged.connect(lambda: self.alter_checkbox())
        #EQUATIONS
        self.main_window.edit_equation_button.clicked.connect(lambda: self.open_equation_selecter_window())
        self.main_window.bisection_solution_button.clicked.connect(lambda: self.get_root_bisection_method())
        self.main_window.newton_solution_button.clicked.connect(lambda: self.get_root_newton_method())
        self.main_window.false_solution_button.clicked.connect(lambda: self.get_root_false_position_method())
        self.main_window.secant_solution_button.clicked.connect(lambda: self.get_root_secant_method())

    @Slot()
    def solution_tab(self):
        matriz = get_data_from_table(self.main_window.input_table)
        if matriz == None:
            warning_box("No se pudo generar esta tabla")
            return
        if not MainController.__valid_matriz(matriz):
            return
        op_solution = self.main_window.table_solution_matrix_combobox.currentData()
        match op_solution:
            case 'reduccion':
                self.open_solution_window(GaussJordan(matriz))
            case 'cramer':
                self.open_cramer_window(CramersRule(matriz))
            case 'index':
                information_box("Seleccione una opcion para resolver")
            case _:
                warning_box('Error inesperado. Reinicie la aplicación')

    def alter_checkbox(self):
        resize_table(self.main_window.input_table,self.main_window.row_spinbox.value(),self.main_window.column_spinbox.value(),last_b=True,letter='X')
        if self.main_window.table_resize_checkbox.isChecked():
            self.main_window.row_spinbox.valueChanged.connect(self.main_window.update_matrix_size)
            self.main_window.column_spinbox.valueChanged.connect(self.main_window.update_matrix_size)
            return
        self.main_window.row_spinbox.valueChanged.disconnect(self.main_window.update_matrix_size)
        self.main_window.column_spinbox.valueChanged.disconnect(self.main_window.update_matrix_size)

    def open_solution_window(self,matrix_instance:GaussJordan):
        config = matrix_instance.gauss_jordan()
        self.solution_controller.set_window(SolutionWindow())
        self.solution_controller.open_solution_window(config)

    def open_vector_window(self):
        matriz = get_data_from_table(self.main_window.input_table)
        if matriz == None:
            warning_box("No se pudo generar esta tabla")
            return
        if not MainController.__valid_matriz(matriz):
            return
        self.vector_controller.set_window(VectorWindow(GaussJordan(matriz)))
        self.vector_controller.open_vector_window()
    
    def open_determinant_window(self):
        matriz = get_data_from_table(self.main_window.input_table)
        if matriz == None:
            warning_box("No se pudo generar esta tabla")
            return
        if not MainController.__valid_matriz(matriz):
            return
        matrix_instance = GaussMethod(matriz[:-1])
        config = matrix_instance.gauss_method()

        if config is False:
            warning_box("La matriz no es cuadrada")
            return
        self.solution_controller.set_window(SolutionWindow())
        self.solution_controller.open_determinant_window(config)

    def open_cramer_window(self,matrix_instance:CramersRule):
        config = matrix_instance.cramersRule()
        if config is False:
            warning_box("La matriz no es cuadrada")
            return
        self.solution_controller.set_window(SolutionWindow())
        self.solution_controller.open_cramer_window(config)

    def open_inverted_matrix_window(self):
        matriz = get_data_from_table(self.main_window.input_table)
        if matriz == None:
            warning_box("No se pudo generar esta tabla")
            return
        if not MainController.__valid_matriz(matriz):
            return
        matrix_instance = InvertibleMatrix(matriz)
        config = matrix_instance.invertibleMatrix()

        if config is False:
            warning_box("La matriz no es cuadrada")
            return
        self.solution_controller.set_window(SolutionWindow())
        self.solution_controller.open_invertible_matrix_window(config)

    def open_bisection_solution_window(self,bisection_instance:BisectionMethod):
        config = bisection_instance.bisection_method()
        if config == 'not tolerance':
            warning_box("El valor de la tolerancia debe ser entre 0 y 1")
            return
        if config == 'Error de dominio matemático':
            warning_box(config)
            return
        self.solution_controller.set_window(SolutionWindow())
        self.solution_controller.open_bisection_equation_window(config)

    def open_newton_solution_window(self,newton_instance:NewthonRaphson):
        config = newton_instance.newton_raphson_method()
        if config == 'not tolerance':
            warning_box("El valor de la tolerancia debe ser entre 0 y 1")
            return
        if config == 'Error de dominio matemático':
            warning_box(config)
            return
        self.solution_controller.set_window(SolutionWindow())
        self.solution_controller.open_newton_equation_window(config)

    def open_false_position_solution_window(self,false_position_instance:FalsePositionMethod):
        config = false_position_instance.false_position_method()
        if config == 'not tolerance':
            warning_box("El valor de la tolerancia debe ser entre 0 y 1")
            return
        if config == 'Error de dominio matemático':
            warning_box(config)
            return
        self.solution_controller.set_window(SolutionWindow())
        self.solution_controller.open_false_position_equation_window(config)

    def open_secant_solution_window(self,secant_instance:SecantMethod):
        config = secant_instance.secant_method()
        if config == 'not tolerance':
            warning_box("El valor de la tolerancia debe ser entre 0 y 1")
            return
        if config == 'Error de dominio matemático':
            warning_box(config)
            return
        self.solution_controller.set_window(SolutionWindow())
        self.solution_controller.open_secant_equation_window(config)

    def open_equation_selecter_window(self):
        self.equation_controller.set_window(EquationSelecterWindow())
        self.equation_controller.open_equation_selecter_window()

    @Slot(str)
    def change_equation(self,rich_text_equation:str):
        self.main_window.equation_text_label.setText(rich_text_equation)
    
    @Slot()
    def transpose_matrix(self):
        self.main_window.transpose_matrix()
        self.solution_combobox_changed()

    @Slot()
    def update_matrix_size(self):
        self.main_window.update_matrix_size()
        self.solution_combobox_changed()
        
    #EQUATION TAB. 

    @Slot()
    def get_root_bisection_method(self):
        interval_a = self.main_window.bisection_interval_a_line_edit.text()
        interval_b = self.main_window.bisection_interval_b_line_edit.text()
        tolerance = self.main_window.bisection_tolerance_line_edit.text()

        interval_a = float_parser(interval_a)
        interval_b = float_parser(interval_b)
        tolerance = float_parser(tolerance)

        if interval_a is False:
            warning_box('El intervalo a no es un número')
            return
        if interval_b is False:
            warning_box('El intervalo b no es un número')
            return
        if tolerance is False:
            warning_box('La tolerancia no es un número')
            return
        if interval_a > interval_b:
            warning_box('El intervalo a debe ser menor que el intervalo b')
            return
        if self.equation_controller.equation is None:
            warning_box('No se ha ingresado la ecuación a resolver')
            return
        parsed_equation = EquationParser(self.equation_controller.equation)
        bisection = BisectionMethod(parsed_equation,interval_a,interval_b,tolerance)
        self.open_bisection_solution_window(bisection)
    @Slot()
    def get_root_newton_method(self):
        x_value = self.main_window.newton_x_value_line_edit.text()
        max_iter = self.main_window.newton_max_iter_line_edit.text()
        tolerance = self.main_window.newton_tolerance_line_edit.text()

        x_value = float_parser(x_value)
        max_iter = float_parser(max_iter)
        tolerance = float_parser(tolerance)

        if x_value is False:
            warning_box('El valor de x no es un número válido')
            return
        if max_iter is False or max_iter <= 0:
            warning_box('El valor de iteraciones máximas no es un número válido')
            return
        if tolerance is False:
            warning_box('La tolerancia no es un número válido')
            return
        if self.equation_controller.equation is None:
            warning_box('No se ha ingresado la ecuación a resolver')
            return
        parsed_equation = EquationParser(self.equation_controller.equation)
        newton = NewthonRaphson(parsed_equation,x_value,tolerance,max_iter)
        self.open_newton_solution_window(newton)
    @Slot()
    def get_root_false_position_method(self):
        interval_a = self.main_window.false_interval_a_line_edit.text()
        interval_b = self.main_window.false_interval_b_line_edit.text()
        tolerance = self.main_window.false_tolerance_line_edit.text()

        interval_a = float_parser(interval_a)
        interval_b = float_parser(interval_b)
        tolerance = float_parser(tolerance)

        if interval_a is False:
            warning_box('El intervalo a no es un número')
            return
        if interval_b is False:
            warning_box('El intervalo b no es un número')
            return
        if tolerance is False:
            warning_box('La tolerancia no es un número')
            return
        if interval_a > interval_b:
            warning_box('El intervalo xl debe ser menor que el intervalo xu')
            return
        if self.equation_controller.equation is None:
            warning_box('No se ha ingresado la ecuación a resolver')
            return
        
        parsed_equation = EquationParser(self.equation_controller.equation)
        false_position = FalsePositionMethod(parsed_equation,interval_a,interval_b,tolerance)
        self.open_false_position_solution_window(false_position)

    def get_root_secant_method(self):
        interval_a = self.main_window.secant_x0_line_edit.text()
        interval_b = self.main_window.secant_xi_line_edit.text()
        tolerance = self.main_window.secant_tolerance_line_edit.text()
        max_iter = self.main_window.secant_max_iter_line_edit.text()

        interval_a = float_parser(interval_a)
        interval_b = float_parser(interval_b)
        tolerance = float_parser(tolerance)
        max_iter = float_parser(max_iter)
        
        if interval_a is False:
            warning_box('El intervalo a no es un número')
            return
        if interval_b is False:
            warning_box('El intervalo b no es un número')
            return
        if tolerance is False:
            warning_box('La tolerancia no es un número')
            return
        if interval_a > interval_b:
            warning_box('El intervalo xl debe ser menor que el intervalo xu')
            return
        if self.equation_controller.equation is None:
            warning_box('No se ha ingresado la ecuación a resolver')
            return
        parsed_equation = EquationParser(self.equation_controller.equation)
        false_position = SecantMethod(parsed_equation,interval_a,interval_b,tolerance,max_iter)
        self.open_secant_solution_window(false_position)
        
    @staticmethod
    def __valid_matriz(matriz: list[list]) ->bool:
        if matriz == []:
            warning_box('La matriz ingresada es invalida')
            return False
        width = len(matriz)
        length = len(matriz[0])
        for row in range(width):    
            if all(matriz[row][col] == 0 for col in range(length-1)) and matriz[row][-1] !=0:
                    warning_box("La matriz ingresada no tiene solucion")
                    return False
            if len(matriz[row]) != length:
                warning_box('La matriz ingresada esta incompleta')
                return False
        return True
    
