import copy
from models.Matrix import Matrix
from models.GaussMethod import GaussMethod

class CramersRule(Matrix):
    def __init__(self, matriz: list[list]) -> None:
        super().__init__(matriz)
        self.config = {}
        self.determinantes = []
        self.soluciones = []
    

    def cramersRule(self):
        if self.filas != self.columnas - 1:
            print("La matriz debe ser CUADRADA 'n x n' (excluyendo la columna 'b')")
            return #HACER ESTA VALIDACION DIRECTAMENTE DESDE LA INTERFAZ :)
        self.imprimir_ecuaciones()
        self.calcular_determinante_por_variable()
        self.solucion_variables()
        self.verificacion()

        return self.config

    def calcular_determinante_por_variable(self):
        n_variables = self.columnas - 1
        matriz_coeficientes = [fila[:-1] for fila in self.matriz]
        columna_resultados = [fila[-1] for fila in self.matriz]

        matriz_coef_copia = copy.deepcopy(matriz_coeficientes)
        sistema = GaussMethod(matriz_coef_copia)

        self.config["\nMATRIZ DE COEFICIENTES\n"] = copy.deepcopy(sistema.matriz)
        '''for fila in sistema.matriz:
            for valor in fila:
                print(f"{int(valor) if valor.is_integer() else f'{valor:.1f}'}", end = " ")
            print()
        print()'''

        sistema.gauss_method()
        determinante_sistema = sistema.det
        self.determinantes.append(determinante_sistema)
        self.config[f"\nDeterminante del sistema de ecuaciones\n"] = (copy.deepcopy(sistema.config), determinante_sistema) 

        for col in range(n_variables):
            matriz_modificada = copy.deepcopy(matriz_coeficientes)
            for fil in range(len(matriz_modificada)):
                matriz_modificada[fil][col] = columna_resultados[fil]
            gauss = GaussMethod(matriz_modificada)

            self.config[f"\nMATRIZ CON COLUMNA #{col + 1} INTERCAMBIADA\n"] = copy.deepcopy(gauss.matriz)
            '''for fila in gauss.matriz:
                for valor in fila:
                    print(f"{int(valor) if valor.is_integer() else f'{valor:.1f}'}", end = " ")
                print()
            print()'''

            gauss.gauss_method()
            determinante_variable = gauss.det
            self.determinantes.append(determinante_variable)
            self.config[f"\nDeterminante de X{col + 1}\n"] = (copy.deepcopy(gauss.config), determinante_variable)


    def solucion_variables(self):
        determinante_sistema = self.determinantes[0]
        n_variables = len(self.determinantes) - 1

        mensajes_solucion = []
        for col in range(n_variables):
            determinante_variable = self.determinantes[col + 1]
            solucion = determinante_variable / determinante_sistema
            self.soluciones.append(solucion)
            mensaje = f"\nX{col + 1} = {determinante_variable}/{determinante_sistema} = {solucion}"
            mensajes_solucion.append(mensaje)
        
        self.config[f"\nSOLUCIONES"] = {f"{i + 1}": msj for i, msj in enumerate(mensajes_solucion)}


    def verificacion(self):
        mensajes_verificacion = []
        for fila in range(self.filas):
            exp = ""
            operacion = 0
            for col in range(self.columnas - 1):
                valor = self.matriz[fila][col]
                if valor == 0: continue
                operacion += valor * self.soluciones[col]
                if valor > 0:
                    operador = "+" if exp else ""
                elif valor < 0:
                    operador = "-"
                    valor = -valor
                else: operador = ""
                coef = f"{("(" + str(int(valor)) + ")" if valor.is_integer() else f'{valor:.1f}')}"
                if operador:
                    exp += f" {operador} {coef}({self.soluciones[col]})"
                else:
                    exp += f"{operador} {coef}({self.soluciones[col]})"
            mensaje = f"Ec. {fila + 1}: {exp} = {operacion}"
            mensajes_verificacion.append(mensaje)
        
        self.config["\n\nVERIFICACIÓN\n"] = {f"{i + 1}": msj for i, msj in enumerate(mensajes_verificacion)}
            

    def imprimir_ecuaciones(self):
        sistema_ecuacion = []
        for fila in range(self.filas):
            ecuacion = ""
            for col in range(self.columnas - 1):
                valor = self.matriz[fila][col]
                if valor == 0: continue
                if valor > 0 and ecuacion != "":
                    operador = "+"
                elif valor < 0:
                    operador = "-"
                    valor = -valor
                else: operador = ""
                coef = f"{("(" + str(int(valor)) + ")" if valor.is_integer() else f'{valor:.1f}') if valor != 1 else ""}"
                if operador:
                    ecuacion += f" {operador} {coef}X{col + 1}"
                else:
                    ecuacion += f"{coef}X{col + 1}"

            resultado = self.matriz[fila][-1]
            ecuacion += f" = {int(resultado) if resultado.is_integer() else f'{resultado:.1f}'}"
            sistema_ecuacion.append(ecuacion)
        
        self.config["\nSISTEMA DE ECUACIÓN INGRESADO"] = {f"{i + 1}": ec for i, ec in enumerate(sistema_ecuacion)}

    def __str__(self) -> str:
        return super().__str__()