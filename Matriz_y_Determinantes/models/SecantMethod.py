import copy
from EquationEvaluator import EquationEvaluator as EC_EVAL

class SecantMethod():
    def __init__(self, f, x0, xi, tol, max_iter) -> None:
        self.funcion = f
        self.x0 = x0
        self.xi = xi
        self.max_iter = int(max_iter)
        self.n_iter = 0
        self.tolerancia = abs(tol)
        self.datos_por_iteracion = []
        self.config = {}
    
    def secant_method(self):
        if not self.tolerancia <=1:
            return 'not tolerance'
        
        for i in range(self.max_iter):
            self.n_iter += 1
            str_n_iteraciones = "#" + str(self.n_iter)
            fx0 = EC_EVAL(self.funcion, self.x0)
            fxi = EC_EVAL(self.funcion, self.xi)

            x_siguiente = self.xi - (fxi*(self.x0 - self.xi))/(fx0 - fxi)

            error_porcentual = abs((x_siguiente - self.xi)/x_siguiente)*100
            str_error_porcentual = str(round(error_porcentual, 6)) + "%"

            self.datos_por_iteracion.append([str_n_iteraciones, self.x0, self.xi, x_siguiente, fx0, fxi, str_error_porcentual])
            self.print_iterations()

            if error_porcentual/100 <= self.tolerancia:
                solucion = f"\nLa raíz aproximada es x = {x_siguiente} con un error porcentual de {error_porcentual}%.\nNúmero de iteraciones: {self.n_iter}"
                print(solucion)
                self.config["Solución Aproximada"] = (copy.deepcopy(self.datos_por_iteracion), solucion)
                return self.config
            
            self.x0 = self.xi
            self.xi = x_siguiente
        
        self.config["Se ha alcanzado el número máximo de iteraciones."] = copy.deepcopy(self.datos_por_iteracion)
        print("Se ha alcanzado el número máximo de iteraciones.")
        return self.config
    
    def print_iterations(self):
        """
        Imprime los datos de cada iteración en formato de tabla.
        """
        headers = ["Iteración", "Xi-1", "Xi", "Xi+1", "f(Xi-1)", "f(Xi)", "Error porcentual"]
        print(f"{' | '.join(headers)}")
        print("-" * 90)
        for row in self.datos_por_iteracion:
            print(" | ".join(f"{value:.6f}" if isinstance(value, float) else str(value) for value in row))
    

if __name__ == '__main__':
    SM = SecantMethod('ln(x)', 0.5, 5, 0.01, 100)
    SM.secant_method()