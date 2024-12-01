import configparser as cp
import os
from functools import wraps

class ConfigBase():
    CONFIG_DIR = 'config'
    CONFIG_FILE = 'config/config.ini'
    
    def __init__(self,config_object:cp.ConfigParser):
        self.config = config_object
        self.check_file_exists()

    def check_file_exists(self):
        if not os.path.exists(self.CONFIG_DIR):
            os.makedirs(self.CONFIG_DIR)
        
        if not os.path.exists(self.CONFIG_FILE):
            self._create_default_config()
        else:
            self.config.read(self.CONFIG_FILE)

    def _create_default_config(self):
        self.config['OPCIONES'] = {
            'MATRIX_SOLVE_METHOD':'0',
            'ROWS': '3',
            'COLUMNS': '3',
            'CURRENT_MATRIX': 'None',
            'CURRENT_MAIN_TAB': '0',
            'CURRENT_EQUATION_TAB': '0'
        }
        self._save_config()
    
    def _save_config(self):
        with open(self.CONFIG_FILE, 'w', encoding='utf-8') as file:
            self.config.write(file)

    def check_section_exists(self,section:str):
        if not self.config.has_section(section):
            self.config.add_section(section)
            self._save_config()

    def section_checker(self,section:str):
        def decorator(func):
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                self.check_section_exists(section) 
                return func(self, *args, **kwargs)
            return wrapper
        return decorator

if __name__ == '__main__':
    config = cp.ConfigParser()
    c_object = ConfigBase(config)
    print(c_object)
    
