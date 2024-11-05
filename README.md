# Calculadora de Álgebra Lineal

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
3. **Agrega el archivo path_config al archivo de activación del entorno virtual**:
   Agrega la siguiente línea en el archivo de activación antes de **:END**:
   
   Windows: 
   ```bash
   python "%VIRTUAL_ENV%\..\path_config.py"
   ```
   Unix/Linux y MacOS
   ```bash
   python "$VIRTUAL_ENV/../path_config.py"
   ```
   Si no estás utilizando un entorno virtual, asegúrate de agregar en el archivo de ejecución la ruta raíz del programa **(Donde se encuentran todas las carpetas)**
   ```bash
   sys.path.append('ruta_raiz')
   ```

## Despliegue

Para desplegar la aplicación, es necesario utilizar el archivo ***deploy_app.spec*** de la carpeta ***deploy_config***. La herramienta utilizada es ***pyside6-deploy***. Asegúrate de haber instalado las dependencias anteriormente.

Configura el archivo ***deploy_app.spec*** según el nombre de las rutas que utilize tu máquina local. 

Por defecto se creará un ejecutable con dependencias y otro de un solo archivo, para facilitar su distribución