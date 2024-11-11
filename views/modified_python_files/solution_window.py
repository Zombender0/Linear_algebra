from views.generated_python_files.ui_solution_window import Ui_main_widget as Generated_SolutionWindow
from PySide6.QtWidgets import (QHBoxLayout, QLabel,QListWidget, QPushButton,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,QTextEdit,
    QWidget,QVBoxLayout,QListWidgetItem)

from PySide6.QtCore import Slot,Qt
from PySide6.QtGui import QFont
from helpers.matrix_helper import insert_data_to_table,customize_headers_in_table
from constants.equation_methods import BISECTION_HEADER,NEWTON_HEADER
class SolutionWindow(QWidget,Generated_SolutionWindow):  
    header_font = QFont('Calibri',30)
    def __init__(self,parent:QWidget=None):
        super().__init__(parent)
        self.setupUi(self)  
        self.setWindowTitle('Solución')

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
                insert_data_to_table(self.s_table,config[step][0],editable=False,last_b=True)
                self.solution_list = QListWidget(self.p)
                self.solution_list.setObjectName('solution_list')
                if matrix[1] != '':
                    for variable in matrix[1]:
                        item = QListWidgetItem(variable)
                        item.setFont(QFont('Calibri',15))
                        self.solution_list.addItem(item)
                    self.verticalLayout.addWidget(self.solution_list)
                else:
                    self.solution_list.hide()
            else:
                insert_data_to_table(self.s_table,config[step],editable=False,last_b=True)
            self.tab_widget.addTab(self.p,f'p{i+1}')
        #set first step
        first_step = self.tab_widget.currentWidget().property('step_data')
        self.label.setText(first_step)
        self.setWindowTitle('Solucción por reducción')
            
    def create_determinant_step(self,config:dict):
        for i,(step,(matriz,determinant)) in enumerate(config.items()):
            self.p = QWidget()
            self.p.setProperty('step_data',step)
            self.p.setObjectName(f'p{i+1}')
            self.horizontal_layout = QHBoxLayout(self.p)
            self.horizontal_layout.setObjectName(f"horizontal_layout{i+1}")
            self.horizontal_layout.setContentsMargins(6,0,0,0)
            self.determinant_label = QLabel(f"{determinant}")
            self.horizontal_layout.addWidget(self.determinant_label, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)
            self.determinant_label.setFont(self.header_font)
            self.s_table = QTableWidget(self.p)
            self.s_table.setObjectName(f"s_table_{i+1}")
            self.horizontal_layout.addWidget(self.s_table)
            insert_data_to_table(self.s_table,matriz,editable=False,last_b=False)
            self.horizontal_layout.setStretch(1,100)
            self.horizontal_layout.setStretch(1,10)
            self.tab_widget.addTab(self.p,f'p{i+1}')
        first_step = self.tab_widget.currentWidget().property('step_data')
        self.label.setText(first_step)
        self.setWindowTitle('Calcular determinante')
    
    def create_cramer_solution(self,config:dict):
        for i,(step,content) in enumerate(config.items()):
            self.p = QWidget()
            self.p.setProperty('step_data',step)
            self.p.setObjectName(f'p{i+1}')

            if not isinstance(content[1],tuple): # This is an step, so horizontal_layout
                self.layout_ = QHBoxLayout(self.p)
                self.layout_.setObjectName(f"horizontal_layout{i+1}")
                self.layout_.setContentsMargins(6,0,0,0)
            else:
                self.layout_ = QVBoxLayout(self.p)
                self.layout_.setObjectName(f"vertical_layout{i+1}")
                self.layout_.setContentsMargins(0,0,0,6)

            self.s_table = QTableWidget(self.p)
            if not isinstance(content[0][0],list):
                content[0] = [content[0]]
            insert_data_to_table(self.s_table,content[0],editable=False,last_b=False,letter=' ')
            self.s_table.setObjectName(f"s_table_{i+1}")
            self.layout_.addWidget(self.s_table)
            
            if not isinstance(content[1],tuple):
                self.determinant_label = QLabel(f"{content[1]}")
                self.layout_.addWidget(self.determinant_label, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)
                self.determinant_label.setFont(self.header_font)
            else:
                self.solution_list = QListWidget(self.p)
                self.solution_list.setObjectName('solution_list')
                for variable in content[1]:
                    item = QListWidgetItem(variable[1])
                    item.setFont(QFont('Calibri',15))
                    self.solution_list.addItem(item)
                self.layout_.addWidget(self.solution_list)
            self.tab_widget.addTab(self.p,f'p{i+1}')
        first_step = self.tab_widget.currentWidget().property('step_data')
        self.label.setText(first_step)
        self.setWindowTitle('Solucción por Cramer')
    
    def create_invertable_solution(self,config:dict)->None:
        for i,(step,aumented_matrix) in enumerate(config.items()):
            columns = len(aumented_matrix[0])//2
            original_matrix = [row[:columns] for row in aumented_matrix]
            inverted_matrix = [row[columns:] for row in aumented_matrix]
            self.p = QWidget()
            self.p.setProperty('step_data',step)
            self.p.setObjectName(f'p{i+1}')
            self.p.setStyleSheet('')
            self.horizontal_layout = QHBoxLayout(self.p)
            self.horizontal_layout.setObjectName(f"horizontal_layout{i+1}")
            self.horizontal_layout.setContentsMargins(0,0,6,0)
            self.original_table = QTableWidget(self.p)
            self.original_table.setObjectName(f"original_table_{i+1}")
            self.inverted_table = QTableWidget(self.p)
            self.inverted_table.setObjectName(f'inverted_table_{i+1}')
            self.horizontal_layout.addWidget(self.original_table)
            self.horizontal_layout.addWidget(self.inverted_table)
            insert_data_to_table(self.original_table,original_matrix,editable=False,last_b=False,letter='X')
            insert_data_to_table(self.inverted_table,inverted_matrix,editable=False,last_b=False,letter='X')
            self.tab_widget.addTab(self.p,f'p{i+1}')
            if step in ('Matriz inversa',
                        'El determinante es igual a 0, por lo tanto, la matriz A no tiene inversa',
                        'No hay solucion en Gauss-Jordan, por lo tanto, la matriz es singular.'):
                self.inverted_table.hide()
                insert_data_to_table(self.original_table,aumented_matrix,editable=False,last_b=False,letter='X')
        first_step = self.tab_widget.currentWidget().property('step_data')
        self.label.setText(first_step)
        self.setWindowTitle('Solucción de matriz invertida')

    def create_bisection_solution(self,config:dict)->None:
        for i,(step,content) in enumerate(config.items()):
            self.p = QWidget()
            self.p.setProperty('step_data',step)
            self.p.setObjectName(f'p{i+1}')
            self.verticalLayout = QVBoxLayout(self.p)
            self.verticalLayout.setObjectName(f"vertical_layout_{i+1}")
            self.verticalLayout.setContentsMargins(0, 0, 0, 0)
            self.s_table = QTableWidget(self.p)
            self.s_table.setObjectName(f"s_table_{i+1}")
            self.verticalLayout.addWidget(self.s_table)
            if isinstance(content,str):#No solution
                self.s_table.hide()
                self.s_label = QLabel(content)
                self.verticalLayout.addWidget(self.s_label)
            else:
                matrix = content[0]
                solution = content[1]
                insert_data_to_table(self.s_table,matrix,editable=False,last_b=False,letter=' ')
                customize_headers_in_table(self.s_table,BISECTION_HEADER)
                self.s_label = QLabel(solution)
                self.s_label.setFont(QFont('Calibri',15))
                self.verticalLayout.addWidget(self.s_label)

            self.tab_widget.addTab(self.p,f'p{i+1}')
        first_step = self.tab_widget.currentWidget().property('step_data')
        self.label.setText(first_step)
        self.setWindowTitle('Raíz de ecuación por bisección')
    
    def create_newton_solution(self,config:dict)->None:
        for i,(step,content) in enumerate(config.items()):
            self.p = QWidget()
            self.p.setProperty('step_data',step)
            self.p.setObjectName(f'p{i+1}')
            self.verticalLayout = QVBoxLayout(self.p)
            self.verticalLayout.setObjectName(f"vertical_layout_{i+1}")
            self.verticalLayout.setContentsMargins(0, 0, 0, 0)
            self.s_table = QTableWidget(self.p)
            self.s_table.setObjectName(f"s_table_{i+1}")
            self.verticalLayout.addWidget(self.s_table)
            if isinstance(content,tuple):
                matrix = content[0]
                solution = content[1]
                insert_data_to_table(self.s_table,matrix,editable=False,last_b=False,letter='')
                customize_headers_in_table(self.s_table,NEWTON_HEADER)
                self.s_label = QLabel(solution)
                self.s_label.setFont(QFont('Calibri',15))
                self.verticalLayout.addWidget(self.s_label)
            else:
                self.s_table.hide()
            self.tab_widget.addTab(self.p,f'p{i+1}')
        first_step = self.tab_widget.currentWidget().property('step_data')
        self.label.setText(first_step)
        self.setWindowTitle('Raíz de ecuación por Newton Raphson')
        
    def show_step_property(self):
        step = self.tab_widget.currentWidget().property('step_data')
        if step is not None:
            self.label.setText(step)
            return
        self.label.setText('Informacion no encontrada')

    @Slot()
    def previous_tab(self):
        current_index = self.tab_widget.currentIndex()
        if current_index > 0:
            self.tab_widget.setCurrentIndex(current_index-1)
    @Slot()
    def next_tab(self):
        current_index = self.tab_widget.currentIndex()
        if current_index < self.tab_widget.count()-1:
            self.tab_widget.setCurrentIndex(current_index+1)
