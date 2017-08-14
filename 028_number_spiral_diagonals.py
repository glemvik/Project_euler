# -*- coding: utf-8 -*- 
# Problem URL: https://projecteuler.net/problem=28
""" 
 
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 1217 16 15 14 13
It can be verified that the sum of the numbers on the diagonals is 101.
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
 
"""

from time import time


DEBUG = False

def dprint(*args):
    if DEBUG:
        print(*args)
        
def sum_of_diagonals(dimension):
    """
    Returns the sum of the numbers on the diagonals in a dimension*timension 
    spiral.
    """
    # CALCULATE VALUE OF THE END OF THE SPIRAL (LARGEST-VALUE OUTER CORNER)
    number = dimension*dimension
    total_sum = number
    
    # THE DISTANCE TO THE NEXT NUMBER WHICH IS ON THE DIAGONAL
    distance_to_diagonal = dimension - 1
    
    # WORK OUR WAY INWARDS ON THE SPIRAL
    while distance_to_diagonal > 1:
        
        # CALCULATE THE NUMBERS LOCATED ON THE CORNERS OF THE CURRENT 'LAYER' 
        # OF THE SPIRAL
        for i in range(4):
            number = number - distance_to_diagonal
            total_sum += number
        
        # MOVE ONE 'LAYER' INWARDS ON THE SPIRAL
        distance_to_diagonal -= 2
    
    return total_sum


#------------------------------------------------------------------------------
#---------------------------------- M A I N -----------------------------------
#------------------------------------------------------------------------------

start_time = time()

dimension = 1001
example_dimension = 5

print(sum_of_diagonals(dimension))
print('Time:', time() - start_time)