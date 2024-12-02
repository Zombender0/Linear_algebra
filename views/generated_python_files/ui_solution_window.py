# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'solution_windowzOsJra.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)
from views.qt_files.qrc_files import resources_rc

class Ui_main_widget(object):
    def setupUi(self, main_widget:QWidget):
        if not main_widget.objectName():
            main_widget.setObjectName(u"main_widget")
        main_widget.resize(600, 450)
        icon = QIcon()
        icon.addFile(u":/icon/Images/ico.ico", QSize(), QIcon.Normal, QIcon.Off)
        main_widget.setWindowIcon(icon)
        main_widget.setStyleSheet(u"*{\n"
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
"\n"
"QTabWidget:pane{\n"
"background-color: #2c313c\n"
"}\n"
"\n"
"#main_widget{\n"
"background: #2c313c\n"
"}\n"
"\n"
"QPushButton{\n"
"color: #ffffff;\n"
"    text-align: center;\n"
"	padding: 3px;\n"
"    border-radius: 10px;\n"
"    background-color: #16191d;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #2a2e35;\n"
"border-color: #454a52;\n"
"}\n"
" QPushButton:pressed {\n"
"background-color: #1d2127;\n"
"	font-weight: 350;\n"
"}\n"
"QLabel {\n"
"background-color: #1f232a;\n"
"padding: 3px;\n"
"font-weight: 700;\n"
"border-radius: 7px;\n"
"font-weight: 400;\n"
"}\n"
"\n"
"#tabWidget QWidget{\n"
"background-color: #3e4555;\n"
"}\n"
"QTableWidget {\n"
"background-color: #3e4555;\n"
"gridline-color: #fff;\n"
"}\n"
"\n"
"QHeaderView{\n"
"background-color: #3e4555;\n"
"color: #fff;\n"
""
                        "}\n"
"\n"
"QHeaderView::section {\n"
"background-color: #3e4555;\n"
"color: #fff;\n"
"}\n"
"QTableCornerButton::section {\n"
"background-color: #3e4555;\n"
"color: #fff;\n"
"}\n"
"QTableWidget::item{\n"
"color: #fff;\n"
"}\n"
"QTableWidget::item::hover{\n"
"background-color: #242831;\n"
"font-weight: 700;\n"
"}\n"
"\n"
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
"background-color: #3e4555;\n"
"border : none\n"
"}\n"
"QListWidget::item{\n"
"margin: 0px;\n"
"color: #fff;\n"
"}\n"
"\n"
"QTabBar::tab{\n"
"background-color: #16191d;\n"
"color: white;\n"
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
        self.label.setMaximumSize(QSize(16777215, 40))
        self.label.setStyleSheet(u"border-radius:6px;\n"
"font: 700 13pt \"Calibri\";")
    
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

        self.tab_widget = QTabWidget(main_widget)
        self.tab_widget.setObjectName(u"tabWidget")

        self.main_widget_vertical_layout.addWidget(self.tab_widget)

        self.main_widget_vertical_layout.setStretch(0, 1)
        self.main_widget_vertical_layout.setStretch(1, 10)

        self.retranslateUi(main_widget)

        QMetaObject.connectSlotsByName(main_widget)

    def retranslateUi(self, main_widget):
        main_widget.setWindowTitle(QCoreApplication.translate("main_widget", u"Solución", None))
        self.back_tab_button.setText("")
        self.label.setText(QCoreApplication.translate("main_widget", u"Procedimiento", None))
        self.next_tab_button.setText("")