# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowYdpude.ui'
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
        MainWindow.resize(716, 491)
        icon = QIcon()
        icon.addFile(u":/icon/Images/ico.ico", QSize(), QIcon.Normal, QIcon.Off)
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
"#MainWindow, #table_buttons_down_widget{\n"
"background: #2c313c\n"
"}\n"
"\n"
"#table_buttons_frame, #matrix_page{\n"
"background-color: #2c313c;\n"
"}\n"
"\n"
"#table_buttons_frame QPushButton, #table_buttons_frame QComboBox,#solution_widget QComboBox, #equations_page QPushButton, #table_options_widget QPushButton, #table_options_widget QComboBox, #table_aumented_widget QPushButton, #equation_widget QComboBox, #main_home_widget QPushButton{\n"
"    color: #ffffff;\n"
"    text-align: center;\n"
"	padding: 3px;\n"
"    border-radius: 10px;\n"
"    background-color: #16191d ;\n"
"}\n"
"/*3c4b84*/\n"
"#table_buttons_frame QPushButton::hover, #table_buttons_frame QComboBox::hover,#equations_page QPushButton::hover, #table_options_widget QPushButton::hover, #table_options_widget QComboBox::hover, #t"
                        "able_aumented_widget QPushButton::hover, #equation_widget QComboBox::hover, #main_home_widget QPushButton::hover{\n"
"    background-color: #2a2e35;\n"
"    border-color: #454a52;\n"
"}\n"
"#table_buttons_frame QPushButton::pressed, #table_buttons_frame QComboBox::pressed,#equations_page QPushButton::pressed, #table_options_widget QPushButton::pressed, #table_options_widget QComboBox::pressed, #table_aumented_widget QPushButton::pressed, #equation_widget QComboBox::pressed{\n"
"    background-color: #1d2127;\n"
"}\n"
"\n"
"#table_buttons_frame QSpinBox{\n"
"color: #fff;\n"
"background-color: #1d2127;\n"
"border-radius: 10px;\n"
"padding: 1px;\n"
"}\n"
"\n"
"#table_buttons_frame QLabel, #table_aumented_widget QLabel{\n"
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
"#table_column_spinbox_widget QSpinBox:up-button, #table_row_"
                        "spinbox_widget QSpinBox:up-button{\n"
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
" #table_buttons_frame QComboBox:dropdown, #equation_widget QComboBox:dropdown{\n"
"border: 0px;\n"
"}\n"
"\n"
"#table_buttons_frame QComboBox:down-arrow, #equation_widget QComboBox:down-arrow{\n"
"subcontrol-position: right;\n"
"width: 18px;\n"
"height: 18px;\n"
"}\n"
"\n"
"#table_buttons_frame QComboBox QListView, #solution_widget QComboBox QListView, #equation_widget QComboBox QListView{\n"
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
"#main_table_"
                        "widget QHeaderView, #main_table_widget QHeaderView::section, #main_table_widget QTableCornerButton::section{\n"
"background-color: #3e4555;\n"
"}\n"
"\n"
"#main_table_widget QTableWidget::item:hover, #main_table_widget QTableWidget::item:selected{\n"
"background-color: #72809b;\n"
"font-weight: 700;\n"
"color: #6e86b1\n"
"}\n"
"\n"
"#main_table_widget QTableWidget::item{\n"
"color: #fff;\n"
"selection-color: #000\n"
"}\n"
"\n"
"/* Estilo para el editor de texto cuando se est\u00e1 editando una celda */\n"
"QTableWidget::item QLineEdit{\n"
"background-color:#8592a9;\n"
"color: #000;\n"
"}\n"
"\n"
"#side_bar{\n"
"background: #16191d\n"
"}\n"
"#sub_side_bar QPushButton, #expand_button_frame QPushButton{\n"
"text-align: left;\n"
"}\n"
"#sub_side_bar QPushButton::hover, #table_buttons_down_widget QPushButton::hover{\n"
"background-color: #1f232a;\n"
"font-weight: 700;\n"
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
                        "#equations_page, #information_page, #home_page{\n"
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
"    text-align: center"
                        ";\n"
"	padding: 3px;\n"
"    border-radius: 10px;\n"
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
"QCheckBox::checked{\n"
"color: #9ba6b9;\n"
"}\n"
"\n"
"QCheckBox::unchecked{\n"
"color: #72809b\n"
"}\n"
"#table_buttons_down_widget QPushButton{\n"
"text-align:left;\n"
"}\n"
"\n"
"#sub_table_column_row_widget QLabel{\n"
"background: none;\n"
"}\n"
"\n"
"#table_aumented_widget QLabel{\n"
"background:none;\n"
"}\n"
"\n"
"#main_table_widget QHeaderView::section, #main_table_widget QTableCornerButton::section{\n"
"background-color: #3e4769;\n"
"}\n"
"\n"
"#main_table_widget QHeaderView::"
                        "section::hover, #main_table_widget QTableCornerButton::section::hover{\n"
