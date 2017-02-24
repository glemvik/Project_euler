# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 00:06:56 2016

Solution is found in less than 1 second.

@author: gunvor
"""

import math
from time import time

def find_prime(limit):
    count = 1 # START WITH 2 AS A PRIME
    number = 3 
    
    # COUNT PRIMES UP TO LIMIT
    while count < limit:
        prime = True
        for i in range(2, math.ceil(math.sqrt(number) + 1)):
            # NOT PRIME:
            if number % i == 0:
                prime = False
                break
        
        if prime:
            count += 1
        
        number += 1
    
    return (number - 1)

# INITIALIZING
start_time = time()
limit = 10001

prime = find_prime(10001)

# RESULTS
print('Prime number {} is {}'.format(limit, prime - 1))
print('Time:', time() - start_time)