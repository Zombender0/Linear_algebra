from PySide6.QtWidgets import QFileDialog,QApplication
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon

from sys import argv
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

def select_path_to_csv(name_filter:str):
    file_dialog = QFileDialog()
    icon = QIcon()
    icon.addFile(u":/icon/Images/grid.ico", QSize(), QIcon.Normal, QIcon.Off)
    file_dialog.setWindowIcon(icon)
    file_dialog.setAcceptMode(QFileDialog.AcceptSave)
    file_dialog.setNameFilter(name_filter)
    file_dialog.setDefaultSuffix('csv')

    file_path, _ = file_dialog.getSaveFileName(
        caption="Guardar archivo como",
        filter=name_filter
    )
    
    return file_path if file_path else None

if __name__ == '__main__':
    app = QApplication(argv)
    file_path = select_path_to_csv("Archivos CSV (*.csv)")
    print(file_path)