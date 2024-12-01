from constants.math_functions import ALLOWED_DATA
import re
from copy import deepcopy
from symengine import diff,sympify, symbols
from math import log

def EquationEvaluator(equation:str,x_value:int|float)->float|None:
    allowed_data_copy = deepcopy(ALLOWED_DATA)
    allowed_data_copy['x'] = x_value
    try:
        result = eval(equation, {"__builtins__": None}, allowed_data_copy)
    except ValueError:
        return 'domain error'
    except Exception as e:
        return None
    return result

def EquationParser(equation:str)->str:
    equation = re.sub(r"(\d)([a-zA-Z\(])", r"\1*\2", equation)
    equation = re.sub(r'√','sqrt',equation)
    equation = re.sub(r'π','pi',equation)
    equation = re.sub(r'log','ln',equation)
    equation = re.sub(r'sen','sin',equation)
    return equation

def differencial(equation:str)->str:
    sympified_function = sympify(equation)
    try:
        differencial = diff(sympified_function,symbols('x'))
    except Exception as e:
        return equation
    return str(differencial)

if __name__ == '__main__':
    function = 'ln(x)'
    function = EquationParser(function)
    print(differencial(function))

