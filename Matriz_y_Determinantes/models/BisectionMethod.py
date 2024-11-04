import copy
from EquationEvaluator import EquationEvaluator

class BisectionMethod():
    def __init__(self, f, a, b, tol) -> None:
        if not abs(tol) <= 1:
            raise ValueError("La tolerancia debe ser un porcentaje entre 0 y 1.")
        
        self.funcion = f
        self.interval_a = a
        self.interval_b = b
        self.media_c = None
        self.n_iter = 0
        self.tolerancia = abs(tol)
        self.datos_por_iteracion = []
        self.config = {}
    
    def bisection_method(self):

        fa = EquationEvaluator(self.funcion, self.interval_a)
        fb = EquationEvaluator(self.funcion, self.interval_b)
        
        if fa * fb >= 0:
            print("La función debe cambiar de signo en el intervalo dado [a, b].")
            return
        
        c_anterior = None
        while True:
            self.n_iter += 1
            self.media_c = (self.interval_a + self.interval_b)/2
            fc = EquationEvaluator(self.funcion, self.media_c)

            if c_anterior is not None:
                error_porcentual = abs(((self.media_c - c_anterior)/self.media_c)*100)
                str_error_porcentual = str(round(error_porcentual, 6)) + "%"
                if error_porcentual/100 <= self.tolerancia:
                    self.datos_por_iteracion.append([self.interval_a, self.interval_b, self.media_c, fa, fb, fc, fa * fc, str_error_porcentual])
                    self.print_iterations()
                    print(f"\nLa raíz aproximada es {self.media_c} con un error porcentual de {error_porcentual}%")
                    print(f"Número de iteraciones: {self.n_iter}\n")
                    break
            else:
                str_error_porcentual = "-"
            
            self.datos_por_iteracion.append([self.interval_a, self.interval_b, self.media_c, fa, fb, fc, fa*fc, str_error_porcentual])
            self.print_iterations()
            
            if fc == 0:
                print(f"\nLa raíz aproximada es {self.media_c}.")
                print(f"Número de iteraciones: {self.n_iter}\n")
                break

        
            if fa*fc > 0:
                print("\nSe sustituye el intervalo a por c\n")
                self.interval_a = self.media_c
                fa = EquationEvaluator(self.funcion, self.interval_a)
            else:
                print("\nSe sustituye el intervalo b por c\n")
                self.interval_b = self.media_c
                fb = EquationEvaluator(self.funcion, self.interval_b)
            
            c_anterior = self.media_c


    def print_iterations(self):
        """
        Imprime los datos de cada iteración en formato de tabla.
        """
        headers = ["intervalo a", "intervalo b", "media c", "fa", "fb", "fc", "fa*fc", "error porcentual"]
        print(f"{' | '.join(headers)}")
        print("-" * 90)
        for row in self.datos_por_iteracion:
            print(" | ".join(f"{value:.6f}" if isinstance(value, float) else str(value) for value in row))


if __name__ == '__main__':
    BM = BisectionMethod('(x**3)-sen(2*x)+(e**x)', -4, 2, 0.001)
    BM.bisection_method()

