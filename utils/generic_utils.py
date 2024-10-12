from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from views.qt_files.qrc_files import resources_rc

def get_file_from_dialog(name_filter:str):
    file_dialog = QFileDialog()
    icon = QIcon()
    icon.addFile(u":/icon/Images/grid.ico", QSize(), QIcon.Normal, QIcon.Off)
    file_dialog.setWindowIcon(icon)
    file_dialog.setFileMode(QFileDialog.ExistingFile)
    file_dialog.setNameFilter(name_filter)
    if file_dialog.exec():
        selected_file = file_dialog.selectedFiles()[0]
        return selected_file
    return None

