# -*- coding: utf-8 -*- 
# Problem URL: https://projecteuler.net/problem=25
""" 
 
The Fibonacci sequence is defined by the recurrence relation:
Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:
F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

Solution is found in less than 1 second.

@author: gunvor 
"""
from math import log, ceil
from time import time

# INITIALIZE
start_time = time()
limit = 1000

# PREPARE FOR FIBONACCI
a, b = 1, 1
index = 2
number_digits = 1

# COMPUTE FIBONACCI UNTIL NUMBER HAS limit NUMBER OF DIGITS
while (number_digits < limit):
    a, b = b, a + b
    index += 1
    number_digits = ceil(log(b)/log(10))

# RESULTS
print('The index of the first fibonacci number that has {} digits is'.format(number_digits),index)
print('Time:', time() - start_time)