# -*- coding: utf-8 -*- 
# Problem URL: https://projecteuler.net/problem=16
""" 
 
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2**1000?
 
Solution is found in less than 1 second.

@author: gunvor
"""
 
from time import time

# INITIALIZE
start_time = time()
n = 1000

# MAKE STRING FOR EASY ITERATION
number_as_string = str(2**n)

sum_of_digits = 0
for letter in number_as_string:
    sum_of_digits += int(letter)

# RESULTS
print('The sum of the digits of 2**{} is {}'.format(n, sum_of_digits))
print('Time:', time() - start_time)

# IN ONE LINE:
# print(sum([int(char) for char in str(2**n)]))