# -*- coding: utf-8 -*- 
# Problem URL: https://projecteuler.net/problem=82
""" 
 
NOTE: This problem is a more challenging version of Problem 81.
The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell in the right column, and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.

$$
\begin{pmatrix}
131 & 673 & \color{red}{234} & \color{red}{103} & \color{red}{18}\\
\color{red}{201} & \color{red}{96} & \color{red}{342} & 965 & 150\\
630 & 803 & 746 & 422 & 111\\
537 & 699 & 497 & 121 & 956\\
805 & 732 & 524 & 37 & 331
\end{pmatrix}
$$

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the left column to the right column.
 
"""

from time import time
from math import inf
from copy import deepcopy


DEBUG = False

def dprint(*args):
    if DEBUG:
        print(*args)

def minimal_path(row, col, matrix):
    """
    Returns the value of the smallest value path from a specified entry in the 
    left column to anywhere in the right column in a matrix, by only moving up, 
    down or right.
    """
    
    # GET DIMENSIONS OF MATRIX
    row_dim = len(matrix)
    col_dim = len(matrix[0])
    
    # PREPARE MATRIX WHICH KEEPS TRACK OF THE VISITED ENTRIES
    visited = [[False for entry in matrix[0]] for entry in matrix]
    visited[row][col] = True
    
    dprint('Row dimension: {}'.format(row_dim))
    dprint('Col dimension: {}'.format(col_dim))
    count = 0
    
    while col < col_dim:
        

        # CALCULATE PATH DOWN FROM CURRENT ENTRY
        
        dprint('Calculate path down from ({},{})'.format(row,col))
        
        for x in range(row+1,row_dim):
            
            dprint('Checking ({},{})'.format(x,col))
            if visited[x][col]:
                continue
            
            if col == 0:
                matrix[x][col] += matrix[x-1][col]
            else:
                matrix[x][col] += min(matrix[x-1][col], matrix[x][col-1])
            
            visited[x][col] = True
        dprint()
            
        
        # CALCULATE PATH UP FROM CURRENT ENTRY
        
        dprint('Calculate path up from ({},{})'.format(row,col))
        
        for x in range(row - 1, -1, -1):
            
            dprint('Checking ({},{})'.format(x,col))
            
            if visited[x][col]:
                continue
            
            if col == 0:
                matrix[x][col] += matrix[x+1][col]
            else:
                matrix[x][col] += min(matrix[x+1][col], matrix[x][col-1])
            
            visited[x][col] = True
        dprint()
            
        # CALCULATE ONE MOVE RIGHT FROM CURRENT ENTRY
        
        dprint('Calculate path right from ({},{})'.format(row,col))
        
        if col != col_dim - 1:
            
            
            dprint('Checking ({},{})'.format(row,col+1))
            
            if visited[row][col+1]:
                continue
            
            matrix[row][col+1] += matrix[row][col]

            
        
            visited[row][col+1] = True
        dprint()
        
        if col == col_dim - 1:
            break

        next_x,next_y = end_of_path(matrix,visited)
        
        dprint('NEXT: ({},{})'.format(next_x,next_y))
        
        
        # PREPARE TO MOVE TO END OF LEAST PATH
        row = next_x
        col = next_y


    # RETURN LEAST VALUE
    return matrix[row][col]
    

def end_of_path(matrix,visited):
    
    ends_of_paths = []
    
    for row in range(0,len(matrix)):
        for col in range(0,len(matrix[row])):
            
            if visited[row][col] and has_unvisited_neighbours(row,col,visited):
                ends_of_paths.append((row,col))
    
    
    dprint('Finding current shortest path:')
    dprint(ends_of_paths)
    least_value_path = inf
    for entry in ends_of_paths:
        
        row,col = entry
        
        dprint('({},{})'.format(row,col))
        if matrix[row][col] < least_value_path:
            least_value_path = matrix[row][col]
            coordinates = (row,col)
    
    return coordinates
    
def has_unvisited_neighbours(x,y,visited):
    
    dprint('Checking ({},{})'.format(x,y))
    
    if x < len(visited)-1 and visited[x+1][y] == False:
        dprint('Unvisited neighbour ({},{})'.format(x+1,y))
        return True
    if y < len(visited[x])-1 and visited[x][y+1] == False:
        dprint('Unvisited neighbour ({},{})'.format(x,y+1))
        return True
    if x > 0 and visited[x-1][y] == False:
        dprint('Unvisited neighbour ({},{})'.format(x-1,y))
        return True
    
    dprint('No unvisited neighbours')
    return False
    
def check_if_smallest(x, y, value, current_value, smallest_value):
    
    dprint('{} < {} and {} > {}?'.format(value, smallest_value, value, current_value))
    
    if value < smallest_value and value > current_value:
        
        dprint('True')
        
        return x, y, value
    
    dprint('False')
    
def continue_least_path(row,col,matrix):

    previous_paths = []
    x_dim = len(matrix) - 1
    
    # PATH UP
    if row > 0:
        previous_paths.append(matrix[row-1][col])
        
    # PATH DOWN
    if row < x_dim:
        previous_paths.append(matrix[row+1][col])
        
    # PATH RIGHT
    if col > 0:
        previous_paths.append(matrix[row][col-1])
    
    return min(previous_paths)
    

start_time = time()


# MATRIX FROM EXMAPLE
example_matrix = [[131,673,234,103,18],
                  [201,96,342,965,150],
                  [630,803,746,422,111],
                  [537,699,497,121,956],
                  [805,732,524,37,331]]

# READ MATRIX FROM FILE AND SAVE AS TWO DIMENSIONAL ARRAY
matrix = []
with open('p082_matrix.txt') as file:
    for line in file:
        row = [int(entry) for entry in line.strip().split(',')]

        matrix.append(row)

minimal_path_sums = []
for row in range(0,len(matrix)):
    working_matrix = deepcopy(matrix)
    minimal_path_sums.append(minimal_path(row,0,working_matrix))
    print('*')

#print(minimal_path(1,0,example_matrix))

# PRINT RESULT
result = min(minimal_path_sums)
print(minimal_path_sums)
print(result)

print('Time:', time() - start_time)