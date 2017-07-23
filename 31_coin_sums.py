# -*- coding: utf-8 -*- 
# Problem URL: https://projecteuler.net/problem=31
""" 
 
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:
1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
 
"""

from time import time

DEBUG = True

def dprint(*args):
    if DEBUG:
        print(*args)


def number_of_summations(coins, size):
    """
    Returns the number of different ways the largest coin provided in the array 
    of coins can be made using any number of the coins in the array.
    """
    largest_coin = coins[-1]
    summations = [[1 for i in range(largest_coin)] for j in range(size)]
    
    # FIND DIFFERENT WAYS OF MAKING THE LARGEST COIN
    for row in range(1,size):
        for col in range(largest_coin):
            
            # The new coin is larger than the coin we wish to make:
                # the number of ways of making the coin is the same as before
            if col+1 < coins[row]:
                summations[row][col] = summations[row-1][col]
                
            # The new coin is exactly the coin we wish to make:
                # the number of ways of making the coin increase by one
            elif col+1 == coins[row]:
                summations[row][col] = summations[row-1][col] + 1
                
            # The new coin is larger than the coin we wish to write:
                # the number of ways of making the coin increase by the number 
                # of ways of making the coin ('current coin' - 'new coin')
            else:
                summations[row][col] = summations[row-1][col] + summations[row][col-coins[row]]
    
    # Return the number of  ways of making the largest coin
    return summations[-1][-1]



#------------------------------------------------------------------------------
#---------------------------------- M A I N -----------------------------------
#------------------------------------------------------------------------------

start_time = time()

coins = [1, 2, 5, 10, 20, 50, 100, 200]
size = len(coins)

print(number_of_summations(coins, size))
print('Time:', time() - start_time)