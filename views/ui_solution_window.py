# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'solution_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication,QMetaObject, Qt,QSize,Slot)
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QHBoxLayout, QLabel,QListWidget, QPushButton,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,QTextEdit,
    QWidget)
from views.QtFiles.qrc_files import resources_rc
class Ui_main_widget(object):
    
    def setupUi(self, main_widget:QWidget):
        if not main_widget.objectName():
            main_widget.setObjectName(u"main_widget")
        main_widget.resize(600, 450)
        icon = QIcon()
        icon.addFile(u":/icon/Images/grid.ico", QSize(), QIcon.Normal, QIcon.Off)
        main_widget.setWindowIcon(icon)
        main_widget.setStyleSheet(u"#Main_widget{\n"
"background-color: #d3d3d3;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"border: 2px solid #404040;\n"
"border-radius: 8px;\n"
"padding: 1px 5px;\n"
"color: #fff;\n"
"background-color: #6c757d;\n"
"font: 700 9pt \"Calibri\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #5c636a;\n"
"}\n"
" QPushButton:pressed {\n"
"    border: 4px solid #c0c4c8 \n"
"}\n"
"QLabel {\n"
"    color: #fff;\n"
" background-color: #6a858d; \n"
"    border:2px solid #404040;        \n"
"    border-radius: 4px;           \n"
"    padding: 2.5px 5px;            \n"
"font: 700 9pt \"Calibri\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"background-color: #819299; \n"
"gridline-color: #fff;  \n"
"color: #fff;\n"
"}\n"
"\n"
"QHeaderView{\n"
"background-color: #85939a;\n"
"color:white;\n"
"font: 700 9pt \"Calibri\";\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"background-color: #85939a;\n"
"}\n"
"QTableCornerButton::section {\n"
"background-color: #85939a;\n"
"}\n"
"QTableWidget::item::hover{\n"
"background-color: #B6BEC2\n"
"}\n"
"\n"
"QTabBar::tab{\n"
""
                        "background-color: #80857C;\n"
"color: white;\n"
"}\n"
"\n"
"QTabBar::tab:hover{\n"
"background-color: #B0B3AD\n"
"}\n"
"\n"
"QTabBar::tab:selected{\n"
"background-color:#454742\n"
"}\n"
"\n"
"QListWidget{\n"
"background: #F1F1F1;\n"
"border : none\n"
"}\n"
"QListWidget::item{\n"
"margin: 2px;\n"
"margin-left:0;\n"
"}\n"
"QListWidget::item::hover{\n"
"color : #1A5276 ;\n"
"font: 700 9pt \"Segoe UI\";\n"
"border: 1.5px solid #2E4053;\n"
"border-radius:7px\n"
"}\n"
"")
        self.main_widget_vertical_layout = QVBoxLayout(main_widget)
        self.main_widget_vertical_layout.setObjectName(u"main_widget_vertical_layout")
        self.options_tab_widget = QWidget(main_widget)
        self.options_tab_widget.setObjectName(u"options_tab_widget")
        self.options_tab_horizontal_layout = QHBoxLayout(self.options_tab_widget)
        self.options_tab_horizontal_layout.setObjectName(u"options_tab_horizontal_layout")
        self.back_tab_button = QPushButton(self.options_tab_widget)
        self.back_tab_button.setObjectName(u"back_tab_button")
        self.back_tab_button.setStyleSheet(u"image: url(:/icon/Images/arrow_left.png);\n"
"width:40px;\n"
"height:30px;\n"
"padding:0\n"
"")

        self.options_tab_horizontal_layout.addWidget(self.back_tab_button, 0, Qt.AlignmentFlag.AlignLeft)

        self.label = QLabel(self.options_tab_widget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"border-radius:6px;\n"
"font: 700 9pt \"Calibri\";")

        self.options_tab_horizontal_layout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.next_tab_button = QPushButton(self.options_tab_widget)
        self.next_tab_button.setObjectName(u"next_tab_button")
        self.next_tab_button.setStyleSheet(u"image: url(:/icon/Images/arrow_right.png);\n"
"width:40px;\n"
"height:30px;\n"
"padding:0\n"
"")

        self.options_tab_horizontal_layout.addWidget(self.next_tab_button, 0, Qt.AlignmentFlag.AlignRight)


        self.main_widget_vertical_layout.addWidget(self.options_tab_widget)

        self.tabWidget = QTabWidget(main_widget)
        self.tabWidget.setObjectName(u"tabWidget")

        self.main_widget_vertical_layout.addWidget(self.tabWidget)

        self.main_widget_vertical_layout.setStretch(0, 1)
        self.main_widget_vertical_layout.setStretch(1, 10)

        self.retranslateUi(main_widget)

        QMetaObject.connectSlotsByName(main_widget)
    # setupUi
    def create_tab_solutions(self,config: dict):
        for i,(step,matrix) in enumerate(config.items()):
            self.p = QWidget()
            self.p.setProperty('step_data',step)
            self.p.setObjectName(f'p{i+1}')
            self.verticalLayout = QVBoxLayout(self.p)
            self.verticalLayout.setObjectName(f"vertical_layout_{i+1}")
            self.verticalLayout.setContentsMargins(0, 0, 0, 0)
            self.s_table = QTableWidget(self.p)
            self.s_table.setObjectName(f"s_table_{i+1}")
            self.verticalLayout.addWidget(self.s_table)
            if i == len(config)-1:
                self.create_matriz(config[step][0],self.s_table)
                self.solution_list = QListWidget(self.p)
                self.solution_list.setObjectName('solution_list')
                if matrix[1] != '':
                    for variable in matrix[1]:
                        self.solution_list.addItem(variable)
                    self.verticalLayout.addWidget(self.solution_list)
                else:
                    self.solution_list.hide()
            else:
                self.create_matriz(config[step],self.s_table)
            self.s_table.resizeColumnsToContents()
            self.tabWidget.addTab(self.p,f'p{i+1}')

    def create_matriz(self,matriz,table_widget:QTableWidget):
        width = len(matriz)
        length = len(matriz[0])
        table_widget.setRowCount(width)
        table_widget.setColumnCount(length)
        for row in range(width):
            table_header = table_widget.verticalHeaderItem(row)
            if table_header is None:
                table_header = QTableWidgetItem()
                table_widget.setVerticalHeaderItem(row,table_header)
            table_header.setText(str(row+1))

        for col in range(length):
            table_header = table_widget.horizontalHeaderItem(col)
            if table_header is None:
                table_header = QTableWidgetItem()
                table_widget.setHorizontalHeaderItem(col,table_header)
            table_header.setText(f'X{col+1}')

        last_table_header = table_widget.horizontalHeaderItem(col-1)
        if last_table_header is None:
            last_table_header = QTableWidgetItem()
            table_widget.setHorizontalHeaderItem(col-1,last_table_header)
        table_header.setText(f'b')

        for row in range(width):
            for col in range(length):
                table_item = table_widget.item(row,col)
                if table_item is None:
                    table_item = QTableWidgetItem()
                    table_item.setText(str(matriz[row][col]))
                    table_item.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
                    table_widget.setItem(row,col,table_item)

    def create_scalar(self,scalar, table_widget:QTableWidget):
        width = len(scalar)
        table_widget.setRowCount(width)
        table_widget.setColumnCount(1)
        for row in range(width):
            table_header = table_widget.verticalHeaderItem(row)
            if table_header is None:
                table_header = QTableWidgetItem()
                table_widget.setVerticalHeaderItem(row,table_header)
            table_header.setText(str(row+1))

        last_table_header = table_widget.horizontalHeaderItem(0)
        if last_table_header is None:
            last_table_header = QTableWidgetItem()
            table_widget.setHorizontalHeaderItem(0,last_table_header)
        table_header.setText(f'b')

        for row in range(width):
            table_item = table_widget.item(row,0)
            if table_item is None:
                table_item = QTableWidgetItem()
                table_item.setText(str(scalar[row]))
                table_widget.setItem(row,0,table_item)
            table_item.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
        
    def show_step_property(self,index):
        step = self.tabWidget.currentWidget().property('step_data')
        if step is not None:
            self.label.setText(step)
            return
        self.label.setText('Informacion no encontrada')

    @Slot()
    def previous_tab(self):
        current_index = self.tabWidget.currentIndex()
        if current_index > 0:
            self.tabWidget.setCurrentIndex(current_index-1)
    @Slot()
    def next_tab(self):
        current_index = self.tabWidget.currentIndex()
        if current_index < self.tabWidget.count()-1:
            self.tabWidget.setCurrentIndex(current_index+1)

    def create_scalar_solution(self,config):
        self.create_tab()
        self.create_scalar(config,self.s_table)

    def create_tab(self):
        self.p = QWidget()
        self.verticalLayout = QVBoxLayout(self.p)
        self.verticalLayout.setContentsMargins(0,0,0,0)
        self.s_table = QTableWidget(self.p)
        self.verticalLayout.addWidget(self.s_table)
        self.tabWidget.addTab(self.p,'Escalar')

    def retranslateUi(self, main_widget):
        main_widget.setWindowTitle(QCoreApplication.translate("main_widget", u"Form", None))
        self.back_tab_button.setText("")
        self.label.setText(QCoreApplication.translate("main_widget", u"Procedimiento", None))
        self.next_tab_button.setText("")
    # retranslateUi

