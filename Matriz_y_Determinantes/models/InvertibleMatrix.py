import copy
from models.Matrix import Matrix
from models.GaussMethod import GaussMethod

class InvertibleMatrix(Matrix):
    def __init__(self, matriz: list[list]) -> None:
        super().__init__(matriz)
        self.config = {}
        self.matriz_identidad = [[1.0 if i == j else 0.0 for j in range(self.filas)] for i in range(self.filas)]
        self.matriz_aumentada = [self.matriz[i] + self.matriz_identidad[i] for i in range(self.filas)]

    def invertibleMatrix(self):
        if self.filas != self.columnas:
            print("La matriz debe ser CUADRADA 'n x n'")
            return #VALIDAR DIRECTAMENTE DESDE LA INTERFAZ
        
        if self.singularMatrix():
            print("El determminante es igual a 0, por lo tanto, la matriz A no tiene inversa")
            return

        print("MATRIZ AUMENTADA")
        self.imprimir_matriz_aumentada()

        self.gauss_jordan_inversa()

        
    def gauss_jordan_inversa(self):
        for col in range(self.columnas):
            if self.convertir_a_1(col):
                self.reduccion_a_cero(col)
        
        if all(self.matriz_aumentada[i][j] == (1.0 if i == j else 0.0) for i in range(self.filas) for j in range(self.columnas)):
            self.solucion_matriz_inversa()
        else:
            print("No hay solución en Gauss-Jordan, por lo tanto, la matriz es singular.")
        
    def solucion_matriz_inversa(self):
        matriz_inversa = [fila[self.columnas:] for fila in self.matriz_aumentada]
        print("\nMATRIZ INVERSA")
        self.imprimir_matriz(matriz_inversa)
     
    def convertir_a_1(self, col: int) -> bool:
        if self.matriz_aumentada[col][col] == 0:
            for fila in range(col+1, self.filas):
                if self.matriz_aumentada[fila][col] != 0:
                    self.intercambio(col, fila)
                    break

        pivote = self.matriz_aumentada[col][col]

        if pivote != 1 and pivote != 0:
            self.matriz_aumentada[col] = [x / pivote for x in self.matriz_aumentada[col]]
            print(f"\nF{col + 1} -> F{col + 1} / {int(pivote) if pivote.is_integer() else f'{pivote:.2f}'}\n")
            self.imprimir_matriz_aumentada()
        
        return True if self.matriz_aumentada[col][col] == 1 else False
        
    def intercambio(self, fila, fila_intercambio) -> None:
        self.matriz_aumentada[fila],self.matriz_aumentada[fila_intercambio] = self.matriz_aumentada[fila_intercambio],self.matriz_aumentada[fila]
        print(f"\nF{fila + 1} <--> F{fila_intercambio + 1}\n")
        self.imprimir_matriz_aumentada()

    def reduccion_a_cero(self, col : int):
        for fila in range(self.filas):
            if fila == col: continue
            if self.matriz_aumentada[fila][col] == 0: continue
            operando = self.matriz_aumentada[fila][col] * -1
            self.matriz_aumentada[fila] = [self.matriz_aumentada[fila][i] + (operando * self.matriz_aumentada[col][i]) for i in range(len(self.matriz_aumentada[0]))]

            if operando > 0:
                operador = "+"
            else:
                operador = "-"
                operando = -operando

            operando_tipo = int(operando) if operando.is_integer() else f"{operando:.2f}"

            print(f"\nF{fila + 1} -> F{fila + 1} {operador} {operando_tipo}F{col + 1}\n")
            self.imprimir_matriz_aumentada()

    def singularMatrix(self) -> bool:
        matriz_cuadrada_copia = copy.deepcopy(self.matriz)
        matrizA = GaussMethod(matriz_cuadrada_copia)

        print("MATRIZ A")
        self.imprimir_matriz(matrizA.matriz)

        matrizA.gauss_method()

        print("MATRIZ A EN FORMA TRIANGULAR (Y SU DETERMINANTE)")
        self.imprimir_matriz(matrizA.matriz)
        determinante_sistema = matrizA.det
        print(f"Det A = {determinante_sistema}\n")

        if determinante_sistema == 0:
            return True
        
        return False

    def imprimir_matriz(self, matriz_cualquiera):
        matriz : str = ''
        maximo_tamaño_fila = max(len(f'{round(matriz_cualquiera[fila][columna], 3)}') for fila in range(len(matriz_cualquiera)) for columna in range(len(matriz_cualquiera[0]))) + 2
        for fila in range(len(matriz_cualquiera)):
            fila_str = ''
            for columna in range(len(matriz_cualquiera[0])):
                fila_str += f'{round(matriz_cualquiera[fila][columna], 3):<{maximo_tamaño_fila}}'
            matriz += fila_str + '\n'
        print(matriz)

    def imprimir_matriz_aumentada(self):
        matriz : str = ''
        maximo_tamaño_fila = max(len(f'{round(self.matriz_aumentada[fila][columna], 3)}') for fila in range(self.filas) for columna in range(len(self.matriz_aumentada[0]))) + 2
        for fila in range(self.filas):
            fila_str = ''
            for columna in range(len(self.matriz_aumentada[0])):
                fila_str += f'{round(self.matriz_aumentada[fila][columna], 3):<{maximo_tamaño_fila}}'
            matriz += fila_str + '\n'
        print(matriz)
    