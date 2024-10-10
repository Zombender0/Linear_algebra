from views.generated_python_files.ui_solution_window import Ui_main_widget as Generated_SolutionWindow
from PySide6.QtWidgets import (QHBoxLayout, QLabel,QListWidget, QPushButton,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,QTextEdit,
    QWidget)
from PySide6.QtCore import Slot
from helpers.matrix_helper import insert_data_to_table

class SolutionWindow(QWidget,Generated_SolutionWindow):
    def __init__(self):
        super.__init__()
        self.setupUi(self)

    def setupUi(self, main_widget):
        super().setupUi(main_widget)

    def create_tab_solutions(self,config: dict):
        for i,(step,matrix) in enumerate(config.items()):
            self.p = QWidget()
            self.p.setProperty('step_data',step)
            self.p.setObjectName(f'p{i+1}')
            self.verticalLayout = QVBoxLayout(self.p)
            self.verticalLayout.setObjectName(f"vertical_layout_{i+1}")
            self.verticalLayout.setContentsMargins(0, 0, 0, 0)
            self.s_table = QTableWidget(self.p)
            self.s_table.setObjectName(f"s_table_{i+1}")
            self.verticalLayout.addWidget(self.s_table)
            if i == len(config)-1:
                insert_data_to_table(self.s_table,config[step][0],editable=False)
                self.solution_list = QListWidget(self.p)
                self.solution_list.setObjectName('solution_list')
                if matrix[1] != '':
                    for variable in matrix[1]:
                        self.solution_list.addItem(variable)
                    self.verticalLayout.addWidget(self.solution_list)
                else:
                    self.solution_list.hide()
            else:
                insert_data_to_table(self.s_table,config[step],editable=False)
            self.s_table.resizeColumnsToContents()
            self.tabWidget.addTab(self.p,f'p{i+1}')


    def show_step_property(self):
        step = self.tabWidget.currentWidget().property('step_data')
        if step is not None:
            self.label.setText(step)
            return
        self.label.setText('Informacion no encontrada')

    @Slot()
    def previous_tab(self):
        current_index = self.tabWidget.currentIndex()
        if current_index > 0:
            self.tabWidget.setCurrentIndex(current_index-1)
    @Slot()
    def next_tab(self):
        current_index = self.tabWidget.currentIndex()
        if current_index < self.tabWidget.count()-1:
            self.tabWidget.setCurrentIndex(current_index+1)
