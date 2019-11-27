
class SudokuGame(object):

    def __init__(self,fileTablero):
        self.fileTablero=fileTablero
        self.EmpezarJuego = SudokuGame(fileTablero).board

    def start(self):
        self.GameOver = False
        self.juego = []
        for i in range(9):
            self.juego.append([])
            for j in range(9):
                self.juego[i].append(self.EmpezarJuego[i][j])

    def verificarWin(self):
        for row in range(9):
            if not self.__validarFila(row):
                return False
        for column in range(9):
            if not self.__validarColumna(column):
                return False
        for row in range(3):
            for column in range(3):
                if not self.__validarCuadrado(row, column):
                    return False
        self.GameOver = True
        return True

    def __validarBloque(self, bloque):
        return set(bloque) == set(range(1, 10))

    def __validarFila(self,row):
        return self.__validarBloque(self.juego[row])

    def __validarColumna(self,columna):
        return self.__validarBloque(
            [self.juego[row][columna] for row in range(9)]
        )

    def __validarCuadrado(self, row, column):
        return self.__validarBloque(
            [
                self.puzzle[r][c]
                for r in range(row*3, (row+1)*3)
                for c in range(column*3, (column+1)*3)
            ]
        )