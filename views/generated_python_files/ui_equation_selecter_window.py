# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'equation_selecter_windownIRGfe.ui'
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
        insert_equation_dialog.resize(454, 382)
        insert_equation_dialog.setMaximumSize(QSize(454, 382))
        icon = QIcon()
        icon.addFile(u":/icon/Images/ico.ico", QSize(), QIcon.Normal, QIcon.Off)
        insert_equation_dialog.setWindowIcon(icon)
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
"#equation_buttons QPushButton::hover, #options_widget QPushButton::hover{\n"
"background-color: #202328;\n"
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
"padding: 4px;\n"
"font-weight: 450;\n"
"}\n"
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
        self.verticalLayout_4 = QVBoxLayout(self.equation_label_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
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
        self.equation_label.setWordWrap(True)
        self.equation_label.setIndent(-1)

        self.verticalLayout_4.addWidget(self.equation_label)


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


        self.verticalLayout.addWidget(self.equation_line_edit_widget, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_2.addWidget(self.equation_visualizer_widget)

        self.equation_buttons = QWidget(insert_equation_dialog)
        self.equation_buttons.setObjectName(u"equation_buttons")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.equation_buttons.sizePolicy().hasHeightForWidth())
        self.equation_buttons.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.equation_buttons)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.buttons_grid_layout = QGridLayout()
        self.buttons_grid_layout.setSpacing(10)
        self.buttons_grid_layout.setObjectName(u"buttons_grid_layout")
        self.buttons_grid_layout.setContentsMargins(-1, -1, -1, 0)
        self.two_button = QPushButton(self.equation_buttons)
        self.two_button.setObjectName(u"two_button")
        self.two_button.setFont(font1)

        self.buttons_grid_layout.addWidget(self.two_button, 1, 3, 1, 1)

        self.nine_button = QPushButton(self.equation_buttons)
        self.nine_button.setObjectName(u"nine_button")
        self.nine_button.setFont(font1)

        self.buttons_grid_layout.addWidget(self.nine_button, 3, 4, 1, 1)

        self.seven_button = QPushButton(self.equation_buttons)
        self.seven_button.setObjectName(u"seven_button")
        self.seven_button.setFont(font1)

        self.buttons_grid_layout.addWidget(self.seven_button, 3, 2, 1, 1)

        self.e_button = QPushButton(self.equation_buttons)
        self.e_button.setObjectName(u"e_button")
        self.e_button.setFont(font1)
        self.e_button.setIconSize(QSize(24, 24))

        self.buttons_grid_layout.addWidget(self.e_button, 1, 0, 1, 1)

        self.log_button = QPushButton(self.equation_buttons)
        self.log_button.setObjectName(u"log_button")
        self.log_button.setFont(font1)

        self.buttons_grid_layout.addWidget(self.log_button, 4, 1, 1, 1)

        self.open_parenthesis_button = QPushButton(self.equation_buttons)
        self.open_parenthesis_button.setObjectName(u"open_parenthesis_button")
        self.open_parenthesis_button.setFont(font1)

        self.buttons_grid_layout.addWidget(self.open_parenthesis_button, 0, 2, 1, 1)

        self.x_to_n_button = QPushButton(self.equation_buttons)
        self.x_to_n_button.setObjectName(u"x_to_n_button")
        self.x_to_n_button.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icon/Images/x_to_2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.x_to_n_button.setIcon(icon1)
        self.x_to_n_button.setIconSize(QSize(24, 24))

        self.buttons_grid_layout.addWidget(self.x_to_n_button, 0, 0, 1, 1)

        self.point_button = QPushButton(self.equation_buttons)
        self.point_button.setObjectName(u"point_button")
        self.point_button.setFont(font1)

        self.buttons_grid_layout.addWidget(self.point_button, 4, 4, 1, 1)

        self.tan_button = QPushButton(self.equation_buttons)
        self.tan_button.setObjectName(u"tan_button")
        self.tan_button.setFont(font1)

        self.buttons_grid_layout.addWidget(self.tan_button, 2, 1, 1, 1)

        self.exp_button = QPushButton(self.equation_buttons)
        self.exp_button.setObjectName(u"exp_button")
        self.exp_button.setFont(font1)

        self.buttons_grid_layout.addWidget(self.exp_button, 3, 1, 1, 1)

        self.four_butotn = QPushButton(self.equation_buttons)
        self.four_butotn.setObjectName(u"four_butotn")
        self.four_butotn.setFont(font1)

        self.buttons_grid_layout.addWidget(self.four_butotn, 2, 2, 1, 1)

        self.pi_button = QPushButton(self.equation_buttons)
        self.pi_button.setObjectName(u"pi_button")
        self.pi_button.setFont(font1)

        self.buttons_grid_layout.addWidget(self.pi_button, 2, 0, 1, 1)

        self.sqrt_button = QPushButton(self.equation_buttons)
        self.sqrt_button.setObjectName(u"sqrt_button")
        self.sqrt_button.setFont(font1)

        self.buttons_grid_layout.addWidget(self.sqrt_button, 3, 0, 1, 1)

        self.zero_button = QPushButton(self.equation_buttons)
        self.zero_button.setObjectName(u"zero_button")
        self.zero_button.setFont(font1)

        self.buttons_grid_layout.addWidget(self.zero_button, 4, 3, 1, 1)

        self.cos_button = QPushButton(self.equation_buttons)
        self.cos_button.setObjectName(u"cos_button")
        self.cos_button.setFont(font1)

        self.buttons_grid_layout.addWidget(self.cos_button, 0, 1, 1, 1)

        self.eight_button = QPushButton(self.equation_buttons)
        self.eight_button.setObjectName(u"eight_button")
        self.eight_button.setFont(font1)

        self.buttons_grid_layout.addWidget(self.eight_button, 3, 3, 1, 1)

        self.one_button = QPushButton(self.equation_buttons)
        self.one_button.setObjectName(u"one_button")
        self.one_button.setFont(font1)

        self.buttons_grid_layout.addWidget(self.one_button, 1, 2, 1, 1)

        self.ln_button = QPushButton(self.equation_buttons)
        self.ln_button.setObjectName(u"ln_button")
        self.ln_button.setFont(font1)

        self.buttons_grid_layout.addWidget(self.ln_button, 4, 0, 1, 1)

        self.sin_button = QPushButton(self.equation_buttons)
        self.sin_button.setObjectName(u"sin_button")
        self.sin_button.setFont(font1)

        self.buttons_grid_layout.addWidget(self.sin_button, 1, 1, 1, 1)

        self.close_parenthesis_button = QPushButton(self.equation_buttons)
        self.close_parenthesis_button.setObjectName(u"close_parenthesis_button")
        self.close_parenthesis_button.setFont(font1)

        self.buttons_grid_layout.addWidget(self.close_parenthesis_button, 0, 3, 1, 1)

        self.six_button = QPushButton(self.equation_buttons)
        self.six_button.setObjectName(u"six_button")
        self.six_button.setFont(font1)

        self.buttons_grid_layout.addWidget(self.six_button, 2, 4, 1, 1)

        self.three_button = QPushButton(self.equation_buttons)
        self.three_button.setObjectName(u"three_button")
        self.three_button.setFont(font1)

        self.buttons_grid_layout.addWidget(self.three_button, 1, 4, 1, 1)

        self.five_button = QPushButton(self.equation_buttons)
        self.five_button.setObjectName(u"five_button")
        self.five_button.setFont(font1)

        self.buttons_grid_layout.addWidget(self.five_button, 2, 3, 1, 1)

        self.delete_button = QPushButton(self.equation_buttons)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setFont(font1)

        self.buttons_grid_layout.addWidget(self.delete_button, 4, 2, 1, 1)

        self.add_button = QPushButton(self.equation_buttons)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setFont(font1)

        self.buttons_grid_layout.addWidget(self.add_button, 1, 5, 1, 1)

        self.substract_button = QPushButton(self.equation_buttons)
        self.substract_button.setObjectName(u"substract_button")
        self.substract_button.setFont(font1)

        self.buttons_grid_layout.addWidget(self.substract_button, 2, 5, 1, 1)

        self.multiply_button = QPushButton(self.equation_buttons)
        self.multiply_button.setObjectName(u"multiply_button")
        self.multiply_button.setFont(font1)

        self.buttons_grid_layout.addWidget(self.multiply_button, 3, 5, 1, 1)

        self.divide_button = QPushButton(self.equation_buttons)
        self.divide_button.setObjectName(u"divide_button")
        self.divide_button.setFont(font1)

        self.buttons_grid_layout.addWidget(self.divide_button, 4, 5, 1, 1)

        self.back_position_button = QPushButton(self.equation_buttons)
        self.back_position_button.setObjectName(u"back_position_button")
        self.back_position_button.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u":/icon/Images/left_ar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.back_position_button.setIcon(icon2)
        self.back_position_button.setIconSize(QSize(22, 22))

        self.buttons_grid_layout.addWidget(self.back_position_button, 0, 4, 1, 1)

        self.next_position_button = QPushButton(self.equation_buttons)
        self.next_position_button.setObjectName(u"next_position_button")
        self.next_position_button.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/icon/Images/right_ar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.next_position_button.setIcon(icon3)
        self.next_position_button.setIconSize(QSize(20, 22))

        self.buttons_grid_layout.addWidget(self.next_position_button, 0, 5, 1, 1)


        self.verticalLayout_3.addLayout(self.buttons_grid_layout)


        self.verticalLayout_2.addWidget(self.equation_buttons)

        self.options_widget = QWidget(insert_equation_dialog)
        self.options_widget.setObjectName(u"options_widget")
        self.options_widget.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.options_widget)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.apply_button = QPushButton(self.options_widget)
        self.apply_button.setObjectName(u"apply_button")
        font2 = QFont()
        font2.setPointSize(12)
        self.apply_button.setFont(font2)

        self.horizontalLayout_3.addWidget(self.apply_button)

        self.accept_button = QPushButton(self.options_widget)
        self.accept_button.setObjectName(u"accept_button")
        self.accept_button.setFont(font2)

        self.horizontalLayout_3.addWidget(self.accept_button)

        self.cancel_button = QPushButton(self.options_widget)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setFont(font2)

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
        self.two_button.setText(QCoreApplication.translate("insert_equation_dialog", u"2", None))
        self.nine_button.setText(QCoreApplication.translate("insert_equation_dialog", u"9", None))
        self.seven_button.setText(QCoreApplication.translate("insert_equation_dialog", u"7", None))
        self.e_button.setText(QCoreApplication.translate("insert_equation_dialog", u"e", None))
        self.log_button.setText(QCoreApplication.translate("insert_equation_dialog", u"log", None))
        self.open_parenthesis_button.setText(QCoreApplication.translate("insert_equation_dialog", u"(", None))
        self.x_to_n_button.setText("")
        self.point_button.setText(QCoreApplication.translate("insert_equation_dialog", u".", None))
        self.tan_button.setText(QCoreApplication.translate("insert_equation_dialog", u"tan", None))
        self.exp_button.setText(QCoreApplication.translate("insert_equation_dialog", u"EXP", None))
        self.four_butotn.setText(QCoreApplication.translate("insert_equation_dialog", u"4", None))
        self.pi_button.setText(QCoreApplication.translate("insert_equation_dialog", u"\u03c0", None))
        self.sqrt_button.setText(QCoreApplication.translate("insert_equation_dialog", u"\u221a", None))
        self.zero_button.setText(QCoreApplication.translate("insert_equation_dialog", u"0", None))
        self.cos_button.setText(QCoreApplication.translate("insert_equation_dialog", u"cos", None))
        self.eight_button.setText(QCoreApplication.translate("insert_equation_dialog", u"8", None))
        self.one_button.setText(QCoreApplication.translate("insert_equation_dialog", u"1", None))
        self.ln_button.setText(QCoreApplication.translate("insert_equation_dialog", u"ln", None))
        self.sin_button.setText(QCoreApplication.translate("insert_equation_dialog", u"sen", None))
        self.close_parenthesis_button.setText(QCoreApplication.translate("insert_equation_dialog", u")", None))
        self.six_button.setText(QCoreApplication.translate("insert_equation_dialog", u"6", None))
        self.three_button.setText(QCoreApplication.translate("insert_equation_dialog", u"3", None))
        self.five_button.setText(QCoreApplication.translate("insert_equation_dialog", u"5", None))
        self.delete_button.setText(QCoreApplication.translate("insert_equation_dialog", u"CE", None))
        self.add_button.setText(QCoreApplication.translate("insert_equation_dialog", u"+", None))
        self.substract_button.setText(QCoreApplication.translate("insert_equation_dialog", u"-", None))
        self.multiply_button.setText(QCoreApplication.translate("insert_equation_dialog", u"\u00d7", None))
        self.divide_button.setText(QCoreApplication.translate("insert_equation_dialog", u"\u00f7", None))
        self.back_position_button.setText("")
        self.next_position_button.setText("")
        self.apply_button.setText(QCoreApplication.translate("insert_equation_dialog", u"Aplicar", None))
        self.accept_button.setText(QCoreApplication.translate("insert_equation_dialog", u"Aceptar", None))
        self.cancel_button.setText(QCoreApplication.translate("insert_equation_dialog", u"Cancelar", None))
    # retranslateUi

