# -*- coding: utf-8 -*- 
# Problem URL: https://projecteuler.net/problem=77
""" 
 
It is possible to write ten as the sum of primes in exactly five different ways:
7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2
What is the first value which can be written as the sum of primes in over five thousand different ways?
 
"""

from time import time

DEBUG = False
PROGRESS = False

def dprint(*args):
    if DEBUG:
        print(*args)
        
def pprint(*args):
    if PROGRESS:
        print(*args)

def number_of_summations(primes, number):
    """
    Returns the number of ways to write 'number' by using primes.
    """
    summations = [[((i+1) % 2) for i in range(number-1)] for j in range(len(primes))]
    
    # FIND DIFFERENT WAYS OF WRITING 'number' BY USING THE ELEMENTS IN 'primes'
    for row in range(1,len(primes)):
        
        dprint('Working on row {}, which is prime {}'.format(row, primes[row]))
        
        for col in range(number-1):
            # The new prime is larger than the number we wish to write:
                # the number of ways of writing the number is the same as before
            if col+2 < primes[row]:
                summations[row][col] = summations[row-1][col]
            
            # Thew new prime is exactly the the number we wish to write:
                # the number of ways of writing the number increase by one
            elif col+2 == primes[row]:
                summations[row][col] = summations[row-1][col] + 1
            
            # Thew new prime is smaller than the number we wish to write:
                # the number of ways of writing the number increase by the number
                # of ways of writing the prime ('current number' - 'new prime')
            else:
                if col+2 - primes[row] > 1:
                    summations[row][col] = summations[row-1][col] + summations[row][col-primes[row]]
                else:
                    summations[row][col] = summations[row-1][col]
                    
        dprint(summations[row])
    
    # Return the number of ways of writing 'number'
    return summations[-1][-1]

def update_primes(primes, number):
    """
    Provided an array of some of the primes that are smaller than 'number', 
    returns an array of all the primes that are smaller than 'number'.
    """
    
    # CHECK ALL THE NUMBERS BETWEEN THE LARGEST PRIME IN 'primes' AND 'number'
    for possible_prime in range(primes[-1]+1, number):
        is_prime = True
        
        # CHECK DIVISIBILITY BY PRIMES IN 'primes'
        for prime in primes:
            if possible_prime % prime == 0:
                is_prime = False
                break
                
        # UPDATE ARRAY OF PRIMES
        if is_prime:
            primes.append(possible_prime)
    
    return primes

def more_than_n_summations(limit):
    """
    Returns the smallest number that can be written in more than 'limit' ways 
    as a sum of primes.
    """
    # SPECIFY STARTING POINT
    primes = [2]
    number = 10
    
    while True:
        # FIND ALL PRIMES SMALLER THAN 'number' AND NUMBER OF SUMMATIONS
        primes = update_primes(primes, number)
        summations = number_of_summations(primes, number)
        
        pprint('Number {} has {} summations'.format(number, summations))
        
        # COMPARE WITH LIMIT
        if summations > limit:
            return number
        
        number += 1
        

#------------------------------------------------------------------------------
#---------------------------------- M A I N -----------------------------------
#------------------------------------------------------------------------------

start_time = time()

limit = 5000

print(more_than_n_summations(limit))
print('Time:', time() - start_time)