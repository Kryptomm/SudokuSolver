import sudokuRequester
import numpy as np

from typing import List, Tuple

class Sudoku:
    def __init__(self, grid : List, box_size : Tuple[int, int] = (3, 3)) -> None:
        self.grid = np.array(grid)
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.box_size = box_size

    def __repr__(self) -> str:
        output = ""
        for y in range(self.rows):
            for x in range(self.cols):
                output += str(self.grid[y][x]) + " "
            output += "\n" if y != 8 else ""
        return output
    
if __name__ == "__main__":
    grid = sudokuRequester.get_random_sudoko_difficulty("easy")
    sudoku = Sudoku(grid)
    print(sudoku)