# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 17:04:51 2016

PROBLEM:

What is the value of the first triangle number to have over 
five hundred divisors?

Solution is found in about 10 seconds.

@author: gunvor
"""
from time import time


def number_of_factors(number):
    if number <= 1:
        return 0
        
    # INITIALIZING VALUES
    possible_divisor = 1
    divisors = set()

    # FIND FACTORS AND ADD THEM TO SET
    while(possible_divisor > 0):
        
        # possible_divisors IS DIVISOR:
        if number % possible_divisor == 0:
            
            # IF possible_divisor ALREADY IN SET: DONE
            if possible_divisor in divisors:
                return len(divisors)
            
            # IF NOT: ADD possible_divisor AND number/possible_divisor
            divisors.add(possible_divisor)
            divisors.add(number//possible_divisor)

        # KEEP EXAMINING        
        possible_divisor += 1
    

# INITIALIZING
start_time = time()
next_additor = 1
triangular_number = 0
limit = 500

# CONSTRUCT TRIANGULAR NUMBERS UNTIL MORE FACTORS THAN LIMIT
while(number_of_factors(triangular_number) < limit):
    triangular_number += next_additor
    next_additor += 1

# RESULTS
print('The first triangular number that contains more than {} factors is {}'.\
format(limit,triangular_number))    
print('Time:', time() - start_time)