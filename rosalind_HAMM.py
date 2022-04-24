# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 10:31:41 2022

@author: Moogie
"""
# =============================================================================
# Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t. See Figure 2.
# 
# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
# 
# Return: The Hamming distance dH(s,t).
# 
# Sample Dataset
# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT
# Sample Output
# 7
# =============================================================================

def dH(s,t):
    if len(s) != len(t):
        return 'strings must be same length'
    pt_count = 0
    index = 0
    for item in s:
        if s[index] != t[index]:
            pt_count += 1
        index += 1      
    return pt_count