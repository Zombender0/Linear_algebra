from constants.math_functions import ALLOWED_DATA
from copy import deepcopy

def EquationEvaluator(equation:str,x_value:int|float)->float|bool:
    allowed_data_copy = deepcopy(ALLOWED_DATA)
    allowed_data_copy['x'] = x_value
    try:
        result = eval(equation, {"__builtins__": None}, allowed_data_copy)
    except Exception as e:
        return None
    return result

if __name__ == '__main__':
    print(EquationEvaluator('2*x**2',2))
