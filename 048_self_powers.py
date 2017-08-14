# -*- coding: utf-8 -*- 
# Problem URL: https://projecteuler.net/problem=48
""" 
 
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
 
"""

from time import time

DEBUG = False
PROGRESS = False

def dprint(*args):
    if DEBUG:
        print(*args)
        
def pprint(*args):
    if PROGRESS:
        print(*args)




#------------------------------------------------------------------------------
#---------------------------------- M A I N -----------------------------------
#------------------------------------------------------------------------------

start_time = time()

mod = 10000000000
n = 1000

result = 0
for i in range(1,n+1):
    result = (result + ((i**i) % mod)) % mod

print(result)
print('Time:', time() - start_time)