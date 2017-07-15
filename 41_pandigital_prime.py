# -*- coding: utf-8 -*- 
# Problem URL: https://projecteuler.net/problem=41
""" 
 
We shall say that an n-digit number is pandigital if it makes use of all the 
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
What is the largest n-digit pandigital prime that exists?
 
"""

from time import time
from itertools import permutations
from math import ceil, sqrt

DEBUG = False

def dprint(*args):
    if DEBUG:
        print(*args)

def find_largest_pandigital_prime(digits):
    """
    Finds the largest n-digit pandigital prime that exists. 
    """
    # BEGINS SEARCHING FOR 9-DIGIT PANDIGITAL PRIME
    number_of_digits = len(digits)
    
    success = False
    
    while not success:
        
        # FIND ALL 'number_of_digits'-DIGIT PANDIGITAL NUMBERS
        pandigital_numbers = construct_pandigital_numbers(digits[:number_of_digits])
        
        # CHECK IF ANY OF THE PANDIGITAL NUMBERS ARE PRIMES
        pandigital_primes = is_prime(pandigital_numbers)
        
        if len(pandigital_primes) > 0:
            largest_pandigital_prime = max(pandigital_primes)
            success = True
            
        # IF NONE: PREPARE TO SEARCH FOR ('number_of_digits' - 1)-DIGIT PANDIGITAL PRIME
        else:
            number_of_digits -= 1
    
    return largest_pandigital_prime

def construct_pandigital_numbers(digits):
    """
    Creates all pandigital numbers constructed from the digits provided.
    """
    return [int(''.join(str(digit) for digit in permutation)) for permutation in permutations(digits)]    

def is_prime(numbers):
    """
    Returns the primes contained in the list of numbers, if there are any.
    """
    prime_numbers = []
    
    # CHECK PRIMALITY OF NUMBERS 
    for number in numbers:
        prime = True
        
        for i in range(2, ceil(sqrt(number) + 1)):            
                # NOT PRIME:
                if number % i == 0:
                    prime = False
                    break
        
        # COLLECT ALL PRIME NUMBERS IN NEW LIST
        if prime:
            prime_numbers.append(number)
        
    return prime_numbers


#------------------------------------------------------------------------------
#---------------------------------- M A I N -----------------------------------
#------------------------------------------------------------------------------

start_time = time()


digits = [digit+1 for digit in range(9)]

largest_pandigital_number = find_largest_pandigital_prime(digits)

print(largest_pandigital_number)
print('Time:', time() - start_time)
