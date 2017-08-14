# -*- coding: utf-8 -*- 
# Problem URL: https://projecteuler.net/problem=83
""" 
 
NOTE: This problem is a significantly more challenging version of Problem 81.
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by moving left, right, up, and down, is indicated in bold red and is equal to 2297.

$$
\begin{pmatrix}
\color{red}{131} & 673 & \color{red}{234} & \color{red}{103} & \color{red}{18}\\
\color{red}{201} & \color{red}{96} & \color{red}{342} & 965 & \color{red}{150}\\
630 & 803 & 746 & \color{red}{422} & \color{red}{111}\\
537 & 699 & 497 & \color{red}{121} & 956\\
805 & 732 & 524 & \color{red}{37} & \color{red}{331}
\end{pmatrix}
$$

Find the minimal path sum, in matrix.txt (right click and 
"Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by moving left, right, up, and down.
 
"""


from time import time
from math import inf
import queue


DEBUG = False

def dprint(*args):
    if DEBUG:
        print(*args)

def minimal_path(value_matrix):
    """
    Returns the value of the smallest value path from a specified entry in the 
    left column to anywhere in the right column in a matrix, by only moving up, 
    down or right.
    """
    
    # GET DIMENSIONS OF VALUE MATRIX
    row_dim = len(value_matrix)
    col_dim = len(value_matrix[0])
    
    # PREPARE MATRIX WHICH CONTAINS VALUE OF MINIMAL PATH TO ALL ENTRIES
    path_matrix = [[inf for entry in value_matrix[0]] for entry in value_matrix]
    path_matrix[0][0] = value_matrix[0][0]
    
    
    # FIND VALUE OF MINIMAL PATH FROM TOP LEFT CORNER TO BOTTOM RIGHT CORNER
    for row in range(0,row_dim):
        for col in range(0, col_dim):
            update_shortest_path(row, col, value_matrix, path_matrix)
    
    for row in path_matrix:
        dprint(row)
    
    # RETURN VALUE OF MINIMAL PATH
    return path_matrix[row_dim - 1][col_dim - 1]
    

def update_shortest_path(x, y, value_matrix, path_matrix):
    
    # CREATE QUEUE OF COORDINATES
    to_update = queue.Queue()
    to_update.put((x,y))
    
    dprint('Working on ({},{})'.format(x,y))
    
    while not to_update.empty():
        x, y = to_update.get()

        dprint('Updating ({},{})'.format(x,y))

        smallest_value, neighbours = get_smallest_neighbour_value(x, y, path_matrix)
        
        # CHECK IF CURRENT VALUE OF MINIMAL PATH IS CORRECT
        if smallest_value + value_matrix[x][y] < path_matrix[x][y]:
            
            path_matrix[x][y] = smallest_value + value_matrix[x][y]
            
            dprint('Changing path to ({},{}) to {}'.format(x, y, path_matrix[x][y]))
            
            # NEED TO UPDATE VALUES OF MINIMAL PATHS OF ALL NEIGHBOURS            
            for neighbour in neighbours:
                x, y = neighbour
                if path_matrix[x][y] < inf:
                    to_update.put(neighbour)
    dprint()


def get_smallest_neighbour_value(x, y, path_matrix):
    
    # GET DIMENSIONS OF MATRIX
    x_dim = len(path_matrix)
    y_dim = len(path_matrix[0])
    
    neighbours = set()
    smallest_value = inf    

    # ADD NEIGHBOURS AND FIND VALUE OF MINIMAL NEIGHBOUR PATH
    if x > 0:
        neighbours.add((x-1,y))
        
        if path_matrix[x-1][y] < smallest_value:
            smallest_value = path_matrix[x-1][y]
        
    if y > 0:
        neighbours.add((x,y-1))
        
        if path_matrix[x][y-1] < smallest_value:
            smallest_value = path_matrix[x][y-1]
            
    if x < x_dim - 1:
        neighbours.add((x+1,y))
        
        if path_matrix[x+1][y] < smallest_value:
            smallest_value = path_matrix[x+1][y]
            
    if y < y_dim - 1:
        neighbours.add((x,y+1))

        if path_matrix[x][y+1] < smallest_value:
            smallest_value = path_matrix[x][y+1]
    
    return smallest_value, neighbours


    


start_time = time()


# MATRIX FROM EXMAPLE
example_matrix = [[131,673,234,103,18],
                  [201,96,342,965,150],
                  [630,803,746,422,111],
                  [537,699,497,121,956],
                  [805,732,524,37,331]]

# READ MATRIX FROM FILE AND SAVE AS TWO DIMENSIONAL ARRAY
matrix = []
with open('p083_matrix.txt') as file:
    for line in file:
        row = [int(entry) for entry in line.strip().split(',')]

        matrix.append(row)

# PRINT RESULT
result = minimal_path(matrix)
print(result)

print('Time:', time() - start_time)