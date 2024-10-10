from views.message_box import warning_box
from views.ui_main_window import Ui_MainWindow 
from views.ui_solution_window import Ui_main_widget as Ui_solution
from views.ui_vector_window import Ui_main_widget as Ui_vector
from models.GaussJordan import GaussJordan
from PySide6.QtCore import Slot,Qt
from PySide6.QtWidgets import QTableWidgetItem,QMainWindow,QWidget
from random import randint

class MatrixController():
    def __init__(self,MainWindow):
        self.main_window = Ui_MainWindow(MainWindow)
        self.connect_main_window_buttons()
        self.main_window.fill_table_widgets()
        self.main_window.input_table.resizeColumnsToContents()
        
    def connect_main_window_buttons(self):
        self.main_window.table_update_button.clicked.connect(lambda: self.main_window.resize_matrix(
            self.main_window.column_spinbox.value(),
            self.main_window.row_spinbox.value()
        ))
        self.main_window.table_fill_0_button.clicked.connect(self.main_window.fill_matrix_0)
        self.main_window.table_clean_matrix_button.clicked.connect(self.main_window.clean_matrix)
        self.main_window.table_random_matrix_button.clicked.connect(self.main_window.random_matrix)
        self.main_window.table_solve_matrix_button.clicked.connect(lambda: self.solution_tab())
        self.main_window.table_transposition_button.clicked.connect(lambda: self.mostrar_matriz_transpuesta())

    @Slot()
    def solution_tab(self):
        matriz = self.main_window.generate_matrix()
        if matriz == None:
            warning_box("No se pudo generar esta tabla")
            return
        if not MatrixController.__valid_matriz(matriz):
            return
        op_solution = self.main_window.table_solution_matrix_combobox.currentData()
        match op_solution:
            case 'reduccion':
                self.open_solution_window(GaussJordan(matriz))
            case 'vxv':
                self.open_vector_window(GaussJordan(matriz))
                pass
            case _:
                warning_box("Seleccione una opcion para resolver")

    def open_solution_window(self,matrix: GaussJordan):
        self.solution_window = Ui_solution()
        self.window = QWidget()
        self.solution_window.setupUi(self.window)
        self.window.setWindowTitle(u'Solución detallada')
        self.solution_window.create_tab_solutions  (matrix.gauss_jordan())
        self.connect_solution_window_buttons()
        self.window.show()

    @Slot()
    def connect_solution_window_buttons(self):
        self.solution_window.tabWidget.currentChanged.connect(self.solution_window.show_step_property)
        self.solution_window.next_tab_button.clicked.connect(self.solution_window.next_tab)
        self.solution_window.back_tab_button.clicked.connect(self.solution_window.previous_tab)

    def open_vector_window(self,matriz:GaussJordan):
        self.vector_window = Ui_vector(matriz.matriz)
        self.window = QWidget()
        self.vector_window.setupUi(self.window)
        self.connect_vector_window_buttons()
        self.window.show()
    
    def connect_vector_window_buttons(self):
        self.vector_window.vxv_row_spinbox.valueChanged.connect(self.vxv_change_row_vector)
        self.vector_window.vxv_solve_scalar_button.clicked.connect(self.vxv_show_scalar)
        self.vector_window.mxv_solution_button.clicked.connect(self.mxv_show_scalar)
        self.vector_window.mxm_solution_button.clicked.connect(lambda: self.mxm_generate_matrix_c_button())
    @Slot()
    def vxv_change_row_vector(self):
        row_number = self.vector_window.vxv_row_spinbox.value()
        if row_number <= 0:
            self.vector_window.vxv_row_spinbox.setValue(0)
            return
        if row_number > len(self.vector_window.matrix_instance): 
            self.vector_window.vxv_row_spinbox.setValue(row_number-1)
            return
        self.vector_window.vxv_set_vector_row(self.vector_window.matrix_instance[row_number-1])

    @Slot()
    def vxv_show_scalar(self):
        column_vector = self.vxv_get_column_vector()
        if column_vector is None:return
        row_vector = self.vxv_get_row_vector()
        if row_vector is None: return
        scalar = GaussJordan.vxv_get_scalar(row_vector,column_vector)
        row = self.vector_window.vxv_row_spinbox.value()
        self.vector_window.vxv_scalar_label.setText(f'Vector fila {row} X vector columna b: {scalar}')

    @Slot()
    def mxv_show_scalar(self):
        vector = self.mxv_get_column_vector() if self.vector_window.mxv_column_vector_table.columnCount() == 1 else self.mxv_get_matrix_vector() 
        if vector is None:return  
        self.solution_scalar_window = Ui_solution()
        self.scalar_window = QWidget()
        self.solution_scalar_window.setupUi(self.scalar_window)
        self.scalar_window.setWindowTitle(u"Escalares")
        self.solution_scalar_window.create_scalar_solution(GaussJordan.mxv_get_scalar(self.vector_window.matrix_instance,vector))
        self.scalar_window.show()
    
    def vxv_get_column_vector(self):
        vector = list()
        for row in range(self.vector_window.vxv_column_vector.rowCount()):
            table_item = self.vector_window.vxv_column_vector.item(row,0)
            if table_item is None:
                warning_box('Vector columna incompleto')
                return
            try:
                vector.append(float(table_item.text()))
            except ValueError:
                warning_box(f'Fila {row+1}: {table_item.text()} no es un número')
                return
            except Exception as e:
                warning_box(f'Error inesperado: {e}')
                return
        return vector
    
    def vxv_get_row_vector(self):
        vector = list()
        for column in range(self.vector_window.vxv_row_vector.columnCount()):
            table_item = self.vector_window.vxv_row_vector.item(0,column)
            try:
                vector.append(float(table_item.text()))
            except Exception as e:
                warning_box(f'Error inesperado: {e}')
                return
        return vector
    
    def mxv_get_column_vector(self):
        vector = list()
        for row in range(self.vector_window.mxv_column_vector_table.rowCount()):
            table_item = self.vector_window.mxv_column_vector_table.item(row,0)
            if table_item is None:
                warning_box('Vector columna incompleto')
                return
            try:
                vector.append(float(table_item.text()))
            except ValueError:
                warning_box(f'Fila {row+1}: {table_item.text()} no es un número')
                return
            except Exception as e:
                warning_box(f'Error inesperado: {e}')
                return
        return vector

    def mxv_get_matrix_vector(self):
        matrix = [] 
        for row in range(self.vector_window.mxv_column_vector_table.rowCount()):
            vector = []  
            for col in range(self.vector_window.mxv_column_vector_table.columnCount()):
                table_item = self.vector_window.mxv_column_vector_table.item(row, col)
                if table_item is None:
                    warning_box('Vector columna incompleto')
                    return  
                try:
                    vector.append(float(table_item.text()))  
                except ValueError:
                    warning_box(f'Fila {row + 1}: {table_item.text()} no es un número')
                    return  
                except Exception as e:
                    warning_box(f'Error inesperado: {e}')
                    return 

            matrix.append(vector) 

        return matrix 
    
    def mostrar_matriz_transpuesta(self):
        matriz = self.main_window.generate_matrix()
        if matriz == None:
            warning_box("No se pudo generar esta tabla")
            return
        if not MatrixController.__valid_matriz(matriz):
            return
        matriz_transpuesta = GaussJordan.obtener_matriz_transpuesta(matriz)
        self.main_window.column_spinbox.setValue(len(matriz_transpuesta[0]))
        self.main_window.row_spinbox.setValue(len(matriz_transpuesta))
        self.main_window.resize_matrix(self.main_window.column_spinbox.value(),self.main_window.row_spinbox.value())
        self.main_window.insertar_matriz(matriz_transpuesta)
        self.main_window.input_table.resizeColumnsToContents()

    def get_matrix_a(self) ->list[list] | None:
        matriz = []
        for row in range(self.vector_window.mxm_a_table.rowCount()):
            row_ = []
            for col in range(self.vector_window.mxm_a_table.columnCount()):
                table_widget = self.vector_window.mxm_a_table.item(row,col)
                if table_widget is None: return None
                try:
                    num = float(table_widget.text())
                except ValueError:
                    return None
                row_.append(num)
            matriz.append(row_)
        return matriz
    
    def get_matrix_b(self) ->list[list] | None:
        matriz = []
        for row in range(self.vector_window.mxm_b_table.rowCount()):
            row_ = []
            for col in range(self.vector_window.mxm_b_table.columnCount()):
                table_widget = self.vector_window.mxm_b_table.item(row,col)
                if table_widget is None: return None
                try:
                    num = float(table_widget.text())
                except ValueError:
                    return None
                row_.append(num)
            matriz.append(row_)
        return matriz
    @Slot()
    def mxm_generate_matrix_c_button(self):
        matrix_a = self.get_matrix_a()
        matrix_b = self.get_matrix_b()
        if matrix_a is None or matrix_b is None:
            warning_box('No se pudo generar la Matriz C')
            return
        matrix_c =  GaussJordan.obtener_matriz_multiplicada(matrix_a,matrix_b)
        self.vector_window.mxm_set_matrix_c(matrix_c)
    @staticmethod
    def __valid_matriz(matriz: list[list],transposition=False) ->bool:
        if matriz == []:
            warning_box('La matriz ingresada es invalida')
            return False
        width = len(matriz)
        length = len(matriz[0])
        for row in range(width):
            if transposition:
                if all(matriz[row][col] == 0 for col in range(length-1)) and matriz[row][-1] !=0:
                    warning_box("La matriz ingresada no tiene solucion")
                    return False
            if len(matriz[row]) != length:
                warning_box('La matriz ingresada esta incompleta')
                return False
        return True