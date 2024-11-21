# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowpOvWNs.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

from PySide6.QtSvg import QtSvg
from views.qt_files.qrc_files import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.WindowModal)
        MainWindow.resize(652, 407)
        icon = QIcon()
        icon.addFile(u":/icon/Images/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
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
"#table_buttons_frame QPushButton, #table_buttons_frame QComboBox,#solution_widget QComboBox, #equations_page QPushButton{\n"
"    color: #ffffff;\n"
"    text-align: center;\n"
"	padding: 3px;\n"
"    border-radius: 10px;\n"
"    background-color: #16191d;\n"
"}\n"
"\n"
"#table_buttons_frame QPushButton::hover, #table_buttons_frame QComboBox::hover,#equations_page QPushButton::hover{\n"
"    background-color: #2a2e35;\n"
"    border-color: #454a52;\n"
"}\n"
"\n"
"#table_buttons_frame QPushButton::pressed, #table_buttons_frame QComboBox::pressed,#equations_page QPushButton::pressed{\n"
"    background-color: #1d2127;\n"
"	font-weight: 350;\n"
"}\n"
"\n"
"#table_buttons_frame QSpin"
                        "Box{\n"
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
" #table_buttons_frame QComboBox:dropdown{\n"
"border: 0px;\n"
"}\n"
"\n"
"#table_buttons_frame QComboBox:down-arrow{\n"
"subcontrol-position: right;\n"
"width: 18px;\n"
"height: 18px;\n"
"}\n"
"\n"
"#table_but"
                        "tons_frame QComboBox QListView, #solution_widget QComboBox QListView{\n"
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
"#equations_page QLabel{\n"
"background-color: #1f232a;\n"
"padding: -3px;\n"
"font-weight: 700;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
""
                        "#equations_page{\n"
"background: #2c313c;\n"
"}\n"
"\n"
"#method_equation_tab_widget QWidget{\n"
"background-color: #3e4555\n"
"}\n"
"\n"
"#equations_page QTabWidget:pane{\n"
"background-color: #2c313c\n"
"}\n"
"\n"
"QTabBar::tab{\n"
"background-color: #16191d;\n"
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
"#bisection_tab QLineEdit, #newton_tab QLineEdit, #false_position_tab QLineEdit, #secant_tab QLineEdit{\n"
"color: #fff;\n"
"background-color: #596379;\n"
"border-radius:10px;\n"
"font-weight: 350;\n"
"}\n"
"\n"
"#bisection_tab QLabel, #newton_tab QLabel, #false_position_tab QLabel, #secant_tab QLabel{\n"
"background-color: #1f232a;\n"
"padding: 1px;\n"
"font-weight: 700;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
" #bisection_tab QPushButton, #newton_tab QPushButton, #false_position_tab QPushButton, #secant_tab QPushButton{\n"
"color: #ffffff;\n"
"    text-align: center;\n"
"	padding: 3px;\n"
" "
                        "   border-radius: 10px;\n"
"    background-color: #16191d;\n"
"}\n"
"\n"
"#bisection_tab QPushButton::hover, #newton_tab QPushButton::hover, #false_position_tab QPushButton::hover, #secant_tab QPushButton::hover{\n"
"    background-color: #2a2e35;\n"
"    border-color: #454a52;\n"
"}\n"
"\n"
"#bisection_tab QPushButton::pressed, #newton_tab QPushButton::pressed, #false_position_tab QPushButton::pressed, #secant_tab QPushButton::pressed{\n"
"background-color: #1d2127;\n"
"font-weight: 350;\n"
"}\n"
"\n"
"QCheckBox::unchecked{\n"
"color: #8b7a78\n"
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
        self.verticalLayout_5.setContentsMargins(5, 0, 0, 0)
        self.sub_side_bar = QWidget(self.side_bar)
        self.sub_side_bar.setObjectName(u"sub_side_bar")
        self.sub_side_bar.setMinimumSize(QSize(0, 0))
        self.sub_side_bar.setMaximumSize(QSize(32, 16777215))
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
        self.tab_buttons_frame.setStyleSheet(u"text-align: left;")
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
        self.main_stacked_widget.setFrameShape(QFrame.Shape.NoFrame)
        self.main_stacked_widget.setFrameShadow(QFrame.Shadow.Plain)
        self.main_stacked_widget.setLineWidth(1)
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
        self.table_buttons_horizontal_layout.setSpacing(0)
        self.table_buttons_horizontal_layout.setObjectName(u"table_buttons_horizontal_layout")
        self.table_buttons_horizontal_layout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.table_buttons_horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.table_column_row_widget = QWidget(self.table_buttons_frame)
        self.table_column_row_widget.setObjectName(u"table_column_row_widget")
        self.verticalLayout_19 = QVBoxLayout(self.table_column_row_widget)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(3, 0, 3, 3)
        self.sub_table_column_row_widget = QWidget(self.table_column_row_widget)
        self.sub_table_column_row_widget.setObjectName(u"sub_table_column_row_widget")
        self.horizontalLayout_3 = QHBoxLayout(self.sub_table_column_row_widget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.table_row_spinbox_widget = QWidget(self.sub_table_column_row_widget)
        self.table_row_spinbox_widget.setObjectName(u"table_row_spinbox_widget")
        self.table_row_spinbox_widget.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.table_row_spinbox_widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
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


        self.horizontalLayout_3.addWidget(self.table_row_spinbox_widget)

        self.table_column_spinbox_widget = QWidget(self.sub_table_column_row_widget)
        self.table_column_spinbox_widget.setObjectName(u"table_column_spinbox_widget")
        self.verticalLayout = QVBoxLayout(self.table_column_spinbox_widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
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


        self.horizontalLayout_3.addWidget(self.table_column_spinbox_widget)


        self.verticalLayout_19.addWidget(self.sub_table_column_row_widget)

        self.table_resize_checkbox = QCheckBox(self.table_column_row_widget)
        self.table_resize_checkbox.setObjectName(u"table_resize_checkbox")
        font2 = QFont()
        font2.setPointSize(11)
        self.table_resize_checkbox.setFont(font2)
        self.table_resize_checkbox.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.table_resize_checkbox.setChecked(False)
        self.table_resize_checkbox.setTristate(False)

        self.verticalLayout_19.addWidget(self.table_resize_checkbox)


        self.table_buttons_horizontal_layout.addWidget(self.table_column_row_widget)

        self.table_grid_options = QGridLayout()
        self.table_grid_options.setObjectName(u"table_grid_options")
        self.table_grid_options.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.table_grid_options.setHorizontalSpacing(5)
        self.table_grid_options.setVerticalSpacing(3)
        self.table_grid_options.setContentsMargins(0, 6, 0, 6)
        self.table_update_button = QPushButton(self.table_buttons_frame)
        self.table_update_button.setObjectName(u"table_update_button")
        self.table_update_button.setFont(font2)
        self.table_update_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.table_update_button.setStyleSheet(u"")

        self.table_grid_options.addWidget(self.table_update_button, 0, 1, 1, 1)

        self.table_vector_button = QPushButton(self.table_buttons_frame)
        self.table_vector_button.setObjectName(u"table_vector_button")
        self.table_vector_button.setFont(font2)

        self.table_grid_options.addWidget(self.table_vector_button, 2, 2, 1, 1)

        self.table_adjust_size_button = QPushButton(self.table_buttons_frame)
        self.table_adjust_size_button.setObjectName(u"table_adjust_size_button")
        self.table_adjust_size_button.setFont(font2)

        self.table_grid_options.addWidget(self.table_adjust_size_button, 2, 1, 1, 1)

        self.table_clean_matrix_button = QPushButton(self.table_buttons_frame)
        self.table_clean_matrix_button.setObjectName(u"table_clean_matrix_button")
        self.table_clean_matrix_button.setFont(font2)
        self.table_clean_matrix_button.setStyleSheet(u"")

        self.table_grid_options.addWidget(self.table_clean_matrix_button, 0, 0, 1, 1)

        self.table_solve_matrix_button = QPushButton(self.table_buttons_frame)
        self.table_solve_matrix_button.setObjectName(u"table_solve_matrix_button")
        self.table_solve_matrix_button.setFont(font2)
        self.table_solve_matrix_button.setStyleSheet(u"")

        self.table_grid_options.addWidget(self.table_solve_matrix_button, 3, 2, 1, 1)

        self.table_solution_matrix_combobox = QComboBox(self.table_buttons_frame)
        self.table_solution_matrix_combobox.addItem("")
        self.table_solution_matrix_combobox.addItem("")
        self.table_solution_matrix_combobox.addItem("")
        self.table_solution_matrix_combobox.setObjectName(u"table_solution_matrix_combobox")
        self.table_solution_matrix_combobox.setFont(font2)
        self.table_solution_matrix_combobox.setCursor(QCursor(Qt.ArrowCursor))
        self.table_solution_matrix_combobox.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.table_solution_matrix_combobox.setAcceptDrops(False)
        self.table_solution_matrix_combobox.setStyleSheet(u"")

        self.table_grid_options.addWidget(self.table_solution_matrix_combobox, 3, 1, 1, 1)

        self.table_random_matrix_button = QPushButton(self.table_buttons_frame)
        self.table_random_matrix_button.setObjectName(u"table_random_matrix_button")
        self.table_random_matrix_button.setFont(font2)
        self.table_random_matrix_button.setStyleSheet(u"")

        self.table_grid_options.addWidget(self.table_random_matrix_button, 2, 0, 1, 1)

        self.table_fill_0_button = QPushButton(self.table_buttons_frame)
        self.table_fill_0_button.setObjectName(u"table_fill_0_button")
        self.table_fill_0_button.setFont(font2)
        self.table_fill_0_button.setStyleSheet(u"")

        self.table_grid_options.addWidget(self.table_fill_0_button, 1, 1, 1, 1)

        self.table_transposition_button = QPushButton(self.table_buttons_frame)
        self.table_transposition_button.setObjectName(u"table_transposition_button")
        self.table_transposition_button.setFont(font2)

        self.table_grid_options.addWidget(self.table_transposition_button, 1, 0, 1, 1)

        self.table_invert_button = QPushButton(self.table_buttons_frame)
        self.table_invert_button.setObjectName(u"table_invert_button")
        self.table_invert_button.setFont(font2)

        self.table_grid_options.addWidget(self.table_invert_button, 1, 2, 1, 1)

        self.table_determinant_button = QPushButton(self.table_buttons_frame)
        self.table_determinant_button.setObjectName(u"table_determinant_button")
        self.table_determinant_button.setFont(font2)

        self.table_grid_options.addWidget(self.table_determinant_button, 0, 2, 1, 1)

        self.table_import_from_csv_button = QPushButton(self.table_buttons_frame)
        self.table_import_from_csv_button.setObjectName(u"table_import_from_csv_button")
        self.table_import_from_csv_button.setFont(font2)

        self.table_grid_options.addWidget(self.table_import_from_csv_button, 3, 0, 1, 1)


        self.table_buttons_horizontal_layout.addLayout(self.table_grid_options)

        self.table_buttons_horizontal_layout.setStretch(1, 200)

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

        self.verticalLayout_2.setStretch(1, 100)

        self.verticalLayout_4.addWidget(self.main_table_widget)

        self.main_stacked_widget.addWidget(self.matrix_page)
        self.equations_page = QWidget()
        self.equations_page.setObjectName(u"equations_page")
        self.verticalLayout_8 = QVBoxLayout(self.equations_page)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.equation_widget = QWidget(self.equations_page)
        self.equation_widget.setObjectName(u"equation_widget")
        self.horizontalLayout_2 = QHBoxLayout(self.equation_widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 0, 0, 0)
        self.side_equation_text_label = QLabel(self.equation_widget)
        self.side_equation_text_label.setObjectName(u"side_equation_text_label")
        self.side_equation_text_label.setMaximumSize(QSize(140, 40))
        self.side_equation_text_label.setFont(font1)

        self.horizontalLayout_2.addWidget(self.side_equation_text_label)

        self.equation_text_label = QLabel(self.equation_widget)
        self.equation_text_label.setObjectName(u"equation_text_label")
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        self.equation_text_label.setFont(font4)
        self.equation_text_label.setStyleSheet(u"background: none")

        self.horizontalLayout_2.addWidget(self.equation_text_label, 0, Qt.AlignmentFlag.AlignLeft)

        self.edit_equation_button = QPushButton(self.equation_widget)
        self.edit_equation_button.setObjectName(u"edit_equation_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.edit_equation_button.sizePolicy().hasHeightForWidth())
        self.edit_equation_button.setSizePolicy(sizePolicy1)
        icon4 = QIcon()
        icon4.addFile(u":/icon/Images/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.edit_equation_button.setIcon(icon4)
        self.edit_equation_button.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.edit_equation_button, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_8.addWidget(self.equation_widget)

        self.method_equation_widget = QWidget(self.equations_page)
        self.method_equation_widget.setObjectName(u"method_equation_widget")
        self.verticalLayout_9 = QVBoxLayout(self.method_equation_widget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.method_equation_tab_widget = QTabWidget(self.method_equation_widget)
        self.method_equation_tab_widget.setObjectName(u"method_equation_tab_widget")
        self.bisection_tab = QWidget()
        self.bisection_tab.setObjectName(u"bisection_tab")
        self.verticalLayout_10 = QVBoxLayout(self.bisection_tab)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 0, 5, 9)
        self.bisection_config_widget = QWidget(self.bisection_tab)
        self.bisection_config_widget.setObjectName(u"bisection_config_widget")
        self.bisection_config_widget.setMaximumSize(QSize(16777215, 16777215))
        font5 = QFont()
        font5.setPointSize(9)
        font5.setKerning(True)
        self.bisection_config_widget.setFont(font5)
        self.verticalLayout_12 = QVBoxLayout(self.bisection_config_widget)
        self.verticalLayout_12.setSpacing(12)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 5, 0, 9)
        self.bisection_config_grid = QGridLayout()
        self.bisection_config_grid.setObjectName(u"bisection_config_grid")
        self.bisection_interval_b_label = QLabel(self.bisection_config_widget)
        self.bisection_interval_b_label.setObjectName(u"bisection_interval_b_label")
        self.bisection_interval_b_label.setFont(font1)
        self.bisection_interval_b_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.bisection_config_grid.addWidget(self.bisection_interval_b_label, 1, 0, 1, 1)

        self.bisection_interval_a_label = QLabel(self.bisection_config_widget)
        self.bisection_interval_a_label.setObjectName(u"bisection_interval_a_label")
        self.bisection_interval_a_label.setFont(font1)
        self.bisection_interval_a_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.bisection_config_grid.addWidget(self.bisection_interval_a_label, 0, 0, 1, 1)

        self.bisection_tolerance_label = QLabel(self.bisection_config_widget)
        self.bisection_tolerance_label.setObjectName(u"bisection_tolerance_label")
        self.bisection_tolerance_label.setFont(font1)
        self.bisection_tolerance_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.bisection_config_grid.addWidget(self.bisection_tolerance_label, 2, 0, 1, 1)

        self.bisection_interval_b_line_edit = QLineEdit(self.bisection_config_widget)
        self.bisection_interval_b_line_edit.setObjectName(u"bisection_interval_b_line_edit")
        font6 = QFont()
        font6.setPointSize(14)
        self.bisection_interval_b_line_edit.setFont(font6)
        self.bisection_interval_b_line_edit.setClearButtonEnabled(True)

        self.bisection_config_grid.addWidget(self.bisection_interval_b_line_edit, 1, 1, 1, 1)

        self.bisection_tolerance_line_edit = QLineEdit(self.bisection_config_widget)
        self.bisection_tolerance_line_edit.setObjectName(u"bisection_tolerance_line_edit")
        self.bisection_tolerance_line_edit.setFont(font6)
        self.bisection_tolerance_line_edit.setClearButtonEnabled(True)

        self.bisection_config_grid.addWidget(self.bisection_tolerance_line_edit, 2, 1, 1, 1)

        self.bisection_interval_a_line_edit = QLineEdit(self.bisection_config_widget)
        self.bisection_interval_a_line_edit.setObjectName(u"bisection_interval_a_line_edit")
        self.bisection_interval_a_line_edit.setFont(font6)
        self.bisection_interval_a_line_edit.setClearButtonEnabled(True)

        self.bisection_config_grid.addWidget(self.bisection_interval_a_line_edit, 0, 1, 1, 1)

        self.bisection_config_grid.setRowStretch(0, 1)
        self.bisection_config_grid.setRowStretch(1, 100)

        self.verticalLayout_12.addLayout(self.bisection_config_grid)


        self.verticalLayout_10.addWidget(self.bisection_config_widget, 0, Qt.AlignmentFlag.AlignTop)

        self.bisection_solution_button = QPushButton(self.bisection_tab)
        self.bisection_solution_button.setObjectName(u"bisection_solution_button")
        self.bisection_solution_button.setFont(font6)

        self.verticalLayout_10.addWidget(self.bisection_solution_button)

        self.bisection_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.bisection_spacer)

        self.method_equation_tab_widget.addTab(self.bisection_tab, "")
        self.newton_tab = QWidget()
        self.newton_tab.setObjectName(u"newton_tab")
        self.verticalLayout_13 = QVBoxLayout(self.newton_tab)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(5, 0, 5, -1)
        self.newton_config_widget = QWidget(self.newton_tab)
        self.newton_config_widget.setObjectName(u"newton_config_widget")
        font7 = QFont()
        font7.setPointSize(9)
        self.newton_config_widget.setFont(font7)
        self.verticalLayout_14 = QVBoxLayout(self.newton_config_widget)
        self.verticalLayout_14.setSpacing(12)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 5, 0, 9)
        self.newton_config_grid = QGridLayout()
        self.newton_config_grid.setObjectName(u"newton_config_grid")
        self.newton_max_iter_label = QLabel(self.newton_config_widget)
        self.newton_max_iter_label.setObjectName(u"newton_max_iter_label")
        self.newton_max_iter_label.setFont(font1)

        self.newton_config_grid.addWidget(self.newton_max_iter_label, 1, 0, 1, 1)

        self.newton_max_iter_line_edit = QLineEdit(self.newton_config_widget)
        self.newton_max_iter_line_edit.setObjectName(u"newton_max_iter_line_edit")
        self.newton_max_iter_line_edit.setFont(font6)
        self.newton_max_iter_line_edit.setClearButtonEnabled(True)

        self.newton_config_grid.addWidget(self.newton_max_iter_line_edit, 1, 1, 1, 1)

        self.newton_tolerance_label = QLabel(self.newton_config_widget)
        self.newton_tolerance_label.setObjectName(u"newton_tolerance_label")
        self.newton_tolerance_label.setFont(font1)
        self.newton_tolerance_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.newton_config_grid.addWidget(self.newton_tolerance_label, 2, 0, 1, 1)

        self.newton_tolerance_line_edit = QLineEdit(self.newton_config_widget)
        self.newton_tolerance_line_edit.setObjectName(u"newton_tolerance_line_edit")
        self.newton_tolerance_line_edit.setFont(font6)
        self.newton_tolerance_line_edit.setClearButtonEnabled(True)

        self.newton_config_grid.addWidget(self.newton_tolerance_line_edit, 2, 1, 1, 1)

        self.newton_x_value_label = QLabel(self.newton_config_widget)
        self.newton_x_value_label.setObjectName(u"newton_x_value_label")
        self.newton_x_value_label.setFont(font1)
        self.newton_x_value_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.newton_config_grid.addWidget(self.newton_x_value_label, 0, 0, 1, 1)

        self.newton_x_value_line_edit = QLineEdit(self.newton_config_widget)
        self.newton_x_value_line_edit.setObjectName(u"newton_x_value_line_edit")
        self.newton_x_value_line_edit.setFont(font6)
        self.newton_x_value_line_edit.setClearButtonEnabled(True)

        self.newton_config_grid.addWidget(self.newton_x_value_line_edit, 0, 1, 1, 1)

        self.newton_config_grid.setColumnStretch(0, 1)
        self.newton_config_grid.setColumnStretch(1, 100)

        self.verticalLayout_14.addLayout(self.newton_config_grid)


        self.verticalLayout_13.addWidget(self.newton_config_widget)

        self.newton_solution_button = QPushButton(self.newton_tab)
        self.newton_solution_button.setObjectName(u"newton_solution_button")
        self.newton_solution_button.setFont(font6)

        self.verticalLayout_13.addWidget(self.newton_solution_button)

        self.newton_spacer = QSpacerItem(20, 240, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.newton_spacer)

        self.method_equation_tab_widget.addTab(self.newton_tab, "")
        self.false_position_tab = QWidget()
        self.false_position_tab.setObjectName(u"false_position_tab")
        self.verticalLayout_16 = QVBoxLayout(self.false_position_tab)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(5, 0, 5, -1)
        self.false_position_config_widget = QWidget(self.false_position_tab)
        self.false_position_config_widget.setObjectName(u"false_position_config_widget")
        self.false_position_config_widget.setMaximumSize(QSize(16777215, 16777215))
        self.false_position_config_widget.setFont(font5)
        self.verticalLayout_15 = QVBoxLayout(self.false_position_config_widget)
        self.verticalLayout_15.setSpacing(12)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 5, 0, 9)
        self.false_position_config_grid = QGridLayout()
        self.false_position_config_grid.setObjectName(u"false_position_config_grid")
        self.false_interval_b_label = QLabel(self.false_position_config_widget)
        self.false_interval_b_label.setObjectName(u"false_interval_b_label")
        self.false_interval_b_label.setFont(font1)
        self.false_interval_b_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.false_position_config_grid.addWidget(self.false_interval_b_label, 1, 0, 1, 1)

        self.false_interval_a_label = QLabel(self.false_position_config_widget)
        self.false_interval_a_label.setObjectName(u"false_interval_a_label")
        self.false_interval_a_label.setFont(font1)
        self.false_interval_a_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.false_position_config_grid.addWidget(self.false_interval_a_label, 0, 0, 1, 1)

        self.false_tolerance_label = QLabel(self.false_position_config_widget)
        self.false_tolerance_label.setObjectName(u"false_tolerance_label")
        self.false_tolerance_label.setFont(font1)
        self.false_tolerance_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.false_position_config_grid.addWidget(self.false_tolerance_label, 2, 0, 1, 1)

        self.false_interval_b_line_edit = QLineEdit(self.false_position_config_widget)
        self.false_interval_b_line_edit.setObjectName(u"false_interval_b_line_edit")
        self.false_interval_b_line_edit.setFont(font6)
        self.false_interval_b_line_edit.setClearButtonEnabled(True)

        self.false_position_config_grid.addWidget(self.false_interval_b_line_edit, 1, 1, 1, 1)

        self.false_tolerance_line_edit = QLineEdit(self.false_position_config_widget)
        self.false_tolerance_line_edit.setObjectName(u"false_tolerance_line_edit")
        self.false_tolerance_line_edit.setFont(font6)
        self.false_tolerance_line_edit.setClearButtonEnabled(True)

        self.false_position_config_grid.addWidget(self.false_tolerance_line_edit, 2, 1, 1, 1)

        self.false_interval_a_line_edit = QLineEdit(self.false_position_config_widget)
        self.false_interval_a_line_edit.setObjectName(u"false_interval_a_line_edit")
        self.false_interval_a_line_edit.setFont(font6)
        self.false_interval_a_line_edit.setClearButtonEnabled(True)

        self.false_position_config_grid.addWidget(self.false_interval_a_line_edit, 0, 1, 1, 1)

        self.false_position_config_grid.setColumnStretch(0, 1)
        self.false_position_config_grid.setColumnStretch(1, 100)

        self.verticalLayout_15.addLayout(self.false_position_config_grid)


        self.verticalLayout_16.addWidget(self.false_position_config_widget)

        self.false_solution_button = QPushButton(self.false_position_tab)
        self.false_solution_button.setObjectName(u"false_solution_button")
        self.false_solution_button.setFont(font6)

        self.verticalLayout_16.addWidget(self.false_solution_button)

        self.false_position_spacer = QSpacerItem(20, 158, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.false_position_spacer)

        self.method_equation_tab_widget.addTab(self.false_position_tab, "")
        self.secant_tab = QWidget()
        self.secant_tab.setObjectName(u"secant_tab")
        self.verticalLayout_18 = QVBoxLayout(self.secant_tab)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(5, 0, 5, -1)
        self.secant_config_widget = QWidget(self.secant_tab)
        self.secant_config_widget.setObjectName(u"secant_config_widget")
        self.secant_config_widget.setFont(font7)
        self.verticalLayout_17 = QVBoxLayout(self.secant_config_widget)
        self.verticalLayout_17.setSpacing(12)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 5, 0, 9)
        self.secant_config_grid = QGridLayout()
        self.secant_config_grid.setObjectName(u"secant_config_grid")
        self.secant_tolerance_label = QLabel(self.secant_config_widget)
        self.secant_tolerance_label.setObjectName(u"secant_tolerance_label")
        self.secant_tolerance_label.setFont(font1)
        self.secant_tolerance_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.secant_config_grid.addWidget(self.secant_tolerance_label, 3, 0, 1, 1)

        self.secant_max_iter_line_edit = QLineEdit(self.secant_config_widget)
        self.secant_max_iter_line_edit.setObjectName(u"secant_max_iter_line_edit")
        self.secant_max_iter_line_edit.setFont(font6)

        self.secant_config_grid.addWidget(self.secant_max_iter_line_edit, 2, 1, 1, 2)

        self.secant_tolerance_line_edit = QLineEdit(self.secant_config_widget)
        self.secant_tolerance_line_edit.setObjectName(u"secant_tolerance_line_edit")
        self.secant_tolerance_line_edit.setFont(font6)

        self.secant_config_grid.addWidget(self.secant_tolerance_line_edit, 3, 1, 1, 1)

        self.secant_xi_line_edit = QLineEdit(self.secant_config_widget)
        self.secant_xi_line_edit.setObjectName(u"secant_xi_line_edit")
        self.secant_xi_line_edit.setFont(font6)
        self.secant_xi_line_edit.setClearButtonEnabled(True)

        self.secant_config_grid.addWidget(self.secant_xi_line_edit, 1, 1, 1, 2)

        self.secant_x0_line_edit = QLineEdit(self.secant_config_widget)
        self.secant_x0_line_edit.setObjectName(u"secant_x0_line_edit")
        self.secant_x0_line_edit.setFont(font6)
        self.secant_x0_line_edit.setClearButtonEnabled(True)

        self.secant_config_grid.addWidget(self.secant_x0_line_edit, 0, 1, 1, 2)

        self.secant_x0_label = QLabel(self.secant_config_widget)
        self.secant_x0_label.setObjectName(u"secant_x0_label")
        self.secant_x0_label.setFont(font1)
        self.secant_x0_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.secant_config_grid.addWidget(self.secant_x0_label, 0, 0, 1, 1)

        self.secant_max_iter_label = QLabel(self.secant_config_widget)
        self.secant_max_iter_label.setObjectName(u"secant_max_iter_label")
        self.secant_max_iter_label.setFont(font1)
        self.secant_max_iter_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.secant_config_grid.addWidget(self.secant_max_iter_label, 2, 0, 1, 1)

        self.secant_xi_label = QLabel(self.secant_config_widget)
        self.secant_xi_label.setObjectName(u"secant_xi_label")
        self.secant_xi_label.setFont(font1)
        self.secant_xi_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.secant_config_grid.addWidget(self.secant_xi_label, 1, 0, 1, 1)

        self.secant_config_grid.setColumnStretch(0, 1)
        self.secant_config_grid.setColumnStretch(1, 10)

        self.verticalLayout_17.addLayout(self.secant_config_grid)


        self.verticalLayout_18.addWidget(self.secant_config_widget)

        self.secant_solution_button = QPushButton(self.secant_tab)
        self.secant_solution_button.setObjectName(u"secant_solution_button")
        self.secant_solution_button.setFont(font6)

        self.verticalLayout_18.addWidget(self.secant_solution_button)

        self.secant_spacer = QSpacerItem(20, 255, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.secant_spacer)

        self.method_equation_tab_widget.addTab(self.secant_tab, "")

        self.verticalLayout_9.addWidget(self.method_equation_tab_widget)


        self.verticalLayout_8.addWidget(self.method_equation_widget)

        self.verticalLayout_8.setStretch(0, 10)
        self.verticalLayout_8.setStretch(1, 100)
        self.main_stacked_widget.addWidget(self.equations_page)

        self.horizontalLayout.addWidget(self.main_stacked_widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.main_stacked_widget.setCurrentIndex(0)
        self.method_equation_tab_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculadora de \u00e1lgebra", None))
#if QT_CONFIG(tooltip)
        self.expand_button.setToolTip(QCoreApplication.translate("MainWindow", u"Expandir Menu", None))
#endif // QT_CONFIG(tooltip)
        self.expand_button.setText("")
#if QT_CONFIG(tooltip)
        self.matrix_tab_button.setToolTip(QCoreApplication.translate("MainWindow", u"Matrices", None))
#endif // QT_CONFIG(tooltip)
        self.matrix_tab_button.setText(QCoreApplication.translate("MainWindow", u"Matrices", None))
#if QT_CONFIG(tooltip)
        self.equation_tab_button.setToolTip(QCoreApplication.translate("MainWindow", u"Ecuaciones", None))
#endif // QT_CONFIG(tooltip)
        self.equation_tab_button.setText(QCoreApplication.translate("MainWindow", u"Ra\u00edz de ecuaciones", None))
#if QT_CONFIG(tooltip)
        self.row_spinbox_label.setToolTip(QCoreApplication.translate("MainWindow", u"Filas de la matriz", None))
#endif // QT_CONFIG(tooltip)
        self.row_spinbox_label.setText(QCoreApplication.translate("MainWindow", u"Filas", None))
#if QT_CONFIG(tooltip)
        self.column_spinbox_label.setToolTip(QCoreApplication.translate("MainWindow", u"Columnas de la matriz", None))
#endif // QT_CONFIG(tooltip)
        self.column_spinbox_label.setText(QCoreApplication.translate("MainWindow", u"Columnas", None))
        self.table_resize_checkbox.setText(QCoreApplication.translate("MainWindow", u"Redimensionar autom\u00e1ticamente", None))
#if QT_CONFIG(tooltip)
        self.table_update_button.setToolTip(QCoreApplication.translate("MainWindow", u"Actualizar dimensiones de la matriz", None))
#endif // QT_CONFIG(tooltip)
        self.table_update_button.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.table_vector_button.setText(QCoreApplication.translate("MainWindow", u"Vectores", None))
#if QT_CONFIG(tooltip)
        self.table_adjust_size_button.setToolTip(QCoreApplication.translate("MainWindow", u"Ajustar tama\u00f1o de la matriz en base al contenido actual", None))
#endif // QT_CONFIG(tooltip)
        self.table_adjust_size_button.setText(QCoreApplication.translate("MainWindow", u"Ajustar tama\u00f1o", None))
#if QT_CONFIG(tooltip)
        self.table_clean_matrix_button.setToolTip(QCoreApplication.translate("MainWindow", u"Limpiar todos los valores de la matriz", None))
#endif // QT_CONFIG(tooltip)
        self.table_clean_matrix_button.setText(QCoreApplication.translate("MainWindow", u"Limpiar Matriz", None))
#if QT_CONFIG(tooltip)
        self.table_solve_matrix_button.setToolTip(QCoreApplication.translate("MainWindow", u"Resolver seg\u00fan el m\u00e9todo seleccionado", None))
#endif // QT_CONFIG(tooltip)
        self.table_solve_matrix_button.setText(QCoreApplication.translate("MainWindow", u"Resolver", None))
        self.table_solution_matrix_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"Resolver por", None))
        self.table_solution_matrix_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"Reducci\u00f3n", None))
        self.table_solution_matrix_combobox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cramer", None))