"background-color: #586596;\n"
"}\n"
"\n"
"#method_equation_tab_widget QLabel{\n"
"background-color: #3e4769;\n"
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
        self.verticalLayout_5.setContentsMargins(3, 0, 0, 0)
        self.sub_side_bar = QWidget(self.side_bar)
        self.sub_side_bar.setObjectName(u"sub_side_bar")
        self.sub_side_bar.setMinimumSize(QSize(0, 0))
        self.sub_side_bar.setMaximumSize(QSize(33, 16777215))
        self.sub_side_bar.setStyleSheet(u"#sub_side_bar QPushButton{\n"
"padding-right: 5px\n"
"}\n"
"#config_button_frame QPushButton{\n"
"padding-left: 0px;\n"
"}")
        self.verticalLayout_11 = QVBoxLayout(self.sub_side_bar)
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.expand_button_frame = QFrame(self.sub_side_bar)
        self.expand_button_frame.setObjectName(u"expand_button_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.expand_button_frame.sizePolicy().hasHeightForWidth())
        self.expand_button_frame.setSizePolicy(sizePolicy)
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
        font.setPointSize(11)
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
        font1 = QFont()
        font1.setPointSize(11)
        self.equation_tab_button.setFont(font1)
        self.equation_tab_button.setStyleSheet(u"text-align:left;\n"
"margin-left:-1px;")
        icon3 = QIcon()
        icon3.addFile(u":/icon/Images/fx.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.equation_tab_button.setIcon(icon3)
        self.equation_tab_button.setIconSize(QSize(32, 32))

        self.verticalLayout_7.addWidget(self.equation_tab_button)


        self.verticalLayout_11.addWidget(self.tab_buttons_frame, 0, Qt.AlignmentFlag.AlignTop)

        self.exportation_importation_button_frame = QFrame(self.sub_side_bar)
        self.exportation_importation_button_frame.setObjectName(u"exportation_importation_button_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.exportation_importation_button_frame.sizePolicy().hasHeightForWidth())
        self.exportation_importation_button_frame.setSizePolicy(sizePolicy1)
        self.exportation_importation_button_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.exportation_importation_button_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.exportation_importation_button_frame)
        self.verticalLayout_21.setSpacing(5)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 4)
        self.export_button = QPushButton(self.exportation_importation_button_frame)
        self.export_button.setObjectName(u"export_button")
        self.export_button.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u":/icon/Images/export.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.export_button.setIcon(icon4)
        self.export_button.setIconSize(QSize(30, 30))

        self.verticalLayout_21.addWidget(self.export_button)

        self.import_button = QPushButton(self.exportation_importation_button_frame)
        self.import_button.setObjectName(u"import_button")
        self.import_button.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(u":/icon/Images/import.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.import_button.setIcon(icon5)
        self.import_button.setIconSize(QSize(30, 30))

        self.verticalLayout_21.addWidget(self.import_button)


        self.verticalLayout_11.addWidget(self.exportation_importation_button_frame, 0, Qt.AlignmentFlag.AlignBottom)

        self.config_button_frame = QFrame(self.sub_side_bar)
        self.config_button_frame.setObjectName(u"config_button_frame")
        sizePolicy.setHeightForWidth(self.config_button_frame.sizePolicy().hasHeightForWidth())
        self.config_button_frame.setSizePolicy(sizePolicy)
        self.config_button_frame.setFont(font1)
        self.config_button_frame.setStyleSheet(u"text-align:left")
        self.verticalLayout_20 = QVBoxLayout(self.config_button_frame)
        self.verticalLayout_20.setSpacing(5)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 5)
        self.information_button = QPushButton(self.config_button_frame)
        self.information_button.setObjectName(u"information_button")
        self.information_button.setFont(font1)
        icon6 = QIcon()
        icon6.addFile(u":/icon/Images/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.information_button.setIcon(icon6)
        self.information_button.setIconSize(QSize(30, 30))

        self.verticalLayout_20.addWidget(self.information_button)


        self.verticalLayout_11.addWidget(self.config_button_frame, 0, Qt.AlignmentFlag.AlignBottom)


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
        self.table_buttons_horizontal_layout.setSpacing(10)
        self.table_buttons_horizontal_layout.setObjectName(u"table_buttons_horizontal_layout")
        self.table_buttons_horizontal_layout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.table_buttons_horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.table_column_row_widget = QWidget(self.table_buttons_frame)
        self.table_column_row_widget.setObjectName(u"table_column_row_widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.table_column_row_widget.sizePolicy().hasHeightForWidth())
        self.table_column_row_widget.setSizePolicy(sizePolicy2)
        self.verticalLayout_19 = QVBoxLayout(self.table_column_row_widget)
        self.verticalLayout_19.setSpacing(5)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 4, 0, 0)
        self.sub_table_column_row_widget = QWidget(self.table_column_row_widget)
        self.sub_table_column_row_widget.setObjectName(u"sub_table_column_row_widget")
        self.horizontalLayout_3 = QHBoxLayout(self.sub_table_column_row_widget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.table_row_spinbox_widget = QWidget(self.sub_table_column_row_widget)
        self.table_row_spinbox_widget.setObjectName(u"table_row_spinbox_widget")
        sizePolicy2.setHeightForWidth(self.table_row_spinbox_widget.sizePolicy().hasHeightForWidth())
        self.table_row_spinbox_widget.setSizePolicy(sizePolicy2)
        self.table_row_spinbox_widget.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.table_row_spinbox_widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.row_spinbox_label = QLabel(self.table_row_spinbox_widget)
        self.row_spinbox_label.setObjectName(u"row_spinbox_label")
        self.row_spinbox_label.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.row_spinbox_label.setFont(font2)

        self.verticalLayout_3.addWidget(self.row_spinbox_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.row_spinbox = QSpinBox(self.table_row_spinbox_widget)
        self.row_spinbox.setObjectName(u"row_spinbox")
        self.row_spinbox.setMinimumSize(QSize(70, 30))
        self.row_spinbox.setMaximumSize(QSize(16777215, 16777215))
        self.row_spinbox.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.row_spinbox.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.row_spinbox, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.table_row_spinbox_widget)

        self.table_column_spinbox_widget = QWidget(self.sub_table_column_row_widget)
        self.table_column_spinbox_widget.setObjectName(u"table_column_spinbox_widget")
        sizePolicy2.setHeightForWidth(self.table_column_spinbox_widget.sizePolicy().hasHeightForWidth())
        self.table_column_spinbox_widget.setSizePolicy(sizePolicy2)
        self.verticalLayout = QVBoxLayout(self.table_column_spinbox_widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.column_spinbox_label = QLabel(self.table_column_spinbox_widget)
        self.column_spinbox_label.setObjectName(u"column_spinbox_label")
        self.column_spinbox_label.setMaximumSize(QSize(16777215, 30))
        self.column_spinbox_label.setFont(font2)

        self.verticalLayout.addWidget(self.column_spinbox_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.column_spinbox = QSpinBox(self.table_column_spinbox_widget)
        self.column_spinbox.setObjectName(u"column_spinbox")
        self.column_spinbox.setMinimumSize(QSize(70, 30))
        self.column_spinbox.setMaximumSize(QSize(16777215, 16777215))
        self.column_spinbox.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.column_spinbox, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.table_column_spinbox_widget)


        self.verticalLayout_19.addWidget(self.sub_table_column_row_widget)

        self.checkbox_widget = QWidget(self.table_column_row_widget)
        self.checkbox_widget.setObjectName(u"checkbox_widget")
        self.checkbox_widget.setFont(font1)
        self.horizontalLayout_5 = QHBoxLayout(self.checkbox_widget)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.table_resize_checkbox = QCheckBox(self.checkbox_widget)
        self.table_resize_checkbox.setObjectName(u"table_resize_checkbox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.table_resize_checkbox.sizePolicy().hasHeightForWidth())
        self.table_resize_checkbox.setSizePolicy(sizePolicy3)
        self.table_resize_checkbox.setMinimumSize(QSize(0, 0))
        self.table_resize_checkbox.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        self.table_resize_checkbox.setFont(font3)
        self.table_resize_checkbox.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.table_resize_checkbox.setStyleSheet(u"")
        self.table_resize_checkbox.setChecked(False)
        self.table_resize_checkbox.setTristate(False)

        self.horizontalLayout_5.addWidget(self.table_resize_checkbox, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_19.addWidget(self.checkbox_widget)

        self.verticalLayout_19.setStretch(0, 100)
        self.verticalLayout_19.setStretch(1, 1)

        self.table_buttons_horizontal_layout.addWidget(self.table_column_row_widget, 0, Qt.AlignmentFlag.AlignLeft)

        self.select_matrix_widget = QWidget(self.table_buttons_frame)
        self.select_matrix_widget.setObjectName(u"select_matrix_widget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(2)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.select_matrix_widget.sizePolicy().hasHeightForWidth())
        self.select_matrix_widget.setSizePolicy(sizePolicy4)
        self.verticalLayout_25 = QVBoxLayout(self.select_matrix_widget)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_25.setContentsMargins(0, 5, 0, 0)
        self.select_table_combobox = QComboBox(self.select_matrix_widget)
        self.select_table_combobox.addItem("")
        self.select_table_combobox.setObjectName(u"select_table_combobox")
        self.select_table_combobox.setMinimumSize(QSize(175, 0))
        font4 = QFont()
        font4.setPointSize(13)
        font4.setBold(True)
        self.select_table_combobox.setFont(font4)
        self.select_table_combobox.setFrame(True)

        self.verticalLayout_25.addWidget(self.select_table_combobox)

        self.select_matrix_options_widget = QWidget(self.select_matrix_widget)
        self.select_matrix_options_widget.setObjectName(u"select_matrix_options_widget")
        self.horizontalLayout_8 = QHBoxLayout(self.select_matrix_options_widget)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(5, 0, 0, 0)
        self.save_current_table_button = QPushButton(self.select_matrix_options_widget)
        self.save_current_table_button.setObjectName(u"save_current_table_button")
        font5 = QFont()
        font5.setPointSize(9)
        self.save_current_table_button.setFont(font5)
        icon7 = QIcon()
        icon7.addFile(u":/icon/Images/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.save_current_table_button.setIcon(icon7)
        self.save_current_table_button.setIconSize(QSize(26, 26))

        self.horizontalLayout_8.addWidget(self.save_current_table_button)

        self.change_current_table_button = QPushButton(self.select_matrix_options_widget)
        self.change_current_table_button.setObjectName(u"change_current_table_button")
        self.change_current_table_button.setFont(font5)
        icon8 = QIcon()
        icon8.addFile(u":/icon/Images/change.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.change_current_table_button.setIcon(icon8)
        self.change_current_table_button.setIconSize(QSize(26, 26))

        self.horizontalLayout_8.addWidget(self.change_current_table_button)

        self.delete_current_table_button = QPushButton(self.select_matrix_options_widget)
        self.delete_current_table_button.setObjectName(u"delete_current_table_button")
        icon9 = QIcon()
        icon9.addFile(u":/icon/Images/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_current_table_button.setIcon(icon9)
        self.delete_current_table_button.setIconSize(QSize(26, 26))

        self.horizontalLayout_8.addWidget(self.delete_current_table_button)


        self.verticalLayout_25.addWidget(self.select_matrix_options_widget)


        self.table_buttons_horizontal_layout.addWidget(self.select_matrix_widget, 0, Qt.AlignmentFlag.AlignLeft)

        self.table_extra_options_widget = QWidget(self.table_buttons_frame)
        self.table_extra_options_widget.setObjectName(u"table_extra_options_widget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy5.setHorizontalStretch(3)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.table_extra_options_widget.sizePolicy().hasHeightForWidth())
        self.table_extra_options_widget.setSizePolicy(sizePolicy5)
        self.table_extra_options_widget.setMinimumSize(QSize(0, 0))
        self.table_extra_options_widget.setSizeIncrement(QSize(0, 0))
        self.verticalLayout_26 = QVBoxLayout(self.table_extra_options_widget)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.table_extra_options_grid = QGridLayout()
        self.table_extra_options_grid.setObjectName(u"table_extra_options_grid")
        self.table_extra_options_grid.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.table_extra_options_grid.setHorizontalSpacing(4)
        self.table_extra_options_grid.setVerticalSpacing(3)
        self.table_extra_options_grid.setContentsMargins(-1, 0, -1, -1)
        self.table_select_solutions_combobox = QComboBox(self.table_extra_options_widget)
        self.table_select_solutions_combobox.addItem("")
        self.table_select_solutions_combobox.addItem("")
        self.table_select_solutions_combobox.addItem("")
        self.table_select_solutions_combobox.setObjectName(u"table_select_solutions_combobox")
        self.table_select_solutions_combobox.setMaximumSize(QSize(16777215, 26))
        self.table_select_solutions_combobox.setFont(font3)

        self.table_extra_options_grid.addWidget(self.table_select_solutions_combobox, 0, 2, 1, 1)

        self.table_solve_button = QPushButton(self.table_extra_options_widget)
        self.table_solve_button.setObjectName(u"table_solve_button")
        self.table_solve_button.setMaximumSize(QSize(16777215, 26))
        self.table_solve_button.setFont(font3)
        self.table_solve_button.setStyleSheet(u"QPushButton{\n"
"background-color: #3c4b84\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: #47599d;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: #4f63ae;\n"
"}\n"
"")

        self.table_extra_options_grid.addWidget(self.table_solve_button, 2, 2, 1, 1)

        self.table_vector_button = QPushButton(self.table_extra_options_widget)
        self.table_vector_button.setObjectName(u"table_vector_button")
        self.table_vector_button.setMaximumSize(QSize(16777215, 26))
        self.table_vector_button.setFont(font1)
        icon10 = QIcon()
        icon10.addFile(u":/icon/Images/vector.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.table_vector_button.setIcon(icon10)
        self.table_vector_button.setIconSize(QSize(21, 21))

        self.table_extra_options_grid.addWidget(self.table_vector_button, 0, 4, 1, 1)

        self.table_invert_button = QPushButton(self.table_extra_options_widget)
        self.table_invert_button.setObjectName(u"table_invert_button")
        self.table_invert_button.setMaximumSize(QSize(16777215, 26))
        self.table_invert_button.setFont(font3)

        self.table_extra_options_grid.addWidget(self.table_invert_button, 2, 3, 1, 1)

        self.table_transpose_button = QPushButton(self.table_extra_options_widget)
        self.table_transpose_button.setObjectName(u"table_transpose_button")
        self.table_transpose_button.setMaximumSize(QSize(16777215, 26))
        icon11 = QIcon()
        icon11.addFile(u":/icon/Images/transpose.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.table_transpose_button.setIcon(icon11)
        self.table_transpose_button.setIconSize(QSize(24, 24))

        self.table_extra_options_grid.addWidget(self.table_transpose_button, 2, 4, 1, 1)

        self.table_determinant_button = QPushButton(self.table_extra_options_widget)
        self.table_determinant_button.setObjectName(u"table_determinant_button")
        self.table_determinant_button.setMaximumSize(QSize(16777215, 26))
        self.table_determinant_button.setFont(font3)
        self.table_determinant_button.setIconSize(QSize(26, 26))

        self.table_extra_options_grid.addWidget(self.table_determinant_button, 0, 3, 1, 1)

        self.table_update_button = QPushButton(self.table_extra_options_widget)
        self.table_update_button.setObjectName(u"table_update_button")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(1)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.table_update_button.sizePolicy().hasHeightForWidth())
        self.table_update_button.setSizePolicy(sizePolicy6)
        self.table_update_button.setMaximumSize(QSize(38, 38))
        icon12 = QIcon()
        icon12.addFile(u":/icon/Images/refresh.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.table_update_button.setIcon(icon12)
        self.table_update_button.setIconSize(QSize(28, 28))

        self.table_extra_options_grid.addWidget(self.table_update_button, 0, 5, 3, 1)


        self.verticalLayout_26.addLayout(self.table_extra_options_grid)


        self.table_buttons_horizontal_layout.addWidget(self.table_extra_options_widget)


        self.verticalLayout_2.addWidget(self.table_buttons_frame)

        self.table_aumented_widget = QWidget(self.main_table_widget)
        self.table_aumented_widget.setObjectName(u"table_aumented_widget")
        self.horizontalLayout_6 = QHBoxLayout(self.table_aumented_widget)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.coeficient_table_widget = QWidget(self.table_aumented_widget)
        self.coeficient_table_widget.setObjectName(u"coeficient_table_widget")
        self.verticalLayout_23 = QVBoxLayout(self.coeficient_table_widget)
        self.verticalLayout_23.setSpacing(3)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.coeficient_option_widget = QWidget(self.coeficient_table_widget)
        self.coeficient_option_widget.setObjectName(u"coeficient_option_widget")
        self.horizontalLayout_7 = QHBoxLayout(self.coeficient_option_widget)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 30, 0)
        self.coeficient_label = QLabel(self.coeficient_option_widget)
        self.coeficient_label.setObjectName(u"coeficient_label")
        sizePolicy2.setHeightForWidth(self.coeficient_label.sizePolicy().hasHeightForWidth())
        self.coeficient_label.setSizePolicy(sizePolicy2)
        self.coeficient_label.setFont(font3)
        self.coeficient_label.setStyleSheet(u"margin-left: 10px;")
        self.coeficient_label.setWordWrap(False)

        self.horizontalLayout_7.addWidget(self.coeficient_label, 0, Qt.AlignmentFlag.AlignLeft)

        self.coeficient_option_sub_widget = QWidget(self.coeficient_option_widget)
        self.coeficient_option_sub_widget.setObjectName(u"coeficient_option_sub_widget")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(1)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.coeficient_option_sub_widget.sizePolicy().hasHeightForWidth())
        self.coeficient_option_sub_widget.setSizePolicy(sizePolicy7)
        self.verticalLayout_27 = QVBoxLayout(self.coeficient_option_sub_widget)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.coeficient_option_grid = QGridLayout()
        self.coeficient_option_grid.setSpacing(6)
        self.coeficient_option_grid.setObjectName(u"coeficient_option_grid")
        self.coeficient_option_grid.setContentsMargins(-1, -1, -1, 0)
        self.adjust_coeficient_matrix_button = QPushButton(self.coeficient_option_sub_widget)
        self.adjust_coeficient_matrix_button.setObjectName(u"adjust_coeficient_matrix_button")
        sizePolicy3.setHeightForWidth(self.adjust_coeficient_matrix_button.sizePolicy().hasHeightForWidth())
        self.adjust_coeficient_matrix_button.setSizePolicy(sizePolicy3)
        self.adjust_coeficient_matrix_button.setMaximumSize(QSize(38, 34))
        icon13 = QIcon()
        icon13.addFile(u":/icon/Images/resize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.adjust_coeficient_matrix_button.setIcon(icon13)
        self.adjust_coeficient_matrix_button.setIconSize(QSize(28, 28))

        self.coeficient_option_grid.addWidget(self.adjust_coeficient_matrix_button, 0, 3, 1, 1)

        self.random_matrix_button = QPushButton(self.coeficient_option_sub_widget)
        self.random_matrix_button.setObjectName(u"random_matrix_button")
        self.random_matrix_button.setMaximumSize(QSize(38, 34))
        self.random_matrix_button.setFont(font1)
        self.random_matrix_button.setStyleSheet(u"")
        icon14 = QIcon()
        icon14.addFile(u":/icon/Images/random.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.random_matrix_button.setIcon(icon14)
        self.random_matrix_button.setIconSize(QSize(36, 36))

        self.coeficient_option_grid.addWidget(self.random_matrix_button, 0, 1, 1, 1)

        self.clean_coeficient_matrix_button = QPushButton(self.coeficient_option_sub_widget)
        self.clean_coeficient_matrix_button.setObjectName(u"clean_coeficient_matrix_button")
        sizePolicy3.setHeightForWidth(self.clean_coeficient_matrix_button.sizePolicy().hasHeightForWidth())
        self.clean_coeficient_matrix_button.setSizePolicy(sizePolicy3)
        self.clean_coeficient_matrix_button.setMaximumSize(QSize(38, 34))
        icon15 = QIcon()
        icon15.addFile(u":/icon/Images/clean.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.clean_coeficient_matrix_button.setIcon(icon15)
        self.clean_coeficient_matrix_button.setIconSize(QSize(28, 28))

        self.coeficient_option_grid.addWidget(self.clean_coeficient_matrix_button, 0, 0, 1, 1)

        self.fill_0_coeficient_matrix_button = QPushButton(self.coeficient_option_sub_widget)
        self.fill_0_coeficient_matrix_button.setObjectName(u"fill_0_coeficient_matrix_button")
        sizePolicy3.setHeightForWidth(self.fill_0_coeficient_matrix_button.sizePolicy().hasHeightForWidth())
        self.fill_0_coeficient_matrix_button.setSizePolicy(sizePolicy3)
        self.fill_0_coeficient_matrix_button.setMaximumSize(QSize(38, 34))
        icon16 = QIcon()
        icon16.addFile(u":/icon/Images/zero.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.fill_0_coeficient_matrix_button.setIcon(icon16)
        self.fill_0_coeficient_matrix_button.setIconSize(QSize(36, 36))

        self.coeficient_option_grid.addWidget(self.fill_0_coeficient_matrix_button, 0, 2, 1, 1)


        self.verticalLayout_27.addLayout(self.coeficient_option_grid)


        self.horizontalLayout_7.addWidget(self.coeficient_option_sub_widget, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_23.addWidget(self.coeficient_option_widget)

        self.coeficient_table = QTableWidget(self.coeficient_table_widget)
        if (self.coeficient_table.columnCount() < 3):
            self.coeficient_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.coeficient_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.coeficient_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.coeficient_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.coeficient_table.rowCount() < 3):
            self.coeficient_table.setRowCount(3)
        font6 = QFont()
        font6.setFamilies([u"Calibri"])
        font6.setPointSize(9)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font6);
        __qtablewidgetitem3.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsEnabled);
        self.coeficient_table.setItem(0, 0, __qtablewidgetitem3)
        self.coeficient_table.setObjectName(u"coeficient_table")
        self.coeficient_table.setStyleSheet(u"")
        self.coeficient_table.setSortingEnabled(False)
        self.coeficient_table.setCornerButtonEnabled(True)
        self.coeficient_table.verticalHeader().setVisible(True)

        self.verticalLayout_23.addWidget(self.coeficient_table)


        self.horizontalLayout_6.addWidget(self.coeficient_table_widget)

        self.independent_terms_widget = QWidget(self.table_aumented_widget)
        self.independent_terms_widget.setObjectName(u"independent_terms_widget")
        self.verticalLayout_24 = QVBoxLayout(self.independent_terms_widget)
        self.verticalLayout_24.setSpacing(3)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.independent_options_widget = QWidget(self.independent_terms_widget)
        self.independent_options_widget.setObjectName(u"independent_options_widget")
        self.horizontalLayout_9 = QHBoxLayout(self.independent_options_widget)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.independent_terms_label = QLabel(self.independent_options_widget)
        self.independent_terms_label.setObjectName(u"independent_terms_label")
        self.independent_terms_label.setFont(font3)
        self.independent_terms_label.setStyleSheet(u"margin-left: -3px;")
        self.independent_terms_label.setWordWrap(False)

        self.horizontalLayout_9.addWidget(self.independent_terms_label)

        self.independent_option_widget = QWidget(self.independent_options_widget)
        self.independent_option_widget.setObjectName(u"independent_option_widget")
        self.horizontalLayout_4 = QHBoxLayout(self.independent_option_widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.independent_option_grid = QGridLayout()
        self.independent_option_grid.setObjectName(u"independent_option_grid")
        self.independent_option_grid.setContentsMargins(-1, -1, -1, 0)
        self.clean_independent_matrix_button = QPushButton(self.independent_option_widget)
        self.clean_independent_matrix_button.setObjectName(u"clean_independent_matrix_button")
        sizePolicy6.setHeightForWidth(self.clean_independent_matrix_button.sizePolicy().hasHeightForWidth())
        self.clean_independent_matrix_button.setSizePolicy(sizePolicy6)
        self.clean_independent_matrix_button.setMaximumSize(QSize(38, 34))
        self.clean_independent_matrix_button.setIcon(icon15)
        self.clean_independent_matrix_button.setIconSize(QSize(28, 28))

        self.independent_option_grid.addWidget(self.clean_independent_matrix_button, 0, 0, 1, 1)

        self.random_independent_matrix_button = QPushButton(self.independent_option_widget)
        self.random_independent_matrix_button.setObjectName(u"random_independent_matrix_button")
        self.random_independent_matrix_button.setMaximumSize(QSize(38, 34))
        self.random_independent_matrix_button.setIcon(icon14)
        self.random_independent_matrix_button.setIconSize(QSize(36, 36))

        self.independent_option_grid.addWidget(self.random_independent_matrix_button, 0, 1, 1, 1)

        self.adjust_independent_matrix_button = QPushButton(self.independent_option_widget)
        self.adjust_independent_matrix_button.setObjectName(u"adjust_independent_matrix_button")
        sizePolicy6.setHeightForWidth(self.adjust_independent_matrix_button.sizePolicy().hasHeightForWidth())
        self.adjust_independent_matrix_button.setSizePolicy(sizePolicy6)
        self.adjust_independent_matrix_button.setMaximumSize(QSize(38, 34))
        self.adjust_independent_matrix_button.setIcon(icon13)
        self.adjust_independent_matrix_button.setIconSize(QSize(28, 28))

        self.independent_option_grid.addWidget(self.adjust_independent_matrix_button, 0, 3, 1, 1)

        self.zero_independent_matrix_button = QPushButton(self.independent_option_widget)
        self.zero_independent_matrix_button.setObjectName(u"zero_independent_matrix_button")
        sizePolicy6.setHeightForWidth(self.zero_independent_matrix_button.sizePolicy().hasHeightForWidth())
        self.zero_independent_matrix_button.setSizePolicy(sizePolicy6)
        self.zero_independent_matrix_button.setMaximumSize(QSize(38, 34))
        self.zero_independent_matrix_button.setIcon(icon16)
        self.zero_independent_matrix_button.setIconSize(QSize(36, 36))

        self.independent_option_grid.addWidget(self.zero_independent_matrix_button, 0, 2, 1, 1)


        self.horizontalLayout_4.addLayout(self.independent_option_grid)


        self.horizontalLayout_9.addWidget(self.independent_option_widget)


        self.verticalLayout_24.addWidget(self.independent_options_widget)

        self.independent_terms_table = QTableWidget(self.independent_terms_widget)
        if (self.independent_terms_table.columnCount() < 1):
            self.independent_terms_table.setColumnCount(1)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.independent_terms_table.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        if (self.independent_terms_table.rowCount() < 1):
            self.independent_terms_table.setRowCount(1)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.independent_terms_table.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.independent_terms_table.setItem(0, 0, __qtablewidgetitem6)
        self.independent_terms_table.setObjectName(u"independent_terms_table")
        self.independent_terms_table.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.independent_terms_table.setTextElideMode(Qt.TextElideMode.ElideLeft)
        self.independent_terms_table.setGridStyle(Qt.PenStyle.SolidLine)
        self.independent_terms_table.setSortingEnabled(True)
        self.independent_terms_table.horizontalHeader().setVisible(True)
        self.independent_terms_table.verticalHeader().setVisible(False)

        self.verticalLayout_24.addWidget(self.independent_terms_table)


        self.horizontalLayout_6.addWidget(self.independent_terms_widget)

        self.horizontalLayout_6.setStretch(0, 10)
        self.horizontalLayout_6.setStretch(1, 1)

        self.verticalLayout_2.addWidget(self.table_aumented_widget)

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
        self.horizontalLayout_2.setContentsMargins(6, 0, 0, 3)
        self.equation_grid = QGridLayout()
        self.equation_grid.setObjectName(u"equation_grid")
        self.equation_grid.setHorizontalSpacing(7)
        self.equation_grid.setVerticalSpacing(0)
        self.equation_grid.setContentsMargins(-1, -1, 0, 2)
        self.equation_derivative_label = QLabel(self.equation_widget)
        self.equation_derivative_label.setObjectName(u"equation_derivative_label")
        font7 = QFont()
        font7.setPointSize(14)
        font7.setBold(True)
        self.equation_derivative_label.setFont(font7)
        self.equation_derivative_label.setStyleSheet(u"background: none")
        self.equation_derivative_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.equation_grid.addWidget(self.equation_derivative_label, 1, 1, 1, 1)

        self.equation_text_label = QLabel(self.equation_widget)
        self.equation_text_label.setObjectName(u"equation_text_label")
        self.equation_text_label.setMaximumSize(QSize(140, 40))
        self.equation_text_label.setFont(font2)
        self.equation_text_label.setStyleSheet(u"padding: 2px;")
        self.equation_text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.equation_grid.addWidget(self.equation_text_label, 0, 0, 1, 1, Qt.AlignmentFlag.AlignVCenter)

        self.equation_label = QLabel(self.equation_widget)
        self.equation_label.setObjectName(u"equation_label")
        self.equation_label.setFont(font7)
        self.equation_label.setStyleSheet(u"background: none;")
        self.equation_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.equation_grid.addWidget(self.equation_label, 0, 1, 1, 1)

        self.equation_integral_text_label = QLabel(self.equation_widget)
        self.equation_integral_text_label.setObjectName(u"equation_integral_text_label")
        self.equation_integral_text_label.setFont(font2)
        self.equation_integral_text_label.setStyleSheet(u"padding: 2px;")
        self.equation_integral_text_label.setTextFormat(Qt.TextFormat.AutoText)
        self.equation_integral_text_label.setScaledContents(False)
        self.equation_integral_text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.equation_grid.addWidget(self.equation_integral_text_label, 1, 0, 1, 1, Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout_2.addLayout(self.equation_grid)

        self.equation_options_widget = QWidget(self.equation_widget)
        self.equation_options_widget.setObjectName(u"equation_options_widget")
        self.horizontalLayout_10 = QHBoxLayout(self.equation_options_widget)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.equation_options_grid_layout = QGridLayout()
        self.equation_options_grid_layout.setObjectName(u"equation_options_grid_layout")
        self.select_equation_combobox = QComboBox(self.equation_options_widget)
        self.select_equation_combobox.addItem("")
        self.select_equation_combobox.setObjectName(u"select_equation_combobox")
        font8 = QFont()
        font8.setPointSize(13)
        font8.setBold(True)
        font8.setUnderline(False)
        self.select_equation_combobox.setFont(font8)

        self.equation_options_grid_layout.addWidget(self.select_equation_combobox, 0, 0, 1, 2)

        self.equation_save_button = QPushButton(self.equation_options_widget)
        self.equation_save_button.setObjectName(u"equation_save_button")
        self.equation_save_button.setIcon(icon7)
        self.equation_save_button.setIconSize(QSize(24, 24))

        self.equation_options_grid_layout.addWidget(self.equation_save_button, 1, 0, 1, 1)

        self.equation_load_button = QPushButton(self.equation_options_widget)
        self.equation_load_button.setObjectName(u"equation_load_button")
        self.equation_load_button.setIcon(icon8)
        self.equation_load_button.setIconSize(QSize(26, 26))

        self.equation_options_grid_layout.addWidget(self.equation_load_button, 2, 0, 1, 1)

        self.equation_delete_button = QPushButton(self.equation_options_widget)
        self.equation_delete_button.setObjectName(u"equation_delete_button")
        self.equation_delete_button.setIcon(icon9)
        self.equation_delete_button.setIconSize(QSize(24, 24))

        self.equation_options_grid_layout.addWidget(self.equation_delete_button, 2, 1, 1, 1)

        self.equation_edit_button = QPushButton(self.equation_options_widget)
        self.equation_edit_button.setObjectName(u"equation_edit_button")
        sizePolicy3.setHeightForWidth(self.equation_edit_button.sizePolicy().hasHeightForWidth())
        self.equation_edit_button.setSizePolicy(sizePolicy3)
        icon17 = QIcon()
        icon17.addFile(u":/icon/Images/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.equation_edit_button.setIcon(icon17)
        self.equation_edit_button.setIconSize(QSize(24, 24))

        self.equation_options_grid_layout.addWidget(self.equation_edit_button, 1, 1, 1, 1)


        self.horizontalLayout_10.addLayout(self.equation_options_grid_layout)


        self.horizontalLayout_2.addWidget(self.equation_options_widget)


        self.verticalLayout_8.addWidget(self.equation_widget)

        self.method_equation_widget = QWidget(self.equations_page)
        self.method_equation_widget.setObjectName(u"method_equation_widget")
        self.horizontalLayout_11 = QHBoxLayout(self.method_equation_widget)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.method_equation_tab_widget = QTabWidget(self.method_equation_widget)
        self.method_equation_tab_widget.setObjectName(u"method_equation_tab_widget")
        self.method_equation_tab_widget.setFont(font3)
        self.bisection_tab = QWidget()
        self.bisection_tab.setObjectName(u"bisection_tab")
        self.verticalLayout_10 = QVBoxLayout(self.bisection_tab)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 0, 5, 9)
        self.bisection_config_widget = QWidget(self.bisection_tab)
        self.bisection_config_widget.setObjectName(u"bisection_config_widget")
        self.bisection_config_widget.setMaximumSize(QSize(16777215, 16777215))
        font9 = QFont()
        font9.setPointSize(9)
        font9.setKerning(True)
        self.bisection_config_widget.setFont(font9)
        self.verticalLayout_12 = QVBoxLayout(self.bisection_config_widget)
        self.verticalLayout_12.setSpacing(12)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 5, 0, 9)
        self.bisection_config_grid = QGridLayout()
        self.bisection_config_grid.setObjectName(u"bisection_config_grid")
        self.bisection_interval_b_label = QLabel(self.bisection_config_widget)
        self.bisection_interval_b_label.setObjectName(u"bisection_interval_b_label")
        self.bisection_interval_b_label.setFont(font2)
        self.bisection_interval_b_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.bisection_config_grid.addWidget(self.bisection_interval_b_label, 1, 0, 1, 1)

        self.bisection_interval_a_label = QLabel(self.bisection_config_widget)
        self.bisection_interval_a_label.setObjectName(u"bisection_interval_a_label")
        self.bisection_interval_a_label.setFont(font2)
        self.bisection_interval_a_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.bisection_config_grid.addWidget(self.bisection_interval_a_label, 0, 0, 1, 1)

        self.bisection_tolerance_label = QLabel(self.bisection_config_widget)
        self.bisection_tolerance_label.setObjectName(u"bisection_tolerance_label")
        self.bisection_tolerance_label.setFont(font2)
        self.bisection_tolerance_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.bisection_config_grid.addWidget(self.bisection_tolerance_label, 2, 0, 1, 1)

        self.bisection_interval_b_line_edit = QLineEdit(self.bisection_config_widget)
        self.bisection_interval_b_line_edit.setObjectName(u"bisection_interval_b_line_edit")
        font10 = QFont()
        font10.setPointSize(14)
        self.bisection_interval_b_line_edit.setFont(font10)
        self.bisection_interval_b_line_edit.setClearButtonEnabled(True)

        self.bisection_config_grid.addWidget(self.bisection_interval_b_line_edit, 1, 1, 1, 1)

        self.bisection_tolerance_line_edit = QLineEdit(self.bisection_config_widget)
        self.bisection_tolerance_line_edit.setObjectName(u"bisection_tolerance_line_edit")
        self.bisection_tolerance_line_edit.setFont(font10)
        self.bisection_tolerance_line_edit.setClearButtonEnabled(True)

        self.bisection_config_grid.addWidget(self.bisection_tolerance_line_edit, 2, 1, 1, 1)

        self.bisection_interval_a_line_edit = QLineEdit(self.bisection_config_widget)
        self.bisection_interval_a_line_edit.setObjectName(u"bisection_interval_a_line_edit")
        self.bisection_interval_a_line_edit.setFont(font10)
        self.bisection_interval_a_line_edit.setClearButtonEnabled(True)

        self.bisection_config_grid.addWidget(self.bisection_interval_a_line_edit, 0, 1, 1, 1)

        self.bisection_config_grid.setRowStretch(0, 1)
        self.bisection_config_grid.setRowStretch(1, 100)

        self.verticalLayout_12.addLayout(self.bisection_config_grid)


        self.verticalLayout_10.addWidget(self.bisection_config_widget, 0, Qt.AlignmentFlag.AlignTop)

        self.bisection_solution_button = QPushButton(self.bisection_tab)
        self.bisection_solution_button.setObjectName(u"bisection_solution_button")
        self.bisection_solution_button.setFont(font7)
        self.bisection_solution_button.setStyleSheet(u"QPushButton{\n"
"background-color: #3c4b84\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: #47599d;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: #4f63ae;\n"
"}")

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
        self.newton_config_widget.setFont(font5)
        self.verticalLayout_14 = QVBoxLayout(self.newton_config_widget)
        self.verticalLayout_14.setSpacing(12)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 5, 0, 9)
        self.newton_config_grid = QGridLayout()
        self.newton_config_grid.setObjectName(u"newton_config_grid")
        self.newton_max_iter_label = QLabel(self.newton_config_widget)
        self.newton_max_iter_label.setObjectName(u"newton_max_iter_label")
        self.newton_max_iter_label.setFont(font2)

        self.newton_config_grid.addWidget(self.newton_max_iter_label, 1, 0, 1, 1)

        self.newton_max_iter_line_edit = QLineEdit(self.newton_config_widget)
        self.newton_max_iter_line_edit.setObjectName(u"newton_max_iter_line_edit")
        self.newton_max_iter_line_edit.setFont(font10)
        self.newton_max_iter_line_edit.setClearButtonEnabled(True)

        self.newton_config_grid.addWidget(self.newton_max_iter_line_edit, 1, 1, 1, 1)

        self.newton_tolerance_label = QLabel(self.newton_config_widget)
        self.newton_tolerance_label.setObjectName(u"newton_tolerance_label")
        self.newton_tolerance_label.setFont(font2)
        self.newton_tolerance_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.newton_config_grid.addWidget(self.newton_tolerance_label, 2, 0, 1, 1)

        self.newton_tolerance_line_edit = QLineEdit(self.newton_config_widget)
        self.newton_tolerance_line_edit.setObjectName(u"newton_tolerance_line_edit")
        self.newton_tolerance_line_edit.setFont(font10)
        self.newton_tolerance_line_edit.setClearButtonEnabled(True)

        self.newton_config_grid.addWidget(self.newton_tolerance_line_edit, 2, 1, 1, 1)

        self.newton_x_value_label = QLabel(self.newton_config_widget)
        self.newton_x_value_label.setObjectName(u"newton_x_value_label")
        self.newton_x_value_label.setFont(font2)
        self.newton_x_value_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.newton_config_grid.addWidget(self.newton_x_value_label, 0, 0, 1, 1)

        self.newton_x_value_line_edit = QLineEdit(self.newton_config_widget)
        self.newton_x_value_line_edit.setObjectName(u"newton_x_value_line_edit")
        self.newton_x_value_line_edit.setFont(font10)
        self.newton_x_value_line_edit.setClearButtonEnabled(True)

        self.newton_config_grid.addWidget(self.newton_x_value_line_edit, 0, 1, 1, 1)

        self.newton_config_grid.setColumnStretch(0, 1)
        self.newton_config_grid.setColumnStretch(1, 100)

        self.verticalLayout_14.addLayout(self.newton_config_grid)


        self.verticalLayout_13.addWidget(self.newton_config_widget)

        self.newton_solution_button = QPushButton(self.newton_tab)
        self.newton_solution_button.setObjectName(u"newton_solution_button")
        self.newton_solution_button.setFont(font7)
        self.newton_solution_button.setStyleSheet(u"QPushButton{\n"
"background-color: #3c4b84\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: #47599d;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: #4f63ae;\n"
"}")

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
        self.false_position_config_widget.setFont(font9)
        self.verticalLayout_15 = QVBoxLayout(self.false_position_config_widget)
        self.verticalLayout_15.setSpacing(12)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 5, 0, 9)
        self.false_position_config_grid = QGridLayout()
        self.false_position_config_grid.setObjectName(u"false_position_config_grid")
        self.false_interval_b_label = QLabel(self.false_position_config_widget)
        self.false_interval_b_label.setObjectName(u"false_interval_b_label")
        self.false_interval_b_label.setFont(font2)
        self.false_interval_b_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.false_position_config_grid.addWidget(self.false_interval_b_label, 1, 0, 1, 1)

        self.false_interval_a_label = QLabel(self.false_position_config_widget)
        self.false_interval_a_label.setObjectName(u"false_interval_a_label")
        self.false_interval_a_label.setFont(font2)
        self.false_interval_a_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.false_position_config_grid.addWidget(self.false_interval_a_label, 0, 0, 1, 1)

        self.false_tolerance_label = QLabel(self.false_position_config_widget)
        self.false_tolerance_label.setObjectName(u"false_tolerance_label")
        self.false_tolerance_label.setFont(font2)
        self.false_tolerance_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.false_position_config_grid.addWidget(self.false_tolerance_label, 2, 0, 1, 1)

        self.false_interval_b_line_edit = QLineEdit(self.false_position_config_widget)
        self.false_interval_b_line_edit.setObjectName(u"false_interval_b_line_edit")
        self.false_interval_b_line_edit.setFont(font10)
        self.false_interval_b_line_edit.setClearButtonEnabled(True)

        self.false_position_config_grid.addWidget(self.false_interval_b_line_edit, 1, 1, 1, 1)

        self.false_tolerance_line_edit = QLineEdit(self.false_position_config_widget)
        self.false_tolerance_line_edit.setObjectName(u"false_tolerance_line_edit")
        self.false_tolerance_line_edit.setFont(font10)
        self.false_tolerance_line_edit.setClearButtonEnabled(True)

        self.false_position_config_grid.addWidget(self.false_tolerance_line_edit, 2, 1, 1, 1)

        self.false_interval_a_line_edit = QLineEdit(self.false_position_config_widget)
        self.false_interval_a_line_edit.setObjectName(u"false_interval_a_line_edit")
        self.false_interval_a_line_edit.setFont(font10)
        self.false_interval_a_line_edit.setClearButtonEnabled(True)

        self.false_position_config_grid.addWidget(self.false_interval_a_line_edit, 0, 1, 1, 1)

        self.false_position_config_grid.setColumnStretch(0, 1)
        self.false_position_config_grid.setColumnStretch(1, 100)

        self.verticalLayout_15.addLayout(self.false_position_config_grid)


        self.verticalLayout_16.addWidget(self.false_position_config_widget)

        self.false_solution_button = QPushButton(self.false_position_tab)
        self.false_solution_button.setObjectName(u"false_solution_button")
        self.false_solution_button.setFont(font7)
        self.false_solution_button.setStyleSheet(u"QPushButton{\n"
"background-color: #3c4b84\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: #47599d;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: #4f63ae;\n"
"}")

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
        self.secant_config_widget.setFont(font5)
        self.verticalLayout_17 = QVBoxLayout(self.secant_config_widget)
        self.verticalLayout_17.setSpacing(12)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 5, 0, 9)
        self.secant_config_grid = QGridLayout()
        self.secant_config_grid.setObjectName(u"secant_config_grid")
        self.secant_tolerance_label = QLabel(self.secant_config_widget)
        self.secant_tolerance_label.setObjectName(u"secant_tolerance_label")
        self.secant_tolerance_label.setFont(font2)
        self.secant_tolerance_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.secant_config_grid.addWidget(self.secant_tolerance_label, 3, 0, 1, 1)

        self.secant_max_iter_line_edit = QLineEdit(self.secant_config_widget)
        self.secant_max_iter_line_edit.setObjectName(u"secant_max_iter_line_edit")
        self.secant_max_iter_line_edit.setFont(font10)

        self.secant_config_grid.addWidget(self.secant_max_iter_line_edit, 2, 1, 1, 2)

        self.secant_xi_line_edit = QLineEdit(self.secant_config_widget)
        self.secant_xi_line_edit.setObjectName(u"secant_xi_line_edit")
        self.secant_xi_line_edit.setFont(font10)
        self.secant_xi_line_edit.setClearButtonEnabled(True)

        self.secant_config_grid.addWidget(self.secant_xi_line_edit, 1, 1, 1, 2)

        self.secant_x0_line_edit = QLineEdit(self.secant_config_widget)
        self.secant_x0_line_edit.setObjectName(u"secant_x0_line_edit")
        self.secant_x0_line_edit.setFont(font10)
        self.secant_x0_line_edit.setClearButtonEnabled(True)

        self.secant_config_grid.addWidget(self.secant_x0_line_edit, 0, 1, 1, 2)

        self.secant_x0_label = QLabel(self.secant_config_widget)
        self.secant_x0_label.setObjectName(u"secant_x0_label")
        self.secant_x0_label.setFont(font2)
        self.secant_x0_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.secant_config_grid.addWidget(self.secant_x0_label, 0, 0, 1, 1)

        self.secant_max_iter_label = QLabel(self.secant_config_widget)
        self.secant_max_iter_label.setObjectName(u"secant_max_iter_label")
        self.secant_max_iter_label.setFont(font2)
        self.secant_max_iter_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.secant_config_grid.addWidget(self.secant_max_iter_label, 2, 0, 1, 1)

        self.secant_xi_label = QLabel(self.secant_config_widget)
        self.secant_xi_label.setObjectName(u"secant_xi_label")
        self.secant_xi_label.setFont(font2)
        self.secant_xi_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.secant_config_grid.addWidget(self.secant_xi_label, 1, 0, 1, 1)

        self.secant_tolerance_line_edit = QLineEdit(self.secant_config_widget)
        self.secant_tolerance_line_edit.setObjectName(u"secant_tolerance_line_edit")
        self.secant_tolerance_line_edit.setFont(font10)

        self.secant_config_grid.addWidget(self.secant_tolerance_line_edit, 3, 1, 1, 2)

        self.secant_config_grid.setColumnStretch(0, 1)
        self.secant_config_grid.setColumnStretch(1, 10)

        self.verticalLayout_17.addLayout(self.secant_config_grid)


        self.verticalLayout_18.addWidget(self.secant_config_widget)

        self.secant_solution_button = QPushButton(self.secant_tab)
        self.secant_solution_button.setObjectName(u"secant_solution_button")
        self.secant_solution_button.setFont(font7)
        self.secant_solution_button.setStyleSheet(u"QPushButton{\n"
"background-color: #3c4b84\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: #47599d;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: #4f63ae;\n"
"}")

        self.verticalLayout_18.addWidget(self.secant_solution_button)

        self.secant_spacer = QSpacerItem(20, 255, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.secant_spacer)

        self.method_equation_tab_widget.addTab(self.secant_tab, "")

        self.horizontalLayout_11.addWidget(self.method_equation_tab_widget)

        self.graphic_widget = QWidget(self.method_equation_widget)
        self.graphic_widget.setObjectName(u"graphic_widget")
        self.verticalLayout_9 = QVBoxLayout(self.graphic_widget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.graphic_label = QLabel(self.graphic_widget)
        self.graphic_label.setObjectName(u"graphic_label")
        self.graphic_label.setFont(font3)
        self.graphic_label.setStyleSheet(u"padding: 3px")
        self.graphic_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.graphic_label, 0, Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_11.addWidget(self.graphic_widget)

        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 1)

        self.verticalLayout_8.addWidget(self.method_equation_widget)

        self.verticalLayout_8.setStretch(0, 10)
        self.verticalLayout_8.setStretch(1, 100)
        self.main_stacked_widget.addWidget(self.equations_page)
        self.information_page = QWidget()
        self.information_page.setObjectName(u"information_page")
        self.verticalLayout_22 = QVBoxLayout(self.information_page)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.information_label = QLabel(self.information_page)
        self.information_label.setObjectName(u"information_label")
        self.information_label.setTextFormat(Qt.TextFormat.RichText)
        self.information_label.setWordWrap(True)

        self.verticalLayout_22.addWidget(self.information_label, 0, Qt.AlignmentFlag.AlignTop)

        self.compiled_label = QLabel(self.information_page)
        self.compiled_label.setObjectName(u"compiled_label")
        self.compiled_label.setMaximumSize(QSize(16777215, 32))
        self.compiled_label.setFont(font2)
        self.compiled_label.setScaledContents(True)

        self.verticalLayout_22.addWidget(self.compiled_label, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignBottom)

        self.main_stacked_widget.addWidget(self.information_page)

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
        self.export_button.setToolTip(QCoreApplication.translate("MainWindow", u"Exportar matriz actual", None))
#endif // QT_CONFIG(tooltip)
        self.export_button.setText(QCoreApplication.translate("MainWindow", u"Exportar matriz", None))
#if QT_CONFIG(tooltip)
        self.import_button.setToolTip(QCoreApplication.translate("MainWindow", u"Importar matriz en formato CSV", None))
#endif // QT_CONFIG(tooltip)
        self.import_button.setText(QCoreApplication.translate("MainWindow", u"Importar matriz", None))
#if QT_CONFIG(tooltip)
        self.information_button.setToolTip(QCoreApplication.translate("MainWindow", u"Informaci\u00f3n", None))
#endif // QT_CONFIG(tooltip)
        self.information_button.setText(QCoreApplication.translate("MainWindow", u"Informaci\u00f3n", None))
#if QT_CONFIG(tooltip)
        self.row_spinbox_label.setToolTip(QCoreApplication.translate("MainWindow", u"Filas de la matriz", None))
#endif // QT_CONFIG(tooltip)
        self.row_spinbox_label.setText(QCoreApplication.translate("MainWindow", u"Filas", None))
#if QT_CONFIG(tooltip)
        self.column_spinbox_label.setToolTip(QCoreApplication.translate("MainWindow", u"Columnas de la matriz", None))
#endif // QT_CONFIG(tooltip)
        self.column_spinbox_label.setText(QCoreApplication.translate("MainWindow", u"Columnas", None))
#if QT_CONFIG(tooltip)
        self.table_resize_checkbox.setToolTip(QCoreApplication.translate("MainWindow", u"Redimensionar autom\u00e1ticamente", None))
#endif // QT_CONFIG(tooltip)
        self.table_resize_checkbox.setText(QCoreApplication.translate("MainWindow", u"Autoescala", None))
        self.select_table_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"Seleccionar matriz", None))

#if QT_CONFIG(tooltip)
        self.save_current_table_button.setToolTip(QCoreApplication.translate("MainWindow", u"Guardar matriz actual", None))
#endif // QT_CONFIG(tooltip)
        self.save_current_table_button.setText("")
#if QT_CONFIG(tooltip)
        self.change_current_table_button.setToolTip(QCoreApplication.translate("MainWindow", u"Cambiar matriz seleccionada", None))
#endif // QT_CONFIG(tooltip)
        self.change_current_table_button.setText("")
#if QT_CONFIG(tooltip)
        self.delete_current_table_button.setToolTip(QCoreApplication.translate("MainWindow", u"Eliminar matriz", None))
#endif // QT_CONFIG(tooltip)
        self.delete_current_table_button.setText("")
        self.table_select_solutions_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"Resolver por", None))
        self.table_select_solutions_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"Reducci\u00f3n", None))
        self.table_select_solutions_combobox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cramer", None))

#if QT_CONFIG(tooltip)
        self.table_select_solutions_combobox.setToolTip(QCoreApplication.translate("MainWindow", u"Seleccionar m\u00e9todo para resolver", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.table_solve_button.setToolTip(QCoreApplication.translate("MainWindow", u"Solucionar matriz", None))
#endif // QT_CONFIG(tooltip)
        self.table_solve_button.setText(QCoreApplication.translate("MainWindow", u"Resolver", None))
#if QT_CONFIG(tooltip)
        self.table_vector_button.setToolTip(QCoreApplication.translate("MainWindow", u"Operaciones con matrices", None))
#endif // QT_CONFIG(tooltip)
        self.table_vector_button.setText("")
#if QT_CONFIG(tooltip)
        self.table_invert_button.setToolTip(QCoreApplication.translate("MainWindow", u"Obtener matriz invertida", None))
#endif // QT_CONFIG(tooltip)
        self.table_invert_button.setText(QCoreApplication.translate("MainWindow", u"Invertir", None))
#if QT_CONFIG(tooltip)
        self.table_transpose_button.setToolTip(QCoreApplication.translate("MainWindow", u"Transponer matriz", None))
#endif // QT_CONFIG(tooltip)
        self.table_transpose_button.setText("")
#if QT_CONFIG(tooltip)
        self.table_determinant_button.setToolTip(QCoreApplication.translate("MainWindow", u"Obtener determinante de la matriz", None))
#endif // QT_CONFIG(tooltip)
        self.table_determinant_button.setText(QCoreApplication.translate("MainWindow", u"Determinante", None))
#if QT_CONFIG(tooltip)
        self.table_update_button.setToolTip(QCoreApplication.translate("MainWindow", u"Actualizar tama\u00f1o", None))
#endif // QT_CONFIG(tooltip)
        self.table_update_button.setText("")
#if QT_CONFIG(tooltip)
        self.coeficient_label.setToolTip(QCoreApplication.translate("MainWindow", u"Matriz de coeficientes", None))
#endif // QT_CONFIG(tooltip)
        self.coeficient_label.setText(QCoreApplication.translate("MainWindow", u"Matriz de coeficientes", None))
#if QT_CONFIG(tooltip)
        self.adjust_coeficient_matrix_button.setToolTip(QCoreApplication.translate("MainWindow", u"Ajustar tama\u00f1o", None))
#endif // QT_CONFIG(tooltip)
        self.adjust_coeficient_matrix_button.setText("")
#if QT_CONFIG(tooltip)
        self.random_matrix_button.setToolTip(QCoreApplication.translate("MainWindow", u"Llenar espacios vac\u00edos de la matriz con n\u00fameros aleatorios", None))
#endif // QT_CONFIG(tooltip)
        self.random_matrix_button.setText("")
#if QT_CONFIG(tooltip)
        self.clean_coeficient_matrix_button.setToolTip(QCoreApplication.translate("MainWindow", u"Limpiar matriz de coeficientes", None))
#endif // QT_CONFIG(tooltip)
        self.clean_coeficient_matrix_button.setText("")
#if QT_CONFIG(tooltip)
        self.fill_0_coeficient_matrix_button.setToolTip(QCoreApplication.translate("MainWindow", u"Rellenar Espacios con cero", None))
#endif // QT_CONFIG(tooltip)
        self.fill_0_coeficient_matrix_button.setText("")
        ___qtablewidgetitem = self.coeficient_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"X1", None));
        ___qtablewidgetitem1 = self.coeficient_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"X2", None));
        ___qtablewidgetitem2 = self.coeficient_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"b", None));

        __sortingEnabled = self.coeficient_table.isSortingEnabled()
        self.coeficient_table.setSortingEnabled(False)
        self.coeficient_table.setSortingEnabled(__sortingEnabled)

#if QT_CONFIG(tooltip)
        self.coeficient_table.setToolTip(QCoreApplication.translate("MainWindow", u"Matriz de coeficientes", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.independent_terms_label.setToolTip(QCoreApplication.translate("MainWindow", u"T\u00e9rminos independientes", None))
#endif // QT_CONFIG(tooltip)
        self.independent_terms_label.setText(QCoreApplication.translate("MainWindow", u"Independientes", None))
#if QT_CONFIG(tooltip)
        self.clean_independent_matrix_button.setToolTip(QCoreApplication.translate("MainWindow", u"Limpiar matriz de coeficientes", None))
#endif // QT_CONFIG(tooltip)
        self.clean_independent_matrix_button.setText("")
#if QT_CONFIG(tooltip)
        self.random_independent_matrix_button.setToolTip(QCoreApplication.translate("MainWindow", u"Llenar espacios vac\u00edos con n\u00fameros aleatorios", None))
#endif // QT_CONFIG(tooltip)
        self.random_independent_matrix_button.setText("")
#if QT_CONFIG(tooltip)
        self.adjust_independent_matrix_button.setToolTip(QCoreApplication.translate("MainWindow", u"Ajustar tama\u00f1o", None))
#endif // QT_CONFIG(tooltip)
        self.adjust_independent_matrix_button.setText("")
#if QT_CONFIG(tooltip)
        self.zero_independent_matrix_button.setToolTip(QCoreApplication.translate("MainWindow", u"Rellenar espacios con cero", None))
#endif // QT_CONFIG(tooltip)
        self.zero_independent_matrix_button.setText("")
        ___qtablewidgetitem3 = self.independent_terms_table.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"b", None));
        ___qtablewidgetitem4 = self.independent_terms_table.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Nueva fila", None));

        __sortingEnabled1 = self.independent_terms_table.isSortingEnabled()
        self.independent_terms_table.setSortingEnabled(False)
        self.independent_terms_table.setSortingEnabled(__sortingEnabled1)

#if QT_CONFIG(tooltip)
        self.independent_terms_table.setToolTip(QCoreApplication.translate("MainWindow", u"T\u00e9rminos independientes", None))
#endif // QT_CONFIG(tooltip)
        self.equation_derivative_label.setText("")
#if QT_CONFIG(tooltip)
        self.equation_text_label.setToolTip(QCoreApplication.translate("MainWindow", u"Ecuaci\u00f3n actual", None))
#endif // QT_CONFIG(tooltip)
        self.equation_text_label.setText(QCoreApplication.translate("MainWindow", u"Ecuacion", None))
        self.equation_label.setText("")
#if QT_CONFIG(tooltip)
        self.equation_integral_text_label.setToolTip(QCoreApplication.translate("MainWindow", u"Derivada de la ecuaci\u00f3n actual", None))
#endif // QT_CONFIG(tooltip)
        self.equation_integral_text_label.setText(QCoreApplication.translate("MainWindow", u"Derivada", None))
        self.select_equation_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"Seleccionar ecuaci\u00f3n", None))

