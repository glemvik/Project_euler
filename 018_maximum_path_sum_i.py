# -*- coding: utf-8 -*- 
# Problem URL: https://projecteuler.net/problem=18
""" 
 
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
37 4
2 4 6
8 5 9 3
That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom of the triangle below:
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

Solution is found in less than 1 second.

@author: gunvor 
"""

from time import time
from copy import deepcopy

def find_maximum_path(triangle):
    
    # Copy of original triangle, to keep track of the maximum totals to entry (i,j)
    path_values = deepcopy(triangle)

    # Iterating over the triangle
    for row in range(1, len(triangle)):
        for col in range(0, row+1):
            
            # If entry is on left edge, only path is through left edge one level above entry
            if col == 0:
                path_values[row][col] = triangle[row][col] + path_values[row-1][col]
            # If entry is on right edge, only path is through right edge one level above entry
            elif col == row:
                path_values[row][col] = triangle[row][col] + path_values[row-1][col-1]
            # If entry not on edge - maximum path is through maximum of entries above
            else:
                path_values[row][col] = triangle[row][col] \
                + max(path_values[row-1][col], path_values[row-1][col-1])

    # Iterating through triangle of maximum values, to find path with largest value
    max_value = 0
    for row in path_values:
        for col in row:
            max_value = max(col, max_value)
            
    return max_value

# INITIALIZE
start_time = time()
input_triangle = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

# CONSTRUCT TRIANGLE IN TWO-DIMENSIONAL LIST
temp_triangle = input_triangle.split('\n')
triangle = []

for line in temp_triangle:
    row = line.split()
    triangle.append([int(number) for number in row])

# RESULTS
print('Maximum total from top to bottom of given triangle is', find_maximum_path(triangle))
print('Time:', time() - start_time)