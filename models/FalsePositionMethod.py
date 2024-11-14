import copy
from models.EquationEvaluator import EquationEvaluator

class FalsePositionMethod():
    
    def __init__(self, f, xl, xu, tol) -> None:
        self.funcion = f
        self.xl = xl
        self.xu = xu
        self.xr = None
        self.n_iter = 0
        self.tolerancia = abs(tol)
        self.datos_por_iteracion = []
        self.config = {}
    
    def false_position_method(self):
        if not self.tolerancia <=1:
            return 'not tolerance'
        
        fxl = EquationEvaluator(self.funcion, self.xl)
        fxu = EquationEvaluator(self.funcion, self.xu)
        
        if fxl * fxu >= 0:
            self.config["La función debe cambiar de signo en el intervalo dado [xl, xu]"] = f"fxl * fxu -> {fxl * fxu} >= 0"
            #print("La función debe cambiar de signo en el intervalo dado [xl, xu].")
            return self.config

        xr_anterior = None
        while True:
            self.n_iter += 1
            self.xr = self.xu - (fxu*(self.xl - self.xu))/(fxl - fxu)
            fxr = EquationEvaluator(self.funcion, self.xr)

            if xr_anterior is not None:
                error_porcentual = abs(((self.xr - xr_anterior)/self.xr)*100)
                str_error_porcentual = str(round(error_porcentual, 6)) + "%"
                if error_porcentual/100 <= self.tolerancia:
                    self.datos_por_iteracion.append([self.xl, self.xu, self.xr, fxl, fxu, fxr, fxl*fxr, str_error_porcentual])
                    #self.print_iterations()
                    solucion = f"La raíz aproximada es {self.xr} con un error porcentual de {error_porcentual}%\nNúmero de iteraciones: {self.n_iter}"

                    self.config[f"ITERACIÓN {self.n_iter}"] = (copy.deepcopy(self.datos_por_iteracion), solucion)

                    #print(f"\nLa raíz aproximada es {self.xr} con un error porcentual de {error_porcentual}%")
                    #print(f"Número de iteraciones: {self.n_iter}\n")
                    break
            else:
                str_error_porcentual = "-"
            
            self.datos_por_iteracion.append([self.xl, self.xu, self.xr, fxl, fxu, fxr, fxl*fxr, str_error_porcentual])
            #self.print_iterations()

            if fxl*fxr == 0:
                solucion = f"La raíz aproximada es {self.xr} con un error porcentual de {error_porcentual}%"
                + f"\nNúmero de iteraciones: {self.n_iter}"
                self.config[f"ITERACIÓN {self.n_iter}"] = (copy.deepcopy(self.datos_por_iteracion), solucion)

                #print(f"\nLa raíz aproximada es {self.xr} con un error porcentual de {error_porcentual}%.")
                #print(f"Número de iteraciones: {self.n_iter}\n")
                break

            if fxl*fxr > 0:
                descripcion_paso = f"fxl*fxr -> {fxl*fxr} > 0, por lo tanto, xl se debe sustituir por xr"
                #print("\nSe sustituye el intervalo xl por xr\n")
                self.xl = self.xr
                fxl = EquationEvaluator(self.funcion, self.xl)
            else:
                descripcion_paso = f"fxl*fxr -> {fxl*fxr} < 0, por lo tanto, xu se debe sustituir por xl"
                #print("\nSe sustituye el intervalo xu por xr\n")
                self.xu = self.xr
                fxu = EquationEvaluator(self.funcion, self.xu)
            
            self.config[f"ITERACIÓN {self.n_iter}"] = (copy.deepcopy(self.datos_por_iteracion), descripcion_paso)
            xr_anterior = self.xr

        return self.config
    
    def print_iterations(self):
        """
        Imprime los datos de cada iteración en formato de tabla.
        """
        headers = ["xl", "xu", "xr", "fxl", "fxu", "fxr", "fxl*fxr", "error porcentual"]
        print(f"{' | '.join(headers)}")
        print("-" * 90)
        for row in self.datos_por_iteracion:
            print(" | ".join(f"{value:.6f}" if isinstance(value, float) else str(value) for value in row))
    
if __name__ == '__main__':
    fp = FalsePositionMethod('(x**3)-(4.23603*x**2)-(2.73620*x)-13.09037', 4.95, 5.5, 0.0001)
    fp.false_position_method()
