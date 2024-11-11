import copy
from symengine import symbols, diff
from models.EquationEvaluator import EquationEvaluator as EC_EVAL
#from DerivativeFunction import funcion_derivada, derivados

class NewthonRaphson():
    def __init__(self, f, x, tol, max_iter) -> None:
        self.funcion = f
        self.x_inicial = x
        self.max_iter = int(max_iter)
        self.n_iter = 0
        self.tolerancia = abs(tol)
        self.datos_por_iteracion = []
        self.config = {}
        
    def newton_raphson_method(self):
        if not self.tolerancia <=1:
            return 'not tolerance'
        
        x_actual = self.x_inicial
        for i in range(self.max_iter):
            self.n_iter += 1
            str_n_iteraciones = "#" + str(self.n_iter)
            fxi = EC_EVAL(self.funcion, x_actual)
            x = symbols('x')
            funcion_derivada = diff(self.funcion, x)
            fxi_derivada = EC_EVAL(str(funcion_derivada), x_actual)

            if fxi_derivada == 0:
                self.config["Derivada cero. No se puede continuar."] = copy.deepcopy([self.datos_por_iteracion])

                return self.config

            x_siguiente = x_actual - (fxi/fxi_derivada)

            if x_siguiente != 0:
                error_absoluto = abs(x_siguiente - x_actual)
            else:
                error_absoluto = abs(x_siguiente - x_actual)
            self.datos_por_iteracion.append([str_n_iteraciones, x_actual, x_siguiente, fxi, fxi_derivada, error_absoluto])
            #self.print_iterations()

            if error_absoluto <= self.tolerancia:
                solucion = f"\nLa raíz{' aproximada' if error_absoluto != 0 else ''} es x = {x_siguiente} con un error absoluto de {error_absoluto}.\nNúmero de iteraciones: {self.n_iter}"
                #print(solucion)
                self.config["Solución Aproximada"] = (copy.deepcopy(self.datos_por_iteracion), solucion)
                return self.config
            
            x_actual = x_siguiente
        
        self.config["Se ha alcanzado el número máximo de iteraciones."] = copy.deepcopy(self.datos_por_iteracion)
        #print("Se ha alcanzado el número máximo de iteraciones.")
        return self.config

    def print_iterations(self):
        """
        Imprime los datos de cada iteración en formato de tabla.
        """
        headers = ["Iteración", "Xi", "Xi + 1", "f(Xi)", "f'(Xi)", "Error porcentual"]
        print(f"{' | '.join(headers)}")
        print("-" * 90)
        for row in self.datos_por_iteracion:
            print(" | ".join(f"{value:.6f}" if isinstance(value, float) else str(value) for value in row))

if __name__ == '__main__':
    NR = NewthonRaphson('cos(2*x)', 10, 0.01, 100)
    NR.newton_raphson_method()
    print(NR.config)
