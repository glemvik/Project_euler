# -*- coding: utf-8 -*- 
# Problem URL: https://projecteuler.net/problem=76
""" 
 
It is possible to write five as a sum in exactly six different ways:
4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1
How many different ways can one hundred be written as a sum of at least two positive integers?
 
"""
from time import time

DEBUG = True

def dprint(*args):
    if DEBUG:
        print(*args)


def number_of_summations(number):
    """
    Returns the number of different ways 'number' can be written as a sum of
    at least two positive integers.
    """
    
    # PREPARE TABLE FOR CALCULATING SUMMATIONS
    summations = [[1 for i in range(number)] for j in range(number)]
    
    # CALCULATE SUMMATIONS
    for row in range(1,number):
        for col in range(number):
            
            # The new digit is larger than the number we wish to write:
                # the number of summations is the same as before
            if col < row:
                summations[row][col] = summations[row-1][col]
                
            # The new digit is exactly the number we wish to write:
                # the number of summations increase by one
            elif row == col:
                summations[row][col] = summations[row-1][col] + 1
                
            # The new digit is larger than the number we wish to write:
                # the number of summations increase by the number of summations 
                # of (number - new digit)
            else:
                summations[row][col] = summations[row-1][col] + summations[row][col-row - 1]
    
    # Return the number of summations of 'number' (excluding the use of the 'number' itself)
    return summations[number-1][number-1] - 1



#------------------------------------------------------------------------------
#---------------------------------- M A I N -----------------------------------
#------------------------------------------------------------------------------

start_time = time()

number = 100

print(number_of_summations(number))
print('Time:', time() - start_time)