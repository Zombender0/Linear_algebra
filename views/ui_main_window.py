# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowAdKMnN.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,Slot)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpinBox, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
from views.message_box import warning_box
from random import randint
from views.QtFiles.qrc_files import resources_rc
class Ui_MainWindow(object):
    def __init__(self,Mainwindow):
        self.setupUi(Mainwindow)
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.resize(675, 270)
        icon = QIcon()
        icon.addFile(u":/icon/Images/grid.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"#MainWindow{\n"
"background-color: #d3d3d3;\n"
"\n"
"}\n"
"\n"
"#MainWindow QPushButton{\n"
"border: 2px solid #404040;\n"
"border-radius: 8px;\n"
"padding: 1px 5px;\n"
"color: #fff;\n"
"background-color: #6c757d;\n"
"font: 700 9pt \"Calibri\";\n"
"}\n"
"\n"
"#MainWindow QPushButton:hover{\n"
"background-color: #5c636a;\n"
"}\n"
"#MainWindow QPushButton:pressed {\n"
"    border: 4px solid #c0c4c8 \n"
"}\n"
"\n"
"QSpinBox{\n"
"color: white;\n"
"background-color: #6c757d;\n"
"}\n"
"QSpinBox:up-button{\n"
"image:url(:/icon/Images/arrow_upwards.png);\n"
"border-left:0.5px solid #fff;\n"
"subcontrol-position:right;\n"
"width: 15px;\n"
"height: 15px;\n"
"}\n"
"QSpinBox:down-button{\n"
"image:url(:/icon/Images/arrow_downwards.png);\n"
"border-right:0.5px solid #fff;\n"
"subcontrol-position:left;\n"
"width:15px;\n"
"height:15px\n"
"}\n"
"QSpinBox:up-button:hover{\n"
"background-color: #5c636f;\n"
"}\n"
"QSpinBox:down-button:hover{\n"
"background-color: #5c636f;\n"
"}\n"
"QLabel {\n"
"    color: #fff;\n"
" background-c"
                        "olor: #6a858d; \n"
"    border:2px solid #404040;        \n"
"    border-radius: 4px;           \n"
"    padding: 2.5px 5px;            \n"
"font: 700 9pt \"Calibri\";\n"
"}\n"
"QComboBox{\n"
"font: 700 9pt \"Calibri\";\n"
"color: white;\n"
"background-color: #6c757d;\n"
"border: 1.5px solid #404040;\n"
"border-radius: 6px;\n"
"padding-left:10px\n"
"}\n"
"QComboBox::drop-down{\n"
"border:0px;\n"
"}\n"
"QComboBox::down-arrow{\n"
"image: url(:/icon/Images/arrow_downwards.png);\n"
"width:20px;\n"
"height: 20px;\n"
"margin-right: 13px;\n"
"}\n"
"\n"
"\n"
"QComboBox QListView{\n"
"font: 700 9pt \"Calibri\";\n"
"border: 1px solid rgba(0,0,0,10%);\n"
"padding: 5px;\n"
"background-color: #6c757d;\n"
"color: white;\n"
"outline: 0px;\n"
"}\n"
"QComboBox::hover{\n"
"background-color: #5c636a;\n"
"}\n"
"\n"
"QTableWidget{\n"
"background-color: #819299; \n"
"gridline-color: #fff;  \n"
"}\n"
"\n"
"QHeaderView{\n"
"background-color: #85939a;\n"
"color:white;\n"
"font: 700 9pt \"Calibri\";\n"
"}\n"
"\n"
"QHeaderView::section "
                        "{\n"
"background-color: #85939a;\n"
"}\n"
"QTableCornerButton::section {\n"
"background-color: #85939a;\n"
"}\n"
"QTableWidget::item{\n"
"color:#fff\n"
"}\n"
"QTableWidget::item::hover{\n"
"background-color: #B6BEC2\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.centralwidget_layout = QVBoxLayout(self.centralwidget)
        self.centralwidget_layout.setObjectName(u"centralwidget_layout")
        self.table_widget = QWidget(self.centralwidget)
        self.table_widget.setObjectName(u"table_widget")
        self.verticalLayout_2 = QVBoxLayout(self.table_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.table_buttons_frame = QFrame(self.table_widget)
        self.table_buttons_frame.setObjectName(u"table_buttons_frame")
        self.table_buttons_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.table_buttons_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.table_buttons_horizontal_layout = QHBoxLayout(self.table_buttons_frame)
        self.table_buttons_horizontal_layout.setObjectName(u"table_buttons_horizontal_layout")
        self.table_buttons_horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.table_row_spinbox_widget = QWidget(self.table_buttons_frame)
        self.table_row_spinbox_widget.setObjectName(u"table_row_spinbox_widget")
        self.table_row_spinbox_widget.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.table_row_spinbox_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.row_spinbox_label = QLabel(self.table_row_spinbox_widget)
        self.row_spinbox_label.setObjectName(u"row_spinbox_label")
        self.row_spinbox_label.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_3.addWidget(self.row_spinbox_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.row_spinbox = QSpinBox(self.table_row_spinbox_widget)
        self.row_spinbox.setObjectName(u"row_spinbox")
        self.row_spinbox.setMinimumSize(QSize(60, 0))
        self.row_spinbox.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.row_spinbox.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.row_spinbox)


        self.table_buttons_horizontal_layout.addWidget(self.table_row_spinbox_widget)

        self.table_column_spinbox_widget = QWidget(self.table_buttons_frame)
        self.table_column_spinbox_widget.setObjectName(u"table_column_spinbox_widget")
        self.verticalLayout = QVBoxLayout(self.table_column_spinbox_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.column_spinbox_label = QLabel(self.table_column_spinbox_widget)
        self.column_spinbox_label.setObjectName(u"column_spinbox_label")
        self.column_spinbox_label.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.column_spinbox_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.column_spinbox = QSpinBox(self.table_column_spinbox_widget)
        self.column_spinbox.setObjectName(u"column_spinbox")
        self.column_spinbox.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.column_spinbox)


        self.table_buttons_horizontal_layout.addWidget(self.table_column_spinbox_widget)

        self.table_grid_options = QGridLayout()
        self.table_grid_options.setObjectName(u"table_grid_options")
        self.table_grid_options.setHorizontalSpacing(6)
        self.table_grid_options.setContentsMargins(9, 9, 9, 9)
        self.table_update_button = QPushButton(self.table_buttons_frame)
        self.table_update_button.setObjectName(u"table_update_button")
        self.table_update_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.table_update_button.setStyleSheet(u"")

        self.table_grid_options.addWidget(self.table_update_button, 0, 0, 1, 1)

        self.table_fill_0_button = QPushButton(self.table_buttons_frame)
        self.table_fill_0_button.setObjectName(u"table_fill_0_button")
        self.table_fill_0_button.setStyleSheet(u"")

        self.table_grid_options.addWidget(self.table_fill_0_button, 0, 1, 1, 1)

        self.table_clean_matrix_button = QPushButton(self.table_buttons_frame)
        self.table_clean_matrix_button.setObjectName(u"table_clean_matrix_button")
        self.table_clean_matrix_button.setStyleSheet(u"")

        self.table_grid_options.addWidget(self.table_clean_matrix_button, 1, 0, 1, 1)

        self.table_random_matrix_button = QPushButton(self.table_buttons_frame)
        self.table_random_matrix_button.setObjectName(u"table_random_matrix_button")
        self.table_random_matrix_button.setStyleSheet(u"")

        self.table_grid_options.addWidget(self.table_random_matrix_button, 0, 2, 1, 1)

        self.table_solution_matrix_combobox = QComboBox(self.table_buttons_frame)
        self.table_solution_matrix_combobox.addItem("")
        self.table_solution_matrix_combobox.addItem("")
        self.table_solution_matrix_combobox.addItem("")
        self.table_solution_matrix_combobox.setItemData(1,"reduccion")
        self.table_solution_matrix_combobox.setItemData(2,"vxv")
        self.table_solution_matrix_combobox.setObjectName(u"table_solution_matrix_combobox")
        self.table_solution_matrix_combobox.setStyleSheet(u"")

        self.table_grid_options.addWidget(self.table_solution_matrix_combobox, 1, 2, 1, 1)

        self.table_transposition_button = QPushButton(self.table_buttons_frame)
        self.table_transposition_button.setObjectName(u"table_transposition_button")

        self.table_grid_options.addWidget(self.table_transposition_button, 1, 1, 1, 1)

        self.table_solve_matrix_button = QPushButton(self.table_buttons_frame)
        self.table_solve_matrix_button.setObjectName(u"table_solve_matrix_button")
        self.table_solve_matrix_button.setStyleSheet(u"")

        self.table_grid_options.addWidget(self.table_solve_matrix_button, 2, 0, 1, 3)


        self.table_buttons_horizontal_layout.addLayout(self.table_grid_options)

        self.table_buttons_horizontal_layout.setStretch(0, 15)
        self.table_buttons_horizontal_layout.setStretch(1, 15)
        self.table_buttons_horizontal_layout.setStretch(2, 80)

        self.verticalLayout_2.addWidget(self.table_buttons_frame)

        self.input_table = QTableWidget(self.table_widget)
        if (self.input_table.columnCount() < 3):
            self.input_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.input_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.input_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.input_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.input_table.rowCount() < 3):
            self.input_table.setRowCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsEnabled);
        self.input_table.setItem(0, 0, __qtablewidgetitem3)
        self.input_table.setObjectName(u"input_table")
        self.input_table.setStyleSheet(u"")
        self.input_table.verticalHeader().setVisible(True)

        self.verticalLayout_2.addWidget(self.input_table)

        self.verticalLayout_2.setStretch(0, 10)
        self.verticalLayout_2.setStretch(1, 100)

        self.centralwidget_layout.addWidget(self.table_widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.row_spinbox.setValue(3)
        self.column_spinbox.setValue(3)
        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculadora de matrices", None))
        self.row_spinbox_label.setText(QCoreApplication.translate("MainWindow", u"Filas", None))
        self.column_spinbox_label.setText(QCoreApplication.translate("MainWindow", u"Columnas", None))
        self.table_update_button.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.table_fill_0_button.setText(QCoreApplication.translate("MainWindow", u"Rellenar espacios con 0", None))
        self.table_clean_matrix_button.setText(QCoreApplication.translate("MainWindow", u"Limpiar Matriz", None))
        self.table_random_matrix_button.setText(QCoreApplication.translate("MainWindow", u"Matriz aleatoria", None))
        self.table_solution_matrix_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"Resolver por", None))
        self.table_solution_matrix_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"Reducci\u00f3n", None))
        self.table_solution_matrix_combobox.setItemText(2, QCoreApplication.translate("MainWindow", u"Vectores", None))

        self.table_transposition_button.setText(QCoreApplication.translate("MainWindow", u"Transponer Matriz", None))
        self.table_solve_matrix_button.setText(QCoreApplication.translate("MainWindow", u"Resolver", None))
        ___qtablewidgetitem = self.input_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"X1", None));
        ___qtablewidgetitem1 = self.input_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"X2", None));
        ___qtablewidgetitem2 = self.input_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"b", None));

        __sortingEnabled = self.input_table.isSortingEnabled()
        self.input_table.setSortingEnabled(False)
        self.input_table.setSortingEnabled(__sortingEnabled)

    # retranslateUi


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
                

