# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 11:42:54 2016

Finds the largest palindrome made from the product of two 3-digit numbers

Solution is found in less than 1 second.

@author: gunvor
"""

from time import time

def is_palindrome(number):
    number = str(number) #TO GET "LENGTH" OF NUMBER

    #EXAMINES IF NUMBER READS THE SAME BOTH WAYS    
    for i in range(0, len(number)//2):
        if number[i] != number[-(i+1)]:
            return False #NUMBER NOT SYMMETRIC
    return True

# INITIALIZING
start_time = time()
palindrome = 0

#FINDS ALL PRODUCTS OF TWO 3-DIGIT NUMBERS
for i in range(100, 1000):
    for j in range(100, 1000): 
        product = i * j

        #EXAMINES IF PRODUCT IS (LARGEST) PALINDROME
        if is_palindrome(product) and product > palindrome:
            palindrome = product
            
# RESULTS
print('Largest palindrome made from the product of two 3-digit numbers:', palindrome)
print('Time:', time() - start_time)
