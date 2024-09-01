'''
Esto lo hizo ChatGPT y, a pesar de que tiene lógica, parece que falta algo. Probablemente en el pivote
'''

def print_matrix(matrix):
    """ Imprime la matriz en un formato amigable. """
    for row in matrix:
        print(" ".join(f"{elem:8.3f}" for elem in row))

def gauss_jordan(A, b):
    """
    Resuelve el sistema de ecuaciones lineales Ax = b usando el método de Gauss-Jordan.
    
    Parámetros:
    A: lista de listas, matriz de coeficientes del sistema
    b: lista, vector de términos independientes

    Retorna:
    lista, solución del sistema
    """
    n = len(A)
    # Crear la matriz aumentada [A|b]
    augmented_matrix = [A[i] + [b[i]] for i in range(n)]

    for i in range(n):
        # Buscar el pivote
        max_row = max(range(i, n), key=lambda r: abs(augmented_matrix[r][i]))
        if augmented_matrix[max_row][i] == 0:
            raise ValueError("El sistema tiene solución infinita o no tiene solución")

        # Intercambiar filas
        if i != max_row:
            augmented_matrix[i], augmented_matrix[max_row] = augmented_matrix[max_row], augmented_matrix[i]

        # Normalizar la fila del pivote
        pivot = augmented_matrix[i][i]
        augmented_matrix[i] = [x / pivot for x in augmented_matrix[i]]

        # Eliminar las otras filas
        for j in range(n):
            if i != j:
                factor = augmented_matrix[j][i]
                augmented_matrix[j] = [augmented_matrix[j][k] - factor * augmented_matrix[i][k] for k in range(n + 1)]

    # La solución es la última columna de la matriz aumentada
    solution = [row[-1] for row in augmented_matrix]
    return solution

# Ejemplo de uso
if __name__ == "__main__":
    # Matriz de coeficientes
    A = [
        [1,2,-3,-1],
        [0,-3,2,6],
        [-1,-1,3,1],
        [2,3,2,-1]
    ]
    
    # Vector de términos independientes
    b = [0,-8,0,-8]
    
    # Resolver el sistema
    solution = gauss_jordan(A, b)
    
    print("La solución del sistema es:")
    print(solution)
