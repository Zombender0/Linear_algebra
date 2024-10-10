# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vector_windowthWCOJ.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
from views.QtFiles.qrc_files import resources_rc
from copy import deepcopy
class Ui_main_widget(object):
    def __init__(self,matrix):
        self.matrix_instance = deepcopy(matrix)
    def setupUi(self, main_widget):
        if not main_widget.objectName():
            main_widget.setObjectName(u"main_widget")
        main_widget.resize(472, 474)
        icon = QIcon()
        icon.addFile(u":/icon/Images/math.ico", QSize(), QIcon.Normal, QIcon.Off)
        main_widget.setWindowIcon(icon)
        main_widget.setStyleSheet(u"#main_widget{\n"
"background-color: #d3d3d3;\n"
"font: 700 9pt \"Calibri\";\n"
"}\n"
"QTabWidget:pane{\n"
"background-color: #d3d3d3\n"
"}\n"
"#vector_x_vector_widget,#matrix_x_matrix_widget,#matrix_x_vector_widget{\n"
"background-color: #d3d3d3;\n"
"}\n"
"QTabBar::tab{\n"
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
"QSpinBox{\n"
"color: white;\n"
"background-color: #6c757d;\n"
"}\n"
"QSpinBox:up-button{\n"
"image:url(:/icon/Images/arrow_upwards.png);\n"
"border-left:0.5px solid #fff;\n"
"subcontrol-position:right;\n"
"width: 20px;\n"
"height: 20px;\n"
"}\n"
"QSpinBox:down-button{\n"
"image:url(:/icon/Images/arrow_downwards.png);\n"
"border-right:0.5px solid #fff;\n"
"subcontrol-position:left;\n"
"width:20px;\n"
"height:20px\n"
"}\n"
"QSpinBox:up-button:hover{\n"
"background-color: #5c636f;\n"
"}\n"
"QSpinBox:down-button:hover{\n"
"background-color: #5c636f;\n"
"}\n"
""
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
"QPushButton:pressed {\n"
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
"QTableWidget::item{\n"
"color:#fff\n"
"}\n"
"QTableWidget::item::hover{\n"
"background-color: #B6BEC2\n"
"}\n"
"QScrollBar {\n"
"	background: #a9a9a9;\n"
""
                        "}")
        self.verticalLayout = QVBoxLayout(main_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tab_widget = QTabWidget(main_widget)
        self.tab_widget.setObjectName(u"tab_widget")
        self.vector_x_vector_widget = QWidget()
        self.vector_x_vector_widget.setObjectName(u"vector_x_vector_widget")
        self.verticalLayout_2 = QVBoxLayout(self.vector_x_vector_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.vxv_options_widget = QWidget(self.vector_x_vector_widget)
        self.vxv_options_widget.setObjectName(u"vxv_options_widget")
        self.horizontalLayout = QHBoxLayout(self.vxv_options_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.vxv_matrix_vector_widget = QWidget(self.vxv_options_widget)
        self.vxv_matrix_vector_widget.setObjectName(u"vxv_matrix_vector_widget")
        self.verticalLayout_3 = QVBoxLayout(self.vxv_matrix_vector_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.vxv_spinbox_widget = QWidget(self.vxv_matrix_vector_widget)
        self.vxv_spinbox_widget.setObjectName(u"vxv_spinbox_widget")
        self.verticalLayout_4 = QVBoxLayout(self.vxv_spinbox_widget)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.vxv_row_label = QLabel(self.vxv_spinbox_widget)
        self.vxv_row_label.setObjectName(u"vxv_row_label")

        self.verticalLayout_4.addWidget(self.vxv_row_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.vxv_row_spinbox = QSpinBox(self.vxv_spinbox_widget)
        self.vxv_row_spinbox.setObjectName(u"vxv_row_spinbox")
        self.vxv_row_spinbox.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.vxv_row_spinbox)


        self.verticalLayout_3.addWidget(self.vxv_spinbox_widget)

        self.vxv_row_vector_widget = QWidget(self.vxv_matrix_vector_widget)
        self.vxv_row_vector_widget.setObjectName(u"vxv_row_vector_widget")
        self.vxv_row_vector_widget.setStyleSheet(u"QTabBar:tab{\n"
"max-width:10px;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.vxv_row_vector_widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.vxv_row_vector = QTableWidget(self.vxv_row_vector_widget)
        if (self.vxv_row_vector.columnCount() < 4):
            self.vxv_row_vector.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.vxv_row_vector.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.vxv_row_vector.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.vxv_row_vector.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.vxv_row_vector.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.vxv_row_vector.rowCount() < 1):
            self.vxv_row_vector.setRowCount(1)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.vxv_row_vector.setItem(0, 0, __qtablewidgetitem4)
        self.vxv_row_vector.setObjectName(u"vxv_row_vector")
        self.vxv_row_vector.setMinimumSize(QSize(230, 0))
        self.vxv_row_vector.setMaximumSize(QSize(16777215, 16777215))
        self.vxv_row_vector.setStyleSheet(u"")
        self.vxv_row_vector.setGridStyle(Qt.PenStyle.SolidLine)
        self.vxv_row_vector.horizontalHeader().setVisible(True)
        self.vxv_row_vector.horizontalHeader().setMinimumSectionSize(10)
        self.vxv_row_vector.horizontalHeader().setDefaultSectionSize(50)
        self.vxv_row_vector.horizontalHeader().setHighlightSections(False)
        self.vxv_row_vector.verticalHeader().setVisible(True)
        self.vxv_row_vector.verticalHeader().setDefaultSectionSize(22)
        self.vxv_row_vector.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_5.addWidget(self.vxv_row_vector, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_3.addWidget(self.vxv_row_vector_widget)

        self.verticalLayout_3.setStretch(0, 10)
        self.verticalLayout_3.setStretch(1, 100)

        self.horizontalLayout.addWidget(self.vxv_matrix_vector_widget)

        self.vxv_column_vector_widget = QWidget(self.vxv_options_widget)
        self.vxv_column_vector_widget.setObjectName(u"vxv_column_vector_widget")
        self.verticalLayout_6 = QVBoxLayout(self.vxv_column_vector_widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.vxv_column_vector_label = QLabel(self.vxv_column_vector_widget)
        self.vxv_column_vector_label.setObjectName(u"vxv_column_vector_label")

        self.verticalLayout_6.addWidget(self.vxv_column_vector_label, 0, Qt.AlignmentFlag.AlignLeft)

        self.vxv_column_vector = QTableWidget(self.vxv_column_vector_widget)
        if (self.vxv_column_vector.columnCount() < 1):
            self.vxv_column_vector.setColumnCount(1)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.vxv_column_vector.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        if (self.vxv_column_vector.rowCount() < 4):
            self.vxv_column_vector.setRowCount(4)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.vxv_column_vector.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.vxv_column_vector.setVerticalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.vxv_column_vector.setVerticalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.vxv_column_vector.setVerticalHeaderItem(3, __qtablewidgetitem9)
        self.vxv_column_vector.setObjectName(u"vxv_column_vector")
        self.vxv_column_vector.setMaximumSize(QSize(50, 16777215))
        self.vxv_column_vector.horizontalHeader().setVisible(True)
        self.vxv_column_vector.horizontalHeader().setMinimumSectionSize(10)
        self.vxv_column_vector.horizontalHeader().setDefaultSectionSize(35)
        self.vxv_column_vector.horizontalHeader().setHighlightSections(True)
        self.vxv_column_vector.verticalHeader().setVisible(False)
        self.vxv_column_vector.verticalHeader().setCascadingSectionResizes(False)
        self.vxv_column_vector.verticalHeader().setMinimumSectionSize(35)
        self.vxv_column_vector.verticalHeader().setDefaultSectionSize(35)
        self.vxv_column_vector.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_6.addWidget(self.vxv_column_vector)


        self.horizontalLayout.addWidget(self.vxv_column_vector_widget)


        self.verticalLayout_2.addWidget(self.vxv_options_widget)

        self.vxv_solution_widget = QWidget(self.vector_x_vector_widget)
        self.vxv_solution_widget.setObjectName(u"vxv_solution_widget")
        self.horizontalLayout_2 = QHBoxLayout(self.vxv_solution_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.vxv_solution_options = QWidget(self.vxv_solution_widget)
        self.vxv_solution_options.setObjectName(u"vxv_solution_options")
        self.horizontalLayout_3 = QHBoxLayout(self.vxv_solution_options)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.vxv_solve_scalar_button = QPushButton(self.vxv_solution_options)
        self.vxv_solve_scalar_button.setObjectName(u"vxv_solve_scalar_button")

        self.horizontalLayout_3.addWidget(self.vxv_solve_scalar_button, 0, Qt.AlignmentFlag.AlignLeft)

        self.vxv_scalar_label = QLabel(self.vxv_solution_options)
        self.vxv_scalar_label.setObjectName(u"vxv_scalar_label")
        self.vxv_scalar_label.setMaximumSize(QSize(16777215, 24))
        self.vxv_scalar_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.vxv_scalar_label, 0, Qt.AlignmentFlag.AlignLeft)


        self.horizontalLayout_2.addWidget(self.vxv_solution_options)

        self.vxv_horizontal_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.vxv_horizontal_spacer)

        self.horizontalLayout_2.setStretch(0, 5)
        self.horizontalLayout_2.setStretch(1, 100)

        self.verticalLayout_2.addWidget(self.vxv_solution_widget)

        self.verticalLayout_2.setStretch(0, 5)
        self.verticalLayout_2.setStretch(1, 1)
        self.tab_widget.addTab(self.vector_x_vector_widget, "")
        self.matrix_x_matrix_widget = QWidget()
        self.matrix_x_matrix_widget.setObjectName(u"matrix_x_matrix_widget")
        self.verticalLayout_18 = QVBoxLayout(self.matrix_x_matrix_widget)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.mxm_options_widget = QWidget(self.matrix_x_matrix_widget)
        self.mxm_options_widget.setObjectName(u"mxm_options_widget")
        self.horizontalLayout_7 = QHBoxLayout(self.mxm_options_widget)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, -1)
        self.mxm_matrix_vector_widget = QWidget(self.mxm_options_widget)
        self.mxm_matrix_vector_widget.setObjectName(u"mxm_matrix_vector_widget")
        self.verticalLayout_13 = QVBoxLayout(self.mxm_matrix_vector_widget)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.mxm_spinbox_widget = QWidget(self.mxm_matrix_vector_widget)
        self.mxm_spinbox_widget.setObjectName(u"mxm_spinbox_widget")
        self.verticalLayout_14 = QVBoxLayout(self.mxm_spinbox_widget)
        self.verticalLayout_14.setSpacing(6)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.mxm_row_label = QLabel(self.mxm_spinbox_widget)
        self.mxm_row_label.setObjectName(u"mxm_row_label")
        self.mxm_row_label.setMaximumSize(QSize(16777215, 28))

        self.verticalLayout_14.addWidget(self.mxm_row_label, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_13.addWidget(self.mxm_spinbox_widget)

        self.mxm_a_widget = QWidget(self.mxm_matrix_vector_widget)
        self.mxm_a_widget.setObjectName(u"mxm_a_widget")
        self.mxm_a_widget.setStyleSheet(u"QTabBar:tab{\n"
"max-width:10px;\n"
"}")
        self.verticalLayout_15 = QVBoxLayout(self.mxm_a_widget)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.mxm_a_table = QTableWidget(self.mxm_a_widget)
        if (self.mxm_a_table.columnCount() < 4):
            self.mxm_a_table.setColumnCount(4)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.mxm_a_table.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.mxm_a_table.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.mxm_a_table.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.mxm_a_table.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        if (self.mxm_a_table.rowCount() < 1):
            self.mxm_a_table.setRowCount(1)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.mxm_a_table.setItem(0, 0, __qtablewidgetitem14)
        self.mxm_a_table.setObjectName(u"mxm_a_table")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mxm_a_table.sizePolicy().hasHeightForWidth())
        self.mxm_a_table.setSizePolicy(sizePolicy)
        self.mxm_a_table.setMinimumSize(QSize(230, 0))
        self.mxm_a_table.setMaximumSize(QSize(16777215, 16777215))
        self.mxm_a_table.setStyleSheet(u"QTableWidget:item{\n"
"max-width:10px;\n"
"}")
        self.mxm_a_table.setGridStyle(Qt.PenStyle.SolidLine)
        self.mxm_a_table.horizontalHeader().setVisible(True)
        self.mxm_a_table.horizontalHeader().setMinimumSectionSize(10)
        self.mxm_a_table.horizontalHeader().setDefaultSectionSize(50)
        self.mxm_a_table.horizontalHeader().setHighlightSections(False)
        self.mxm_a_table.verticalHeader().setVisible(True)
        self.mxm_a_table.verticalHeader().setDefaultSectionSize(22)
        self.mxm_a_table.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_15.addWidget(self.mxm_a_table)


        self.verticalLayout_13.addWidget(self.mxm_a_widget)

        self.verticalLayout_13.setStretch(0, 10)
        self.verticalLayout_13.setStretch(1, 100)

        self.horizontalLayout_7.addWidget(self.mxm_matrix_vector_widget)

        self.mxm_column_vector_widget = QWidget(self.mxm_options_widget)
        self.mxm_column_vector_widget.setObjectName(u"mxm_column_vector_widget")
        self.verticalLayout_16 = QVBoxLayout(self.mxm_column_vector_widget)
        self.verticalLayout_16.setSpacing(4)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.mmv_column_vector_options_widget = QWidget(self.mxm_column_vector_widget)
        self.mmv_column_vector_options_widget.setObjectName(u"mmv_column_vector_options_widget")
        self.horizontalLayout_9 = QHBoxLayout(self.mmv_column_vector_options_widget)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.mxm_column_vector_label = QLabel(self.mmv_column_vector_options_widget)
        self.mxm_column_vector_label.setObjectName(u"mxm_column_vector_label")
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.mxm_column_vector_label.setFont(font)

        self.horizontalLayout_9.addWidget(self.mxm_column_vector_label, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.mxm_column_widget = QWidget(self.mmv_column_vector_options_widget)
        self.mxm_column_widget.setObjectName(u"mxm_column_widget")
        sizePolicy.setHeightForWidth(self.mxm_column_widget.sizePolicy().hasHeightForWidth())
        self.mxm_column_widget.setSizePolicy(sizePolicy)
        self.verticalLayout_19 = QVBoxLayout(self.mxm_column_widget)
        self.verticalLayout_19.setSpacing(5)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.mxm_column_label = QLabel(self.mxm_column_widget)
        self.mxm_column_label.setObjectName(u"mxm_column_label")

        self.verticalLayout_19.addWidget(self.mxm_column_label, 0, Qt.AlignmentFlag.AlignTop)

        self.mxm_column_buttons_widget = QWidget(self.mxm_column_widget)
        self.mxm_column_buttons_widget.setObjectName(u"mxm_column_buttons_widget")
        self.horizontalLayout_10 = QHBoxLayout(self.mxm_column_buttons_widget)
        self.horizontalLayout_10.setSpacing(7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.mxm_add_column_button = QPushButton(self.mxm_column_buttons_widget)
        self.mxm_add_column_button.setObjectName(u"mxm_add_column_button")
        icon1 = QIcon()
        icon1.addFile(u":/icon/Images/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mxm_add_column_button.setIcon(icon1)
        self.mxm_add_column_button.setIconSize(QSize(12, 16))

        self.horizontalLayout_10.addWidget(self.mxm_add_column_button)

        self.mxm_substract_column_button = QPushButton(self.mxm_column_buttons_widget)
        self.mxm_substract_column_button.setObjectName(u"mxm_substract_column_button")
        icon2 = QIcon()
        icon2.addFile(u":/icon/Images/substract.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mxm_substract_column_button.setIcon(icon2)
        self.mxm_substract_column_button.setIconSize(QSize(12, 16))

        self.horizontalLayout_10.addWidget(self.mxm_substract_column_button)


        self.verticalLayout_19.addWidget(self.mxm_column_buttons_widget)


        self.horizontalLayout_9.addWidget(self.mxm_column_widget, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_16.addWidget(self.mmv_column_vector_options_widget)

        self.mxm_b_table = QTableWidget(self.mxm_column_vector_widget)
        if (self.mxm_b_table.columnCount() < 1):
            self.mxm_b_table.setColumnCount(1)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.mxm_b_table.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        if (self.mxm_b_table.rowCount() < 4):
            self.mxm_b_table.setRowCount(4)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.mxm_b_table.setVerticalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.mxm_b_table.setVerticalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.mxm_b_table.setVerticalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.mxm_b_table.setVerticalHeaderItem(3, __qtablewidgetitem19)
        self.mxm_b_table.setObjectName(u"mxm_b_table")
        self.mxm_b_table.setMaximumSize(QSize(16777215, 16777215))
        self.mxm_b_table.horizontalHeader().setVisible(True)
        self.mxm_b_table.horizontalHeader().setMinimumSectionSize(10)
        self.mxm_b_table.horizontalHeader().setDefaultSectionSize(35)
        self.mxm_b_table.horizontalHeader().setHighlightSections(True)
        self.mxm_b_table.verticalHeader().setVisible(False)
        self.mxm_b_table.verticalHeader().setCascadingSectionResizes(False)
        self.mxm_b_table.verticalHeader().setMinimumSectionSize(35)
        self.mxm_b_table.verticalHeader().setDefaultSectionSize(35)
        self.mxm_b_table.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_16.addWidget(self.mxm_b_table)


        self.horizontalLayout_7.addWidget(self.mxm_column_vector_widget)


        self.verticalLayout_18.addWidget(self.mxm_options_widget)

        self.mxm_solution_widget = QWidget(self.matrix_x_matrix_widget)
        self.mxm_solution_widget.setObjectName(u"mxm_solution_widget")
        self.verticalLayout_17 = QVBoxLayout(self.mxm_solution_widget)
        self.verticalLayout_17.setSpacing(3)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.mxm_solution_button_widget = QWidget(self.mxm_solution_widget)
        self.mxm_solution_button_widget.setObjectName(u"mxm_solution_button_widget")
        self.verticalLayout_20 = QVBoxLayout(self.mxm_solution_button_widget)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.mxm_solution_button = QPushButton(self.mxm_solution_button_widget)
        self.mxm_solution_button.setObjectName(u"mxm_solution_button")
        self.mxm_solution_button.setFont(font)

        self.verticalLayout_20.addWidget(self.mxm_solution_button)


        self.verticalLayout_17.addWidget(self.mxm_solution_button_widget, 0, Qt.AlignmentFlag.AlignLeft)

        self.mxm_c_matrix = QTableWidget(self.mxm_solution_widget)
        self.mxm_c_matrix.setObjectName(u"mxm_c_matrix")

        self.verticalLayout_17.addWidget(self.mxm_c_matrix)


        self.verticalLayout_18.addWidget(self.mxm_solution_widget)

        self.tab_widget.addTab(self.matrix_x_matrix_widget, "")
        self.matrix_x_vector_widget = QWidget()
        self.matrix_x_vector_widget.setObjectName(u"matrix_x_vector_widget")
        self.verticalLayout_7 = QVBoxLayout(self.matrix_x_vector_widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.mxv_options_widget = QWidget(self.matrix_x_vector_widget)
        self.mxv_options_widget.setObjectName(u"mxv_options_widget")
        self.horizontalLayout_6 = QHBoxLayout(self.mxv_options_widget)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, -1, 0, -1)
        self.mxv_matrix_vector_widget = QWidget(self.mxv_options_widget)
        self.mxv_matrix_vector_widget.setObjectName(u"mxv_matrix_vector_widget")
        self.verticalLayout_8 = QVBoxLayout(self.mxv_matrix_vector_widget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.mxv_spinbox_widget = QWidget(self.mxv_matrix_vector_widget)
        self.mxv_spinbox_widget.setObjectName(u"mxv_spinbox_widget")
        self.verticalLayout_9 = QVBoxLayout(self.mxv_spinbox_widget)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.mxv_row_label = QLabel(self.mxv_spinbox_widget)
        self.mxv_row_label.setObjectName(u"mxv_row_label")

        self.verticalLayout_9.addWidget(self.mxv_row_label, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_8.addWidget(self.mxv_spinbox_widget)

        self.mxv_row_vector_widget = QWidget(self.mxv_matrix_vector_widget)
        self.mxv_row_vector_widget.setObjectName(u"mxv_row_vector_widget")
        self.mxv_row_vector_widget.setStyleSheet(u"QTabBar:tab{\n"
"max-width:10px;\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.mxv_row_vector_widget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.mxv_row_vector = QTableWidget(self.mxv_row_vector_widget)
        if (self.mxv_row_vector.columnCount() < 4):
            self.mxv_row_vector.setColumnCount(4)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.mxv_row_vector.setHorizontalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.mxv_row_vector.setHorizontalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.mxv_row_vector.setHorizontalHeaderItem(2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.mxv_row_vector.setHorizontalHeaderItem(3, __qtablewidgetitem23)
        if (self.mxv_row_vector.rowCount() < 1):
            self.mxv_row_vector.setRowCount(1)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.mxv_row_vector.setItem(0, 0, __qtablewidgetitem24)
        self.mxv_row_vector.setObjectName(u"mxv_row_vector")
        self.mxv_row_vector.setMinimumSize(QSize(230, 0))
        self.mxv_row_vector.setMaximumSize(QSize(16777215, 16777215))
        self.mxv_row_vector.setStyleSheet(u"QTableWidget:item{\n"
"max-width:10px;\n"
"}")
        self.mxv_row_vector.setGridStyle(Qt.PenStyle.SolidLine)
        self.mxv_row_vector.horizontalHeader().setVisible(True)
        self.mxv_row_vector.horizontalHeader().setMinimumSectionSize(10)
        self.mxv_row_vector.horizontalHeader().setDefaultSectionSize(50)
        self.mxv_row_vector.horizontalHeader().setHighlightSections(False)
        self.mxv_row_vector.verticalHeader().setVisible(True)
        self.mxv_row_vector.verticalHeader().setDefaultSectionSize(22)
        self.mxv_row_vector.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_10.addWidget(self.mxv_row_vector)


        self.verticalLayout_8.addWidget(self.mxv_row_vector_widget)

        self.verticalLayout_8.setStretch(0, 10)
        self.verticalLayout_8.setStretch(1, 100)

        self.horizontalLayout_6.addWidget(self.mxv_matrix_vector_widget)

        self.mxv_column_vector_widget = QWidget(self.mxv_options_widget)
        self.mxv_column_vector_widget.setObjectName(u"mxv_column_vector_widget")
        self.verticalLayout_11 = QVBoxLayout(self.mxv_column_vector_widget)
        self.verticalLayout_11.setSpacing(4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.mxv_column_vector_options_widget = QWidget(self.mxv_column_vector_widget)
        self.mxv_column_vector_options_widget.setObjectName(u"mxv_column_vector_options_widget")
        self.horizontalLayout_8 = QHBoxLayout(self.mxv_column_vector_options_widget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.mxv_column_substact_vector_button = QPushButton(self.mxv_column_vector_options_widget)
        self.mxv_column_substact_vector_button.setObjectName(u"mxv_column_substact_vector_button")
        self.mxv_column_substact_vector_button.setIcon(icon2)

        self.horizontalLayout_8.addWidget(self.mxv_column_substact_vector_button)

        self.mxv_column_vector_label = QLabel(self.mxv_column_vector_options_widget)
        self.mxv_column_vector_label.setObjectName(u"mxv_column_vector_label")

        self.horizontalLayout_8.addWidget(self.mxv_column_vector_label)

        self.mxv_column_add_vector_button = QPushButton(self.mxv_column_vector_options_widget)
        self.mxv_column_add_vector_button.setObjectName(u"mxv_column_add_vector_button")
        self.mxv_column_add_vector_button.setIcon(icon1)

        self.horizontalLayout_8.addWidget(self.mxv_column_add_vector_button)


        self.verticalLayout_11.addWidget(self.mxv_column_vector_options_widget)

        self.mxv_column_vector_table = QTableWidget(self.mxv_column_vector_widget)
        if (self.mxv_column_vector_table.columnCount() < 1):
            self.mxv_column_vector_table.setColumnCount(1)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.mxv_column_vector_table.setHorizontalHeaderItem(0, __qtablewidgetitem25)
        if (self.mxv_column_vector_table.rowCount() < 4):
            self.mxv_column_vector_table.setRowCount(4)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.mxv_column_vector_table.setVerticalHeaderItem(0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.mxv_column_vector_table.setVerticalHeaderItem(1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.mxv_column_vector_table.setVerticalHeaderItem(2, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.mxv_column_vector_table.setVerticalHeaderItem(3, __qtablewidgetitem29)
        self.mxv_column_vector_table.setObjectName(u"mxv_column_vector_table")
        self.mxv_column_vector_table.setMaximumSize(QSize(16777215, 16777215))
        self.mxv_column_vector_table.horizontalHeader().setVisible(True)
        self.mxv_column_vector_table.horizontalHeader().setMinimumSectionSize(10)
        self.mxv_column_vector_table.horizontalHeader().setDefaultSectionSize(35)
        self.mxv_column_vector_table.horizontalHeader().setHighlightSections(True)
        self.mxv_column_vector_table.verticalHeader().setVisible(False)
        self.mxv_column_vector_table.verticalHeader().setCascadingSectionResizes(False)
        self.mxv_column_vector_table.verticalHeader().setMinimumSectionSize(35)
        self.mxv_column_vector_table.verticalHeader().setDefaultSectionSize(35)
        self.mxv_column_vector_table.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_11.addWidget(self.mxv_column_vector_table)


        self.horizontalLayout_6.addWidget(self.mxv_column_vector_widget)

        self.horizontalLayout_6.setStretch(0, 100)
        self.horizontalLayout_6.setStretch(1, 50)

        self.verticalLayout_7.addWidget(self.mxv_options_widget)

        self.mxv_solution_widget = QWidget(self.matrix_x_vector_widget)
        self.mxv_solution_widget.setObjectName(u"mxv_solution_widget")
        self.horizontalLayout_4 = QHBoxLayout(self.mxv_solution_widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.mxv_solution_button_widget = QWidget(self.mxv_solution_widget)
        self.mxv_solution_button_widget.setObjectName(u"mxv_solution_button_widget")
        self.verticalLayout_12 = QVBoxLayout(self.mxv_solution_button_widget)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.mxv_solution_button = QPushButton(self.mxv_solution_button_widget)
        self.mxv_solution_button.setObjectName(u"mxv_solution_button")

        self.verticalLayout_12.addWidget(self.mxv_solution_button, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_4.addWidget(self.mxv_solution_button_widget)


        self.verticalLayout_7.addWidget(self.mxv_solution_widget)

        self.verticalLayout_7.setStretch(0, 100)
        self.verticalLayout_7.setStretch(1, 5)
        self.tab_widget.addTab(self.matrix_x_vector_widget, "")

        self.verticalLayout.addWidget(self.tab_widget)

        self.vxv_resize_vector_row()
        self.vxv_resize_vector_column()
        self.vxv_set_vector_row(self.matrix_instance[0])
        self.mxv_resize_column_vector()
        self.set_matrix_vectors()
        self.mxm_set_matrix()
        self.tab_widget.setCurrentIndex(0)
        self.vxv_row_spinbox.setValue(1)
        self.mxv_column_add_vector_button.clicked.connect(lambda: self.add_vector)
        self.mxv_column_substact_vector_button.clicked.connect(lambda: self.delete_vector)
        self.mxm_add_column_button.clicked.connect(lambda: self.mxm_add_column_table_b())
        self.mxm_substract_column_button.clicked.connect(lambda: self.mxm_substract_column_table_b())
        self.mxm_b_table.setRowCount(self.mxm_a_table.rowCount())
        self.retranslateUi(main_widget)

        self.tab_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(main_widget)
    # setupUi

    def retranslateUi(self, main_widget):
        main_widget.setWindowTitle(QCoreApplication.translate("main_widget", u"Vectores", None))
        self.vxv_row_label.setText(QCoreApplication.translate("main_widget", u"Fila de la columna", None))

        __sortingEnabled = self.vxv_row_vector.isSortingEnabled()
        self.vxv_row_vector.setSortingEnabled(False)
        self.vxv_row_vector.setSortingEnabled(__sortingEnabled)

        self.vxv_column_vector_label.setText(QCoreApplication.translate("main_widget", u"Vector", None))

        self.vxv_solve_scalar_button.setText(QCoreApplication.translate("main_widget", u"Obtener escalar", None))
        self.vxv_scalar_label.setText(QCoreApplication.translate("main_widget", u"Valor", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.vector_x_vector_widget), QCoreApplication.translate("main_widget", u"Vector por vector", None))
        self.mxm_row_label.setText(QCoreApplication.translate("main_widget", u"Matriz A", None))

        __sortingEnabled1 = self.mxm_a_table.isSortingEnabled()
        self.mxm_a_table.setSortingEnabled(False)
        self.mxm_a_table.setSortingEnabled(__sortingEnabled1)

        self.mxm_column_vector_label.setText(QCoreApplication.translate("main_widget", u"Matriz B", None))
        self.mxm_column_label.setText(QCoreApplication.translate("main_widget", u"Cantidad de columnas", None))
        self.mxm_add_column_button.setText("")
        self.mxm_substract_column_button.setText("")

        self.mxm_solution_button.setText(QCoreApplication.translate("main_widget", u"Matriz C", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.matrix_x_matrix_widget), QCoreApplication.translate("main_widget", u"Matriz por matriz", None))
#if QT_CONFIG(accessibility)
        self.matrix_x_vector_widget.setAccessibleName(QCoreApplication.translate("main_widget", u"asd", None))
#endif // QT_CONFIG(accessibility)
        self.mxv_row_label.setText(QCoreApplication.translate("main_widget", u"Matriz", None))

        __sortingEnabled2 = self.mxv_row_vector.isSortingEnabled()
        self.mxv_row_vector.setSortingEnabled(False)
        self.mxv_row_vector.setSortingEnabled(__sortingEnabled2)

        self.mxv_column_substact_vector_button.setText("")
        self.mxv_column_vector_label.setText(QCoreApplication.translate("main_widget", u"Vectores", None))
        self.mxv_column_add_vector_button.setText("")
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.matrix_x_vector_widget), QCoreApplication.translate("main_widget", u"Matriz por vector", None))
        self.mxm_b_table.horizontalHeaderItem(0).setText('X1')
    # retranslateUi


    def mxv_resize_column_vector(self):
        rows = len(self.matrix_instance[0])
        self.mxv_column_vector_table.setRowCount(rows)
        table_header = self.mxv_column_vector_table.horizontalHeaderItem(0)
        if table_header is None:
            table_header = QTableWidgetItem()
            self.mxv_column_vector_table.setHorizontalHeaderItem(0,table_header)
        table_header.setText("v1")

    def vxv_set_vector_row(self,vector:list[int|float]):
        for i in range(self.vxv_row_vector.columnCount()):
            table_item = self.vxv_row_vector.item(0,i)
            if table_item is None:
                table_item = QTableWidgetItem()
                table_item.setFlags(Qt.ItemIsEnabled)
                self.vxv_row_vector.setItem(0,i,table_item)
            table_item.setText(str(vector[i]))
    
    def vxv_resize_vector_row(self):
        width = len(self.matrix_instance[0])
        self.vxv_row_vector.setRowCount(1)
        self.vxv_row_vector.setColumnCount(width)
        for i in range(width):
            table_header = self.vxv_row_vector.horizontalHeaderItem(i)
            if table_header is None:
                table_header = QTableWidgetItem()
                self.vxv_column_vector.setHorizontalHeaderItem(i,table_header)
            table_header.setText(f'X{i+1}')
    
    def vxv_resize_vector_column(self):
        length = len(self.matrix_instance)
        self.vxv_column_vector.setRowCount(length)
        self.vxv_column_vector.setColumnCount(1)
        table_header = self.vxv_column_vector.horizontalHeaderItem(0)
        if table_header is None:
            table_header = QTableWidgetItem()
            self.vxv_column_vector.setHorizontalHeaderItem(0,table_header)
        table_header.setText('b')

    def set_matrix_vectors(self):
        width = len(self.matrix_instance)
        length = len(self.matrix_instance[0])
        self.mxv_row_vector.setRowCount(width)
        self.mxv_row_vector.setColumnCount(length)
        for row in range(width):
            table_header = self.mxv_row_vector.verticalHeaderItem(row)
            if table_header is None:
                table_header = QTableWidgetItem()
                self.mxv_row_vector.setVerticalHeaderItem(row,table_header)
            table_header.setText(f'{row+1}')
        for col in range(length):
            table_header = self.mxv_row_vector.horizontalHeaderItem(col)
            if table_header is None:
                table_header = QTableWidgetItem()
                self.mxv_row_vector.setHorizontalHeaderItem(col,table_header)
            table_header.setText(f"X{col+1}")
        self.fill_mxv_matrix(width,length)

    def fill_mxv_matrix(self,rows,columns):
        for row in range(rows):
            for col in range(columns):
                table_item:QTableWidgetItem = self.mxv_row_vector.item(row,col)
                if table_item is None:
                    table_item = QTableWidgetItem()
                    table_item.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
                    self.mxv_row_vector.setItem(row,col,table_item)
                table_item.setText(str(self.matrix_instance[row][col]))

    def mxm_set_matrix(self):
        width = len(self.matrix_instance)
        length = len(self.matrix_instance[0])
        self.mxm_a_table.setRowCount(width)
        self.mxm_a_table.setColumnCount(length)
        for row in range(width):
            table_header = self.mxm_a_table.verticalHeaderItem(row)
            if table_header is None:
                table_header = QTableWidgetItem()
                self.mxm_a_table.setVerticalHeaderItem(row,table_header)
            table_header.setText(f'{row+1}')
        for col in range(length):
            table_header = self.mxm_a_table.horizontalHeaderItem(col)
            if table_header is None:
                table_header = QTableWidgetItem()
                self.mxm_a_table.setHorizontalHeaderItem(col,table_header)
            table_header.setText(f"X{col+1}")
        self.fill_mxm_matrix_a(width,length)

    def fill_mxm_matrix_a(self,rows,columns):
        for row in range(rows):
            for col in range(columns):
                table_item:QTableWidgetItem = self.mxm_a_table.item(row,col)
                if table_item is None:
                    table_item = QTableWidgetItem()
                    table_item.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
                    self.mxm_a_table.setItem(row,col,table_item)
                table_item.setText(str(self.matrix_instance[row][col]))
    
    @Slot()
    def add_vector(self):
        column_count = self.mxv_column_vector_table.columnCount()
        self.mxv_column_vector_table.setColumnCount(column_count+1)
        table_header = self.mxv_column_vector_table.horizontalHeaderItem(column_count+1)
        if table_header is None:
            table_header = QTableWidgetItem()
            self.mxv_column_vector_table.setHorizontalHeaderItem(column_count,table_header)
        table_header.setText(f"v{column_count+1}")

    @Slot()
    def delete_vector(self):
        column_count = self.mxv_column_vector_table.columnCount()
        if column_count <=1:return
        self.mxv_column_vector_table.setColumnCount(column_count-1)

    @Slot()
    def mxm_add_column_table_b(self):
        column_count = self.mxm_b_table.columnCount()
        self.mxm_b_table.setColumnCount(column_count+1)
        table_header = self.mxm_b_table.horizontalHeaderItem(column_count+1)
        if table_header is None:
            table_header = QTableWidgetItem()
            self.mxm_b_table.setHorizontalHeaderItem(column_count,table_header)
        table_header.setText(f"X{column_count+1}")

    @Slot()
    def mxm_substract_column_table_b(self):
        column_count = self.mxm_b_table.columnCount()
        if column_count <=1:return
        self.mxm_b_table.setColumnCount(column_count-1)

    def mxm_set_matrix_c(self,matrix_c):
        filas = len(matrix_c)
        columnas = len(matrix_c[0])
        self.mxm_c_matrix.setRowCount(filas)
        self.mxm_c_matrix.setColumnCount(columnas)
        for i in range(filas):
            for j in range(columnas):
                item = self.mxm_c_matrix.item(i,j)
                if item is None:
                    item = QTableWidgetItem()
                    self.mxm_c_matrix.setItem(i,j,item)
                item.setText(str(matrix_c[i][j]))
