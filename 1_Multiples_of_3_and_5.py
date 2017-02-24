# -*- coding: utf-8 -*-
"""
Finds sum of all numbers, less than a given limit, that are divisible by 3 or 5

Solution is found in less than 1 second.

@author: gunvor
"""
from time import time

def find_sum(limit):
    result = 0
    
    #FINDS ALL MULTIPLES
    for i in range(3, limit):
        if i % 3 == 0 or i % 5 == 0: #IF MULTIPLE OF 3 OR 5
            #print(i, end=" ")
            result += i

    return result

# INITIALIZING
start_time = time()
limit = 1000

number = find_sum(limit)

# RESULTS
print('Sum of multiples of 3 or 5, less than {} is {}'.format(limit, number))
print('Time:', time() - start_time)