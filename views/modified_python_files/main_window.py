from views.generated_python_files.ui_main_window import Ui_MainWindow as Generated_MainWindow
from PySide6.QtWidgets import QMainWindow,QTableWidgetItem
from PySide6.QtCore import Slot

from random import randint
from helpers.box_helper import warning_box
class MainWindow(QMainWindow,Generated_MainWindow):
    def __init__(self):
        super.__init__()
        self.setupUi()
    
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.row_spinbox.setValue(3)
        self.column_spinbox.setValue(3)
    
    @Slot()
    def resize_matrix(self,columns,rows):
        columns = self.column_spinbox.value()
        rows = self.row_spinbox.value()
        if rows <=0 or columns <=0:
            warning_box('No es posible redimensionar esta matriz.')
            return
        self.input_table.setRowCount(rows)
        self.input_table.setColumnCount(columns)
        for row in range(rows):
            table_header = self.input_table.verticalHeaderItem(row)
            if table_header is None:
                table_header = QTableWidgetItem()
                self.input_table.setVerticalHeaderItem(row,table_header)
            table_header.setText(str(row+1))
        for col in range(columns-1):
            table_header = self.input_table.horizontalHeaderItem(col)
            if table_header is None:
                table_header = QTableWidgetItem()
                self.input_table.setHorizontalHeaderItem(col, table_header)
            table_header.setText(f'X{col+1}')

        last_column_header = self.input_table.horizontalHeaderItem(columns - 1)
        if last_column_header is None:
            last_column_header = QTableWidgetItem()
            self.input_table.setHorizontalHeaderItem(columns - 1, last_column_header)
        last_column_header.setText('b')
        self.fill_table_widgets()
        self.input_table.resizeColumnsToContents()

    @Slot()
    def clean_matrix(self):
        for row in range(self.input_table.rowCount()):
            for col in range(self.input_table.columnCount()):
                table_widget = self.input_table.item(row,col)
                if table_widget is None:
                    table_widget = QTableWidgetItem("")  # Crear nuevo item si no existe
                    self.input_table.setItem(row, col, table_widget)
                table_widget.setText("")
    @Slot()
    def fill_matrix_0(self):
        for row in range(self.input_table.rowCount()):
            for col in range(self.input_table.columnCount()):
                table_widget:QTableWidgetItem = self.input_table.item(row,col)
                if table_widget.text() !='':continue
                table_widget.setText('0')

    @Slot()
    def random_matrix(self):
        for row in range(self.input_table.rowCount()):
            for col in range(self.input_table.columnCount()):
                table_widget:QTableWidgetItem = self.input_table.item(row,col)
                if table_widget.text() != '':continue
                table_widget.setText(str(randint(-99,99)))

    @Slot()
    def fill_table_widgets(self):
        for row in range(self.input_table.rowCount()):
            for col in range(self.input_table.columnCount()):
                table_widget = self.input_table.item(row,col)
                if table_widget is None: 
                    table_widget =QTableWidgetItem()
                    self.input_table.setItem(row,col,table_widget)

    def generate_matrix(self) ->list[list] | None:
        matriz = []
        for row in range(self.input_table.rowCount()):
            row_ = []
            for col in range(self.input_table.columnCount()):
                table_widget = self.input_table.item(row,col)
                if table_widget is None: return None
                try:
                    num = float(table_widget.text())
                except ValueError:
                    return None
                row_.append(num)
            matriz.append(row_)
        return matriz
    
    def insertar_matriz(self,matriz) ->None:
        if len(matriz) != self.row_spinbox.value() or len(matriz[0]) != self.column_spinbox.value():
            warning_box("Error inesperado")
            return
        for row in range(self.input_table.rowCount()):
            for col in range(self.input_table.columnCount()):
                table_widget = self.input_table.item(row,col)
                if table_widget is None: 
                    table_widget =QTableWidgetItem()
                    self.input_table.setItem(row,col,table_widget)
                table_widget.setText(str(matriz[row][col]))
                

