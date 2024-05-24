import sudokuRequester
import numpy as np

from typing import List, Tuple

class Sudoku:
    def __init__(self, grid : List, box_size : Tuple[int, int] = (3, 3)) -> None:
        """
        -box_size = (size right, size down)
        """
        self.grid = np.array(grid)
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.box_size = box_size

        if self.rows % box_size[1] != 0:
            raise Exception("Rows and Box Row size does not match")

        if self.cols % box_size[0] != 0:
            raise Exception ("Columns and Box Columns size does not match")
        self.box_rows = self.rows // box_size[1]
        self.box_cols = self.cols // box_size[0]

    def __repr__(self) -> str:
        output = ""
        for y in range(self.rows):
            for x in range(self.cols):
                output += str(self.grid[y][x]) + " "
            output += "\n" if y != 8 else ""
        return output
    
if __name__ == "__main__":
    grid = [[1,2,3],
            [4,5,6]]
    sudoku = Sudoku(grid, box_size=(1,2))
    print(sudoku, sudoku.box_rows, sudoku.box_cols)

    exit()
    grid = sudokuRequester.get_random_sudoko_difficulty("easy")
    sudoku = Sudoku(grid)
    print(sudoku)