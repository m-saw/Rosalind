# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 14:54:47 2022

@author: Moogie
"""
"""
Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.

Sample Dataset
AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
Sample Output
MAMAPRTEINSTRING
"""
"""
UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA *      CAA Q      AAA K      GAA E
UAG *      CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA *      CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G 
"""

def RNA_protein(s):
    
    # d = {'F': ['UUU','UUC'],
    #      'L': ['UUA', 'UUG','CUU','CUC','CUA','CUG'],
    #      'S': ['UCU','UCC','UCA','UCG','AGU','AGC'],
    #      'Y': ['UAU','UAC'],
    #      '*': ['UAA','UAG','UGA'],
    #      'C': ['UGU','UGC'],
    #      'W': 'UGG',
    #      'P': ['CCU','CCC','CCA','CCG'],
    #      'H': ['CAU','CAC'],
    #      'Q': ['CAA','CAG'],
    #      'R': ['CGU','CGC','CGA','CGG','AGA','AGG'],
    #      'I': ['AUU','AUC','AUA'],
    #      'M': ['AUG'],
    #      'T': ['ACU','ACA','ACC','ACG'],
    #      'N': ['AAU','AAC'],
    #      'K': ['AAA','AAG'],
    #      'V': ['GUU','GUC','GUA','GUG'],
    #      'A': ['GCU','GCC','GCA','GCG'],
    #      'D': ['GAU','GAC'],
    #      'E': ['GAA','GAG'],
    #      'G': ['GGU','GGC','GGA','GGG']
    #      }
    
    d = {
        'UUU' :'F','CUU' :'L','AUU' :'I',     
        'GUU' :'V','UUC' :'F','CUC' :'L',      
        'AUC' :'I','GUC' :'V','UUA' :'L',     
        'CUA' :'L','AUA' :'I','GUA' :'V',
        'UUG' :'L','CUG' :'L','AUG' :'M',     
        'GUG' :'V','UCU' :'S','CCU' :'P',      
        'ACU' :'T','GCU' :'A','UCC' :'S',      
        'CCC' :'P','ACC' :'T','GCC' :'A',
        'UCA' :'S','CCA' :'P','ACA' :'T',      
        'GCA' :'A','UCG' :'S','CCG' :'P',      
        'ACG' :'T','GCG' :'A','UAU' :'Y',      
        'CAU' :'H','AAU' :'N','GAU' :'D',
        'UAC' :'Y','CAC' :'H','AAC' :'N',      
        'GAC' :'D','UAA' :'*','CAA' :'Q',      
        'AAA' :'K','GAA' :'E','UAG' :'*',   
        'CAG' :'Q','AAG' :'K','GAG' :'E',
        'UGU' :'C','CGU' :'R','AGU' :'S',      
        'GGU' :'G','UGC' :'C','CGC' :'R',      
        'AGC' :'S','GGC' :'G','UGA' :'*',   
        'CGA' :'R','AGA' :'R','GGA' :'G',
        'UGG' :'W','CGG' :'R','AGG' :'R',      
        'GGG' :'G' 
        }
    
    codon = ''
    codon_list = []
    i = 0
    while i < len(s)-3: # for i in s[::3 ?]
        codon = s[i] + s[i+1] + s[i+2]
        codon_list.append(codon)
        
        i += 3
        
    # print(codon_list)
    protein = ''
    for string in codon_list:
        #if string in d and d[string] != '*':
        protein += d[string]
    
    # print(codon_list)
    return protein
    
    
    
    
    
    
    
    
    
    
    
    
    