from tkinter import Label, Tk, Entry, Button, Canvas, messagebox
from tkinter.font import BOLD
from functools import partial
from pyswip import Prolog

prolog = Prolog()
prolog.consult("prologSudoku.pl")

base = Tk()

base.title("Sudoku solver")
base.resizable(0, 0)
base.geometry("800x540")
base.config(bg="#025939")

canvas = Canvas(base, width=440, height=440,
                bg="#0E7344", highlightthickness=0)
canvas.place(x=300, y=50)

global solList
global whichSol
global nSolutions
solList = []
whichSol = 0
nSolutions = 0

def boardFormat(tab):
    parameter = str(tab)
    parameter = parameter.replace("\'", "")
    return parameter

def resetBoard():
    global solList
    global whichSol
    global nSolutions
    solList = []
    whichSol = 0
    nSolutions = 0
    for i in range(9):
        for j in range(9):
            entrys[i][j].config(state="normal", readonlybackground="#F29F05")
            if (i in [0, 1, 2] and j in [0, 1, 2, 6, 7, 8]) or (i in [3, 4, 5] and j in [3, 4, 5]) or (i in [6, 7, 8] and j in [0, 1, 2, 6, 7, 8]):
                entrys[i][j].config(readonlybackground="#F2B705")
            entrys[i][j].delete(0, "end")
    resetButton.config(state="disabled")
    nextButton.config(state="disabled")


def nextSol():
    global solList
    global whichSol
    global nSolutions
    if whichSol < nSolutions:
        for i in range(9):
            for j in range(9):
                entrys[i][j].config(state="normal")
                entrys[i][j].delete(0, "end")
                entrys[i][j].insert(0, solList[0][i][j])
                entrys[i][j].config(state="readonly")
        solList.pop(0)
        whichSol += 1
        nSolLabel.config(text="Solución " + str(whichSol) +
                         " de " + str(nSolutions))

def solveSudoku(sudokuType):
    global solList
    global whichSol
    global nSolutions
    tablero = [["_" for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if entrys[i][j].get() in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                tablero[i][j] = entrys[i][j].get()
            elif entrys[i][j].get() != "":
                messagebox.showinfo("Error", "El valor de la casilla " +
                                    str(i+1) + "x" + str(j+1) + " debe ser un número entre 1 y 9")
                return

    if sudokuType == "tradicional":
        query = "sudoku(SOL, " + boardFormat(tablero) + ")"
    elif sudokuType == "diagonal":
        query = "sudoku_diagonal(SOL, " + boardFormat(tablero) + ")"
    elif sudokuType == "win":
        query = "sudoku_win(SOL, " + boardFormat(tablero) + ")"

    nSolutions = 1
    try:
        if nSol.get() != "" and int(nSol.get()) > 0:
            nSolutions = int(nSol.get())
    except:
        messagebox.showinfo(
            "Error", "El número de soluciones debe ser un número entero")
        return

    whichSol = 1

    for sol in prolog.query(query, maxresult=nSolutions):
        solList.append(sol["SOL"])
    nSolutions = len(solList)

    nSolLabel.config(text="Solución " + str(whichSol) +
                     " de " + str(nSolutions))

    if len(solList) > 0:
        for i in range(9):
            for j in range(9):
                entrys[i][j].delete(0, "end")
                entrys[i][j].insert(0, solList[0][i][j])
                entrys[i][j].config(state="readonly")
        solList.pop(0)
        nextButton.config(state="normal")
        resetButton.config(state="normal")
        if sudokuType == "diagonal":
            for i in range(9):
                for j in range(9):
                    if i == j or i == 8-j:
                        entrys[i][j].config(readonlybackground="#91A646")
        elif sudokuType == "win":
            for i in range(9):
                for j in range(9):
                    if i in [1, 2, 3, 5, 6, 7] and j in [1, 2, 3, 5, 6, 7]:
                        entrys[i][j].config(readonlybackground="#91A646")
    else:
        messagebox.showinfo("Sudoku solver", "No se encontró solución")


entrys = [[Entry(base, justify="center") for x in range(9)] for y in range(9)]

for i in range(9):
    for j in range(9):
        entrys[i][j].place(x=340+j*40, y=90+i*40, width=40, height=40)
        entrys[i][j].config(bg="#F2B705", font=("Arial", 20), fg="#025939", highlightthickness=0.5,
                            highlightbackground="#025939", border=0, readonlybackground="#F29F05")
        if (i in [0, 1, 2] and j in [0, 1, 2, 6, 7, 8]) or (i in [3, 4, 5] and j in [3, 4, 5]) or (i in [6, 7, 8] and j in [0, 1, 2, 6, 7, 8]):
            entrys[i][j].config(bg="#F29F05", readonlybackground="#F2B705")

title = Label(base, text="Sudoku solver", font=(
    "verdana", 23, BOLD), bg="#025939", fg="#F2B705")
title.place(x=20, y=60)

solveClassicSudokuButton = Button(base, text="Sudoku Classic", command=partial(solveSudoku, "tradicional"), bg="#0E7344", fg="#F2B705", font=(
    "Arial", 12, BOLD), border=0, highlightthickness=0.5, highlightbackground="#025939")
solveClassicSudokuButton.place(x=70, y=160, width=160, height=40)

solveDiagonalSudokuButton = Button(base, text="Sudoku Diagonal", command=partial(solveSudoku, "diagonal"), bg="#0E7344", fg="#F2B705", font=(
    "Arial", 12, BOLD), border=0, highlightthickness=0.5, highlightbackground="#025939")
solveDiagonalSudokuButton.place(x=70, y=220, width=160, height=40)

solveWinSudokuButton = Button(base, text="Sudoku Win", command=partial(solveSudoku, "win"), bg="#0E7344", fg="#F2B705", font=(
    "Arial", 12, BOLD), border=0, highlightthickness=0.5, highlightbackground="#025939")
solveWinSudokuButton.place(x=70, y=280, width=160, height=40)

resetButton = Button(base, text="Reset", command=resetBoard, bg="#0E7344", fg="#F2B705", font=(
    "Arial", 12, BOLD), border=0, highlightthickness=0.5, highlightbackground="#025939", state="disabled")
resetButton.place(x=70, y=370, width=160, height=40)

nextButton = Button(base, text="Next", command=nextSol, bg="#0E7344", fg="#F2B705", font=(
    "Arial", 12, BOLD), border=0, highlightthickness=0.5, highlightbackground="#025939", state="disabled")
nextButton.place(x=70, y=430, width=160, height=40)

label = Label(base, text="Number of possible solutions",
              font=("Arial", 10), bg="#025939", fg="#F2B705")
label.place(x=30, y=497)

nSol = Entry(base, justify="center")
nSol.place(x=220, y=500, width=40, height=20)
nSol.insert(0, "1")
nSol.config(bg="#F2B705", font=("Arial", 12), fg="#025939",
            highlightthickness=0.5, highlightbackground="#025939", border=0)

nSolLabel = Label(base, text="", font=(
    "Arial", 10), bg="#025939", fg="#F2B705")
nSolLabel.place(x=300, y=497)

base.mainloop()
