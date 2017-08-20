# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 14:33:55 2016

PROBLEM:

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Solution is found in about 20 seconds.

@author: gunvor
"""

from time import time
from math import sqrt, ceil

def find_primes(limit):
    
    # INITIAL VALUES
    primes = [2]
    last_index = 0
    
    # EXAMINING NUMBERS UP TO LIMIT
    for i in range(3, limit):
        
        # UPDATING INDEX
        index = 0
        
        # EXAMINE IF i IS DIVISIBLE NY NUMBERS IN primes
        while(index <= last_index):
            
            # IF DIVISIBLE: NOT PRIME
            if i % primes[index] == 0:
                break
            
            # IF NOT DIVISIBLE BY ANY PRIME LESS THAN OR EQUAL TO CEILING OF
            # SQUARE ROOT OF i: PRIME.
            if index == last_index or primes[index] > ceil(sqrt(i)):
                primes.append(i)
                last_index += 1
                break
                
            index += 1
    
    return primes

def sum_primes(primes):
    
    # SET INITIAL SUM TO ZERO
    sum_primes = int()

    # ADD ALL PRIMES IN LIST TO SUM    
    for prime in primes:
        sum_primes += prime
    
    return sum_primes


# INITIALIZING
start_time = time()
limit = 2000000

sum_of_primes = sum_primes(find_primes(limit))

# RESULTS
print('The sum of all primes below {} is {}'.format(limit, sum_of_primes))
print('Time:', time() - start_time)       