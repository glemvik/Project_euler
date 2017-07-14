# -*- coding: utf-8 -*- 
# Problem URL: https://projecteuler.net/problem=81
""" 
 
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.

$$
\begin{pmatrix}
\color{red}{131} & 673 & 234 & 103 & 18\\
\color{red}{201} & \color{red}{96} & \color{red}{342} & 965 & 150\\
630 & 803 & \color{red}{746} & \color{red}{422} & 111\\
537 & 699 & 497 & \color{red}{121} & 956\\
805 & 732 & 524 & \color{red}{37} & \color{red}{331}
\end{pmatrix}
$$

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.
 
"""

from time import time

def minimal_path(matrix):
    """
    Returns the value of the smallest value path from top left corner to bottom 
    right corner of a matrix, by only moving right or down.
    """
    for row in range(0,len(matrix)):
        for col in range(0,len(matrix[row])):
            
            # IF IN TOP LEFT CORNER
            if row == 0 and col == 0:
                continue
            
            # IF ON TOP EDGE OF MATRIX
            if row == 0 and col > 0:
                matrix[row][col] += matrix[row][col-1]
            
            # IF ON LEFT EDGE OF MATRIX
            if row > 0 and col == 0:
                matrix[row][col] += matrix[row-1][col]
            
            # IF NOT ON ANY EDGE OF MATRIX
            if row > 0 and col > 0:
                matrix[row][col] += min(matrix[row][col-1], matrix[row-1][col])
                
    dimension = len(matrix) - 1
    
    return matrix[dimension][dimension]


start_time = time()

# READ MATRIX FROM FILE AND SAVE AS TWO DIMENSIONAL ARRAY
matrix = []
with open('p081_matrix.txt') as file:
    for line in file:
        row = [int(entry) for entry in line.strip().split(',')]

        matrix.append(row)
   
# PRINT RESULT
result = minimal_path(matrix)
print(result)

print('Time:', time() - start_time)