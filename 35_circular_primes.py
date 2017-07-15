# -*- coding: utf-8 -*- 
# Problem URL: https://projecteuler.net/problem=35
""" 
 
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?
 
"""

from time import time
from math import ceil, sqrt

DEBUG = False

def dprint(*args):
    if DEBUG:
        print(*args)

def number_of_circular_primes(limit):
    
    primes = [2]
    count = 1

    for number in range(3, limit):
        if is_prime(number, primes):
            primes.append(number)
            
            if is_circular(number, primes):
                count += 1
        
    return count


def is_circular(prime, smaller_primes):
    pivots = len(str(prime)) - 1
    
    dprint('Checking:', prime)
    
    for pivot in range(pivots):
        
        prime = int(str(prime)[-1] + str(prime)[:-1])
        
        dprint('Pivoted:', prime)
        
        if not is_prime(prime, smaller_primes):
            return False
        
    return True


def is_prime(number, smaller_primes):
    """
    Checks whether a number is a prime
    """
    for prime in smaller_primes:
        
        # NOT PRIME
        if number % prime == 0:
            return False
        
        # ONLY CHECK PRIME FACTORS UP TO SQUARE ROOT OF NUMBER
        if prime > ceil(sqrt(number)) + 1:
            break
    
    return True



#------------------------------------------------------------------------------
#---------------------------------- M A I N -----------------------------------
#------------------------------------------------------------------------------

start_time = time()

limit = 1000000

print(number_of_circular_primes(limit))
print('Time:', time() - start_time)