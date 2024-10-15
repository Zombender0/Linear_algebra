from PySide6.QtWidgets import QTableWidget, QTableWidgetItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

def resize_to_content(function):
    def wrapper(*args, **kwargs):
        result = function(*args,**kwargs)
        table = args[0]
        
        table.resizeColumnsToContents()
        table.resizeRowsToContents()
        return result
    return wrapper

@resize_to_content
def resize_table(table: QTableWidget, rows: int = 1, columns: int = 1,last_b=False,letter='X') -> None:
    table.setRowCount(rows)
    table.setColumnCount(columns)
    header_font = QFont('Calibri',14)
    #Stabish QTableWidgetItems for headers
    for row in range(rows):
        vertical_item = table.verticalHeaderItem(row)
        if vertical_item is None:
            vertical_item = QTableWidgetItem()
            table.setVerticalHeaderItem(row,vertical_item)
        vertical_item.setText(str(row+1))
        vertical_item.setFont(header_font)

    for col in range(columns):
        horizontal_item = table.horizontalHeaderItem(col)
        if horizontal_item is None:
            horizontal_item = QTableWidgetItem()
            table.setHorizontalHeaderItem(col,horizontal_item)
        horizontal_item.setText(f'{letter}{col+1}')
        horizontal_item.setFont(header_font)

    if last_b:
        last_horizontal_item = table.horizontalHeaderItem(columns-1)
        last_horizontal_item.setText('b')

    for row in range(rows):
        for col in range(columns):
            item = table.item(row,col)
            if item is None:
                item = QTableWidgetItem()
                table.setItem(row,col,item)
            font = QFont('Calibri',14)
            item.setFont(font)

def get_data_from_table(table:QTableWidget)->list[list]:
    matrix = list()
    for row in range(table.rowCount()):
        row_= list()
        for col in range(table.columnCount()):
            #Error handler
            try:
                data = float(table.item(row,col).text())
                row_.append(data)
            except ValueError:
                return None
            except Exception as e:
                print(f'Error inesperado: {e}')
                return None
        matrix.append(row_)
    return matrix

@resize_to_content
def insert_data_to_table(table:QTableWidget,matrix:list[list]|list,editable=False,last_b=False)->None:
    rows = len(matrix)
    columns = len(matrix[0])
    if table.rowCount() != rows or table.columnCount() !=columns:
        resize_table(table,rows,columns,last_b=last_b)
    for row in range(rows):
        for col in range(columns):
            item = table.item(row,col)
            item.setText(str(matrix[row][col]))
            if editable:item.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
    

