from constants.math_functions import ALLOWED_DATA
import re
from copy import deepcopy

def EquationEvaluator(equation:str,x_value:int|float)->float|bool:
    allowed_data_copy = deepcopy(ALLOWED_DATA)
    allowed_data_copy['x'] = x_value
    try:
        result = eval(equation, {"__builtins__": None}, allowed_data_copy)
    except Exception as e:
        return None
    return result

def EquationParser(equation:str)->str:
    equation = re.sub(r"(\d)([a-zA-Z\(])", r"\1*\2", equation)
    equation = re.sub(r'√','sqrt',equation)
    equation = re.sub(r'π','pi',equation)
    equation = re.sub(r'log10','ln',equation)
    equation = re.sub(r'sen','sin',equation)
    return equation

if __name__ == '__main__':
    print(EquationEvaluator('',2))
