class Matrix():
    def __init__(self, matriz: list[list]) -> None:
        self.matriz = matriz
        self.filas = len(matriz) #Cantidad de filas
        self.columnas = len(matriz[0]) #Cantidad de columnas
    
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
    
    def __str__(self) -> str:
        matriz : str = ''
        maximo_tamaño_fila = max(len(f'{round(self.matriz[fila][columna], 4)}') for fila in range(self.filas) for columna in range(self.columnas)) + 2
        for fila in range(self.filas):
            fila_str = ''
            for columna in range(self.columnas):
                fila_str += f'{round(self.matriz[fila][columna], 4):<{maximo_tamaño_fila}}'
            matriz += fila_str + '\n'
        return matriz