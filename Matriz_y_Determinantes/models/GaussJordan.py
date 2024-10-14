class GaussJordan():
    def __init__(self, matriz: list[list]) -> None:
        self.matriz = matriz
        self.filas = len(matriz) #Cantidad de filas
        self.columnas = len(matriz[0]) #Cantidad de columnas
        self.filas_pivotes = set() #Para almacenar el índice de filas que contienen pivotes como valores únicos
        self.det = 1 #Determinante inicializado
    
    @staticmethod
    def crear_matriz(cantFilas: int, cantColum: int) -> list[list[float]]:
        matriz = []
        print("\nOJO: Separa con espacios y escribe 0 cuando falte una variable.")
        for fila in range(cantFilas):
            while True:
                try:
                    print(f"Ingrese los {cantColum} valores para la fila {fila + 1}:")
                    entrada = input(" ----> ")
                    print()
                    caracteres_validos = set("0123456789.- ")
                    if not all(char in caracteres_validos for char in entrada):
                        raise ValueError("Entrada inválida. Usa solo números, puntos" 
                                         " decimales, signos negativos y espacios.")
                    contenido = list(map(float, entrada.split()))
                    if len(contenido) != cantColum:
                        raise ValueError(f"Debes introducir exactamente {cantColum} números.")
                    matriz.append(contenido)
                    break
                except ValueError as Error:
                    print(Error)
        return matriz
    
    
    def gauss_jordan(self):
        '''Se inicializa el proceso de eliminación Gauss Jordan.
        Se recorren los índices de cada columnas menos la de resultados, es decir, de manera horizontal, para determinar un pivote.
        En caso de que se encuentre una columna pivote, se procede a reducir los elementos de la 
        columna correspondiente a 0, excepto el 1.'''

        for col in range(self.columnas - 1):
            if not self.convertir_a_1(col):
                print(f"\nNo se puede encontrar un pivote adecuado en la columna {col+1}.")
                continue
            self.reduccion_a_cero(col)
                

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



    def pivote(self, col : int) -> int | bool:
        '''Es una función que devuelve un entero (int) o False.
        Parámetro: el índice de la columna para evaluar si contiene un pivote adecuado.

        Mediante un ciclo, se itera por cada valor de la columna evaluada de manera vertical.
        Si un término es distinto que 0 y el índice de su fila no se encuentra en el set() de la clase,
        la función retorna ese mismo índice y continúa con las operaciones.
        En caso de no cumplirse niguno de los criterios, se retorna un False.'''

        for fila in range(self.filas):
            if self.matriz[fila][col] != 0 and fila not in self.filas_pivotes:
                return fila
        return False


    def convertir_a_1(self, col : int) -> bool:
        '''Es una función que devuelve True o False.
        Parámetro: el índice de la columna para evaluar si contiene un pivote adecuado.
        
        Primero, se revisa si en la columna hay presente un pivote. En caso de que no, se retorna un False y termina el proceso.
        
        En el caso contrario, con el índice dado de la fila en la que se encuentra el pivote, se obtiene el número pivote en la
        columna en la que se está trabajando. Si el pivote es diferente que 1, la fila que lo contiene se divide con el pivote
        para transformarlo en 1. 
        
        Igualmente, hay otra condicional if que verifica si el índice de la fila con el pivote es distinta al índice de la primera
        fila disponible sin pivote, lo cual da paso a un intercambio entre filas si es necesario. Por último, se actualiza el set()'''

        pivote_fila = self.pivote(col)
        if pivote_fila is False:
            return False
        
        pivote = self.matriz[pivote_fila][col]
    
        if pivote != 1:
            self.matriz[pivote_fila] = [x / pivote for x in self.matriz[pivote_fila]]
            print(f"\nF{pivote_fila + 1} -> F{pivote_fila + 1} / {int(pivote) if pivote.is_integer() else f'{pivote:.1f}'}\n")
            print(self)

        for fila in range(self.filas):
            if fila not in self.filas_pivotes:
                fila_sin_pivote = fila
                break
        
        if pivote_fila != fila_sin_pivote:
            self.intercambio(fila_sin_pivote, pivote_fila)
            pivote_fila = fila_sin_pivote

        self.filas_pivotes.add(pivote_fila)
        return True

    
    #Cuando hay columna pivote
    def reduccion_a_cero(self, col : int):
        '''Parámetros: índice de la columna con pivote
        Teniendo en cuenta que a este punto del programa, ya existe un 1 en la columna a trabajar, el pivote 1 
        se busca mediante un for y se le asigna a la variable pivote_fila el índice de la fila donde se encuentra.
        De este modo, se transforma el resto de números de la columna a 0 (exceptuando la fila pivote).'''

        pivote_fila = None
        for fila in self.filas_pivotes:
            if self.matriz[fila][col] == 1 and all(number != 1 for number in self.matriz[fila][:col]):
                pivote_fila = fila
                break

        for fila in range(self.filas):
            if fila == pivote_fila: continue
            if self.matriz[fila][col] == 0: continue
            operando = self.matriz[fila][col] * -1
            self.matriz[fila] = [self.matriz[fila][i] + (operando * self.matriz[pivote_fila][i]) for i in range(self.columnas)]

            if operando > 0:
                operador = "+"
            else:
                operador = "-"
                operando = -operando
            
            operando_tipo = int(operando) if operando.is_integer() else f"{operando:.1f}"
            
            print(f"\nF{fila + 1} -> F{fila + 1} {operador} {operando_tipo}F{pivote_fila + 1}\n")
            print(self)
    
    
    def soluciones(self):
        '''Si la matriz tiene una fila con ceros menos en la columna de resultados, no hay solución.
        Si en la matriz hay menos filas no nulas (es decir, con coeficientes) que columnas de incógnitas,
        existen infinitas soluciones.
        Si ninguno de estos casos se cumplen, se asume que la matriz presenta una solución única y los
        resultados de las incógnitas se muestran en pantalla.'''

        print("\n\nSOLUCIÓN EN FORMA DE ECUACIONES:\n")
        self.imprimir_ecuaciones()
        print()

        for fila in range(self.filas):
            if all(self.matriz[fila][i] == 0 for i in range(self.columnas - 1)) and self.matriz[fila][-1] != 0:
                print("\nLa matriz no tiene solución.")
                return
  
        filas_no_nulas = [fila for fila in self.matriz if any(f != 0 for f in fila[:-1])]
        if len(filas_no_nulas) < self.columnas - 1:
            print("\nLa matriz tiene infinitas soluciones.\n")
            self.variables_libres()
            return

        print("\nLa matriz tiene una solución única:\n")
        soluciones = []
        for fila in range(self.filas):
            if fila < self.columnas - 1:
                soluciones.append(self.matriz[fila][-1])
        for i, sol in enumerate(soluciones):
            print(f"X{i+1} = {int(sol) if sol.is_integer() else f'{sol:.1f}'}")


    def variables_libres(self):
        '''Se ejecuta cuando la matriz tiene infinitas soluciones.
        En una lista se almacenan las columnas con pivotes (1). Si la lista no contiene el índice
        de una columna, se considera que esa columna tiene una variable libre.'''

        columnas_pivotes = []
        for fila in range(self.filas):
            for col in range(self.columnas - 1):
                if self.matriz[fila][col] !=1: continue
                if any(self.matriz[fila][i] != 0 for i in range(col)): continue
                columnas_pivotes.append(col)
                break
        
        for col in range(self.columnas - 1):
            if col not in columnas_pivotes:
                print(f'X{col+1} es una variable libre')
                continue
            for fila in range(self.filas):
                if self.matriz[fila][col] != 1: 
                    continue
                resultado = self.matriz[fila][-1]
                expr = f"X{col+1} = " + ((f"{int(resultado) if resultado.is_integer() else f'{resultado:.1f}'}") 
                                          if resultado != 0 else "")
                for i, valor in enumerate(self.matriz[fila][:-1]):
                    if i in columnas_pivotes: continue
                    if valor == 0: continue
                    operador, valor = (" -",valor) if valor > 0 else(" +",-valor)
                    expr += f"{operador} {("(" + str(int(valor)) + ")" if valor.is_integer() else f'{valor:.1f}') if valor != 1 else ""}X{i+1}"
                print(expr)


    def __str__(self) -> str:
        matriz : str = ''
        maximo_tamaño_fila = max(len(f'{round(self.matriz[fila][columna], 3)}') for fila in range(self.filas) for columna in range(self.columnas)) + 2
        for fila in range(self.filas):
            fila_str = ''
            for columna in range(self.columnas):
                fila_str += f'{round(self.matriz[fila][columna], 3):<{maximo_tamaño_fila}}'
            matriz += fila_str + '\n'
        return matriz
    

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
            if resultado == 0 and all(self.matriz[fila][i] == 0 for i in range(self.columnas - 1)):
                ecuacion = "0 = 0"
                print(ecuacion)
                continue
            
            ecuacion += f" = {int(resultado) if resultado.is_integer() else f'{resultado:.1f}'}"
            print(ecuacion)