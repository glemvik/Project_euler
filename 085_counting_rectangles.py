# -*- coding: utf-8 -*- 
# Problem URL: https://projecteuler.net/problem=85
""" 
 
By counting carefully it can be seen that a rectangular grid measuring 3 by 2 
contains eighteen rectangles:

Although there exists no rectangular grid that contains exactly two million 
rectangles, find the area of the grid with the nearest solution. 
"""


from time import time
from math import inf

DEBUG = False
PROGRESS = False

def dprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)
        
def pprint(*args, **kwargs):
    if PROGRESS:
        print(*args, **kwargs)

def add_column(breadth, length):
    """
    Returns the number of new rectangles inside the grid if a new column is 
    added.
    """
    number_of_new_rectangles = 0
    
    # ADD NUMBER OF NEW (_x1)-SQUARES
    for b in range(1, breadth + 1):
        number_of_new_rectangles += b
    
        dprint('>({}x1) += {}'.format(b, breadth-b+1))
    dprint('>')
    
    # ADD ALL OTHER NEW RECTANGLES AND SQUARES
    for b in range(0,breadth):
        new_rectangles = (length - 1) * (breadth - b)
        number_of_new_rectangles += new_rectangles
        
        dprint('>({}x_) += {}'.format(b+1, new_rectangles))
    
    return number_of_new_rectangles

def add_row(breadth, length):
    """
    Returns the number of new rectangles inside the grid if a new row is added.
    """
    number_of_new_rectangles = 0
    
    # ADD NUMBER OF NEW (1x_)-SQUARES
    for l in range(1, length + 1):
        number_of_new_rectangles += l
        
        dprint('>(1x{}) += {}'.format(l, length-l+1))
    dprint('>')
    
    # ADD ALL OTHER NEW RECTANGLES AND SQUARES
    for l in range(0,length):
        new_rectangles = (breadth-1) * (length-l)
        number_of_new_rectangles += new_rectangles
        
        dprint('>(_x{}) += {}'.format(l+1, new_rectangles))
    
    return number_of_new_rectangles


#------------------------------------------------------------------------------
#---------------------------------- M A I N -----------------------------------
#------------------------------------------------------------------------------

start_time = time()

# GUESS DIMENSION OF GRID CONTAINING SOLUTION
dimension = 400
grid = [[0 for i in range(dimension)] for j in range(dimension)]

# INITIALIZE
limit = 2000000
difference = inf
l, b = (0,0)
grid[0][0] = 1

# SEARCH THROUGH GRID
for row in range(0,dimension):
    for col in range(row,dimension):
        if row == col:
            if row == 0:
                continue
            
            # IF FIRST ENTRY IN ROW: ADD NEW ROW (CALCULATE FROM ENTRY IN PREVIOUS ROW)
            grid[row][col] = grid[row-1][col] + add_row(row+1,col+1)
            
        else:
            # ADD NEW COLUMN (CALCULATE FROM ENTRY IN PREVIOUS COLUMN)
            grid[row][col] = grid[row][col-1] + add_column(row+1,col+1)
            
        # CHECK DISTANCE TO LIMIT
        d = abs(limit - grid[row][col])
        if d < difference:
            difference = d
            l, b = col+1, row+1
    
print('({}x{}), difference {}'.format(l,b, difference))
print('Time:', time() - start_time)