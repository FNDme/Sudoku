# Sudoku Solver - Windows
Solucionador de tableros de Sudoku, Sudoku Diagonal y Sudoku Win creado en Prolog y usando la interfaz gráfica de la librería Tkinter para Python

## Instalación
Para que el programa se ejecute con normalidad es importante que se tenga instalado SWI-PROLOG en el dispositivo en que queramos ejecutar.

## Ejecución
La forma de ejecución, si cumplimos con los requisitos de la instalación es extremadamente sencilla. En el repositorio se encontrarán dos archivos, `Sudoku.exe` y `\lib\prologSudoku.pl`. Basta con ejecutar el archivo `Sudoku.exe` y el programa se iniciará.

## Dependencias
En caso de que estemos interesados en ejecutar el programa desde `mainWindow.py`, modificarlo o volver a compilar el .exe, es indispensable tener instaladas las siguientes dependencias.
### Python

[Install](https://www.python.org/downloads/)

### PIP

[Install](https://pypi.org/project/pip/)

### SWI-PROLOG

[Install](https://www.swi-prolog.org/download/stable)

### pyswip
`pip install pyswip`

## Compilación del fichero .exe
Para realizar la compilación se ha hecho uso de pyinstaller.
El archivo .spec ya esta definido, con que basta con ejecutar la siguiente sentencia:
`pyinstaller .\mainWindow.spec --onefile --windowed`