# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 23:55:08 2016

Solution is found in less than 1 second.

@author: gunvor
"""

from time import time

def find_difference(limit):
    sum_of_squares = 0
    square_of_sum = 0
    
    for i in range(1, limit + 1):
        sum_of_squares += i**2
        square_of_sum += i
        
    square_of_sum = square_of_sum**2
    
    return (square_of_sum - sum_of_squares)
    #print("Difference between sum of squares and square of sum of the first", limit, 
    #"natural numbers is:", square_of_sum - sum_of_squares)

# INITIALIZING
start_time = time()
limit = 100    
    
difference = find_difference(limit)

# RESULTS
print('Difference between sum of squares and square of sum of the first {} natural numbers is {}'.format(limit, difference))
print('Time:', time() - start_time)