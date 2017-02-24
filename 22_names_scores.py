# -*- coding: utf-8 -*- 
# Problem URL: https://projecteuler.net/problem=22
""" 
 
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
What is the total of all the name scores in the file?
 
Solution is found in less than 1 second.

@author: gunvor 
"""

from time import time



def value_string(word):
    """
    Gives alphabetical value of string using ascii
    """
    value = 0

    # CAPITAL 'A' HAS VALUE 65 IN ASCII
    for letter in word:
        value += ord(letter) - 64
    
    return value

    
# INITIALIZE
start_time = time()
names = open('p022_names.txt', 'r').read()

# PUT INTO LIST
names = names[1:-1]
names = names.split('","')
names.sort()

# CALCULATE
name_score = 0
for index in range(0, len(names)):
    name_score += (index + 1) * value_string(names[index])

# PRINT RESULTS
print('Total name score:', name_score)
print('Time:', time() - start_time)