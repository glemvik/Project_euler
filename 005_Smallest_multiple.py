# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 19:12:41 2016

Finds the smallest positive number that is evenly divisible by all of the 
numbers from 1 to a given limit

Solution is found in less than 1 second.

@author: gunvor
"""

from time import time

def lowest_common_multiple(limit):
    lcm = [2] # ASSUMES LIMIT LARGER THAN 2

    # FIND LOWEST COMMON MULTIPLE
    for i in range(2, limit + 1):
        number = i
        index = 0
        
        # ADDS MISSING FACTORS OF i TO lcm
        while True:
            if number / lcm[index] == 1: # ALL FACTORS ARE IN lcm
                break

            # IF NUMBER DIVISIBLE BY CURRENT FACTOR: DIVIDE
            if number / lcm[index] == number // lcm[index]:
                number = number / lcm[index]

            #EXAMINE FURTHER
            index += 1

            # END OF lcm: ADD NUMBER AS FACTOR IN lcm
            if index == len(lcm):
                lcm.append(number)
                break
    
    # MULTIPLY ALL FACTORS IN lcm
    result = 1
    for i in lcm:
        result *= i
    
    return int(result)


# INITIALIZING
start_time = time()
limit = 20

number = lowest_common_multiple(limit)

# RESULTS
print("Smallest number that is evenly divisible by all numbers from 1 to {} is {}".format(limit,number))
print('Time:', time() - start_time)
