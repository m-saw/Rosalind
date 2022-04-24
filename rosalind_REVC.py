# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 13:06:16 2022

@author: Moogie
"""

# =============================================================================
# Problem
# In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
# 
# The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
# 
# Given: A DNA string s of length at most 1000 bp.
# 
# Return: The reverse complement sc of s.
# 
# Sample Dataset
# AAAACCCGGT
# Sample Output
# ACCGGGTTTT
# =============================================================================

# Dictionary???
test = 'AAAACCCGGT'

def DNA_REVC(DNA):
    complement = ''
    reverse = DNA[::-1]
    for letter in reverse:
        if letter == 'A':
            complement += 'T'
            
        elif letter == 'T':
            complement += 'A'
            
        elif letter == 'G':
            complement += 'C'
            
        elif letter == 'C':
            complement += 'G'
        else:
            print('error')
    return complement

def RNA_REVC(RNA):
    complement = ''
    reverse = RNA[::-1]
    for letter in reverse:
        if letter == 'A':
            complement += 'U'
            
        elif letter == 'U':
            complement += 'A'
            
        elif letter == 'G':
            complement += 'C'
            
        elif letter == 'C':
            complement += 'G'
        else:
            print('error')
    return complement

# rev_complement(test)

# =============================================================================
# Problem
# s ='ATACAGGCCTTCGACCAGCGTGTTCGGCATAGGTTCAGAAATATGAAGCCTGCCCCCGAGGAAGAGGTCTCATCAAGGTTCCCAGAGTGACTTCAGGAGACTTCCCCGCTCATATATGCATACTCACAACTATGTTGTGCTTTAGTATCGACTTATAGATCCCCGGGGGGGAGGTTGTACGTCCCTCGAGATTCGCGCCCGGCGGGCTAGAATCGAACAATAGTGGAAGCTCTCAGGGCTAACTTTGTGCGGCTCTGTTCCACCAGCAGGATAAGGTTAACCACTTATGAATGATCCCGTAGCCAGTGTTGAATACGAAAATTCCGGGTAACTCACAGGATCTAGAGGGGTGGTTCAAGATTAAAATCCAGAAGAATCATCCTTAATTGTGTCCGCCATAGAGATCATACCTCATCACATTTAACCTAGTTGTCAGGGTGTCTAACTCGCGGCCCCAAAATAAGCAAGTCCCCAGTCGTTCGGCCTATGACCCTGTGACGGGAATAGACTCCTCGACCAACGGGAAAAGACCGTTGAACGAATAAGATTTTTCCATTCGGAGTATGCTCCATAAAAAGGTGTTTTTAAACCGGCACTAAATCGGACACCGGGAGTTAGTTAGAATTACATTATACGTGGCCTTTCGTGGCGTATTTCCACCCTAACCTCCTGGACGCCGACCACGGTACGCTCACCTTCCTCTGAACTCATGCACGCAGATACTTATATTTTACTATAGAAGGACGATGATTAGTATGGATAGATGCCGAGCCTCCGCTGGTTCTCCGTCTATAGAAGGCGGCTAGCGGTGCGCACGCCTGCGACCAGTGACACGCGTCAGGAATACCTCAATATGCCGGTTAGTGGTCTGGGAGCGAGGGACCGTGAATCAATTAGGTATAGGAATGTATGATCCCCGTGCCGGCCGGGCCACCGATATATGGCGCAGCACGTCCATAAGGCATGTAGTAATAGCTGCGCCACTCAACATC'
# rev_complement(s)
# =============================================================================
