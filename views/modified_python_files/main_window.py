from views.generated_python_files.ui_main_window import Ui_MainWindow as Generated_MainWindow
from PySide6.QtWidgets import QMainWindow,QTableWidgetItem,QTableWidget
from PySide6.QtCore import Slot

from random import randint
from helpers.box_helper import warning_box,question_box
from helpers.matrix_helper import get_data_from_table,insert_data_to_table,resize_table

from utils.matrix_utils import get_transposed_matrix,create_matrix_from_csv
from utils.generic_utils import get_file_from_dialog
from constants.file_filter import CSV_FILTER
from helpers.graph_helper import PyQtGraphWidget

class MainWindow(Generated_MainWindow):
    def __init__(self,main_window:QMainWindow):
        self.setupUi(main_window)
        #loadJsonStyle(self,self)
        
    def setupUi(self, MainWindow:QMainWindow):
        super().setupUi(MainWindow)
        rows = 3
        columns = 3
        self.resize_aumented_matrix(rows,columns)
        self.row_spinbox.setValue(rows)
        self.column_spinbox.setValue(columns)
        self.table_select_solutions_combobox.setItemData(0,"index")
        self.table_select_solutions_combobox.setItemData(1,"reduccion")
        self.table_select_solutions_combobox.setItemData(2,"cramer")
        self.main_stacked_widget.setCurrentIndex(3)
        self.method_equation_tab_widget.setCurrentIndex(0)
        self.graph = PyQtGraphWidget(self.graphic_widget)
        self.verticalLayout_9.addWidget(self.graph)
        
        MainWindow.showMaximized()

    def resize_aumented_matrix(self, rows:int,columns:int)->None:
        resize_table(self.coeficient_table,rows,columns,last_b=False,letter='X')
        resize_table(self.independent_terms_table,rows,1,last_b=True,letter=' ')

    def insert_data_to_aumented_matrix(self,matrix:list[list]):
        rows = len(matrix)
        columns = len(matrix[0])
        coeficient_matrix = [row[:-1] for row in matrix]
        independent_terms_matrix = [[row[-1]] for row in matrix]
        self.resize_aumented_matrix(rows,columns)
        insert_data_to_table(self.coeficient_table,coeficient_matrix,editable=True,last_b=False,letter='X')
        insert_data_to_table(self.independent_terms_table,independent_terms_matrix,editable=True,last_b=True,letter=' ')
    
    @Slot()
    def update_matrix_size(self):
        rows = self.row_spinbox.value()
        columns = self.column_spinbox.value()
        if rows <=0 or columns <=0:
            warning_box('No es posible redimensionar esta matriz.')
            return
        self.resize_aumented_matrix(rows,columns)
        

    @Slot()
    def clean_table(self,table:QTableWidget):
        for row in range(table.rowCount()):
            for col in range(table.columnCount()):
                table_widget = table.item(row,col)
                if table_widget is None:
                    table_widget = QTableWidgetItem()
                    table.setItem(row, col, table_widget)
                table_widget.setText("")
    @Slot()
    def fill_matrix_0(self,table:QTableWidget):
        for row in range(table.rowCount()):
            for col in range(table.columnCount()):
                table_widget:QTableWidgetItem = table.item(row,col)
                if table_widget.text() !='':continue
                table_widget.setText('0')
        self.adjust_matrix(table)

    @Slot()
    def random_matrix(self,table:QTableWidget):
        for row in range(table.rowCount()):
            for col in range(table.columnCount()):
                table_widget:QTableWidgetItem = table.item(row,col)
                if table_widget.text() != '':continue
                table_widget.setText(str(randint(-99,99)))
        self.adjust_matrix(table)

    @Slot()
    def adjust_matrix(self,table:QTableWidget):
        table.resizeColumnsToContents()
        table.resizeRowsToContents()

    @Slot()
    def import_matrix_from_csv(self):
        file_path = get_file_from_dialog(CSV_FILTER)
        if file_path is None:
            return
        matrix = create_matrix_from_csv(file_path)
        if matrix is None:
            return
        rows = len(matrix)
        columns = len(matrix[0])-1
        self.row_spinbox.setValue(rows)
        self.column_spinbox.setValue(columns)
        self.insert_data_to_aumented_matrix(matrix)
        
