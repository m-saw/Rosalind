# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 09:48:48 2022

@author: Moogie
""" 
# =============================================================================
# Problem
# A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.
# 
# An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."
# 
# Given: A DNA string s of length at most 1000 nt.
# 
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s."
# =============================================================================

#import string
import random

#RandomNT = string.ascii_letters 
#[random letters from A-Z; can be repeating, include both upper & lowercase]
#print ( ''.join(random.choice(letters) for i in range(10)) )

randomDNA = (''.join(random.choice('CGTA') for i in range(1000)))
# ''.join(your_tuple or list) ; joins all tuple values into one string/list with '' (nothing) as a separator (they're all next to each other)
#print(len(RandomDNA))


def CountNT(s):
    T = 0
    C = 0
    G = 0
    A = 0
    for letter in s:
        if letter == 'T':
            T+=1
        elif letter == 'C':
            C+=1
        elif letter == 'G':
            G+=1
        elif letter == 'A':
            A+=1
        else:
            print("error")
    # print(f'T : {T}\nC : {C}\nG : {G}\nA : {A}') # f' ' format string; includes variables in {} into a string... {x:#} adds # spaces 
    print(f'{A} {C} {G} {T}')

# =============================================================================
# Problem dataset
# x = 'TCCCGACGCAATTTTCCCCTTCGTCTACAGCCAACTATTAACCACGAAATCGTATAAGGACTGAGCATATATCGACTCAAGTGATATCGCTTTTCCATGAATCAATAGACCCGGTACTAGGCTGTTACATCCGCTAATATTTTGTTAGGGAGCTTGCATGGCTACGCGGAGATTCGAGGAACCGTCAGAACTGATAAAACTCAATTACGTCTGCCAACATACATAAAAGTCCGACCCGATTGACCCATTCTAGCCTCACGTCGCCCCCGGTAATCCCGGAAGGATTTAAACGATCAGAGAGACATGACAGATTCCCCGCAGCGGCAGATGTAGAACAGAAGAGCCACAAGTCTAGCTGGTTGGACCGAGTACCGACCATTTCAATTCTGACGATTGCGTTTCGTTAGCTGGCTATTAGATCCCGTTTACAGTTGGAATTTCGAGATCGATTAGACGTTAAAGGAAGCCTCCGTGACAAGAGAACGTCGTTTTAGCCATGCTGGACGCAGATAGTGGAATTTGCCAAACTAATCATAGGCGAGACTGTCCACTCTAACGGGTGGGAGACCTGACGTTGCTTACCGCGCTTGCAGACGCTACGGATTCGGGCTGCTCTAAAGTCTGTGTGACACGGCGATAACTATGTTACCAGGGTAAGTTCGCCCTATGGAACATTCTTGCGCCCATCTATCTGAAGAAATACGGCCTAGAAGCATAACGTACAACGCTTTACTTGGTATCATACACGGCGAGTGAGTGGTCTTAAACTGCACAGCTCCGACATCAAGATGATCTTGTTGCTAGATCAACTTAGATCGTCGTTATAAGTGAAACACTAGTTCTACATCGTCGATGCGTGCAGCTGTTCGTTCTAAAGCTCCGCAATGTCTGTAGATTAGCTATC'
# 
# CountNT(x)
# =============================================================================
            
            
            
            
            
    