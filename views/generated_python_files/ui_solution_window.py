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
        icon.addFile(u":/icon/Images/grid.ico", QSize(), QIcon.Normal, QIcon.Off)
        main_widget.setWindowIcon(icon)
        main_widget.setStyleSheet(u"*{\n"
"background-color: #d3d3d3;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"}\n"
"\n"
"#Main_widget{\n"
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
"font: 700 13pt \"Calibri\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"background-color: #819299; \n"
"gridline-color: #fff;  \n"
"color:#fff\n"
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
"background-color: #85939"
                        "a;\n"
"}\n"
"QTableWidget::item::hover{\n"
"background-color: #B6BEC2\n"
"}\n"
"\n"
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
"QListWidget{\n"
"background: #F1F1F1;\n"
"border : none\n"
"}\n"
"QListWidget::item{\n"
"margin: 0px;\n"
"color: #fff;\n"
"}\n"
"#tabWidget QWidget{\n"
"background-color: #85939a\n"
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