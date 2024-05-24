import numpy as np
import sudokuRequester

from sudoku import Sudoku
from collections import Counter

class Solver:
    def __init__(self, sudoku : Sudoku) -> None:
        self.sudoku = sudoku
        self.possibleNumbers = []

        self.__reset_possible_numbers()
        print("Sudoku loaded")

    def __reset_possible_numbers(self) -> None:
        self.possibleNumbers = np.array([[set([i+1 for i in range(self.sudoku.box_size[0] * self.sudoku.box_size[1])]) if self.sudoku.grid[y][x] == 0 else set() for x in range(self.sudoku.cols)] for y in range(sudoku.rows)])

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

    def __sort_out_boxes(self) -> None:
        for box_row in range(self.sudoku.box_rows):
            for box_col in range(self.sudoku.box_cols):
                box_top_left =      (box_row * self.sudoku.box_size[1], box_col * self.sudoku.box_size[0])
                box_bottom_right =  ((box_row + 1) * self.sudoku.box_size[1], (box_col + 1) * self.sudoku.box_size[0])
                
                box = self.sudoku.grid[range(box_top_left[0], box_bottom_right[0]),:]
                box = box[:,range(box_top_left[1], box_bottom_right[1])]

                box = set(box.flatten())
                for row in range(box_top_left[0], box_bottom_right[0]):
                    for col in range(box_top_left[1], box_bottom_right[1]):
                        self.possibleNumbers[row][col] -= box

    def __sort_out_possible_numbers(self) -> None:
        self.__sort_out_rows()
        self.__sort_out_columns()
        self.__sort_out_boxes()

    def __place_lonely_numbers(self) -> int:
        placed = 0
        for row in range(self.sudoku.rows):
            for col in range(self.sudoku.cols):
                if len(self.possibleNumbers[row][col]) != 1: continue
                
                elem = self.possibleNumbers[row][col].pop()
                self.sudoku.grid[row][col] = elem
                self.possibleNumbers[row][col].add(elem)
                placed += 1
                
        return placed

    def __place_lonely_row_numbers(self) -> int:
        placed = 0
        for row in range(self.sudoku.rows):
            flattened_list = [num for subset in self.possibleNumbers[row] for num in subset]
            occurences = dict(Counter(flattened_list))
            
            for col in range(self.sudoku.cols):
                for pn in self.possibleNumbers[row][col]:
                    if occurences[pn] == 1:
                        self.sudoku.grid[row][col] = pn
                        placed += 1
                        break
            
        return placed
    
    def __place_lonely_col_numbers(self) -> int:
        placed = 0
        
        for col in range(self.sudoku.cols):
            flattened_list = [num for subset in self.possibleNumbers.T[col] for num in subset]
            occurences = dict(Counter(flattened_list))
            
            for row in range(self.sudoku.rows):
                for pn in self.possibleNumbers[row][col]:
                    if occurences[pn] == 1:
                        self.sudoku.grid[row][col] = pn
                        placed += 1
                        break
        
        return placed
    
    def __place_lonley_box_numbers(self) -> int:
        placed = 0
        for box_row in range(self.sudoku.box_rows):
            for box_col in range(self.sudoku.box_cols):
                box_top_left =      (box_row * self.sudoku.box_size[1], box_col * self.sudoku.box_size[0])
                box_bottom_right =  ((box_row + 1) * self.sudoku.box_size[1], (box_col + 1) * self.sudoku.box_size[0])
                
                box = self.possibleNumbers[range(box_top_left[0], box_bottom_right[0]),:]
                box = box[:,range(box_top_left[1], box_bottom_right[1])]
                box = box.flatten()
                
                flattened_list = [num for subset in box for num in subset]
                occurences = dict(Counter(flattened_list))
                
                for row in range(box_top_left[0], box_bottom_right[0]):
                    for col in range(box_top_left[1], box_bottom_right[1]):
                        for pn in self.possibleNumbers[row][col]:
                            if occurences[pn] == 1:
                                self.sudoku.grid[row][col] = pn
                                placed += 1
                                break

        return placed
    
    def __place_possible_numbers(self) -> int:
        placed = 0

        placed += self.__place_lonely_numbers()
        placed += self.__place_lonely_row_numbers()
        placed += self.__place_lonely_col_numbers()
        placed += self.__place_lonley_box_numbers()

        return placed

    def is_solved(self) -> bool:
        return np.all(self.sudoku.grid)

    def solve(self) -> bool:
        iter = 1
        print(sudoku)
        while not self.is_solved():
            self.__reset_possible_numbers()
            print(f"Iteration: {iter}")
            self.__sort_out_possible_numbers()

            placed = self.__place_possible_numbers()
            print(f"Placed {placed} tiles!\n")
            if placed == 0:
                print(sudoku)
                for i in self.possibleNumbers:
                    print(i)
                return False

            print(self.sudoku)
            #Security for no endless loop
            if iter > (self.sudoku.rows * self.sudoku.cols):
                return False
            iter += 1
        return True

if __name__ == "__main__":
    grid = sudokuRequester.get_random_sudoko_difficulty("easy")
    
    sudoku = Sudoku(grid)
    solver = Solver(sudoku)
    print(solver.solve())
    