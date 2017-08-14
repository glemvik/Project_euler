# -*- coding: utf-8 -*- 
# Problem URL: https://projecteuler.net/problem=17
""" 
 
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? 
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
 
Solution is found in less than 1 second.

@author: gunvor
"""
 
from time import time

# INITIALIZING
start_time = time()
sum_of_letters = 0

# LISTS FOR COUNTING TO ONE THOUSAND
digits = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

# COUNTING THE HUNDREDS (0, 100, 200, 300, etc)
for hundred in digits:
    counter = 0

    # COUNTING THE TENS (0, 10, 20, 30, etc)
    for ten in tens:
        counter +=1
        
        # Counter == 2 means we are counting the numbers from 10 to 20. Need special
        # list (teens) to do this
        if counter == 2:
            number = ''
            
            # Determine if we have counted past 100
            if len(hundred) > 0:
                current_hundred = hundred + 'hundredand'
            else:
                current_hundred = ''
            
            # Manually count current_hundred and ten (doesn't "fit" into any of the lists)
            sum_of_letters += len(current_hundred + 'ten')
            
            # Count the numbers from 10 to 19
            for teen in teens:
                sum_of_letters += len(current_hundred + teen)
                
        # Counting all other tens than those from 10 to 20
        else:
            # Counting the digits from 0 to 9
            for digit in digits:
                number = ''

                # Checking value of hundred, ten and digit. If not zero - use to construct
                # number
                if len(hundred) > 0:
                    number += hundred + 'hundred'
                    if len(ten) > 0:
                        number += 'and' + ten
                        if len(digit) > 0:
                            number += digit
                    else:
                        if len(digit) > 0:
                            number += 'and' + digit
                else:
                    if len(ten) > 0:
                        number += ten
                    if len(digit) > 0:
                        number += digit
                
                # Count
                sum_of_letters += len(number)

# Count last number
sum_of_letters += len('onethousand')

# RESULTS
print('The sum of the letters of numerals of the numbers from one to one thousand is', sum_of_letters)
print('Time', time() - start_time)