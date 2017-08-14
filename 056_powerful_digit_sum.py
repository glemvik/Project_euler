# -*- coding: utf-8 -*- 
# Problem URL: https://projecteuler.net/problem=56
""" 
 
A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.
Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
 
Solution is found in less than 1 second.

@author: gunvor 
"""

from time import time

def digit_sum(number):
    """
    Function for finding and returning sum of digits of number
    """
    return sum([int(letter) for letter in str(number)])


# INITIALIZE
start_time = time()
n = 100

# EXAMINE ALL a**b WITHIN LIMITS
answer = 0
for a in range(n,1,-1):
    for b in range(n,1,-1):
        temp_ans = digit_sum(a**b)
        
        if temp_ans > answer:
            answer = temp_ans
            
    if temp_ans < 0.90 * answer:
        break

# RESULTS
print(answer)
print('Time:', time() - start_time)


# IN ONE LINE:
#print(max([sum([int(letter) for letter in str(a**b)]) for b in range(k, n) 
#for a in range(k,n)]))