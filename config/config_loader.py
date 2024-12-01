import configparser as cp
from ast import literal_eval
from config.config_base import ConfigBase

class ConfigLoader(ConfigBase):
    def __init__(self, config_object):
        super().__init__(config_object)
    
    def parsed_config(self):
        parsed_config = dict()
        for section in self.config.sections():
            parsed_config[section] = {}
            for key, value in self.config.items(section):
                key = str(key).upper()
                try:
                    parsed_config[section][key] = literal_eval(value)
                except (ValueError,SyntaxError):
                    return False
        return parsed_config
    
if __name__ == '__main__':
    config = cp.ConfigParser()
    c_object = ConfigLoader(config)
    print(c_object.parsed_config())