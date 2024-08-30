class Matrix():

    def __init__(self,matrix: list[list]) -> None:
        self.matrix = matrix
        self.width = len(matrix)
        self.length = len(matrix[0])
    
    def __valid_matrix(self):
        pass
    def swap(self,row,row_to_swap,print=True) -> None:
        '''
        Permite cambiar entre dos filas de una matriz. 
        
        Parámetros:
        row (int) : Una de las filas que se va a intercambiar
        row_to_swap (int) : La otra fila que se va a intercambiar
        print (bool) : Determina si se debe imprimir el cambio realizado con la matriz. Por defecto es verdadero

        El cambio se realiza en la matriz de la instancia que se esté trabajando.
        '''

        self.matrix[row],self.matrix[row_to_swap] = self.matrix[row_to_swap],self.matrix[row]
        if print: 
            print(f"f{row+1} <--> f{row_to_swap+1}\n")
            self

    @staticmethod
    def gcd(a: int,b: int) -> int: 
        '''
        Retorna el máximo común divisor entre dos números enteros

        Parámetros:
        a (int) : El primer numero
        b (int) : El segundo numero
        '''
        if a == 0:
            return b
        return Matrix.gcd(b%a,a)

    @staticmethod
    def lcd(a: int, b:int) ->int:
        '''
        Retorna el mínimo común múltiplo entre dos números enteros

        Parámetros:
        a (int) : El primer numero
        b (int) : El segundo numero
        '''
        return a*b // Matrix.gcd(a,b)
    
    def __str__(self) -> str:
        rep = ''
        for row in range(self.width):
            for col in range(self.length):
                rep+=f'{self.matrix[row][col]} '
            rep +='\n'
        return rep