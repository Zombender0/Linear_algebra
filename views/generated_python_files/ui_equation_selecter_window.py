# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'equation_selecter_windowLNxlPI.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

from PySide6.QtSvg import QtSvg
from views.qt_files.qrc_files import resources_rc

class Ui_insert_equation_dialog(object):
    def setupUi(self, insert_equation_dialog):
        if not insert_equation_dialog.objectName():
            insert_equation_dialog.setObjectName(u"insert_equation_dialog")
        icon = QIcon()
        icon.addFile(u":/icon/Images/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        insert_equation_dialog.setWindowIcon(icon)
        insert_equation_dialog.resize(425, 356)
        insert_equation_dialog.setStyleSheet(u"#insert_equation_dialog{\n"
"background-color: #2c313c\n"
"}\n"
"\n"
"#equation_buttons QPushButton,#options_widget QPushButton{\n"
"color: #ffffff;\n"
"text-align: center;\n"
"padding:2px;\n"
"border-radius: 10px;\n"
"background-color: #16191d;\n"
"}\n"
"\n"
"#equation_buttons QPushButton::hover{\n"
"background-color: #2a2e35;\n"
"border-color: #454a52;\n"
"}\n"
"\n"
"#equation_buttons QPushButton::pressed, #options_widget QPushButton::pressed{\n"
"background-color: #1d2127;\n"
"}\n"
"\n"
"#equation_visualizer_widget QLineEdit{\n"
"color: #fff;\n"
"background-color: #596379;\n"
"border-radius:10px;\n"
"padding: 2px;\n"
"font-weight: 350;\n"
"}\n"
"\n"
"#equation_visualizer_widget QLabel{\n"
"color: #fff;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#options_widget QPushButton{\n"
"padding: 6px;\n"
"font-weight: 450;\n"
"}\n"
"\n"
"#options_widget QPushButton::hover{\n"
"color: #58a0a7;\n"
"background-color: #21252a;\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout_2 = QVBoxLayout(insert_equation_dialog)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 5, 0)
        self.equation_visualizer_widget = QWidget(insert_equation_dialog)
        self.equation_visualizer_widget.setObjectName(u"equation_visualizer_widget")
        self.verticalLayout = QVBoxLayout(self.equation_visualizer_widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.equation_label_widget = QWidget(self.equation_visualizer_widget)
        self.equation_label_widget.setObjectName(u"equation_label_widget")
        self.horizontalLayout = QHBoxLayout(self.equation_label_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.equation_label = QLabel(self.equation_label_widget)
        self.equation_label.setObjectName(u"equation_label")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setStyleStrategy(QFont.PreferDefault)
        font.setHintingPreference(QFont.PreferDefaultHinting)
        self.equation_label.setFont(font)
        self.equation_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.equation_label.setTextFormat(Qt.TextFormat.RichText)
        self.equation_label.setScaledContents(True)
        self.equation_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.equation_label.setIndent(-1)

        self.horizontalLayout.addWidget(self.equation_label, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout.addWidget(self.equation_label_widget)

        self.equation_line_edit_widget = QWidget(self.equation_visualizer_widget)
        self.equation_line_edit_widget.setObjectName(u"equation_line_edit_widget")
        self.horizontalLayout_2 = QHBoxLayout(self.equation_line_edit_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.equation_line_edit = QLineEdit(self.equation_line_edit_widget)
        self.equation_line_edit.setObjectName(u"equation_line_edit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equation_line_edit.sizePolicy().hasHeightForWidth())
        self.equation_line_edit.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(14)
        self.equation_line_edit.setFont(font1)

        self.horizontalLayout_2.addWidget(self.equation_line_edit)


        self.verticalLayout.addWidget(self.equation_line_edit_widget)


        self.verticalLayout_2.addWidget(self.equation_visualizer_widget)

        self.equation_buttons = QWidget(insert_equation_dialog)
        self.equation_buttons.setObjectName(u"equation_buttons")
        self.verticalLayout_3 = QVBoxLayout(self.equation_buttons)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.buttons_grid_layout = QGridLayout()
        self.buttons_grid_layout.setSpacing(10)
        self.buttons_grid_layout.setObjectName(u"buttons_grid_layout")
        self.buttons_grid_layout.setContentsMargins(-1, -1, -1, 0)
        self.x_to_n_button = QPushButton(self.equation_buttons)
        self.x_to_n_button.setObjectName(u"x_to_n_button")
        self.x_to_n_button.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icon/Images/x_to_2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.x_to_n_button.setIcon(icon)
        self.x_to_n_button.setIconSize(QSize(24, 24))

        self.buttons_grid_layout.addWidget(self.x_to_n_button, 0, 0, 1, 1)

        self.sin_button = QPushButton(self.equation_buttons)
        self.sin_button.setObjectName(u"sin_button")
        self.sin_button.setFont(font1)

        self.buttons_grid_layout.addWidget(self.sin_button, 1, 1, 1, 1)

        self.tan_button = QPushButton(self.equation_buttons)
        self.tan_button.setObjectName(u"tan_button")
        self.tan_button.setFont(font1)

        self.buttons_grid_layout.addWidget(self.tan_button, 2, 1, 1, 1)

        self.pi_button = QPushButton(self.equation_buttons)
        self.pi_button.setObjectName(u"pi_button")
        self.pi_button.setFont(font1)

        self.buttons_grid_layout.addWidget(self.pi_button, 2, 0, 1, 1)

        self.cos_button = QPushButton(self.equation_buttons)
        self.cos_button.setObjectName(u"cos_button")
        self.cos_button.setFont(font1)

        self.buttons_grid_layout.addWidget(self.cos_button, 0, 1, 1, 1)

        self.e_button = QPushButton(self.equation_buttons)
        self.e_button.setObjectName(u"e_button")
        self.e_button.setFont(font1)
        self.e_button.setIconSize(QSize(24, 24))

        self.buttons_grid_layout.addWidget(self.e_button, 1, 0, 1, 1)

        self.sqrt_button = QPushButton(self.equation_buttons)
        self.sqrt_button.setObjectName(u"sqrt_button")
        self.sqrt_button.setFont(font1)
 
        self.buttons_grid_layout.addWidget(self.sqrt_button, 3, 0, 1, 2)


        self.verticalLayout_3.addLayout(self.buttons_grid_layout)


        self.verticalLayout_2.addWidget(self.equation_buttons)

        self.options_widget = QWidget(insert_equation_dialog)
        self.options_widget.setObjectName(u"options_widget")
        self.horizontalLayout_3 = QHBoxLayout(self.options_widget)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.apply_button = QPushButton(self.options_widget)
        self.apply_button.setObjectName(u"apply_button")

        self.horizontalLayout_3.addWidget(self.apply_button)

        self.accept_button = QPushButton(self.options_widget)
        self.accept_button.setObjectName(u"accept_button")

        self.horizontalLayout_3.addWidget(self.accept_button)

        self.cancel_button = QPushButton(self.options_widget)
        self.cancel_button.setObjectName(u"cancel_button")
  
        self.horizontalLayout_3.addWidget(self.cancel_button)


        self.verticalLayout_2.addWidget(self.options_widget, 0, Qt.AlignmentFlag.AlignRight)

        self.verticalLayout_2.setStretch(0, 10)
        self.verticalLayout_2.setStretch(1, 8)
        self.verticalLayout_2.setStretch(2, 4)

#if QT_CONFIG(shortcut)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(insert_equation_dialog)
        QMetaObject.connectSlotsByName(insert_equation_dialog)
    # setupUi

    def retranslateUi(self, insert_equation_dialog):
        insert_equation_dialog.setWindowTitle(QCoreApplication.translate("insert_equation_dialog", u"Dialog", None))
        self.equation_label.setText("")
        self.equation_line_edit.setPlaceholderText(QCoreApplication.translate("insert_equation_dialog", u"Insertar ecuaci\u00f3n", None))
        self.x_to_n_button.setText("")
        self.sin_button.setText(QCoreApplication.translate("insert_equation_dialog", u"sen()", None))
        self.tan_button.setText(QCoreApplication.translate("insert_equation_dialog", u"tan()", None))
        self.pi_button.setText(QCoreApplication.translate("insert_equation_dialog", u"\u03c0", None))
        self.cos_button.setText(QCoreApplication.translate("insert_equation_dialog", u"cos()", None))
        self.e_button.setText(QCoreApplication.translate("insert_equation_dialog", u"e", None))
        self.sqrt_button.setText(QCoreApplication.translate("insert_equation_dialog", u"\u221a", None))
        self.apply_button.setText(QCoreApplication.translate("insert_equation_dialog", u"Aplicar", None))
        self.accept_button.setText(QCoreApplication.translate("insert_equation_dialog", u"Aceptar", None))
        self.cancel_button.setText(QCoreApplication.translate("insert_equation_dialog", u"Cancelar", None))
    # retranslateUi

