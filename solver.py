import sudokuRequester

import numpy as np
import itertools

from collections import Counter
from colorama import Fore, Back, Style, init
from termcolor import colored

#Constants
INDICES = list(range(8))

#init colorama
init()

def print_sudoku(new_state, state_before) -> None:
    output = ""
    for row, col in itertools.product(range(9), range(9)):
        if new_state[row][col] == state_before[row][col]:
            output += " " + str(new_state[row][col])
        else:
            output += " " + Fore.GREEN + str(new_state[row][col])
        
        if col != 8 and col % 3 == 2: output += " |"
        if col == 8 and row != 8: output += "\n"
        if row % 3 == 2 and col == 8 and row != 8: output += " - - - + - - - + - - -\n"
    
    print(output)

def solve(grid : list) -> np.ndarray:
    grid = np.array(grid)
    copied_grid = grid.copy()
    copied_grid[8][8] = 2
    print_sudoku(grid, copied_grid)

if __name__ == "__main__":
    grid = sudokuRequester.get_random_sudoko_difficulty("easy")
    solve(grid)