#if QT_CONFIG(tooltip)
        self.select_equation_combobox.setToolTip(QCoreApplication.translate("MainWindow", u"Seleccionar ecuaci\u00f3n", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.equation_save_button.setToolTip(QCoreApplication.translate("MainWindow", u"Guardar ecuaci\u00f3n", None))
#endif // QT_CONFIG(tooltip)
        self.equation_save_button.setText("")
#if QT_CONFIG(tooltip)
        self.equation_load_button.setToolTip(QCoreApplication.translate("MainWindow", u"Cargar ecuaci\u00f3n", None))
#endif // QT_CONFIG(tooltip)
        self.equation_load_button.setText("")
#if QT_CONFIG(tooltip)
        self.equation_delete_button.setToolTip(QCoreApplication.translate("MainWindow", u"Eliminar ecuaci\u00f3n", None))
#endif // QT_CONFIG(tooltip)
        self.equation_delete_button.setText("")
#if QT_CONFIG(tooltip)
        self.equation_edit_button.setToolTip(QCoreApplication.translate("MainWindow", u"Editar ecuaci\u00f3n", None))
#endif // QT_CONFIG(tooltip)
        self.equation_edit_button.setText("")
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
        self.graphic_label.setText(QCoreApplication.translate("MainWindow", u"Gr\u00e1fica de ecuaci\u00f3n", None))
        self.information_label.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<h1 style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; font-weight:700;\">Calculadora de \u00e1lgebra lineal - Algebrier</span></h1>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:700;\">Creadores</span></h2>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px"
                        "; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Johan Enrique Reyes Rojas</span></li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Karen Mariza Rosa Yolanda Fonseca Vega</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Oscar Enrrique Arnuero Ramos</li></ul>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700;\">Prop\u00f3sito</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px"
                        "; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Esta calculadora ha sido dise\u00f1ada para asistir en la </span><span style=\" font-size:12pt; font-weight:700;\">resoluci\u00f3n</span><span style=\" font-size:12pt;\"> de </span><span style=\" font-size:12pt; font-weight:700;\">problemas</span><span style=\" font-size:12pt;\"> relacionados con el </span><span style=\" font-size:12pt; font-weight:700;\">\u00e1lgebra</span><span style=\" font-size:12pt;\"> </span><span style=\" font-size:12pt; font-weight:700;\">lineal</span><span style=\" font-size:12pt;\">, facilitando c\u00e1lculos complejos de manera eficiente y precisa. Algunas de las funcionalidades clave incluyen:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Resoluci"
                        "\u00f3n de sistemas de ecuaciones</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Operaciones con matrices</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Ra\u00edces de ecuaciones</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Graficadora de ecuaciones</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">C\u00e1lculo de determinante y matriz inversa</li></ul>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom"
                        ":0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Si necesitas ayuda, comun\u00edcate con nosotros con el siguiente correo: </span><a href=\"mailto:rrojas1enrique@gmail.com\"><span style=\" font-size:12pt; text-decoration: underline; color:#0078d7;\">rrojas1enrique@gmail.com</span></a><span style=\" font-size:12pt;\"> </span></p></body></html>", None))
        self.compiled_label.setText(QCoreApplication.translate("MainWindow", u"Compilado el 4 de Diciembre de 2024", None))
    # retranslateUi

