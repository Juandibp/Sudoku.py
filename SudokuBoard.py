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