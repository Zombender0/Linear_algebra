from views.modified_python_files.main_window import MainWindow 
from config.config_loader import ConfigLoader
from config.config_writer import ConfigWriter
from configparser import ConfigParser
from PySide6.QtCore import Qt,QThreadPool
from helpers.box_helper import warning_box
class ConfigController():
    def __init__(self,config:ConfigParser,window:MainWindow):
        self.config = config
        self.window = window
        self.config_loader = ConfigLoader(self.config)
        self.config_writer = ConfigWriter(self.config)
        
    def load_config_to_interface(self):
        parsed_config = self.config_loader.parsed_config()
        if parsed_config is False:
            return None
        self.load_common_options_config(parsed_config['OPCIONES'])
        self.load_matrices_config({key: value for key, value in parsed_config.items() if key.startswith('MATRICES.')})
        self.load_equations_config([key for key in parsed_config.keys() if key.startswith('ECUACIONES.')])
        self.load_equation_methods_config({key:value for key,value in parsed_config.items() if key in ('BISECTION', 'NEWTON', 'FALSA POSICION', 'SECANTE')})
        
    def load_common_options_config(self,common_options:dict):
        try:
            self.window.table_select_solutions_combobox.setCurrentIndex(common_options['MATRIX_SOLVE_METHOD'])
            self.window.column_spinbox.setValue(common_options['COLUMNS'])
            self.window.row_spinbox.setValue(common_options['ROWS'])
            self.window.main_stacked_widget.setCurrentIndex(common_options['CURRENT_MAIN_TAB'])
            self.window.method_equation_tab_widget.setCurrentIndex(common_options['CURRENT_EQUATION_TAB'])
            self.window.table_resize_checkbox.setCheckState(
                Qt.Unchecked if common_options['CHECK_AUTOSCALE'] == False else Qt.Checked
                )
        except Exception as e:
            warning_box(f'Error en cargar la configuración principal: {e}')

    def load_matrices_config(self,matrices:dict):
        try:
            for i, (key,value) in enumerate(matrices.items()):
                if len(value['MATRIZ_COEFICIENTES']) != len(value['TERMINOS_INDEPENDIENTES']) and value['TERMINOS_INDEPENDIENTES'] !=None:
                    continue
                self.window.select_table_combobox.addItem(key.split('MATRICES.')[1])
        except Exception as e:
            warning_box(f'Error al cargar algunas matrices: {e}')

    def load_equations_config(self,equations:list):

        try:
            for equation in equations:
                equation_name:str = equation.split('ECUACIONES.')[1]
                self.window.select_equation_combobox.addItem(f'{equation_name}')
        except Exception as e:
            warning_box(f'Error al cargar algunas funciones: {e}')

    def load_equation_methods_config(self,methods:dict):
        try:
            bisection = methods['BISECTION']
            bisection = {key: (str(value) if value is not None else '') for key, value in bisection.items()}
            self.window.bisection_interval_a_line_edit.setText(bisection['INTERVAL_A'])
            self.window.bisection_interval_b_line_edit.setText(bisection['INTERVAL_B'])
            self.window.bisection_tolerance_line_edit.setText(bisection['TOLERANCE'])
        except Exception as e:
            warning_box(f'Error al cargar valores de método de Bisección: {e}')
        try:
            newton = methods['NEWTON']
            newton = {key: (str(value) if value is not None else '') for key, value in newton.items()}
            self.window.newton_x_value_line_edit.setText(newton['X_VALUE'])
            self.window.newton_max_iter_line_edit.setText(newton['MAX_ITER'])
            self.window.newton_tolerance_line_edit.setText(newton['TOLERANCE'])
        except Exception as e:
            warning_box(f'Error al cargar valores de método de Newton Raphson: {e}')
        
        try:
            false_position = methods['FALSA POSICION']
            false_position = {key: (str(value) if value is not None else '') for key, value in false_position.items()}
            self.window.false_interval_a_line_edit.setText(false_position['INTERVAL_XL'])
            self.window.false_interval_b_line_edit.setText(false_position['INTERVAL_XI'])
            self.window.false_tolerance_line_edit.setText(false_position['TOLERANCE'])

        except Exception as e:
            warning_box(f'Error al cargar valores de método de Falsa posición: {e}')
        try:
            secant = methods['SECANTE']
            secant = {key: (str(value) if value is not None else '') for key, value in secant.items()}
            self.window.secant_x0_line_edit.setText(secant['X0'])
            self.window.secant_xi_line_edit.setText(secant['XI'])
            self.window.secant_max_iter_line_edit.setText(secant['MAX_ITER'])
            self.window.secant_tolerance_line_edit.setText(secant['TOLERANCE'])
        except Exception as e:
            warning_box(f'Error al cargar valores de método de Secante: {e}')
    