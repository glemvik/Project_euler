# -*- coding: utf-8 -*- 
# Problem URL: https://projecteuler.net/problem=34
""" 
 
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: as 1! = 1 and 2! = 2 are not sums they are not included.
 
"""


from time import time
from math import factorial as fact


DEBUG = False
PROGRESS = True

def dprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)
        
def pprint(*args, **kwargs):
    if PROGRESS:
        print(*args, **kwargs)

def factorial_sum(number):
    return sum(fact(int(digit)) for digit in str(number))


#------------------------------------------------------------------------------
#---------------------------------- M A I N -----------------------------------
#------------------------------------------------------------------------------

start_time = time()

sum_of_numbers = 0

for number in range(3, int(1000000)):
    if factorial_sum(number) == number:
        sum_of_numbers += number
        pprint('\n',number)
    
    if number % 100000 == 0:
        pprint('*', end='')

print(sum_of_numbers)
print('Time:', time() - start_time)