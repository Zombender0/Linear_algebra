from csv import reader
from helpers.box_helper import warning_box

def matrix_error_handler(f):
    def wrapper(*args,**kwargs):
        try:
            if not args[0].endswith('.csv'):
                raise FileNotFoundError
            result = f(*args,**kwargs)
        except ValueError:
            warning_box('Tipo de dato inválido en el archivo')
            return None
        except FileNotFoundError:
            warning_box('Archivo no encontrado')
            return None
        except Exception as e:
            warning_box(f'Error: {e}')
            return None
        else:
            return result
    return wrapper

def get_transposed_matrix(original_matrix) ->list[list]:
    matriz_transpuesta = [[original_matrix[fila][col] for fila in range(len(original_matrix))] 
                            for col in range(len(original_matrix[0]))]
    return matriz_transpuesta

@matrix_error_handler
def create_matrix_from_csv(file_path: str) ->list[list[float]]:
    with open(file_path,mode='r',encoding='utf-8') as f:
        content = list(reader(f,delimiter=';'))
        content = [list(map(float, row)) for row in content]
        return content
