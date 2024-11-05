# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowWopQvr.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpinBox, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

from PySide6.QtSvg import QtSvg
from views.qt_files.qrc_files import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.resize(657, 491)
        icon = QIcon()
        icon.addFile(u":/icon/Images/grid.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"*{\n"
"border:none;\n"
"background-color: transparent;\n"
"background: none;\n"
"padding: 0;\n"
"margin: 0;\n"
"color: #fff;\n"
"}\n"
"\n"
"QToolTip{\n"
"color: #000;\n"
"padding: 2px;\n"
"border-radius:3px;\n"
"}\n"
"#MainWindow{\n"
"background: #2c313c\n"
"}\n"
"\n"
"#table_buttons_frame{\n"
"background-color: #2c313c\n"
"}\n"
"\n"
"#table_buttons_frame QPushButton, #table_buttons_frame QComboBox,#solution_widget QComboBox, #solution_widget QPushButton {\n"
"    color: #ffffff;\n"
"    text-align: center;\n"
"	padding: 3px;\n"
"    border-radius: 10px;\n"
"    background-color: #16191d;\n"
"}\n"
"\n"
"#table_buttons_frame QPushButton::hover, #table_buttons_frame QComboBox::hover,#solution_widget QComboBox::hover, #solution_widget QPushButton::hover {\n"
"    background-color: #2a2e35;\n"
"    border-color: #454a52;\n"
"}\n"
"\n"
"#table_buttons_frame QPushButton::pressed, #table_buttons_frame QComboBox::pressed,#solution_widget QComboBox::pressed, #solution_widget QPushButton::pressed {\n"
"    background-co"
                        "lor: #1d2127;\n"
"	font-weight: 350;\n"
"}\n"
"\n"
"#table_buttons_frame QSpinBox{\n"
"color: #fff;\n"
"background-color: #1d2127;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#table_buttons_frame QLabel{\n"
"background-color: #1f232a;\n"
"padding: 3px;\n"
"font-weight: 700;\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"#table_column_spinbox_widget QSpinBox, #table_row_spinbox_widget QSpinBox{\n"
"color: #fff;\n"
"font-weight: 700;\n"
"}\n"
"\n"
"#table_column_spinbox_widget QSpinBox:up-button, #table_row_spinbox_widget QSpinBox:up-button{\n"
"image:url(:/icon/Images/arrow_upwards.png);\n"
"subcontrol-position: right;\n"
"width: 18px;\n"
"height: 18px;\n"
"}\n"
"\n"
"#table_column_spinbox_widget QSpinBox:down-button, #table_row_spinbox_widget QSpinBox:down-button{\n"
"image:url(:/icon/Images/arrow_downwards.png);\n"
"subcontrol-position: left;\n"
"width: 18px;\n"
"height: 18px;\n"
"}\n"
"\n"
" #table_buttons_frame QComboBox:dropdown, #solution_widget QComboBox{\n"
"border: 0px;\n"
"}\n"
"\n"
"#table_buttons_frame QComboBo"
                        "x:down-arrow, #solution_widget QComboBox{\n"
"subcontrol-position: right;\n"
"width: 18px;\n"
"height: 18px;\n"
"}\n"
"\n"
"#table_buttons_frame QComboBox QListView, #solution_widget QComboBox QListView{\n"
"color: #fff;\n"
"font-weight: 500;\n"
"background-color: #2c313c;\n"
"outline: 0px;\n"
"padding: 5px;\n"
"}\n"
"\n"
"#main_table_widget QTableWidget{\n"
"background-color: #3e4555;\n"
"gridline-color:#fff;\n"
"}\n"
"\n"
"#main_table_widget QHeaderView, #main_table_widget QHeaderView::section, #main_table_widget QTableCornerButton::section{\n"
"background-color: #3e4555;\n"
"color: #fff;\n"
"}\n"
"\n"
"#main_table_widget QTableWidget::item{\n"
"color: #fff;\n"
"}\n"
"\n"
"#main_table_widget QTableWidget::item::hover{\n"
"background-color: #242831;\n"
"font-weight: 700;\n"
"}\n"
"\n"
"#side_bar{\n"
"background: #16191d\n"
"}\n"
"#tab_buttons_frame QPushButton, #expand_button_frame QPushButton{\n"
"text-align: left;\n"
"}\n"
"#tab_buttons_frame QPushButton::hover{\n"
"background-color: #1f232a;\n"
"}\n"
"\n"
""
                        "#equation_widget QLineEdit{\n"
"color: #fff;\n"
"background-color: #596379;\n"
"border-radius:10px;\n"
"padding: 5px;\n"
"font-weight: 350;\n"
"}\n"
"\n"
"#equation_buttons_frame QLineEdit{\n"
"color: #fff;\n"
"background-color: #596379;\n"
"border-radius:10px;\n"
"padding: 5px;\n"
"font-weight: 350;\n"
"}\n"
"#equation_buttons_frame QLabel{\n"
"background-color: #1f232a;\n"
"padding: 3px;\n"
"font-weight: 700;\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"#equations_page{\n"
"background: #2c313c\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.side_bar = QWidget(self.centralwidget)
        self.side_bar.setObjectName(u"side_bar")
        self.side_bar.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.side_bar)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.verticalLayout_5.setContentsMargins(9, 0, 0, 0)
        self.sub_side_bar = QWidget(self.side_bar)
        self.sub_side_bar.setObjectName(u"sub_side_bar")
        self.sub_side_bar.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_11 = QVBoxLayout(self.sub_side_bar)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.expand_button_frame = QFrame(self.sub_side_bar)
        self.expand_button_frame.setObjectName(u"expand_button_frame")
        self.expand_button_frame.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.expand_button_frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.expand_button = QPushButton(self.expand_button_frame)
        self.expand_button.setObjectName(u"expand_button")
        self.expand_button.setStyleSheet(u"text-align:left;")
        icon1 = QIcon()
        icon1.addFile(u":/icon/Images/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.expand_button.setIcon(icon1)
        self.expand_button.setIconSize(QSize(28, 28))

        self.verticalLayout_6.addWidget(self.expand_button, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_11.addWidget(self.expand_button_frame)

        self.tab_buttons_frame = QFrame(self.sub_side_bar)
        self.tab_buttons_frame.setObjectName(u"tab_buttons_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_buttons_frame.sizePolicy().hasHeightForWidth())
        self.tab_buttons_frame.setSizePolicy(sizePolicy)
        self.tab_buttons_frame.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_7 = QVBoxLayout(self.tab_buttons_frame)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.matrix_tab_button = QPushButton(self.tab_buttons_frame)
        self.matrix_tab_button.setObjectName(u"matrix_tab_button")
        self.matrix_tab_button.setEnabled(True)
        font = QFont()
        font.setBold(False)
        self.matrix_tab_button.setFont(font)
        self.matrix_tab_button.setStyleSheet(u"text-align:left;")
        icon2 = QIcon()
        icon2.addFile(u":/icon/Images/matrix.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.matrix_tab_button.setIcon(icon2)
        self.matrix_tab_button.setIconSize(QSize(28, 28))

        self.verticalLayout_7.addWidget(self.matrix_tab_button)

        self.equation_tab_button = QPushButton(self.tab_buttons_frame)
        self.equation_tab_button.setObjectName(u"equation_tab_button")
        self.equation_tab_button.setStyleSheet(u"text-align:left;")
        icon3 = QIcon()
        icon3.addFile(u":/icon/Images/fx.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.equation_tab_button.setIcon(icon3)
        self.equation_tab_button.setIconSize(QSize(32, 32))

        self.verticalLayout_7.addWidget(self.equation_tab_button)


        self.verticalLayout_11.addWidget(self.tab_buttons_frame, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_5.addWidget(self.sub_side_bar)


        self.horizontalLayout.addWidget(self.side_bar)

        self.main_stacked_widget = QStackedWidget(self.centralwidget)
        self.main_stacked_widget.setObjectName(u"main_stacked_widget")
        self.matrix_page = QWidget()
        self.matrix_page.setObjectName(u"matrix_page")
        self.verticalLayout_4 = QVBoxLayout(self.matrix_page)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(4, 0, 0, 0)
        self.main_table_widget = QWidget(self.matrix_page)
        self.main_table_widget.setObjectName(u"main_table_widget")
        self.verticalLayout_2 = QVBoxLayout(self.main_table_widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.table_buttons_frame = QFrame(self.main_table_widget)
        self.table_buttons_frame.setObjectName(u"table_buttons_frame")
        self.table_buttons_frame.setStyleSheet(u"")
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
        self.row_spinbox_label.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.row_spinbox_label.setFont(font1)

        self.verticalLayout_3.addWidget(self.row_spinbox_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.row_spinbox = QSpinBox(self.table_row_spinbox_widget)
        self.row_spinbox.setObjectName(u"row_spinbox")
        self.row_spinbox.setMinimumSize(QSize(60, 30))
        self.row_spinbox.setMaximumSize(QSize(16777215, 16777215))
        self.row_spinbox.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.row_spinbox.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.row_spinbox, 0, Qt.AlignmentFlag.AlignHCenter)


        self.table_buttons_horizontal_layout.addWidget(self.table_row_spinbox_widget)

        self.table_column_spinbox_widget = QWidget(self.table_buttons_frame)
        self.table_column_spinbox_widget.setObjectName(u"table_column_spinbox_widget")
        self.verticalLayout = QVBoxLayout(self.table_column_spinbox_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.column_spinbox_label = QLabel(self.table_column_spinbox_widget)
        self.column_spinbox_label.setObjectName(u"column_spinbox_label")
        self.column_spinbox_label.setMaximumSize(QSize(16777215, 30))
        self.column_spinbox_label.setFont(font1)

        self.verticalLayout.addWidget(self.column_spinbox_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.column_spinbox = QSpinBox(self.table_column_spinbox_widget)
        self.column_spinbox.setObjectName(u"column_spinbox")
        self.column_spinbox.setMinimumSize(QSize(60, 30))
        self.column_spinbox.setMaximumSize(QSize(16777215, 16777215))
        self.column_spinbox.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.column_spinbox, 0, Qt.AlignmentFlag.AlignHCenter)


        self.table_buttons_horizontal_layout.addWidget(self.table_column_spinbox_widget)

        self.table_grid_options = QGridLayout()
        self.table_grid_options.setObjectName(u"table_grid_options")
        self.table_grid_options.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.table_grid_options.setHorizontalSpacing(5)
        self.table_grid_options.setContentsMargins(0, 6, 0, 6)
        self.table_clean_matrix_button = QPushButton(self.table_buttons_frame)
        self.table_clean_matrix_button.setObjectName(u"table_clean_matrix_button")
        font2 = QFont()
        font2.setPointSize(11)
        self.table_clean_matrix_button.setFont(font2)
        self.table_clean_matrix_button.setStyleSheet(u"")

        self.table_grid_options.addWidget(self.table_clean_matrix_button, 0, 0, 1, 1)

        self.table_fill_0_button = QPushButton(self.table_buttons_frame)
        self.table_fill_0_button.setObjectName(u"table_fill_0_button")
        self.table_fill_0_button.setFont(font2)
        self.table_fill_0_button.setStyleSheet(u"")

        self.table_grid_options.addWidget(self.table_fill_0_button, 1, 1, 1, 1)

        self.table_update_button = QPushButton(self.table_buttons_frame)
        self.table_update_button.setObjectName(u"table_update_button")
        self.table_update_button.setFont(font2)
        self.table_update_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.table_update_button.setStyleSheet(u"")
        self.table_grid_options.addWidget(self.table_update_button, 0, 1, 1, 1)

        self.table_transposition_button = QPushButton(self.table_buttons_frame)
        self.table_transposition_button.setObjectName(u"table_transposition_button")
        self.table_transposition_button.setFont(font2)

        self.table_grid_options.addWidget(self.table_transposition_button, 1, 0, 1, 1)

        self.table_random_matrix_button = QPushButton(self.table_buttons_frame)
        self.table_random_matrix_button.setObjectName(u"table_random_matrix_button")
        self.table_random_matrix_button.setFont(font2)
        self.table_random_matrix_button.setStyleSheet(u"")

        self.table_grid_options.addWidget(self.table_random_matrix_button, 2, 0, 1, 1)

        self.table_adjust_size_button = QPushButton(self.table_buttons_frame)
        self.table_adjust_size_button.setObjectName(u"table_adjust_size_button")
        self.table_adjust_size_button.setFont(font2)

        self.table_grid_options.addWidget(self.table_adjust_size_button, 2, 1, 1, 1)

        self.table_import_from_csv_button = QPushButton(self.table_buttons_frame)
        self.table_import_from_csv_button.setObjectName(u"table_import_from_csv_button")
        self.table_import_from_csv_button.setFont(font2)

        self.table_grid_options.addWidget(self.table_import_from_csv_button, 0, 2, 1, 1)

        self.table_solution_matrix_combobox = QComboBox(self.table_buttons_frame)
        self.table_solution_matrix_combobox.addItem("")
        self.table_solution_matrix_combobox.addItem("")
        self.table_solution_matrix_combobox.addItem("")
        self.table_solution_matrix_combobox.addItem("")
        self.table_solution_matrix_combobox.addItem("")
        self.table_solution_matrix_combobox.addItem("")
        self.table_solution_matrix_combobox.setObjectName(u"table_solution_matrix_combobox")
        self.table_solution_matrix_combobox.setFont(font2)
        self.table_solution_matrix_combobox.setCursor(QCursor(Qt.ArrowCursor))
        self.table_solution_matrix_combobox.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.table_solution_matrix_combobox.setAcceptDrops(False)
        self.table_solution_matrix_combobox.setStyleSheet(u"")

        self.table_grid_options.addWidget(self.table_solution_matrix_combobox, 1, 2, 1, 1)

        self.table_solve_matrix_button = QPushButton(self.table_buttons_frame)
        self.table_solve_matrix_button.setObjectName(u"table_solve_matrix_button")
        self.table_solve_matrix_button.setFont(font2)
        self.table_solve_matrix_button.setStyleSheet(u"")

        self.table_grid_options.addWidget(self.table_solve_matrix_button, 2, 2, 1, 1)


        self.table_buttons_horizontal_layout.addLayout(self.table_grid_options)

        self.table_buttons_horizontal_layout.setStretch(0, 15)
        self.table_buttons_horizontal_layout.setStretch(1, 15)
        self.table_buttons_horizontal_layout.setStretch(2, 100)

        self.verticalLayout_2.addWidget(self.table_buttons_frame)

        self.input_table = QTableWidget(self.main_table_widget)
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
        font3 = QFont()
        font3.setFamilies([u"Calibri"])
        font3.setPointSize(9)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font3);
        __qtablewidgetitem3.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsEnabled);
        self.input_table.setItem(0, 0, __qtablewidgetitem3)
        self.input_table.setObjectName(u"input_table")
        self.input_table.setStyleSheet(u"")
        self.input_table.verticalHeader().setVisible(True)

        self.verticalLayout_2.addWidget(self.input_table)

        self.verticalLayout_2.setStretch(0, 10)
        self.verticalLayout_2.setStretch(1, 100)

        self.verticalLayout_4.addWidget(self.main_table_widget)

        self.main_stacked_widget.addWidget(self.matrix_page)
        self.equations_page = QWidget()
        self.equations_page.setObjectName(u"equations_page")
        self.verticalLayout_8 = QVBoxLayout(self.equations_page)
        self.verticalLayout_8.setSpacing(15)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(4, 0, 5, 5)
        self.equation_widget = QWidget(self.equations_page)
        self.equation_widget.setObjectName(u"equation_widget")
        self.verticalLayout_9 = QVBoxLayout(self.equation_widget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.equation_input = QLineEdit(self.equation_widget)
        self.equation_input.setObjectName(u"equation_input")
        self.equation_input.setFont(font2)
        self.equation_input.setInputMethodHints(Qt.InputMethodHint.ImhNone)

        self.verticalLayout_9.addWidget(self.equation_input)


        self.verticalLayout_8.addWidget(self.equation_widget, 0, Qt.AlignmentFlag.AlignTop)

        self.equation_buttons_frame = QFrame(self.equations_page)
        self.equation_buttons_frame.setObjectName(u"equation_buttons_frame")
        sizePolicy.setHeightForWidth(self.equation_buttons_frame.sizePolicy().hasHeightForWidth())
        self.equation_buttons_frame.setSizePolicy(sizePolicy)
        self.verticalLayout_10 = QVBoxLayout(self.equation_buttons_frame)
        self.verticalLayout_10.setSpacing(15)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.interval_a_widget = QWidget(self.equation_buttons_frame)
        self.interval_a_widget.setObjectName(u"interval_a_widget")
        sizePolicy.setHeightForWidth(self.interval_a_widget.sizePolicy().hasHeightForWidth())
        self.interval_a_widget.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.interval_a_widget)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.interval_a_label = QLabel(self.interval_a_widget)
        self.interval_a_label.setObjectName(u"interval_a_label")
        self.interval_a_label.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_2.addWidget(self.interval_a_label)

        self.interval_a_line_edit = QLineEdit(self.interval_a_widget)
        self.interval_a_line_edit.setObjectName(u"interval_a_line_edit")

        self.horizontalLayout_2.addWidget(self.interval_a_line_edit)


        self.verticalLayout_10.addWidget(self.interval_a_widget)

        self.interval_b_widget = QWidget(self.equation_buttons_frame)
        self.interval_b_widget.setObjectName(u"interval_b_widget")
        sizePolicy.setHeightForWidth(self.interval_b_widget.sizePolicy().hasHeightForWidth())
        self.interval_b_widget.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QHBoxLayout(self.interval_b_widget)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.interval_b_label = QLabel(self.interval_b_widget)
        self.interval_b_label.setObjectName(u"interval_b_label")
        self.interval_b_label.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_3.addWidget(self.interval_b_label)

        self.interval_b_line_edit = QLineEdit(self.interval_b_widget)
        self.interval_b_line_edit.setObjectName(u"interval_b_line_edit")

        self.horizontalLayout_3.addWidget(self.interval_b_line_edit)


        self.verticalLayout_10.addWidget(self.interval_b_widget)

        self.tolerance_widget = QWidget(self.equation_buttons_frame)
        self.tolerance_widget.setObjectName(u"tolerance_widget")
        sizePolicy.setHeightForWidth(self.tolerance_widget.sizePolicy().hasHeightForWidth())
        self.tolerance_widget.setSizePolicy(sizePolicy)
        self.horizontalLayout_4 = QHBoxLayout(self.tolerance_widget)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tolerance_label = QLabel(self.tolerance_widget)
        self.tolerance_label.setObjectName(u"tolerance_label")
        self.tolerance_label.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_4.addWidget(self.tolerance_label)

        self.tolerance_line_edit = QLineEdit(self.tolerance_widget)
        self.tolerance_line_edit.setObjectName(u"tolerance_line_edit")

        self.horizontalLayout_4.addWidget(self.tolerance_line_edit)


        self.verticalLayout_10.addWidget(self.tolerance_widget)


        self.verticalLayout_8.addWidget(self.equation_buttons_frame, 0, Qt.AlignmentFlag.AlignTop)

        self.solution_widget = QWidget(self.equations_page)
        self.solution_widget.setObjectName(u"solution_widget")
        self.horizontalLayout_5 = QHBoxLayout(self.solution_widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.solution_solve_button = QPushButton(self.solution_widget)
        self.solution_solve_button.setObjectName(u"solution_solve_button")
        self.solution_solve_button.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_5.addWidget(self.solution_solve_button)

        self.solution_combobox_options = QComboBox(self.solution_widget)
        self.solution_combobox_options.addItem("")
        self.solution_combobox_options.addItem("")
        self.solution_combobox_options.setObjectName(u"solution_combobox_options")
        self.solution_combobox_options.setMinimumSize(QSize(160, 0))

        self.horizontalLayout_5.addWidget(self.solution_combobox_options)


        self.verticalLayout_8.addWidget(self.solution_widget, 0, Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout_8.setStretch(0, 10)
        self.verticalLayout_8.setStretch(1, 9)
        self.verticalLayout_8.setStretch(2, 9)
        self.main_stacked_widget.addWidget(self.equations_page)

        self.horizontalLayout.addWidget(self.main_stacked_widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.main_stacked_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculadora de matrices", None))
#if QT_CONFIG(tooltip)
        self.expand_button.setToolTip(QCoreApplication.translate("MainWindow", u"Expandir Menu", None))
#endif // QT_CONFIG(tooltip)
        self.expand_button.setText("")
#if QT_CONFIG(tooltip)
        self.matrix_tab_button.setToolTip(QCoreApplication.translate("MainWindow", u"Matrices", None))
#endif // QT_CONFIG(tooltip)
        self.matrix_tab_button.setText("")
#if QT_CONFIG(tooltip)
        self.equation_tab_button.setToolTip(QCoreApplication.translate("MainWindow", u"Ecuaciones", None))
#endif // QT_CONFIG(tooltip)
        self.equation_tab_button.setText("")
#if QT_CONFIG(tooltip)
        self.row_spinbox_label.setToolTip(QCoreApplication.translate("MainWindow", u"Filas de la matriz", None))
#endif // QT_CONFIG(tooltip)
        self.row_spinbox_label.setText(QCoreApplication.translate("MainWindow", u"Filas", None))
#if QT_CONFIG(tooltip)
        self.column_spinbox_label.setToolTip(QCoreApplication.translate("MainWindow", u"Columnas de la matriz", None))
#endif // QT_CONFIG(tooltip)
        self.column_spinbox_label.setText(QCoreApplication.translate("MainWindow", u"Columnas", None))
#if QT_CONFIG(tooltip)
        self.table_clean_matrix_button.setToolTip(QCoreApplication.translate("MainWindow", u"Limpiar todos los valores de la matriz", None))
#endif // QT_CONFIG(tooltip)
        self.table_clean_matrix_button.setText(QCoreApplication.translate("MainWindow", u"Limpiar Matriz", None))
#if QT_CONFIG(tooltip)
        self.table_fill_0_button.setToolTip(QCoreApplication.translate("MainWindow", u"Rellenar espacios de la matriz con 0", None))
#endif // QT_CONFIG(tooltip)
        self.table_fill_0_button.setText(QCoreApplication.translate("MainWindow", u"Rellenar con 0", None))
#if QT_CONFIG(tooltip)
        self.table_update_button.setToolTip(QCoreApplication.translate("MainWindow", u"Actualizar dimensiones de la matriz", None))
#endif // QT_CONFIG(tooltip)
        self.table_update_button.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
#if QT_CONFIG(tooltip)
        self.table_transposition_button.setToolTip(QCoreApplication.translate("MainWindow", u"Transponer matriz", None))
#endif // QT_CONFIG(tooltip)
        self.table_transposition_button.setText(QCoreApplication.translate("MainWindow", u"Transponer Matriz", None))
#if QT_CONFIG(tooltip)
        self.table_random_matrix_button.setToolTip(QCoreApplication.translate("MainWindow", u"Llenar espacios vac\u00edos de la matriz con n\u00fameros aleatorios", None))
#endif // QT_CONFIG(tooltip)
        self.table_random_matrix_button.setText(QCoreApplication.translate("MainWindow", u"Matriz aleatoria", None))
#if QT_CONFIG(tooltip)
        self.table_adjust_size_button.setToolTip(QCoreApplication.translate("MainWindow", u"Ajustar tama\u00f1o de la matriz en base al contenido actual", None))
#endif // QT_CONFIG(tooltip)
        self.table_adjust_size_button.setText(QCoreApplication.translate("MainWindow", u"Ajustar tama\u00f1o", None))
#if QT_CONFIG(tooltip)
        self.table_import_from_csv_button.setToolTip(QCoreApplication.translate("MainWindow", u"Importar matriz desde un archivo CSV", None))
#endif // QT_CONFIG(tooltip)
        self.table_import_from_csv_button.setText(QCoreApplication.translate("MainWindow", u"Importar CSV", None))
        self.table_solution_matrix_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"Resolver por", None))
        self.table_solution_matrix_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"Reducci\u00f3n", None))
        self.table_solution_matrix_combobox.setItemText(2, QCoreApplication.translate("MainWindow", u"Vectores", None))
        self.table_solution_matrix_combobox.setItemText(3, QCoreApplication.translate("MainWindow", u"Determinante", None))
        self.table_solution_matrix_combobox.setItemText(4, QCoreApplication.translate("MainWindow", u"Cramer", None))
        self.table_solution_matrix_combobox.setItemText(5, QCoreApplication.translate("MainWindow", u"Invertir ", None))

#if QT_CONFIG(tooltip)
        self.table_solution_matrix_combobox.setToolTip(QCoreApplication.translate("MainWindow", u"Opciones para resolver matriz", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.table_solve_matrix_button.setToolTip(QCoreApplication.translate("MainWindow", u"Resolver seg\u00fan el m\u00e9todo seleccionado", None))
#endif // QT_CONFIG(tooltip)
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

        self.equation_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Insertar ecuaci\u00f3n", None))
        self.interval_a_label.setText(QCoreApplication.translate("MainWindow", u"Intervalo a", None))
        self.interval_b_label.setText(QCoreApplication.translate("MainWindow", u"Intervalo b", None))
        self.tolerance_label.setText(QCoreApplication.translate("MainWindow", u"Tolerancia", None))
        self.solution_solve_button.setText(QCoreApplication.translate("MainWindow", u"Resolver", None))
        self.solution_combobox_options.setItemText(0, QCoreApplication.translate("MainWindow", u"Obtener ra\u00edces por", None))
        self.solution_combobox_options.setItemText(1, QCoreApplication.translate("MainWindow", u"Bisecci\u00f3n", None))

    # retranslateUi

