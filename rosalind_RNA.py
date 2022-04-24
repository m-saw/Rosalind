# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 11:05:37 2022

@author: Moogie
"""
# =============================================================================
# Problem
# An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
# 
# Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.
# 
# Given: A DNA string t having length at most 1000 nt.
# 
# Return: The transcribed RNA string of t.
# =============================================================================

# Use .replace() and write out a replace function



import random
randomDNA = (''.join(random.choice('CGTA') for i in range(50)))

# str.replace(old, new[, count])
#print(randomDNA.replace('T', 'U'))


# =============================================================================
# def ReplaceT(s):
#     newRNA = []
#     for letter in s:
#         if letter == 'T':
#             newRNA.append('U')
#         else:
#             newRNA.append(letter)
#     print(''.join(newRNA))
# 
# ReplaceT(randomDNA)
# =============================================================================

# =============================================================================
# Problem
t = 'GCAACTTTCCATTCAATTTACTTCAGTTCGCAGAATGTTACTTACGGAGTAGAGGAAAACGTAAAACTAACTGACAAGGGCTCTGTACGAGGTGAATTATGTCCCCCTACAGCTTTCGGAGACTGGACTCTCATCTGACCTCCATGGGCGGCGCACGAGGCTATTAATGGACCTGGACAGCCAATCTTGCGCACATCAAGGTACAAGAAGGAGAATGTAACAAGCGTCTGTCCGCGCGCTTACACAATCTCTCACAACGATACCAATACCCCAGTATTTAGGAGTGGATACTGGAGATCATACAAATACCCCGACATTGACGATTCAATCCTGGGCTCTAATATAGGACAACTAGCTACCTTAACTCCCCCCATGTTGTCAACTTTTGATTGTGGACGCCGGTCCTTTAACCACTGCAGACGCCCACAAGCACATGCAGGCCCCTCCCTGGGCAAAGAAGACAAATTCCATTTGGTGAGCGTCAAGGTTCGGGGACAGCCAGTAACCGGCGTAGTCCGCTTCGATGCTGTGGCCGTTCGCTTACTGGAATTAATGATTGTCCTCAGCCACATAGAGTACGCCGAATGTGTGATGCTTCTTCTGCTCAAGCCTCAGAGTTAGAGCTGCCTTGAGTAGGATTTGAGACTATCAGAGTACTTCCAATTTCACGATGAAGAGGGTCGAACCTTACCGTCCCTTTGTGGGTGAGGGCATCGTGCACACCCTGGCGTACAAGTGTACCATCGGGCTACCCACGTTATTCGTTCATTCGCGAGTGGGCACCAATCATGACTGCGACACTGTTCCGGGTTCTTCATCGTTACTCGGGGTTAATTCGGCCCAACGTGGGTTGGGTATTATAGCAGGATACAGGATCCTGTCGAGTGTGGATTATAGTACGCGTACTTCATTCTACTCTAGATGAGAAGCGCGAAACGAGCACTTCTCTATTGCAACTTAG'
print(t.replace('T', 'U'))
# 
# =============================================================================
