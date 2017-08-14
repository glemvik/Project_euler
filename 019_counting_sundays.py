# -*- coding: utf-8 -*- 
# Problem URL: https://projecteuler.net/problem=19
""" 
 
You are given the following information, but you may prefer to do some research for yourself.
1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

Solution is found in less than 1 second.

@author: gunvor 
"""

from time import time

def check_sunday(number):
    if number % 7 == 0:
        return 1
        
    return 0

# INITIALIZE
start_time = time()
year = 1900
end_year = 2001
sundays = 0
day = 1

# COUNT SUNDAYS ON THE FIRST OF THE MONTH
while(year < end_year): 
    
    # JANUARY
    day += 31
    sundays += check_sunday(day)
        
    # FEBRUARY
    day += 28
    if year % 4 == 0:
        # LEAP YEAR
        if year % 100 != 0:
            day += 1
        # LEAP YEAR
        elif year % 400 == 0:
            day += 1
    sundays += check_sunday(day)
    
    # MARCH
    day += 31
    sundays += check_sunday(day)
    
    # APRIL
    day += 30
    sundays += check_sunday(day)
    
    # MAY
    day += 31
    sundays += check_sunday(day)
    
    # JUNE
    day += 30
    sundays += check_sunday(day)
    
    # JULY
    day += 31
    sundays += check_sunday(day)
    
    # AUGUST
    day += 31
    sundays += check_sunday(day)
    
    # SEPTEMBER
    day += 30
    sundays += check_sunday(day)
    
    # OCTOBER
    day += 31
    sundays += check_sunday(day)
    
    # NOVEMBER
    day += 30
    sundays += check_sunday(day)
    
    # DECEMBER
    day += 31
    sundays += check_sunday(day)

    # ONLY NEED 1900 TO FIND FIRST DAY OF THE YEAR OF 1901
    if year == 1900:
        sundays = 0

    year += 1

# RESULTS
print('Sundays on the first of the month:', sundays)
print('Time:', time() - start_time)