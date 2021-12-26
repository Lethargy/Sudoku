def candidates(X):
    """
    Finds candidate digits for each blank square of 9 x 9 Sudoku grid.
    
    Parameters
    ----------
    X : 9 x 9 array of integers.
        The unsolved Sudoku grid.
        Unknown digits are denoted by 0.
        Known digits are denoted by their integer value.

    Returns
    ----------
    C : 9 x 9 array of sets (or possibly NoneTypes).
        If the (i,j) square of X is unknown, the (i,j) entry of C lists its candidate digits.
        If the (i,j) square of X is known, the (i,j) entry of C is a NoneType.
        Expects a Python array.
    
    N : Array of integers, length 81.
        The sizes of each set in C.
        NoneTypes are given the size inf.
        C[0][0] through C[0][8] are stored in N[0] through N[8].
        C[1][0] through C[1][8] are stored in N[9] through N[16].
        The array is 1 dimensional to faciliate searches.
    
    solvabe: boolean.
        False if the function detects X to be an impossible puzzle.
        (It may fail to do so.)
        Otherwise, True.
    """
    
    # Initialize variables.
    solvable = True
    C = [None] * 9
    for i in range(9):
        C[i] = [None for j in range(9)]
        
    # Fill in C.
    for i in range(9):
        for j in range(9):
            if X[i][j] == 0:
                # Assume all candidates 1,2,...,9 are possible.
                z = set(range(1,10))

                # Remove those in the same row, column, and 3x3 block.
                for n in range(9):
                    z = z - {X[n][j]}
                for m in range(9):
                    z = z - {X[i][m]}
                for n in range(3*(i//3), 3*(i//3)+3):
                    for m in range(3*(j//3), 3*(j//3)+3):
                        z = z - {X[n][m]}

                # Store remainder in C.
                C[i][j] = z
                
                # If an unknown square has no candidates, the puzzle is unsolvable. 
                if len(C[i][j]) == 0:
                    solvable = False
                    
    # Compute lengths of each set in C.
    N = [len(C[i][j]) if C[i][j] != None else float('inf')
         for i in range(9) for j in range(9)]
    return C, N, solvable
    
def sudoku(X):
    """
    Solves the Sudoku puzzle.
    
    Parameters
    ----------
    X : 9 x 9 array of integers.
        The unsolved Sudoku grid.
        Unknown digits are denoted by 0.
        Known digits are denoted by their integer value.
        
    Returns
    ----------
        If X admits a solution, returns 9 x 9 array of integers.
        The solved Sudoku grid.
        
        If X does not admit a solution, returns None.
    """
    
    # Fill in all singletons until guesswork is needed.
    C, N, solvable = candidates(X)
    while 1 in N and solvable:
        i = N.index(1) // 9
        j = N.index(1) % 9
        X[i][j] = C[i][j].pop()
        C, N, solvable = candidates(X)
        
    # Return None for impossible puzzles.
    if not solvable:
        return
        
    # If there are still blanks:
    if any(X[i][j] == 0 for i in range(9) for j in range(9)):
        
        # Choose a square with the least number of candidates.
        i = N.index(min(N)) // 9
        j = N.index(min(N)) % 9
        
        # Keep a copy of the puzzle as it is.
        Y = [[] + row for row in X]
        
        # For each candidate in the shortest list:
        for r in C[i][j]:
            
            # Make a separate copy of the puzzle.
            X = [[] + row for row in Y]
            
            # Insert tentative value.
            X[i][j] = r
            
            # Recursive call.
            X = sudoku(X)
            
            # Solution found.
            if X != None and all(X[i][j] > 0 for i in range(9) for j in range(9)):
                return X
            
    # Return solution from original function call.
    else:
        return X
        
def recordsudoku(X,f):
    """
    Solves the Sudoku puzzle and records progress.
    
    Parameters
    ----------
    X : 9 x 9 array of integers.
        The unsolved Sudoku grid.
        Unknown digits are denoted by 0.
        Known digits are denoted by their integer value.
        
    f : File object, opened in 'w' mode.
        Text file to store intermediate steps in solving.
        
    Returns
    ----------
        If X admits a solution, returns 9 x 9 array of integers.
        The solved Sudoku grid.
        
        If X does not admit a solution, returns None.
    """
       
    # Fill in all singletons until guesswork is needed.
    C, N, solvable = candidates(X)
    while 1 in N and solvable:
        i = N.index(1) // 9
        j = N.index(1) % 9
        X[i][j] = C[i][j].pop()
        C, N, solvable = candidates(X)
        
    # If puzzle is impossible, write "Wrong guess." and return nothing.
    if not solvable:
        f.write("Wrong guess.\n\n")
        return
        
    # If there are still blanks:
    if any(X[i][j] == 0 for i in range(9) for j in range(9)):
        
        # Choose a square with the least number of candidates.
        i = N.index(min(N)) // 9
        j = N.index(min(N)) % 9
        
        # Keep a copy of the puzzle as it is.
        Y = [[] + row for row in X]
        
        # For each candidate in the shortest list:
        for r in C[i][j]:
            
            # Make a separate copy of the puzzle.
            X = [[] + row for row in Y]
            
            # Insert tentative value.
            X[i][j] = r
            
            # Record the guess and the square.
            f.write("Try {} in square ({},{}).\n".format(r, i+1, j+1))
            
            # Record the puzzle.
            for k in range(9):
                f.write(str(X[k]) + '\n')
            f.write('\n')
            
            # Recursive call.
            X = recordsudoku(X,f)
            
            # Solution found.
            if X != None and all(X[i][j] > 0 for i in range(9) for j in range(9)):
                return X
    else:
        
        # Announce solution from original function call.
        f.write('We found the solution:\n')
        for k in range(9):
            f.write(str(X[k]) + '\n')
        return X