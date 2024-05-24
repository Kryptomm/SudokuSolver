from ast import Return
import numpy as np
import sudokuRequester
from sudoku import Sudoku

class Solver:
    def __init__(self, sudoku : Sudoku) -> None:
        self.sudoku = sudoku
        self.possibleNumbers = []

        self.__reset_possible_numbers()
        print("Sudoku loaded")

    def __reset_possible_numbers(self) -> None:
        self.possibleNumbers = [[set([i+1 for i in range(self.sudoku.box_size[0] * self.sudoku.box_size[1])]) if self.sudoku.grid[y][x] == 0 else set() for x in range(self.sudoku.cols)] for y in range(sudoku.rows)]

    def __sort_out_rows(self) -> None:
        for row in range(self.sudoku.rows):
            nums = set(self.sudoku.grid[row])
            for col in range(self.sudoku.cols):
                self.possibleNumbers[row][col] -= nums

    def __sort_out_columns(self) -> None:
        for col in range(self.sudoku.cols):
            nums = set(self.sudoku.grid.T[col])
            for row in range(self.sudoku.rows):
                self.possibleNumbers[row][col] -= nums

    def __sort_out_possible_numbers(self) -> None:
        self.__sort_out_rows()
        self.__sort_out_columns()

    def __place_lonely_numbers(self) -> int:
        placed = 0
        for row in range(self.sudoku.rows):
            for col in range(self.sudoku.cols):
                if len(self.possibleNumbers[row][col]) != 1: continue

                self.sudoku.grid[row][col] = self.possibleNumbers[row][col].pop()
                placed += 1
        return placed

    def __place_possible_numbers(self) -> int:
        placed = 0

        placed += self.__place_lonely_numbers()

        return placed

    def is_solved(self) -> bool:
        return np.all(self.sudoku.grid)

    def solve(self) -> bool:
        iter = 0
        while not self.is_solved():
            self.__reset_possible_numbers()
            print(self.sudoku)
            print(f"Iteration: {iter}")
            self.__sort_out_possible_numbers()

            if self.__place_possible_numbers() == 0:
                return False

            #Security for no endless loop
            if iter > self.sudoku.rows * self.sudoku.cols:
                return False
            iter += 1
        return True

if __name__ == "__main__":
    grid = sudokuRequester.get_random_sudoko_difficulty("easy")
    sudoku = Sudoku(grid)
    solver = Solver(sudoku)
    print(solver.solve())