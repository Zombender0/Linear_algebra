from views.generated_python_files.ui_main_window import Ui_MainWindow as Generated_MainWindow
from PySide6.QtWidgets import QMainWindow,QTableWidgetItem,QFileDialog
from PySide6.QtCore import Slot

from random import randint
from helpers.box_helper import warning_box
from helpers.matrix_helper import get_data_from_table,insert_data_to_table,resize_table
from utils.matrix_utils import get_transposed_matrix,create_matrix_from_csv
from utils.generic_utils import get_file_from_dialog
from constants.file_filter import CSV_FILTER

class MainWindow(Generated_MainWindow):
    def __init__(self,main_window:QMainWindow):
        self.setupUi(main_window)
        resize_table(self.input_table,3,3,last_b=True)
    
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.row_spinbox.setValue(3)
        self.column_spinbox.setValue(3)
        self.table_solution_matrix_combobox.setItemData(1,"reduccion")
        self.table_solution_matrix_combobox.setItemData(2,"vxv")
        self.table_solution_matrix_combobox.setItemData(3,"determinante")
        self.table_solution_matrix_combobox.setItemData(4,"cramer")

    @Slot()
    def update_matrix_size(self):
        rows = self.row_spinbox.value()
        columns = self.column_spinbox.value()
        if rows <=0 or columns <=0:
            warning_box('No es posible redimensionar esta matriz.')
            return
        resize_table(self.input_table,rows,columns,last_b=True)

    @Slot()
    def clean_matrix(self):
        for row in range(self.input_table.rowCount()):
            for col in range(self.input_table.columnCount()):
                table_widget = self.input_table.item(row,col)
                if table_widget is None:
                    table_widget = QTableWidgetItem()
                    self.input_table.setItem(row, col, table_widget)
                table_widget.setText("")
    @Slot()
    def fill_matrix_0(self):
        for row in range(self.input_table.rowCount()):
            for col in range(self.input_table.columnCount()):
                table_widget:QTableWidgetItem = self.input_table.item(row,col)
                if table_widget.text() !='':continue
                table_widget.setText('0')
        self.adjust_matrix()

    @Slot()
    def random_matrix(self):
        for row in range(self.input_table.rowCount()):
            for col in range(self.input_table.columnCount()):
                table_widget:QTableWidgetItem = self.input_table.item(row,col)
                if table_widget.text() != '':continue
                table_widget.setText(str(randint(-99,99)))
        self.adjust_matrix()

    @Slot()
    def transpose_matrix(self):
        original_matrix = get_data_from_table(self.input_table)
        if original_matrix is None:
            warning_box("Matriz invalida")
            return
        transposed_matrix = get_transposed_matrix(original_matrix)
        insert_data_to_table(self.input_table,transposed_matrix,editable=True,last_b=True)
        self.row_spinbox.setValue(len(transposed_matrix))
        self.column_spinbox.setValue(len(transposed_matrix[0]))

    @Slot()
    def adjust_matrix(self):
        self.input_table.resizeColumnsToContents()
        self.input_table.resizeRowsToContents()

    @Slot()
    def import_matrix_from_csv(self):
        file_path = get_file_from_dialog(CSV_FILTER)
        if file_path is None:
            return
        matrix = create_matrix_from_csv(file_path)
        if matrix is None:
            return
        insert_data_to_table(self.input_table,matrix,editable=True,last_b=True)
        rows = len(matrix)
        columns = len(matrix[0])
        self.row_spinbox.setValue(rows)
        self.column_spinbox.setValue(columns)                

