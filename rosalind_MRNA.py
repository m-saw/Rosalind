# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 09:18:03 2022

@author: Moogie
"""
'''
Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)

Sample Dataset
MA
Sample Output
12
'''
# Codon Table:
#     UUU F      CUU L      AUU I      GUU V
#     UUC F      CUC L      AUC I      GUC V
#     UUA L      CUA L      AUA I      GUA V
#     UUG L      CUG L      AUG M      GUG V
#     UCU S      CCU P      ACU T      GCU A
#     UCC S      CCC P      ACC T      GCC A
#     UCA S      CCA P      ACA T      GCA A
#     UCG S      CCG P      ACG T      GCG A
#     UAU Y      CAU H      AAU N      GAU D
#     UAC Y      CAC H      AAC N      GAC D
#     UAA Stop   CAA Q      AAA K      GAA E
#     UAG Stop   CAG Q      AAG K      GAG E
#     UGU C      CGU R      AGU S      GGU G
#     UGC C      CGC R      AGC S      GGC G
#     UGA Stop   CGA R      AGA R      GGA G
#     UGG W      CGG R      AGG R      GGG G

# MA(Stop) : 1 x 4 x 3 = 12 ; 12 % 1,000,000 = 12


def protein_mRNA(s):
    '''
    string s
    predict how many possible mRNA/codon combinations make the protein s string
    '''
    
    d = {
    'F':2,'L':6,'S':6,'Y':2,'C':2,'W':1,'P':4,'H':2,
    'Q':2,'R':6,'I':3,'M':1,'T':4,'N':2,'K':2,'V':4,
    'A':4,'D':2,'E':2,'G':4
    }
    # stop codons are blank
    # print(d)
    # print(d['R'])
    
    count = 3
    for char in s:
        # print(char)
        count = count * d[char]
        # print(count)
    count = count % 1000000
    print(count)
    
    