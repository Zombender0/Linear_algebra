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
            print("La matriz debe ser cuadrada (sin contar la columna de los resultados).")
            return
        self.imprimir_ecuaciones()
        self.calcular_determinante_por_variable()
        self.solucion_variables()
        self.verificacion()


    def calcular_determinante_por_variable(self):
        n_variables = self.columnas - 1
        matriz_coeficientes = [fila[:-1] for fila in self.matriz]
        columna_resultados = [fila[-1] for fila in self.matriz]

        matriz_coef_copia = copy.deepcopy(matriz_coeficientes)
        sistema = GaussMethod(matriz_coef_copia)

        print("\nMATRIZ DE COEFICIENTES\n")
        for fila in sistema.matriz:
            for valor in fila:
                print(f"{int(valor) if valor.is_integer() else f'{valor:.1f}'}", end = " ")
            print()
        print()

        sistema.gauss_method()
        determinante_sistema = sistema.det
        self.determinantes.append(determinante_sistema)
        print(f"\nDeterminante del sistema de ecuaciones: {determinante_sistema}\n")

        for col in range(n_variables):
            matriz_modificada = copy.deepcopy(matriz_coeficientes)
            for fil in range(len(matriz_modificada)):
                matriz_modificada[fil][col] = columna_resultados[fil]
            gauss = GaussMethod(matriz_modificada)

            print(f"\nCOLUMNA #{col + 1} INTERCAMBIADA\n")
            for fila in gauss.matriz:
                for valor in fila:
                    print(f"{int(valor) if valor.is_integer() else f'{valor:.1f}'}", end = " ")
                print()
            print()

            gauss.gauss_method()
            determinante_variable = gauss.det
            self.determinantes.append(determinante_variable)
            print(f"Determinante de X{col + 1}: {determinante_variable}\n")


    def solucion_variables(self):
        determinante_sistema = self.determinantes[0]
        n_variables = len(self.determinantes) - 1

        for col in range(n_variables):
            determinante_variable = self.determinantes[col + 1]
            solucion = determinante_variable / determinante_sistema
            self.soluciones.append(solucion)
            print(f"\nX{col + 1} = {determinante_variable}/{determinante_sistema} = {solucion}")


    def verificacion(self):
        print("\n\nVERIFICACIÓN\n")
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
            resultado_esperado = self.matriz[fila][-1]
            es_correcta = "Correcta" if operacion == resultado_esperado else "Incorrecta"
            print(f"Ec. {fila + 1}: {exp} = {resultado_esperado} → {es_correcta}")
            

    def imprimir_ecuaciones(self):
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
            print(ecuacion)

    def __str__(self) -> str:
        return super().__str__()