#if QT_CONFIG(tooltip)
        self.table_solution_matrix_combobox.setToolTip(QCoreApplication.translate("MainWindow", u"Opciones para resolver matriz", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.table_random_matrix_button.setToolTip(QCoreApplication.translate("MainWindow", u"Llenar espacios vac\u00edos de la matriz con n\u00fameros aleatorios", None))
#endif // QT_CONFIG(tooltip)
        self.table_random_matrix_button.setText(QCoreApplication.translate("MainWindow", u"Matriz aleatoria", None))
#if QT_CONFIG(tooltip)
        self.table_fill_0_button.setToolTip(QCoreApplication.translate("MainWindow", u"Rellenar espacios de la matriz con 0", None))
#endif // QT_CONFIG(tooltip)
        self.table_fill_0_button.setText(QCoreApplication.translate("MainWindow", u"Rellenar con 0", None))
#if QT_CONFIG(tooltip)
        self.table_transposition_button.setToolTip(QCoreApplication.translate("MainWindow", u"Transponer matriz", None))
#endif // QT_CONFIG(tooltip)
        self.table_transposition_button.setText(QCoreApplication.translate("MainWindow", u"Transponer Matriz", None))
        self.table_invert_button.setText(QCoreApplication.translate("MainWindow", u"Invertir", None))
        self.table_determinant_button.setText(QCoreApplication.translate("MainWindow", u"Determinante", None))
#if QT_CONFIG(tooltip)
        self.table_import_from_csv_button.setToolTip(QCoreApplication.translate("MainWindow", u"Importar matriz desde un archivo CSV", None))
#endif // QT_CONFIG(tooltip)
        self.table_import_from_csv_button.setText(QCoreApplication.translate("MainWindow", u"Importar Matriz", None))
        ___qtablewidgetitem = self.input_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"X1", None));
        ___qtablewidgetitem1 = self.input_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"X2", None));
        ___qtablewidgetitem2 = self.input_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"b", None));

        __sortingEnabled = self.input_table.isSortingEnabled()
        self.input_table.setSortingEnabled(False)
        self.input_table.setSortingEnabled(__sortingEnabled)

        self.side_equation_text_label.setText(QCoreApplication.translate("MainWindow", u"Ecuacion actual: ", None))
        self.equation_text_label.setText("")
