# -*- coding: utf-8 -*- 
# Problem URL: https://projecteuler.net/problem=53
""" 
 
There are exactly ten ways of selecting three from five, 12345:
123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
In combinatorics, we use the notation, 5C3 = 10.
In general,

nCr = 
n!r!(n−r)!
,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?
 
"""

from time import time
from math import factorial

DEBUG = False

def dprint(*args):
    if DEBUG:
        print(*args)

def combinations_greater_than_limit(elements, limit):
    """
    Returns the number of values of combinations of r elements from n elements 
    which are greater than the specified limit.
    """
    count = 0
    
    for n in range(1, elements+1):
        for r in range(1,n+1):
            if combinations(n,r) > limit:
                count += 1

    return count


def combinations(n,r):
    """
    Number of ways of selecting r elements from n elements.
    """
    return factorial(n) / (factorial(n-r) * factorial(r))


#------------------------------------------------------------------------------
#---------------------------------- M A I N -----------------------------------
#------------------------------------------------------------------------------

start_time = time()

elements = 100
limit = 1000000

print(combinations_greater_than_limit(elements, limit)) 

print('Time:', time() - start_time)