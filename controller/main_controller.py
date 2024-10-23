from helpers.box_helper import *
from helpers.matrix_helper import *
from views.modified_python_files.main_window import MainWindow 
from views.modified_python_files.solution_window import SolutionWindow
from views.modified_python_files.vector_window import VectorWindow

from controller.subcontrollers.solution_controller import SolutionController
from controller.subcontrollers.vector_controller import VectorController

from models.GaussJordan import GaussJordan
from models.GaussMethod import GaussMethod
from models.CramersRule import CramersRule
from models.InvertibleMatrix import InvertibleMatrix
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QTableWidgetItem,QMainWindow,QWidget

#Continue here

class MainController():
    def __init__(self,window:QMainWindow):
        self.main_window = MainWindow(window)
        self.solution_controller = SolutionController()
        self.vector_controller = VectorController()
        #self.vector_controller = VectorController()
        self.connect_main_window_buttons()
        
    def connect_main_window_buttons(self):
        self.main_window.table_update_button.clicked.connect(lambda: self.main_window.update_matrix_size())
        self.main_window.table_fill_0_button.clicked.connect(lambda: self.main_window.fill_matrix_0())
        self.main_window.table_clean_matrix_button.clicked.connect(lambda: self.main_window.clean_matrix())
        self.main_window.table_random_matrix_button.clicked.connect(lambda: self.main_window.random_matrix())
        self.main_window.table_solve_matrix_button.clicked.connect(lambda: self.solution_tab())
        self.main_window.table_transposition_button.clicked.connect(lambda: self.main_window.transpose_matrix())
        self.main_window.table_adjust_size_button.clicked.connect(lambda: self.main_window.adjust_matrix())
        self.main_window.table_import_from_csv_button.clicked.connect(lambda: self.main_window.import_matrix_from_csv())
        self.main_window.table_solution_matrix_combobox.currentIndexChanged.connect(lambda: self.solution_combobox_changed())
    @Slot()
    def change_horizontal_headers(self):
        pass
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
            case 'vector':
                self.open_vector_window(GaussJordan(matriz))
            case 'determinante':
                self.open_determinant_window(GaussMethod(matriz))
            case 'cramer':
                self.open_cramer_window(CramersRule(matriz))
            case 'invertible':
                self.open_inverted_matrix_window(InvertibleMatrix(matriz))
            case _:
                information_box("Seleccione una opcion para resolver")

    def open_solution_window(self,matrix_instance:GaussJordan):
        config = matrix_instance.gauss_jordan()
        self.solution_controller.set_window(SolutionWindow())
        self.solution_controller.open_solution_window(config)

    def open_vector_window(self,matrix_instance:GaussJordan):
        self.vector_controller.set_window(VectorWindow(matrix_instance))
        self.vector_controller.open_vector_window()
    
    def open_determinant_window(self,matrix_instance:GaussMethod):
        config = matrix_instance.gauss_method()
        if config is False:
            warning_box("La matriz no es cuadrada")
            return
        self.solution_controller.set_window(SolutionWindow())
        self.solution_controller.open_determinant_window(config)

    def open_cramer_window(self,matrix_instance:CramersRule ):
        config = matrix_instance.cramersRule()
        if config is False:
            warning_box("La matriz no es cuadrada")
            return
        self.solution_controller.set_window(SolutionWindow())
        self.solution_controller.open_cramer_window(config)

    def open_inverted_matrix_window(self,matrix_instance:InvertibleMatrix):
        config = matrix_instance.invertibleMatrix()
        if config is False:
            warning_box("La matriz no es cuadrada")
            return
        self.solution_controller.set_window(SolutionWindow())
        self.solution_controller.open_invertible_matrix_window(config)
    @Slot()
    def solution_combobox_changed(self):
        option = self.main_window.table_solution_matrix_combobox.currentData()
        if option == 'determinante' or option == 'invertible':
            resize_table(self.main_window.input_table,
                         self.main_window.row_spinbox.value(),
                         self.main_window.column_spinbox.value(),
                         last_b=False)
        else:
            resize_table(self.main_window.input_table,
                         self.main_window.row_spinbox.value(),
                         self.main_window.column_spinbox.value(),
                         last_b=True)

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