#if QT_CONFIG(tooltip)
        self.edit_equation_button.setToolTip(QCoreApplication.translate("MainWindow", u"Editar ecuaci\u00f3n", None))
#endif // QT_CONFIG(tooltip)
        self.edit_equation_button.setText("")
        self.bisection_interval_b_label.setText(QCoreApplication.translate("MainWindow", u"Intervalo b", None))
        self.bisection_interval_a_label.setText(QCoreApplication.translate("MainWindow", u"Intervalo a", None))
        self.bisection_tolerance_label.setText(QCoreApplication.translate("MainWindow", u"Tolerancia", None))
        self.bisection_solution_button.setText(QCoreApplication.translate("MainWindow", u"Obtener ra\u00edz", None))
        self.method_equation_tab_widget.setTabText(self.method_equation_tab_widget.indexOf(self.bisection_tab), QCoreApplication.translate("MainWindow", u"Bisecci\u00f3n", None))
        self.newton_max_iter_label.setText(QCoreApplication.translate("MainWindow", u"Iteraciones m\u00e1ximas", None))
        self.newton_tolerance_label.setText(QCoreApplication.translate("MainWindow", u"Tolerancia", None))
        self.newton_x_value_label.setText(QCoreApplication.translate("MainWindow", u"Valor de x", None))
        self.newton_solution_button.setText(QCoreApplication.translate("MainWindow", u"Obtener ra\u00edz", None))
        self.method_equation_tab_widget.setTabText(self.method_equation_tab_widget.indexOf(self.newton_tab), QCoreApplication.translate("MainWindow", u"Newton", None))
        self.false_interval_b_label.setText(QCoreApplication.translate("MainWindow", u"Intervalo xu", None))
        self.false_interval_a_label.setText(QCoreApplication.translate("MainWindow", u"Intervalo xl", None))
        self.false_tolerance_label.setText(QCoreApplication.translate("MainWindow", u"Tolerancia", None))
        self.false_solution_button.setText(QCoreApplication.translate("MainWindow", u"Obtener ra\u00edz", None))
        self.method_equation_tab_widget.setTabText(self.method_equation_tab_widget.indexOf(self.false_position_tab), QCoreApplication.translate("MainWindow", u"Falsa posici\u00f3n", None))
        self.secant_tolerance_label.setText(QCoreApplication.translate("MainWindow", u"Tolerancia", None))
        self.secant_x0_label.setText(QCoreApplication.translate("MainWindow", u"X0", None))
        self.secant_max_iter_label.setText(QCoreApplication.translate("MainWindow", u"Iteraciones m\u00e1ximas", None))
        self.secant_xi_label.setText(QCoreApplication.translate("MainWindow", u"Xi", None))
        self.secant_solution_button.setText(QCoreApplication.translate("MainWindow", u"Obtener ra\u00edz", None))
        self.method_equation_tab_widget.setTabText(self.method_equation_tab_widget.indexOf(self.secant_tab), QCoreApplication.translate("MainWindow", u"Secante", None))
    # retranslateUi

