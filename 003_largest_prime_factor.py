# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 23:32:35 2016

Prints largest prime factor of a given number

Solution is found in less than 1 second.

@author: gunvor
"""

from math import ceil, sqrt
from time import time

def findFactors(number):
    divisor = 2
    while(number > 1 and divisor < ceil(sqrt(number))):
        if number % divisor == 0:
            number = number // divisor
        else:
            divisor += 1
    return number
    
# INITIALIZING
start_time = time()
number = 600851475143

largest_factor = findFactors(number)

# RESULTS
print('Largest prime factor:', largest_factor)
print('Time:', time() - start_time)