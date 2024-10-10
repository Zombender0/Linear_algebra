from PySide6.QtWidgets import QTableWidget, QTableWidgetItem
from PySide6.QtCore import Qt
def resize_to_content(function):
    def wrapper(*args, **kwargs):
        result = function
        table = args[0]
        if isinstance(table,QTableWidget):
            table.resizeColumnsToContents()
        return result
    return wrapper

@resize_to_content
def resize_table(table: QTableWidget, rows: int = 1, columns: int = 1,last_b=False) -> None:
    table.setRowCount(rows)
    table.setColumnCount(columns)
    #Stabish QTableWidgetItems for headers
    for row in range(rows):
        vertical_item = table.verticalHeaderItem(row)
        if vertical_item is None:
            vertical_item = QTableWidgetItem()
            table.setVerticalHeaderItem(vertical_item)
        vertical_item.setText(str(row+1))

    for col in range(columns):
        horizontal_item = table.horizontalHeaderItem(col)
        if horizontal_item is None:
            horizontal_item = QTableWidgetItem()
            table.setHorizontalHeaderItem(horizontal_item)
        horizontal_item.setText(f'X{col}')
    if last_b:
        last_horizontal_item = table.horizontalHeaderItem(columns-1)
        last_horizontal_item.setText('b')
    #Stablish QTableWidgetItems for content
    for row in range(rows):
        for col in range(columns):
            item = table.item(row,col)
            if item is None:
                item = QTableWidgetItem()
                table.setItem(row,col,item)
@resize_to_content
def get_data_from_table(table:QTableWidget)->list[list]:
    matrix = list()
    for row in range(table.rowCount()):
        for col in range(table.columnCount()):
            #Error handler
            try:
                data = float(table.item(row,col).text())
                matrix.append(data)
            except ValueError:
                return None
            except Exception as e:
                print(f'Error inesperado: {e}')
                return None
    return matrix

@resize_to_content
def insert_data_to_table(table:QTableWidget,matrix:list[list]|list,editable=False)->None:
    rows = len(matrix)
    columns = len(matrix[0])
    if table.rowCount() != rows and table.columnCount !=columns():
        resize_table(table,rows,columns,last_b=True)
    for row in range(rows):
        for col in range(columns):
            item = table.item(row,col)
            item.setText(str(matrix[row][col]))
            if editable:item.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)



