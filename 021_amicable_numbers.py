# -*- coding: utf-8 -*- 
# Problem URL: https://projecteuler.net/problem=21
""" 
 
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.
 
Solution is found in less than 1 second.

@author: gunvor 
"""

from time import time


def find_sum_divisors(number):
    sum_divisors = 1
    possible_divisors = [i for i in range(2, int(number**0.5 + 1))]

    for divisor in possible_divisors:
        if number % divisor == 0:
            sum_divisors += number//divisor
            sum_divisors += divisor

    return sum_divisors

# INITIALIZE
start_time = time()
limit = 10000

# CREATE DICTIONARY OF NUMBERS FROM 1 TO LIMIT AND THEIR CORRESPDONDING SUM OF DIVISORS
all_numbers = {number:find_sum_divisors(number) for number in range(1,limit)}
amicable_numbers = set()

# ITERATE THROUGH DICTIONARY TO FIND AMICABLE NUMBERS
for key in range(1, limit):
    value = all_numbers[key]
    
    # VALUES LARGER THAN LIMIT ARE INVALID AS KEYS
    # ENTRIES WHERE KEY AND VALUE IS EQUAL ARE NOT AMICABLE NUMBERS
    if value >= limit or value == key: 
        continue
    
    # ADDING AMICABLE NUMBERS TO SET
    if all_numbers[value] == key:
        amicable_numbers.add(key)
        amicable_numbers.add(value)

# RESULTS
print('The sum of all amicable numbers below {} is'.format(limit), sum(amicable_numbers))
print('Time:', time() - start_time)