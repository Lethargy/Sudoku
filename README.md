# Sudoku
I present a sudoku solver written in Python, adapted from the MatLab code from Cleve Moler [[1]](#1).

# Description
Sudoku is a puzzle game whose objective is to fill a 9 × 9 grid with the digits 1, 2, ... ,9 so that each row, column, and 3 × 3 "subgrid" contains exactly one of each digit. The 9 × 9 grid is presented partially filled with enough digits to ensure a unique solution. It is known that there are at least 17 digits needed for this task [[2]](#2).

The solver that I present here uses recursive backtracking.

# Dependencies
My code uses no libraries, but requires at least Python version 3.x. 

# References
<a id="1">[1]</a> 
Moler, C., 2009: Solving Sudoku with MATLAB.
https://www.mathworks.com/company/newsletters/articles/solving-sudoku-with-matlab.html
(Accessed December 24, 2021).

<a id="2">[2]</a>
McGuire, G., Tugemann, B., and Civario, G., 2012: There is no 16-Clue Sudoku: Solving the Sudoku Minimum Number of Clues Problem.
https://www.math.ie/McGuire_V1.pdf
(Accessed December 24, 2021).
