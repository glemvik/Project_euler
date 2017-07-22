# -*- coding: utf-8 -*- 
# Problem URL: https://projecteuler.net/problem=74
""" 
 
The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:
1! + 4! + 5! = 1 + 24 + 120 = 145
Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:
169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872
It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,
69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)
Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.
How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
 
"""
from time import time
from math import factorial

DEBUG = True

def dprint(*args):
    if DEBUG:
        print(*args)

def chains_with_60_terms(limit, terms):
    """
    Returns the number of chains with starting number below 'limit' which 
    contains exactly 'terms' number of terms.
    """
    count = 0
    
    # REGISTER LENGTH OF CYCLES AS THEY ARE DISCOVERED
    length_of_cycles = dict()
    
    for number in range(1,limit):
        
        if number % 1000 == 0:
            dprint(number)
        
        # GET LENGTH OF CHAIN, AND UPDATE 'length_of_cycles'
        length, length_of_cycles = number_of_non_repeating_terms(number, length_of_cycles)
        
        if length == terms:
            count += 1
    
    return count

def number_of_non_repeating_terms(number, length_of_cycles):
    """
    Returns the number of non-repeating terms in the chain beginning with 
    'number' and the updated dictionary 'length_of_cycles'.
    """
    non_repeating_terms = set()
    found_known_cycle = False
    
    while number not in non_repeating_terms:
        non_repeating_terms.add(number)
        number = next_number_in_chain(number)
        
        # CHECK IF CURRENT NUMBER IN CHAIN IS PART OF CYCLE
        if number in length_of_cycles:
            found_known_cycle = True
            break

    if found_known_cycle:
        length = len(non_repeating_terms) + length_of_cycles[number]            
    
    else:
        length = len(non_repeating_terms)
    
        # REGISTER LENGTH OF NEW CYCLE
        cycle = set()
        while number not in cycle:
            cycle.add(number)
            number = next_number_in_chain(number)
            
        for number in cycle:
            length_of_cycles[number] = len(cycle)

    return length, length_of_cycles

def next_number_in_chain(number):
    """
    Returns the next number in the factoiral chain.
    """
    new_number = 0
    
    for digit in str(number):
        new_number += factorial(int(digit))    
    
    return new_number

#------------------------------------------------------------------------------
#---------------------------------- M A I N -----------------------------------
#------------------------------------------------------------------------------

start_time = time()

limit = 1000000
practice_limit = 10000
terms = 60

print(chains_with_60_terms(limit, terms))
print('Time:', time() - start_time)