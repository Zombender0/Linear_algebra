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
    def setupUi(self, main_widget):
        if not main_widget.objectName():
            main_widget.setObjectName(u"main_widget")
        main_widget.resize(472, 362)
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

        self.step_label = QLabel(self.options_tab_widget)
        self.step_label.setObjectName(u"step_label")
        self.step_label.setStyleSheet(u"border-radius:6px;\n"
"font: 700 9pt \"Calibri\";")

        self.options_tab_horizontal_layout.addWidget(self.step_label, 0, Qt.AlignmentFlag.AlignHCenter)

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
        self.p1 = QWidget()
        self.p1.setObjectName(u"p1")
        self.verticalLayout = QVBoxLayout(self.p1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.s_table = QTableWidget(self.p1)
        if (self.s_table.columnCount() < 3):
            self.s_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.s_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.s_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.s_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.s_table.rowCount() < 3):
            self.s_table.setRowCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.s_table.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.s_table.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.s_table.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.s_table.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.s_table.setItem(1, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.s_table.setItem(2, 2, __qtablewidgetitem8)
        self.s_table.setObjectName(u"s_table")

        self.verticalLayout.addWidget(self.s_table)

        self.solution_list = QTextEdit(self.p1)
        self.solution_list.setObjectName(u"solution_list")

        self.verticalLayout.addWidget(self.solution_list)

        self.tabWidget.addTab(self.p1, "")

        self.main_widget_vertical_layout.addWidget(self.tabWidget)

        self.main_widget_vertical_layout.setStretch(0, 1)
        self.main_widget_vertical_layout.setStretch(1, 10)

        self.retranslateUi(main_widget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(main_widget)
    # setupUi

    def retranslateUi(self, main_widget):
        main_widget.setWindowTitle(QCoreApplication.translate("main_widget", u"Soluci\u00f3n", None))
        self.back_tab_button.setText("")
        self.step_label.setText(QCoreApplication.translate("main_widget", u"Procedimiento", None))
        self.next_tab_button.setText("")
        ___qtablewidgetitem = self.s_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("main_widget", u"Nueva columna", None));
        ___qtablewidgetitem1 = self.s_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("main_widget", u"Nueva columna", None));
        ___qtablewidgetitem2 = self.s_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("main_widget", u"Nueva columna", None));
        ___qtablewidgetitem3 = self.s_table.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("main_widget", u"Nueva fila", None));
        ___qtablewidgetitem4 = self.s_table.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("main_widget", u"Nueva fila", None));
        ___qtablewidgetitem5 = self.s_table.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("main_widget", u"Nueva fila", None));

        __sortingEnabled = self.s_table.isSortingEnabled()
        self.s_table.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.s_table.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("main_widget", u"magic", None));
        ___qtablewidgetitem7 = self.s_table.item(1, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("main_widget", u"is", None));
        ___qtablewidgetitem8 = self.s_table.item(2, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("main_widget", u"awesome", None));
        self.s_table.setSortingEnabled(__sortingEnabled)

        self.solution_list.setHtml(QCoreApplication.translate("main_widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.p1), QCoreApplication.translate("main_widget", u"p1", None))
    # retranslateUi

