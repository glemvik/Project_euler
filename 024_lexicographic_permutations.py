# -*- coding: utf-8 -*- 
# Problem URL: https://projecteuler.net/problem=24
""" 
 
A permutation is an ordered arrangement of objects. For example, 3124 is one 
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations 
are listed numerically or alphabetically, we call it lexicographic order. The 
lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
 
"""

from time import time
from itertools import permutations

start_time = time()

# INITIALIZE
digits = [digit for digit in range(10)]
limit = 1000000
count = 0

# PERMUTATE LEXICOGRAPHICALLY
for permutation in permutations(digits):
    count += 1
    
    # LEXICOGRPHICAL PERMUTATION NUMBER 'limit'
    if count == limit:
        print(''.join(str(digit) for digit in permutation))
        break

print('Time:', time() - start_time)