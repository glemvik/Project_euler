# -*- coding: utf-8 -*- 
# Problem URL: https://projecteuler.net/problem=23
""" 
 
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

Solution is found in about 5 seconds.

@author: gunvor 
"""

from time import time

def is_abundant(number):
    """
    Returns True if number is abundant and False if not.
    """
    sum_divisors = 1
    possible_divisors = [i for i in range(2, int(number**0.5 + 1))]

    for divisor in possible_divisors:
        if number % divisor == 0:
            sum_divisors += number//divisor
            if number // divisor != divisor:
                sum_divisors += divisor

    return sum_divisors > number

# INITIALIZING
start_time = time()
limit = 28123

# FIND ALL ABUNDANT NUMBERS UP TO LIMIT IN LIST
abundant_numbers = [number for number in range(1, limit+1) 
    if is_abundant(number) is True]

# FIND ALL SUMS (ALL COMBINATIONS) OF THE ABUNDANT NUMBERS IN LIST
# AND STORE IN SET (AVOID DUPLICATES)
sum_of_abundant_numbers = set()
for i,num1 in enumerate(abundant_numbers):
    for j,num2 in enumerate(abundant_numbers):
        if j > i:
            break
        if num1+num2 > limit:
            break
        sum_of_abundant_numbers.add(num1+num2)

# FOR ALL NUMBERS UP TO LIMIT: IF NUMBER NOT IN SET OF SUMS OF 
# ABUNDANT NUMBERS, ADD TO FINAL SUM
sum_numbers = int(limit*(limit+1)/2 - sum(list(sum_of_abundant_numbers)))

# PRINT RESULTS
print('The sum of all the numbers from 1 to {} is {}'.format(limit, sum_numbers))
print('Time:', time() - start_time)