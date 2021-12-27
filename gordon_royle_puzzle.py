from sudoku import *

X = [
    [0, 2, 0, 0, 3, 0, 0, 4, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 3],
    [0, 0, 4, 0, 0, 0, 5, 0, 0],
    [0, 0, 0, 8, 0, 6, 0, 0, 0],
    [8, 0, 0, 0, 1, 0, 0, 0, 6],
    [0, 0, 0, 7, 0, 5, 0, 0, 0],
    [0, 0, 7, 0, 0, 0, 6, 0, 0],
    [4, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 3, 0, 0, 4, 0, 0, 2, 0]
]

with open("Gordon_Royle.txt", 'w') as f:
    f.write("The puzzle to be solved:\n")
    for k in range(9):
        f.write(str(X[k]) + '\n')
    f.write('\n')
        
    recordsudoku(X,f)