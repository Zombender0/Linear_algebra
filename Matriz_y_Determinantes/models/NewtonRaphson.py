import copy
from sympy import symbols, diff
from EquationEvaluator import EquationEvaluator as EC_EVAL
#from DerivativeFunction import funcion_derivada, derivados

class NewthonRaphson():
    def __init__(self, f, x, tol, max_iter) -> None:
        self.funcion = f
        self.x_inicial = x
        self.max_iter = max_iter
        self.n_iter = 0
        self.tolerancia = abs(tol)
        self.datos_por_iteracion = []
        self.config = {}


    def newton_raphson_method(self):

        x_actual = self.x_inicial
        for i in range(self.max_iter):
            self.n_iter += 1
            str_n_iteraciones = "#" + str(self.n_iter)
            fxi = EC_EVAL(self.funcion, x_actual)
            x = symbols('x')
            funcion_derivada = diff(self.funcion, x)
            fxi_derivada = EC_EVAL(str(funcion_derivada), x_actual)

            if fxi_derivada == 0:
                self.config["Derivada cero. No se puede continuar."] = copy.deepcopy(self.datos_por_iteracion)
                print("\nDerivada cero. No se puede continuar.")
                return self.config

            x_siguiente = x_actual - (fxi/fxi_derivada)

            error_absoluto = abs((x_siguiente - x_actual)/x_siguiente)*100
            str_error_porcentual = str(round(error_absoluto, 6)) + "%"
            self.datos_por_iteracion.append([str_n_iteraciones, x_actual, x_siguiente, fxi, fxi_derivada, str_error_porcentual])
            self.print_iterations()

            if error_absoluto/100 <= self.tolerancia:
                solucion = f"\nLa raíz aproximada es {x_siguiente} con un error porcentual de {error_absoluto}%\nNúmero de iteraciones: {self.n_iter}"
                print(solucion)
                self.config["Solución Aproximada"] = (copy.deepcopy(self.datos_por_iteracion), solucion)
                return self.config
            
            x_actual = x_siguiente
        
        self.config["Se ha alcanzado el número máximo de iteraciones."] = copy.deepcopy(self.datos_por_iteracion)
        print("Se ha alcanzado el número máximo de iteraciones.")
        return self.config

    def print_iterations(self):
        """
        Imprime los datos de cada iteración en formato de tabla.
        """
        headers = ["Iteración", "Xi", "Xi + 1", "f(Xi)", "f'(Xi)", "Error absoluto"]
        print(f"{' | '.join(headers)}")
        print("-" * 90)
        for row in self.datos_por_iteracion:
            print(" | ".join(f"{value:.6f}" if isinstance(value, float) else str(value) for value in row))

if __name__ == '__main__':
    NR = NewthonRaphson('cos(2*x)', 10, 0.01, 100)
    NR.newton_raphson_method()