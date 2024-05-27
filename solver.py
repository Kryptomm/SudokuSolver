import sudokuRequester

import numpy as np
import itertools

from collections import Counter
from colorama import Fore, Back, Style, init
from termcolor import colored

#Constants
INDICES = list(range(9))

#init colorama
init()

#!GENERAL

def print_sudoku(new_state, state_before=None, possible_nums =None) -> None:
    output = ""
    for row, col in itertools.product(INDICES, INDICES):
        if state_before is not None and new_state[row][col] != state_before[row][col]:
            output += " " + Fore.GREEN + str(new_state[row][col])
        else:
            output += " " + str(new_state[row][col])
            
        output += Style.RESET_ALL
        
        if col != 8 and col % 3 == 2: output += " |"
        if col == 8 and row != 8:
            if possible_nums is not None:
                for col in INDICES:
                    if len(possible_nums[row][col]) > 0:
                        output += f" {str(possible_nums[row][col]):<15}"
                    else: output += f" {str([]):<15}"
            output += "\n"
        if row % 3 == 2 and col == 8 and row != 8: output += " - - - + - - - + - - -\n"
    output += "\n"
    print(output)

def is_solved(grid):
    return np.all(grid)

def get_possible_numbers(grid) -> np.ndarray:
    return np.array([[set([i+1 for i in INDICES]) if grid[y][x] == 0 else set() for x in INDICES] for y in INDICES])

#!SORTING OUT

def sort_out_rows(grid, possible_numbers):
    for row in INDICES:
        nums = set(grid[row])
        for col in INDICES:
            possible_numbers[row][col] -= nums

def sort_out_columns(grid, possible_numbers):
    for col in INDICES:
        nums = set(grid.T[col])
        for row in INDICES:
            possible_numbers[row][col] -= nums

def sort_out_boxes(grid, possible_numbers):
    for box_row in range(3):
        for box_col in range(3):
            box_top_left =      (box_row * 3, box_col * 3)
            box_bottom_right =  (box_row * 3 + 3, box_col * 3 + 3)
            
            box = grid[range(box_top_left[0], box_bottom_right[0]),:]
            box = box[:,range(box_top_left[1], box_bottom_right[1])]
            
            box = set(box.flatten())
            
            for row in range(box_top_left[0], box_bottom_right[0]):
                for col in range(box_top_left[1], box_bottom_right[1]):
                    possible_numbers[row][col] -= box

def sort_out_possible_numbers(grid, possible_numbers):
    sort_out_rows(grid, possible_numbers)
    sort_out_columns(grid, possible_numbers)
    sort_out_boxes(grid, possible_numbers)

#! PLACING

def place_lonely_numbers(grid, possible_numbers):
    placed = 0
    for row in INDICES:
            for col in INDICES:
                if len(possible_numbers[row][col]) != 1: continue
                
                elem = possible_numbers[row][col].pop()
                grid[row][col] = elem
                possible_numbers[row][col].add(elem)
                placed += 1
    return placed

def place_lonely_row_numbers(grid, possible_numbers):
        placed = 0
        for row in INDICES:
            flattened_list = [num for subset in possible_numbers[row] for num in subset]
            occurences = dict(Counter(flattened_list))
            
            for col in INDICES:
                for pn in possible_numbers[row][col]:
                    if occurences[pn] == 1:
                        grid[row][col] = pn
                        placed += 1
                        break
            
        return placed
    
def place_lonely_column_numbers(grid, possible_numbers):
        placed = 0
        for col in INDICES:
            flattened_list = [num for subset in possible_numbers.T[col] for num in subset]
            occurences = dict(Counter(flattened_list))
            
            for row in INDICES:
                for pn in possible_numbers[row][col]:
                    if occurences[pn] == 1:
                        grid[row][col] = pn
                        placed += 1
                        break
            
        return placed
    
def place_lonely_box_numbers(grid, possible_numbers):
    placed = 0
    for box_row in range(3):
        for box_col in range(3):
            box_top_left =      (box_row * 3, box_col * 3)
            box_bottom_right =  (box_row * 3 + 3, box_col * 3 + 3)
            
            box = possible_numbers[range(box_top_left[0], box_bottom_right[0]),:]
            box = box[:,range(box_top_left[1], box_bottom_right[1])]
            box = box.flatten()
            
            flattened_list = [num for subset in box for num in subset]
            occurences = dict(Counter(flattened_list))
            
            for row in range(box_top_left[0], box_bottom_right[0]):
                for col in range(box_top_left[1], box_bottom_right[1]):
                    for pn in possible_numbers[row][col]:
                        if occurences[pn] == 1:
                            grid[row][col] = pn
                            placed += 1
                            break

    return placed

def place_possible_numbers(grid, possible_numbers):
    placed = 0
    
    placed += place_lonely_numbers(grid, possible_numbers)
    placed += place_lonely_row_numbers(grid, possible_numbers)
    placed += place_lonely_column_numbers(grid, possible_numbers)
    placed += place_lonely_box_numbers(grid, possible_numbers)
    
    return placed

def solve(grid):
    grid = np.array(grid)
    iter = 1
    
    print(f"Given Sudoku:")
    print_sudoku(grid)
    
    while not is_solved(grid) and iter < 81:
        print(f"Iteration {iter}:")
        
        possible_numbers = get_possible_numbers(grid)
        old_grid = np.copy(grid)
        
        sort_out_possible_numbers(grid, possible_numbers)
        placed = place_possible_numbers(grid, possible_numbers)
        
        print_sudoku(grid, state_before=old_grid)
        
        if placed == 0:
            print("Could not finish the Sudoku.")
            print_sudoku(grid, state_before=old_grid, possible_nums=possible_numbers)
            return False
        
        iter += 1
        
    return True

if __name__ == "__main__":
    grid = sudokuRequester.get_random_sudoko_difficulty("medium")
    solve(grid)