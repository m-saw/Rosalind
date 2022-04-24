# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 13:13:43 2022

@author: Moogie
"""
# =============================================================================
# Dictionaries: 
# = similar to a list, but instead of integer indices, you provide your own index, called a "key". For ex: phones = {'Zoe':'232-43-58', 'Alice':'165-88-56'}
# Accessing values is similar to lists:
# phones = {'Zoe':'232-43-58', 'Alice':'165-88-56'}
# print phones['Zoe']
# output should be: 232-43-58
# ----------------------------------------------------------------------------
# Adding new values/Assigning a new value to an existing key:
#
# phones['Zoe'] = '658-99-55'
# phones['Bill'] = '342-18-25'
# print(phones)
# This should produce the following:
#
# {'Bill': '342-18-25', 'Zoe': '658-99-55', 'Alice': '165-88-56'}
# Note that the new 'Bill' appeared in the beginning of the dictionary, not in the end, as you might expect. Dictionaries do not have an obvious ordering.
# ----------------------------------------------------------------------------
# If you need to check whether there a key in dictionary, you can use key in d syntax:
#
# if 'Peter' in phones:
#     print "We know Peter's phone"
# else:
#     print "We don't know Peter's phone"
# ----------------------------------------------------------------------------
# d = {}
# d['key'] = 1
# d['Key'] = 2
# d['KEY'] = 3
# print d
# Output:
# 
# {'KEY': 3, 'Key': 2, 'key': 1}
#----------------------------------------------------------------------------
# In case you need to delete a value from a dictionary, use the del command:
#
# phones = {'Zoe':'232-43-58', 'Alice':'165-88-56'}
# del phones['Zoe']
# print phones
# This produces the following output:
#
# {'Alice': '165-88-56'}
#
#------------------------------------------------------------------------------
# set() on a sequence eliminates duplicate elements. Pair with sorted() for sorted list.
# Ex: basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for f in sorted(set(basket)):
# apple
# banana
# orange
# pear
#
# =============================================================================

# =============================================================================
# Problem
# Given: A string s of length at most 10000 letters.
# 
# Return: The number of occurrences of each word in s, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.
# 
# Sample Dataset
# We tried list and we tried dicts also we tried Zen
#
# Sample Output
# and 1
# We 1
# tried 3
# dicts 1
# list 1
# we 2
# also 1
# Zen 1
#----------------------------------------------------------------------------
# Hints:
# To iterate over the words in a string, you can split it at each occurrence of empty space as follows:

# for word in str.split(' '):
#     print word
# For a pretty representation when outputting a dictionary, you can use the built in .items() function:

# for key, value in dict.items():
#     print key
#     print value
# =============================================================================
x = 'We tried list and we tried dicts also we tried Zen'
def word_freq(s):
    d = {}
    # d = set(s.split())   # seemed to work, but 'set' object is not subscriptable.(d[word] += 1 doesn't work). set() takes all unique values.
    for word in s.split(' '):
        d[word] = 0
        
    # print(d)
    for word in s.split(' '):   # could also make new list of s.split(' ') values
        if word in d:
            d[word] += 1
    for k, v in d.items():
        print(f'{k} {v}')
    # could also use .count() ...
    
# Answer/Explanation (there are a few...):
    # txtStr = words
    # wordCoutDict = {}
    # for word in txtStr.split():
    #     if word in wordCoutDict:
    #         wordCoutDict[word] +=1
    #     else:
    #         wordCoutDict[word] = 1
    # for key, value in wordCoutDict.items():
    #     print(key, value)
        
    






