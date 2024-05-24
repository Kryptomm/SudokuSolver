import numpy as np

sudoku = np.array([[1,2],[4,0],[7,8]])

A = np.array = [[set([i+1 for i in range(6)]) if sudoku[y][x] == 0 else set() for x in range(2)] for y in range(3)]

for i in A:
    print(i)