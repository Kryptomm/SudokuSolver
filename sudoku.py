import sudokuRequester
import numpy as np

from typing import List, Tuple, Union

class Sudoku:
    def __init__(self, grid : Union[List, str], box_size : Tuple[int, int] = (3, 3), rows=9, cols=9) -> None:
        """
        -box_size = (size right, size down)
        """
        self.grid = None
        if type(grid) is str:
            self.grid = self.__convert_string_to_grid(grid, rows, cols)
        else:
            self.grid = np.array(grid)
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        self.box_size = box_size

        if self.rows % box_size[1] != 0:
            raise Exception("Rows and Box Row size does not match")

        if self.cols % box_size[0] != 0:
            raise Exception ("Columns and Box Columns size does not match")
        self.box_rows = self.rows // box_size[1]
        self.box_cols = self.cols // box_size[0]

    def __convert_string_to_grid(self, grid : str, rows : int, cols : int) -> np.ndarray:
        grid = np.array([int(a) for a in grid])
        grid.shape = (rows, cols)
        return np.array(grid)
    
    def __repr__(self) -> str:
        output = ""
        for y in range(self.rows):
            for x in range(self.cols):
                output += str(self.grid[y][x]) + " "
            output += "\n" if y != 8 else ""
        return output
    
if __name__ == "__main__":
    grid = "102004070890176045060000198700000926025760081900201000000097060608003000009008032"
    sudoku = Sudoku(grid)