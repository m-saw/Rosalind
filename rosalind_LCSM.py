# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 10:06:17 2022

@author: Moogie
"""
'''
Longest Common Substring:
    
Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

Sample Dataset
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA
Sample Output
AC

Matrix:
Start with list of 2 DNA strings [s1, s2]
Empty LCString = ''
make matrix len(s1) long and len(s2) wide  #could do len(list[-1]) as well?
So... 

using 2 FOR loops:
if char between s1 and s2 match,
    current position = # up and left += 1  #so if up-left is 0, current = 1; if 1, current = 2, and so on.

e.g.
     G A T T A C A
   0 0 0 0 0 0 0 0
T  0 0 0 1 1 0 0 0
A  0 0 1 0 0 2 0 1
G  0 1 0 0 0 0 0 0
A  0 0 2 0 0 1 0 1
C  0 0 0 0 0 0 2 0
C  0 0 0 0 0 0 1 0
A  0 0 1 0 0 1 0 2

then maybe look for largest #? max() ?
print that char and every char diagonal up left until position = 0

But how to do this for more than one string?
maybe save results to empty string (as long as len() is not less) and loop?

Iteration?:
DNA_list of all DNA_strings []
empty new_string = ''
empty lcstring_list = []
for each item in DNA_list, for each char in DNA_string, if char = char in item+1, new_string.append(char)
else 
lcstring_list.append(new_string)
new_string = ''

then go through each string in lcstring_list and return the one with longest len()
'''

import rosalind_REGEX_fileparser as moogie
import numpy as np

def LCS_DNA(x):
    collection = moogie.fileparse(x) # list of lists containing [Ros ID, DNA string]
    # print(moogie.fileparse(x))
    DNA_Strings = []
    for items in collection:
        DNA_Strings.append(items[1]) # list of DNA strings only
    # print(DNA_Strings)
    
    i = 1 # row
    j = 1 # column
    # new_string = ''
    # Matrix_results = []
    DNA_matrix = np.zeros((len(DNA_Strings[0])+1,len(DNA_Strings[1])+1)) # matrix of len(s1) and len(s2), both +1 to add extra row and column of 0
    for char1 in DNA_Strings[0]:
        for char2 in DNA_Strings[1]:
            if char1 == char2:
                DNA_matrix[i][j] += DNA_matrix[i-1][j-1] + 1
                
            i += 1
        i = 1
        j += 1
        
    # print(len(DNA_matrix))
    # print(DNA_matrix.max())
    
    m_value = DNA_matrix.max()

    k = -1 # row
    m = -1 # column
    Matrix_results = []
    new_string = ''
    for r in DNA_matrix:
        for c in r:
            # print(c)
            if c == m_value:
                # print(f'{c} [{k}],[{m}]')
                new_string = DNA_Strings[0][m+1-int(c):m+1]
                Matrix_results.append(new_string)
            m += 1
        m = -1
        k += 1
    # print(Matrix_results)
    
    d = {}
    for motifs in Matrix_results:
        d[motifs] = 0
        for strings in DNA_Strings:
            if motifs in strings:
                d[motifs] += 1
        
    max_key = max(d, key=d.get)
    print(max_key)
    
        
        
              