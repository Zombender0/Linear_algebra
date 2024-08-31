class Matrix():

    def __init__(self,matrix: list[list]) -> None:
        self.matrix = matrix
        self.width = len(matrix)
        self.length = len(matrix[0])
    
    @staticmethod
    def _valid_matrix(matrix: list[list]) -> bool:
        width = len(matrix)
        length = len(matrix[0])
        zero_row = True
        for row in range(width):
            zero_row = True
            for col in range(length):
                if matrix [row][col] !=0: zero_row = False
                if isinstance(matrix[row][col],float):
                    matrix[row][col] = int(matrix[row][col])
                    continue
                if isinstance(matrix[row][col], str):
                    print('Valor no numérico encontrado')
                    return False
                if len(matrix[row]) !=length:
                    print('Matriz incompleta')
                    return False
            if zero_row:
                print('Matriz inconsistente')
                return False
        return True

    def swap(self,row,row_to_swap,print_=True) -> None:
        '''
        Permite cambiar entre dos filas de una matriz. 
        
        Parámetros:
        row (int) : Una de las filas que se va a intercambiar
        row_to_swap (int) : La otra fila que se va a intercambiar
        print_ (bool) : Determina si se debe imprimir el cambio realizado con la matriz. Por defecto es verdadero

        El cambio se realiza en la matriz de la instancia que se esté trabajando.
        '''

        self.matrix[row],self.matrix[row_to_swap] = self.matrix[row_to_swap],self.matrix[row]
        if print_: 
            print(f"f{row+1} <--> f{row_to_swap+1}\n")
            print(self)

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
                rep+=f'{int(self.matrix[row][col])} '
            rep +='\n'
        return rep