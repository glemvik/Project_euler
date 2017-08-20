# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 13:41:38 2016

PROBLEM:

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Solution is found in less than 1 second.

@author: gunvor
"""

from time import time

# INITIALIZING
start_time = time()
sum = 1000

# BECAUSE a < b < c WE MUST HAVE a < sum/3
for a in range(1, 1000//3):
    
    # BECAUSE b < c WE MUST HAVE b < sum/2 
    for b in range(a, 1000//2):
        
        # c IS NOW DETERMINED BY sum, a, b
        c = sum - a - b
        
        # CHECK IF PYTHAGOREAN TRIPLET
        if a**2 + b**2 == c**2:
            print('The given special case of pythagorean triplet is true for the numbers {}, {} and {}, which gives {} * {} * {} = {}'.format(a, b, c, a, b, c, a*b*c))
            break

print('Time: {}'.format(time() - start_time))