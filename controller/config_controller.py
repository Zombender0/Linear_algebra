from views.modified_python_files.main_window import MainWindow 
from config.config_loader import ConfigLoader
from config.config_writer import ConfigWriter
from configparser import ConfigParser
from helpers.matrix_helper import insert_data_to_table
from PySide6.QtCore import Qt
from helpers.box_helper import warning_box
class ConfigController():
    def __init__(self,config:ConfigParser,window:MainWindow):
        self.config = config
        self.window = window
        self.config_loader = ConfigLoader(self.config)
        self.config_writer = ConfigWriter(self.config)
        self.load_config_to_interface()
        
    def load_config_to_interface(self):
        parsed_config = self.config_loader.parsed_config()
        if parsed_config is False:
            warning_box('Error al cargar la configuracion')
            return None
        self.load_common_options_config(parsed_config['OPCIONES'])
        self.load_matrices_config({key: value for key, value in parsed_config.items() if key.startswith('MATRICES.')})
    
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
                self.window.select_table_combobox.setItemData(i+1,key)
                
        except Exception as e:
            warning_box(f'Error al cargar algunas matrices: {e}')
        