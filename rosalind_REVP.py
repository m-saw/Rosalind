# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 09:27:06 2022

@author: Moogie
"""
'''
Problem

Figure 2. Palindromic recognition site:
    5'...GAT | ATC...3' read ->
    3'...CTA | TAG...5' read <-
    
A DNA string is a reverse palindrome if it is
equal to its reverse complement. 
For instance, GCATGC is a reverse palindrome 
because its reverse (right to left)
complement (base-pairing)
is GCATGC (the same). 

Given: A DNA string of length at most 1 kbp 
in FASTA format.

Return: The position and length of 
every reverse palindrome in the string 
having length between 4 and 12. 
You may return these pairs in any order.

Sample Dataset
>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT
length is 25
1-based ?
Include position ? so start reading at pos-1 ?

Sample Output
4 6 # ATGCAT
5 4 # TGCA
6 6  # GCATGC
7 4 # CATG
17 4 #  TATA
18 4 # ATAT
20 6 # ATGCAT
21 4 # TGCA
'''
import regex as re
import numpy as np
import rosalind_REGEX_fileparser as moogie 

with open('rosalind_REVP.txt','r') as f:
    parse = moogie.fileparse('rosalind_REVP.txt')
    # print(parse[0][1])
    t = parse[0][1]

def REVP(s):
    F = s # read ->
    R = F[::-1] # read <-
    # print(R)
    
    bp = {'A':'T','G':'C','T':'A','C':'G'}
    
    RC = ''
    for i in R:
        RC += bp[i]
    # print(RC)
    
    # F ='TCAATGCATGCGGGTCTATATGCAT' ->
    # RC='ATGCATATAGACCCGCATGCATTGA' -> but matches wont be in same pos

               # matrix method:
    i = 1
    j = 1
    DNA_matrix = np.zeros((len(F)+1,len(RC)+1))
    # print(m)
    for char1 in F:
        for char2 in RC:
            if char1 == char2:
                DNA_matrix[i][j] += DNA_matrix[i-1][j-1] + 1
                
            i += 1
        i = 1
        j += 1
    # print(DNA_matrix)    
    
    k = -1 # row
    m = -1 # column
    Matrix_results = []
    new_string = ''
    for r in DNA_matrix:
        for c in r:
            # print(c)
            if c > 3 and c < 13:
                # print(f'{c} [{k}],[{m}]')
                new_string = F[m+1-int(c):m+1]
                Matrix_results.append(new_string)
            m += 1
        m = -1
        k += 1
    print(set(Matrix_results))

    'matrix may not work bc of PARTIAL overlap'

REVP('TCAATGCATGCGGGTCTATATGCAT')


    # matrix method:
    # i = 1
    # j = 1
    # DNA_matrix = np.zeros((len(F)+1,len(RC)+1))
    # # print(m)
    # for char1 in F:
    #     for char2 in RC:
    #         if char1 == char2:
    #             DNA_matrix[i][j] += DNA_matrix[i-1][j-1] + 1
                
    #         i += 1
    #     i = 1
    #     j += 1
    # print(DNA_matrix)    
    
    # k = -1 # row
    # m = -1 # column
    # Matrix_results = []
    # new_string = ''
    # for r in DNA_matrix:
    #     for c in r:
    #         # print(c)
    #         if c > 3 and c < 13:
    #             # print(f'{c} [{k}],[{m}]')
    #             new_string = F[m+1-int(c):m+1]
    #             Matrix_results.append(new_string)
    #         m += 1
    #     m = -1
    #     k += 1
    # print(Matrix_results)

    # regex method ?
    # FandRC = [F,RC]
    # FandRC = ' '.join(FandRC)
    # print(FandRC)
    # matches = re.findall(r'(?=([A]\w{4})\w* ([A]\w{4}))',FandRC)
    # print(matches)
    # for match in matches:
        # print(match)
    
    # Need to return matches that occur more than once...
    # ways to regex multiple strings?
    
    # from internet: re.search(r'pattern1(.*?)pattern2', s).group(1) ; 
    # returns text b/t p1 and p2
    
    # OR: s = 'step 1 some text\nstep 2 more text\nstep 3 then more text\nconclusion'
    # re.findall(r'(?:step \d)(.*?)(?:\n)', s)
    # (?:step \d) - Non-capturing group - ?: - it will be matched but not extracted
    # step \d - matches the characters step (case sensitive) followed by a digit
    # (.*?) - 1st Capturing Group - capture anything lazy mode
    # (?:\n) - Non-capturing group
    # \n matches a newline character
    
    # Or, can iterate forward through F and backward through RC until match is found or s/t

