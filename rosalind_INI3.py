# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 10:20:45 2022

@author: Moogie
"""

# =============================================================================
# Lists:  
# tea_party = ['March Hare', 'Hatter', 'Dormouse', 'Alice']
# print tea_party[2]     [returns Dormouse]
# 
# tea_party[1] = 'Cheshire Cat'
# print tea_party     [replaces Hatter with Cheshire Cat]
# 
# tea_party.append('Jabberwocky')
# print tea_party     [adds Jabberwocky to the end]
# 
# list slicing: If you need to obtain only some of a list, you can use the notation list_name[a:b] to get only those from index a up to but NOT including index b.
# Ex: tea_party[1:3]
# [:2] starts at the end until [1] 
# [3:] starts at [3] until the end
# 
# You can also use negative indices to count items backtracking from the end of the list. So tea_party[-2:] returns the same output as tea_party[3:]: Alice, Jabberwocky.
# [Does not include [-2]]
#
# Can also slice strings:
# a = 'flimsy'
# b = 'miserable'
# c = b[0:1] + a[2:]
# print c
# =============================================================================

# =============================================================================
# Given: A string s of length at most 200 letters and four integers a, b, c and d.
# 
# Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.
# 
# Sample Dataset
# HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.
# 22 27 97 102
# Sample Output
# Humpty Dumpty
#
# str.splitlines(keepends=False)
# Return a list of the lines in the string, breaking at line boundaries. Line breaks are not included in the resulting list unless keepends is given and true.
# =============================================================================

def slice_str(s,a,b,c,d):
    ab = s[a:b+1]
    cd = s[c:d+1]
    print(f'{ab} {cd}')
    
    
    









