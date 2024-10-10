from PySide6.QtWidgets import QMessageBox

def warning_box(message):
    box = QMessageBox()
    box.setIcon(QMessageBox.Critical)
    box.setText(message)
    box.setWindowTitle('Error al ingresar datos.')
    box.setStandardButtons(QMessageBox.Ok)
    return box.exec()
    
def information_box(message):
    box = QMessageBox()
    box.setIcon(QMessageBox.Information)
    box.setText(message)
    box.setWindowTitle('Información')
    box.setStandardButtons(QMessageBox.Ok)
    return box.exec()

def question_box(message):
    box = QMessageBox()
    box.setIcon(QMessageBox.Question)
    box.setText(message)
    box.setWindowTitle('Pregunta')
    box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    return box.exec()