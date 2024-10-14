from models.Matrix import Matrix

class GaussMethod(Matrix):
    def __init__(self, matriz: list[list]) -> None:
        super().__init__(matriz)
        self.det = 1 #Determinante inicializado
    
    def gauss_method(self):
        if not self.determinante_nulo():
            for col in range(self.columnas):
                self.pivote_triangular(col)
                self.reduccion_triangular(col)
            self.calculo_determinante()
    
    def determinante_nulo(self) -> bool:
        #Validación por si una matriz tiene líneas de ceros.
        for fila in range(self.filas):
            if all(self.matriz[fila][i] == 0 for i in range(self.columnas)):
                print("\nLa fila " + str(fila+1) + " es una línea de ceros. Por lo tanto, el determinante es igual a 0")
                return True

        for col in range(self.columnas):
            if all(self.matriz[i][col] == 0 for i in range(self.filas)):
                print("\nLa columna " + str(col+1) + " es una línea de ceros. Por lo tanto, el determinante es igual a 0")
                return True
        
        #Validación en caso de que una matriz tenga dos filas o dos columnas iguales.
        for i in range(self.filas):
            for j in range(i + 1, self.filas):
                if self.matriz[i] == self.matriz[j]:
                    print(f"\nLas filas {i+1} y {j+1} son iguales. Por lo tanto, el determinante es igual a 0.")
                    return True

        for i in range(self.columnas):
            for j in range(i + 1, self.columnas):
                col_i = [self.matriz[k][i] for k in range(self.filas)]
                col_j = [self.matriz[k][j] for k in range(self.filas)]
                if col_i == col_j:
                    print(f"\nLas columnas {i+1} y {j+1} son iguales. Por lo tanto, el determinante es igual a 0.")
                    return True
        
        return False
    
    def calculo_determinante(self):
        exp = "DET A = "
        operacion = f"({self.det}) "
        for i in range(self.filas):
            operacion += f"({self.matriz[i][i]:.1f})"
            self.det *= self.matriz[i][i]
        
        respuesta = exp + operacion
        print(respuesta)
        print(f"DET A = {self.det}")
    
    def pivote_triangular(self, col: int):
        mejor_fila = -1
        mejor_columna = col
        mejor_distancia = float('inf')

        for fila in range(col, self.filas):
            if self.matriz[fila][col] == 0:
                continue
            if self.matriz[fila][col] == 1:
                mejor_fila = fila
                break
            else:
                distancia = abs(self.matriz[fila][col] - 1)
                if distancia < mejor_distancia:
                    mejor_distancia = distancia
                    mejor_fila = fila

        posible_fila_pivote = self.matriz[mejor_fila][col]
        if posible_fila_pivote != 1:
            for col_alt in range(col+1, self.columnas):
                if self.matriz[col][col_alt] == 0:
                    continue
                if self.matriz[col][col_alt] == 1:
                    mejor_columna = col_alt
                    break
                else:
                    distancia = abs(self.matriz[col][col_alt] - 1)
                    mejor_distancia = abs(posible_fila_pivote - 1)
                    if distancia < mejor_distancia:
                        mejor_distancia = distancia
                        mejor_columna = col_alt
        
        if mejor_fila == -1:
            print(f"\nNo se encontró pivote en la columna {col + 1}.\n")
            print(self)
            print(f" DET A = {self.det}\n\n")
            return
        
        if mejor_columna != col:
            self.intercambio_col(col, mejor_columna)
            self.det = self.det * -1
            print(f" DET A = {self.det}\n\n")
            return
        
        if mejor_fila != col:
            self.intercambio(col, mejor_fila)
            self.det = self.det * -1
            print(f" DET A = {self.det}\n\n")
            return
    
    def intercambio_col(self, col, columna_intercambio) -> None:
        for fila in range(self.filas):
            self.matriz[fila][col],self.matriz[fila][columna_intercambio] = self.matriz[fila][columna_intercambio],self.matriz[fila][col]
        print(f"\nC{col + 1} <--> C{columna_intercambio + 1}\n")
        print(self)


    def intercambio(self, fila, fila_intercambio) -> None:
        '''Es una función que no devuelve nada.
        Tiene como parámetros el índice de la fila sin pivote y el índice de la fila con pivote para intercambiarlas.'''

        self.matriz[fila],self.matriz[fila_intercambio] = self.matriz[fila_intercambio],self.matriz[fila]
        print(f"\nF{fila + 1} <--> F{fila_intercambio + 1}\n")
        print(self)
    

    def reduccion_triangular(self, col: int):
        pivote = self.matriz[col][col]
        
        for fila in range(col + 1, self.filas):
            if self.matriz[fila][col] == 0:
                continue
            
            dividendo = self.matriz[fila][col]
            operando = dividendo / pivote
            self.matriz[fila] = [
                self.matriz[fila][i] - (operando * self.matriz[col][i]) for i in range(self.columnas)
            ]

            divisor = pivote

            if operando > 0:
                operador = "-"
            else:
                operador = "+"
                operando = -operando  
            
            dividendo_tipo = int(abs(dividendo)) if abs(dividendo).is_integer() else f"{abs(dividendo):.1f}"

            if abs(divisor) == 1:
                print(f"\nF{fila + 1} -> F{fila + 1} {operador} {dividendo_tipo}F{col + 1}\n")
            else:
                divisor_tipo = int(abs(divisor)) if abs(divisor).is_integer() else f"{abs(divisor):.1f}"
                print(f"\nF{fila + 1} -> F{fila + 1} {operador} ({dividendo_tipo}/{divisor_tipo})F{col + 1}\n")
            print(self)
            print(f" DET A = {self.det}\n\n")


    
    def __str__(self) -> str:
        return super().__str__()
