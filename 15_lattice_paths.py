# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 21:02:14 2016

PROBLEM:

Starting in the top left corner of a 2×2 grid, and only being able to 
move to the right and down, there are exactly 6 routes to the bottom 
right corner.
How many such routes are there through a 20×20 grid?

Solution is found in less than 1 second.

@author: gunvor
"""

from time import time

start_time = time()

# REPRESENTING THE VERTICES IN THE GRID AS A TWO DIMENSIONAL LIST
dimension = 20
grid = []

# CREATING AND INITIALIZING GRID
for row in range(0, dimension+1):
    grid.append([0 for col in range(0, dimension+1)])

# FOR ALGORITHM TO WORK, TOP RIGHT CORNER OF GRID MUST INITIALLY BE 1
grid[0][0] = 1

# FINDING NUMBER OF ROUTES:
"""The number of routes to any vertex is the sum of the number of routes 
to the vertices directly above and directly to the left of the vertex."""
for row in range(0, dimension+1):
    for col in range(0, dimension+1):
        if row == 0:
            if col > 0:
                grid[row][col] = grid[row][col-1]
        if col == 0:
            if row > 0:
                grid[row][col] = grid[row-1][col]
        if row > 0 and col > 0:
            grid[row][col] = grid[row][col-1] + grid[row-1][col]

# RESULTS
print('Number of routes are:', grid[dimension][dimension])
print("Time:", time() - start_time)