# Calculadora de Álgebra Lineal - ALGEBRIER

Este proyecto es una calculadora para la clase de álgebra lineal.

## Requisitos

- **Entorno Virtual**: Es recomendable utilizar un entorno virtual para ejecutar el programa principal en la carpeta `app`.

### Pasos para Configurar el Entorno Virtual

1. **Crear un Entorno Virtual**:
   Utiliza el siguiente comando para crear un entorno virtual:
   ```bash
   python -m venv venv
2. **Agrega las dependencias en el entorno virtual**:
   Utiliza el siguiente comando con el entorno virtual ya activado:
   ```bash
   pip install -r requirements.txt
3. **Agrega un archivo .pth con la ruta raíz del proyecto en el entorno virtual**:
   Agrega un archivo .pth que contenga la ruta raíz del proyecto en site-packages del entorno virtual utilizado. Esto es para que python reconozca que debe buscar módulos en esa ruta
   ***RECUERDA: SOLO COPIA Y PEGA LA RUTA RAÍZ EN EL ARCHIVO .PTH***

## Despliegue

Para desplegar la aplicación, es necesario utilizar el archivo ***pysidedeploy.spec*** de la carpeta ***app***. La herramienta utilizada es ***pyside6-deploy***. Asegúrate de haber instalado las dependencias anteriormente.

Configura el archivo ***pysidedeploy.spec*** según el nombre de las rutas que utilize tu máquina local. 

Por defecto se creará un ejecutable con dependencias y otro de un solo archivo, para facilitar su distribución. Este proceso puede tardar un tiempo
