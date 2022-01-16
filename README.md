# Sudoku Solver - Windows
Solucionador de tableros de Sudoku, Sudoku Diagonal y Sudoku Win creado en Prolog y usando la interfaz gráfica de la librería Tkinter para Python
## Instalación
Para que el programa se ejecute con normalidad hay que cumplir dos requisitos.
### SWI-PROLOG
El programa hace uso de Prolog, y por tanto, es requisito indispensable tener instalado SWI-PROLOG en el dispositivo que queramos ejecutarlo.
### Fichero Prolog
El siguiente requisito es que el fichero .exe se encuentre en la misma carpeta que el fichero `prologSudoku.pl`. En caso contrario, la aplicación será incapaz de encontrar el fichero y no se ejecutará.

## Uso
La forma de ejecución, si cumplimos con los requisitos de la instalación es extremadamente sencilla. En la carpeta dist se encontrarán dos archivos, `mainWindow.exe` y `prologSudoku.pl`. Basta con ejecutar el archivo mainWindow.exe y el programa se iniciará.

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

### Uso

Abrimos una terminal y ejecutamos el archivo python
`python mainWindow.py`