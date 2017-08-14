# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 19:46:50 2016

PROBLEM:

The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Which starting number, under one million, produces the longest chain?

Solution is found in about 90 seconds.

@author: gunvor
"""

from time import time

def collatz_sequence(number, path):

    # END OF SEQUENCE
    if number in path:
        return len(path)
    
    # UPDATING PATH
    path.add(number)

    # FINDING NEXT TERM
    if number % 2 == 0:
        return collatz_sequence(number//2, path)
    else:
        return collatz_sequence(3*number + 1, path)
    

# INITIALIZING
start_time = time()
limit = 1000000

# FINDING LONGEST PATH OF NUMBER UNDER 1000000 IS 525
print('Finding the length of the longest chain produced by a number under one million')
length = max(collatz_sequence(number,set()) for number in range(0,limit))

# FINDING INDEX OF LONGEST PATH
print('Finding the starting number of the longest chain')
for number in range(1, limit):
    if collatz_sequence(number, set()) == length:
        break

# PRINTING RESULTS
print('The number under', limit, 'that produces the longest chain is', number)
print('Time:', time() - start_time)