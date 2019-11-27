import argparse
from tkinter import Tk
from SudokuUI import *
from SudokuGame import *




TABLEROS=["debug","MeCagoEnFranco","ForceError"]
MARGINS= 20
SIDE = 50
WIDTH = HEIGHT = MARGINS*2 + SIDE * 9

def parse_args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--board",
                            help="Nombre del Tablero Requerido",
                            type=str,
                            choices=TABLEROS,
                            required=True)

    # Creates a dictionary of keys = argument flag, and value = argument
    args = vars(arg_parser.parse_args())
    return args['board']

if __name__ == '__main__':
    board_name = parse_args()

    with open('%s.sudoku' % board_name, 'r') as boards_file:
        game = SudokuGame(boards_file)
        game.start()

        root = Tk()
        SudokuUI(root, game)
        root.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
        root.mainloop()