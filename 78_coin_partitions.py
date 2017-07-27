# -*- coding: utf-8 -*- 
# Problem URL: https://projecteuler.net/problem=78
""" 
 
Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O

Find the least value of n for which p(n) is divisible by one million.
 
"""
from time import time
from collections import defaultdict

DEBUG = True

def dprint(*args):
    if DEBUG:
        print(*args)



def number_of_summations(divisor):
    """
    Returns the number of different ways 'number' can be written as a sum of
    at least two positive integers.
    """

    summations = defaultdict(lambda : 1)
     
    for col in range(2,int(10e10)):
        for row in range(2,col+1):
            
            if col == row:
                summations[(row,col)] = summations[(row-1,col)] + 1
                
                
                if summations[(row,col)] % divisor == 0:
                    return (row,col), summations[(row,col)]
                
            elif col > row:
                
                summations[(row,col)] = summations[(row-1,col)] + summations[(min(col-row,row),col-row)]
                
                
        




#------------------------------------------------------------------------------
#---------------------------------- M A I N -----------------------------------
#------------------------------------------------------------------------------

start_time = time()

divisor = 1000000
divisor = 10000

print(number_of_summations(divisor))
print('Time:', time() - start_time)