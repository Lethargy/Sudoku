# Sudoku
I present a sudoku solver written in Python, adapted from the MatLab code from Cleve Moler [[1]](#1).

# Description
Sudoku is a puzzle game whose objective is to fill a 9 × 9 grid with the digits 1, 2, ... ,9 so that each row, column, and 3 × 3 "subgrid" contains exactly one of each digit. The 9 × 9 grid is presented partially filled with enough digits to ensure a unique solution. It is known that there are at least 17 digits needed for this task [[2]](#2).

The solver that I present here uses recursive backtracking.

# Contents of `sudoku.py`
## The `Sudoku` class
An encapsulation of the sudoku puzzle. Known squares are represented by dictionaries with keys that correspond to coordinates and values that correspond to the numbers at those coordinates. Blank squares are represented similarly, but its dictionary values are sets containing candidates. Another dictionary categorizes the blank squares by their number of candidates.

Although the code is heavily adapted from Cleve Moler, my code starts guessing at the blank square with the the least candidates.

# Demonstration
We demonstrate the code on some well-known sudoku puzzles.

- Arto Inkala's _Everest_
- Arto Inkala's _Al Escargot_

# Dependencies
My code uses no libraries, but was written with Python version 3.8.

# References
<a id="1">[1]</a> 
Moler, C., 2009: _Solving Sudoku with MATLAB._
https://www.mathworks.com/company/newsletters/articles/solving-sudoku-with-matlab.html
(Accessed December 24, 2021).

<a id="2">[2]</a>
McGuire, G., Tugemann, B., and Civario, G., 2012: _There is no 16-Clue Sudoku: Solving the Sudoku Minimum Number of Clues Problem._
https://www.math.ie/McGuire_V1.pdf
(Accessed December 24, 2021).
