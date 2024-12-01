import re
from symengine import latex
def equation_to_rich_text(equation: str) -> str:
    equation = equation.replace("**", "^") 
    equation = re.sub(r'\bcos\b', 'cos', equation)
    equation = re.sub(r'\bsin\b', 'sin', equation)
    equation = re.sub(r'\bsen\b', 'sin', equation)  
    equation = re.sub(r'\btan\b', 'tan', equation)
    equation = re.sub(r'\blog10\b', 'log₁₀', equation)  
    equation = re.sub(r'\bln\b', 'ln', equation)  
    equation = re.sub(r'\blog\b', 'log', equation)
    equation = re.sub(r'\be\b', '𝑒', equation) 
    equation = re.sub(r'\bpi\b', 'π', equation)  
    equation = re.sub(r'\bsqrt\b', '√', equation)  

    equation = equation.replace('*', '·')
    equation = equation.replace('/', '÷')
    equation = equation.replace('sqrt', '√')
    pattern = r"(\d+|\w+|\([^()]*\))\^(\d+|\w+|\([^()]*\))"
    equation = re.sub(pattern, lambda m: m.group(1) + f'<sup>{m.group(2)}</sup>', equation)
    print(equation)
    q_label_output = f"<html><body><p>{equation}</p></body></html>"
    return q_label_output

if __name__ == '__main__':
    value = equation_to_rich_text('5x**(cos(2x))')
    print(value)
