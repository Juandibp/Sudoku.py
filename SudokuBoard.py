from SudokuError import *

class SudokuBoard(object):

    def __init__(self,fileTablero):
        self.tablero= self.__createBoard(fileTablero)

    def __createBoard(self,fileTablero):
        tablero=[]
        for line in fileTablero:
            line = line.strip()
            if len(line) !=9:
                raise SudokuError(
                    "Cada linea del tablero deben ser de 9 de largo"
                )
            tablero.append([])

            for c in line:
                if not c.isdigit():
                    raise SudokuError(
                        "Caracteres Validos solo son de 0-9"
                    )
                tablero[-1].append(int(c))
        if len(tablero)!=9:
            raise SudokuError("Cada Sudoku debe ser 9 lineas de largo")
        return tablero
