# -*- coding: utf-8 -*- 
# Problem URL: https://projecteuler.net/problem=99
""" 
 
Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that 211 = 2048 < 37 = 2187.
However, confirming that 632382518061 > 519432525806 would be much more difficult, as both numbers contain over three million digits.
Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.
NOTE: The first two lines in the file represent the numbers in the example given above.
 
"""

from time import time
from math import log

DEBUG = True

def dprint(*args):
    if DEBUG:
        print(*args)

#------------------------------------------------------------------------------
#---------------------------------- M A I N -----------------------------------
#------------------------------------------------------------------------------

start_time = time()

filename = 'p099_base_exp.txt'
logarithms = []

# READ FILE AND SAVE THE LOGARITHM OF THE VALUE OF 'base'^'exponent' IN ARRAY
with open(filename) as file:
    for line in file:
        
        base, exponent = [int(entry) for entry in line.strip().split(',')]
        logarithms.append(exponent * log(base))

# FIND LARGEST VALUE OF THE ITEMS IN THE ARRAY, ALONG WITH THE LINE-NUMBER
largest_value = 0
line_number = 0
for i,item in enumerate(logarithms):

    # If largest item so far
    if item > largest_value:
        largest_value = item
        line_number = i + 1

print(line_number, largest_value)
print('Time:', time() - start_time)