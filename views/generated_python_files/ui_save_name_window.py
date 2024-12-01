# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'save_name_windowRlnPtF.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
from views.qt_files.qrc_files import resources_rc

class Ui_save_dialog(object):
    def setupUi(self, save_dialog):
        if not save_dialog.objectName():
            save_dialog.setObjectName(u"save_dialog")
        save_dialog.resize(434, 108)
        icon = QIcon()
        icon.addFile(u":/icon/Images/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        save_dialog.setWindowIcon(icon)
        save_dialog.setStyleSheet(u"*{\n"
"border:none;\n"
"background-color: transparent;\n"
"background: none;\n"
"padding: 0;\n"
"margin: 0;\n"
"color: #fff;\n"
"}\n"
"\n"
"#save_dialog{\n"
"background-color: #2c313c\n"
"}\n"
"\n"
"QLineEdit{\n"
"color: #fff;\n"
"background-color: #596379;\n"
"border-radius:10px;\n"
"font-weight: 350;\n"
"}\n"
"\n"
"#save_dialog QPushButton{\n"
"color: #ffffff;\n"
"text-align: center;\n"
"padding:2px;\n"
"border-radius: 10px;\n"
"background-color: #16191d;\n"
"}\n"
"\n"
"#save_dialog QPushButton::hover{\n"
"background-color: #202328;\n"
"border-color: #454a52;\n"
"}\n"
"\n"
"#save_dialog QPushButton::pressed{\n"
"background-color: #1d2127;\n"
"}")
        self.verticalLayout = QVBoxLayout(save_dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(save_dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.main_line_edit = QLineEdit(save_dialog)
        self.main_line_edit.setObjectName(u"main_line_edit")
        self.main_line_edit.setFont(font)

        self.verticalLayout.addWidget(self.main_line_edit)

        self.buttons_widget = QWidget(save_dialog)
        self.buttons_widget.setObjectName(u"buttons_widget")
        self.horizontalLayout = QHBoxLayout(self.buttons_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.accept_button = QPushButton(self.buttons_widget)
        self.accept_button.setObjectName(u"accept_button")
        font1 = QFont()
        font1.setPointSize(11)
        self.accept_button.setFont(font1)

        self.horizontalLayout.addWidget(self.accept_button)

        self.cancel_button = QPushButton(self.buttons_widget)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setFont(font1)

        self.horizontalLayout.addWidget(self.cancel_button)


        self.verticalLayout.addWidget(self.buttons_widget, 0, Qt.AlignmentFlag.AlignRight)


        self.retranslateUi(save_dialog)

        QMetaObject.connectSlotsByName(save_dialog)
    # setupUi

    def retranslateUi(self, save_dialog):
        save_dialog.setWindowTitle(QCoreApplication.translate("save_dialog", u"Guardar", None))
        self.label.setText(QCoreApplication.translate("save_dialog", u"Ingresar nombre de matriz", None))
        self.accept_button.setText(QCoreApplication.translate("save_dialog", u"Aceptar", None))
        self.cancel_button.setText(QCoreApplication.translate("save_dialog", u"Cancelar", None))
    # retranslateUi

