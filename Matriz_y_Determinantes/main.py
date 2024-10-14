from models.GaussJordan import GaussJordan as GJ
from models.GaussMethod import GaussMethod as GM
from models.Matrix import Matrix as M

def main():
    #Para resolución de matriz gauss jordan
    '''filas = int(input("Ingresa la cantidad de filas de la matriz: "))
    columnas = int(input("Ingresa la cantidad de columnas de la matriz: "))
    matriz = M.crear_matriz(filas, columnas)
    
    print("\nSISTEMA DE ECUACIONES INGRESADO\n")
    matriz_aumentada = GJ(matriz)
    matriz_aumentada.imprimir_ecuaciones()

    print("\nMATRIZ A RESOLVER:\n")
    for fila in matriz:
        for valor in fila:
            print(f"{int(valor) if valor.is_integer() else f'{valor:.1f}'}", end = " ")
        print()
    
    matriz_aumentada.gauss_jordan()
    matriz_aumentada.soluciones()'''



    #Para resolución de determinante de una matriz
    while True:
        filas = int(input("Cantidad de filas de la matriz: "))
        columnas = int(input("Cantidad de columnas de la matriz: "))
        
        if filas == columnas:
            break
        
        mensaje = ("\nLas filas y columnas deben contener el mismo número de entradas.\n"
                "Sólo se puede encontrar el DETERMINANTE en matrices cuadradas.\n ")
        print(mensaje)
    
    matriz = M.crear_matriz(filas, columnas)

    print("\nMATRIZ A RESOLVER:\n")
    for fila in matriz:
        for valor in fila:
            print(f"{int(valor) if valor.is_integer() else f'{valor:.1f}'}", end = " ")
        print()
    print()
    
    matriz_det = GM(matriz)
    matriz_det.gauss_method()


if __name__ == '__main__':
    main()