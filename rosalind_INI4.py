# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 11:04:06 2022

@author: Moogie
"""
# =============================================================================
# Conditions & Loops: 
# if/else statements;
# a = 42
# if a < 10:
#   print 'the number is less than 10'
# else:
#   print 'the number is greater or equal to 10'
# 
# if we leave out an else, then the program continues on.
# ----------------------------------------------------------------------------
# Repeat an action several times; use a while loop.
# greetings = 1
# while greetings <= 3:
#   print 'Hello! ' * greetings
#   greetings = greetings + 1
#
# This will print 'Hello!' a number of times equal to greetings... once, twice, then three times until greetings == 4. Note that when greetings == 3, the loop will run.
#-----------------------------------------------------------------------------
# If you want to carry out some action on every element of a list, the for loop will be handy:
#
# names = ['Alice', 'Bob', 'Charley']
# for name in names:
#   print 'Hello, ' + name
#
# n = 10
# for i in range(n):
#   print i
# In the above code, range is a function that creates a list of integers between 0 and n, where n is not included.
#
# =============================================================================

# =============================================================================
# Problem
# Given: Two positive integers a and b (a<b<10000).
# 
# Return: The sum of all odd integers from a through b, inclusively.
# 
# Sample Dataset
# 100 200
# Sample Output
# 7500
# Hintclick to collapse
# You can use a % 2 == 1 to test if a is odd.
# =============================================================================

def sum_odd(a, b):
    sum = 0
    for n in range(a,b+1):
        if n % 2 == 1:
           sum += n
    print(sum)
    

