import configparser as cp
import os
from config.config_base import ConfigBase

class ConfigWriter(ConfigBase):
    def __init__(self,config_object:cp.ConfigParser):
        super().__init__(config_object)

    def save_matrix(self,nombre: str, matriz_coeficientes: list[list], terminos_independientes: list):
        nombre = f'MATRICES.{nombre}'
        try:
            self.config.add_section(nombre)
        except (cp.DuplicateSectionError,ValueError):
            return False
        matriz_coeficientes = str(matriz_coeficientes)
        terminos_independientes = str(terminos_independientes)
        self.config.set(nombre,'MATRIZ_COEFICIENTES',matriz_coeficientes)
        self.config.set(nombre,'TERMINOS_INDEPENDIENTES',terminos_independientes)
        self._save_config()
        return True

    def save_equation(self,nombre: str, ecuacion: str):
        nombre = f'ECUACIONES.{nombre}'
        try:
            self.config.add_section(nombre)
        except (cp.DuplicateSectionError,ValueError):
            return False
        self.config.set(nombre,'nombre',ecuacion)
        self._save_config()
        return True
    
    def save_option(self,options:dict):
        if not self.config.has_section('OPCIONES'):
            self._create_default_config()
        
        for key, value in options.items():
            self.config.set('OPCIONES', key, str(value))

    def delete_matrix(self,nombre:str):
        self.config.remove_section(f'MATRICES.{nombre}')
        self._save_config()

    def delete_equation(self,nombre:str):
        self.config.remove_section(f'ECUACIONES.{nombre}')
        self._save_config()
        
if __name__ == '__main__':
    config = cp.ConfigParser()
    c_object = ConfigWriter(config)
    c_object.delete_matrix('A')