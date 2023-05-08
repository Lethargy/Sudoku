class Sudoku:
    '''
    Representation of the sudoku puzzle.
    ...
    
    Attributes
    ----------
    M : 2D array of integers
        (M)atrix of size 9x9 representing the grid
        blanks are represented by 0's
    K : dictionary
        Summary of the (K)nown squares
        (key:value) pairs are of the form (i,j):v
            i: int, row (0 base) index
            j: int, column index
            v: int, value at square (i,j)
    C : dictionary
        Summary of the (C)andidates for blank squares
        (key:value) pairs are of the form (i,j):{v1,...,vk}
            i and j are the same as in K, but specify a blank square
            v1,...,vk are candidate values at that blank square
    N : dictionary
        Categorization of blank squares by (N)umber of candidates
        (key:value) pairs are of the form n:{(i1,j1),...,(ik,jk)}
            n: int, number of candidates at the squares
            (i1,j1),...,(ik,jk)
    L : int
        (L)east number of candidates among all blank squares
        if L = 1, at least one blank square is obvious
        if L = 0, the puzzle is impossible
        if L = 2 or greater, we need to start guessing
        if L = -1, the puzzle is solved, and we are done
        
    Methods
    -------
    update(n, m, val)
        Updates sudoku puzzle with a known (val)ue at square (n,m).
    '''
    def __init__(self, M):
        '''
        Parameters
        ----------
        M : 9x9 array of integers, see above
        '''
        self.M = M
        self.K = {(i,j): M[i][j] for i in range(9)
                  for j in range(9) if M[i][j] > 0}
        self.C = {(i,j): set(range(1,10)) for i in range(9)
                  for j in range(9) if M[i][j] == 0}
        
        # nested loop over blank squares and known squares
        for i,j in self.C.keys():
            for n,m in self.K.keys():
                
                same_row = i == n
                same_column = j == m
                same_block = (i // 3 == n // 3) and (j // 3 == m // 3)
                
                # if squares fall on same row, column, or 3x3 block...
                if same_row or same_column or same_block:
                     # ...cross out known value from candidates
                    self.C[(i,j)] = self.C[(i,j)] - {self.K[(n,m)]}
        
        # categorize blank squares by (N)umber of candidates
        self.N = {i:set() for i in range(10)}
        for (i,j), v in self.C.items():
            self.N[len(v)] = self.N[len(v)] | {(i,j)}
            
        # (L)east number of candidates among all blank squares
        self.L = min(n for n,v in self.N.items()
                     if len(v) > 0) if self.C else -1
        
    def __repr__(self):
        '''
        Prints out M, the numerical representation of the matrix.
        '''
        return '\n'.join(str(m) for m in self.M)
    
    def update(self, n, m, val):
        '''
        Updates sudoku puzzle with a known (val)ue at square (n,m).
        Value may be incorrect, resulting in an impossible puzzle.
        
        Parameters
        ----------
        n : int
            row index
        m : int
            column index
        val : int
            value at square (n,m)
        '''
        del self.C[(n,m)]
        self.K[(n,m)] = val
        self.M[n][m] = val

        for i,j in self.C.keys():
            
            row = i == n
            col = j == m
            block = (i // 3 == n // 3) and (j // 3 == m // 3)
            
            if row or col or block:
                self.C[(i,j)] = self.C[(i,j)] - {val}

        self.N = {i:set() for i in range(10)}
        for (i,j), v in self.C.items():
            self.N[len(v)] = self.N[len(v)] | {(i,j)}
            
        self.L = min(n for n,v in self.N.items()
                     if len(v) > 0) if self.C else -1
        
from copy import deepcopy

def solve(P):
    '''
    Solves sudoku (P)uzzle using recursive backtracking.
    
    Parameters
    ----------
    P : Sudoku
        The sudoku object must be initialized by a 9x9 array.
    '''
    
    # while there are obvious blanks, fill them in
    while P.L == 1:
        # get coordinates of blank square
        (i,j) = P.N[1].pop()
        
        # get value of blank square
        val = P.C[(i,j)].pop()
        
        # call update function
        P.update(i,j,val)

    if P.L > 0:
        # we have to start guessing
        # choose any square with least candidates
        (i,j) = P.N[P.L].pop()
        
        for r in P.C[(i,j)]: # choose candidate r
            
            # copy puzzle
            Q = deepcopy(P)
            
            # insert guess into copy
            Q.update(i,j,r)
            
            # recursive call
            Q = solve(Q)
            
            # solution is found
            if Q != None:
                return Q
    
    elif P.L == 0:
        # if puzzle is impossible, return None
        return None
    
    else:
        # we had it on the first guess
        return P
