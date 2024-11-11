from views.generated_python_files.ui_vector_window import Ui_main_widget as Generated_VectorWindow
from PySide6.QtWidgets import (QHBoxLayout, QLabel,QListWidget, QPushButton,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,QTextEdit,
    QWidget)
from PySide6.QtCore import Slot
from helpers.matrix_helper import *
from models.GaussJordan import GaussJordan
from PySide6.QtGui import QFont


class VectorWindow(QWidget,Generated_VectorWindow):
    header_font = QFont('Calibri',14)
    def __init__(self,matrix_instance:GaussJordan, parent:QWidget=None)->None:
        super().__init__(parent)
        self.matrix_instance = matrix_instance
        self.setupUi(self)
    
    def setupUi(self, main_widget):
        super().setupUi(main_widget)
        self.resize_matrices()
        self.setWindowTitle('Operaciones con vectores')

    def resize_matrices(self):
        #Tablas de vector por vector
        insert_data_to_table(self.vxv_row_vector, [self.matrix_instance.matriz[0]], editable=False,last_b=False)
        self.vxv_row_spinbox.setValue(1)
        resize_table(self.vxv_column_vector, rows=self.matrix_instance.columnas,columns=1,last_b=False)
        #Tablas de matriz por vector
        insert_data_to_table(self.mxv_matrix,self.matrix_instance.matriz,editable=False,last_b=False)
        resize_table(self.mxv_column_vector_table,rows=self.matrix_instance.columnas,columns=1,last_b=False,letter='V')
        #Tablas de matriz por matriz
        insert_data_to_table(self.mxm_a_table,self.matrix_instance.matriz)
        resize_table(self.mxm_b_table,rows=self.matrix_instance.columnas,columns=1,last_b=False)
    
    @Slot()
    def vxv_change_row_vector(self):
        row_number = self.vxv_row_spinbox.value()
        if row_number <= 0:
            self.vxv_row_spinbox.setValue(0)
            return
        if row_number > len(self.matrix_instance.matriz): 
            self.vxv_row_spinbox.setValue(row_number-1)
            return
        insert_data_to_table(self.vxv_row_vector,[self.matrix_instance.matriz[row_number-1]],editable=False,last_b=False)

    @Slot()
    def vxv_show_scalar(self):
        row_vector = get_data_from_table(self.vxv_row_vector)[0]
        if row_vector is None: return
        column_vector =  get_data_from_table(self.vxv_column_vector)[0]
        if column_vector is None:return
        scalar = GaussJordan.vxv_get_scalar(row_vector,column_vector)
        self.vxv_scalar_label.setText(f"{scalar}")

    @Slot()
    def mxv_add_vector(self):
        column_count = self.mxv_column_vector_table.columnCount()
        resize_table(self.mxv_column_vector_table,self.mxv_column_vector_table.rowCount(),column_count+1,letter='V')
    @Slot()
    def mxv_delete_vector(self):
        column_count = self.mxv_column_vector_table.columnCount()
        if column_count <=1:return
        self.mxv_column_vector_table.setColumnCount(column_count-1)

    @Slot()
    def mxv_show_scalar(self):
        matrix = get_data_from_table(self.mxv_matrix)
        if matrix is None: return
        vectors = get_data_from_table(self.mxv_column_vector_table)
        if vectors is None: return
        scalar = GaussJordan.mxv_get_scalar(matrix,vectors)
        insert_data_to_table(self.tableWidget,[scalar],editable=True,last_b=False)

    @Slot()
    def mxm_add_column_table_b(self):
        column_count = self.mxm_b_table.columnCount()
        resize_table(self.mxm_b_table,self.mxm_b_table.rowCount(),column_count+1)
        
    @Slot()
    def mxm_substract_column_table_b(self):
        column_count = self.mxm_b_table.columnCount()
        if column_count <=1:return
        self.mxm_b_table.setColumnCount(column_count-1)

    @Slot()
    def mxm_show_matrix_c(self):
        matrix_a = get_data_from_table(self.mxm_a_table)
        if matrix_a is None: return
        matrix_b = get_data_from_table(self.mxm_b_table)
        if matrix_b is None: return
        matrix_c = GaussJordan.mxm_get_multiplied_matrix(matrix_a,matrix_b)
        insert_data_to_table(self.mxm_c_table,matrix_c,editable=True,last_b=False)
    
    