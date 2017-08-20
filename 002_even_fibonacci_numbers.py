# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 23:11:25 2016

Finds sum of even-valued terms in Fibonacci sequence, whose values are lower than a given limit

Solution is found in less than 1 second.

@author: gunvor
"""

from time import time

def find_sum(limit):
    result = 0
    a, b = 1, 1
    
    #CONSTRUCTING FIBONACCI SEQUENCE
    while b < limit:
        #print(b)
        
        if b % 2 == 0: #ADDING EVEN TERMS TO SUM
            result += b
        
        a, b = b, a + b
        
    return result

# INITIALIZING
start_time = time()
limit = 4000000

number = find_sum(limit)

# RESULTS
print('Sum of even-valued terms in Fibonacci sequence, whose values are lower than {} is {}'.format(limit, number))
print('Time:', time() - start_time)