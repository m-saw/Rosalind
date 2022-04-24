# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 12:37:37 2022

@author: Moogie
"""
'import rosalind_REGEX_fileparser as moogie'

import regex as re

def fileparse(x):
    '''
    takes 1 .txt argument
    outputs [['>Rosalind_ID','DNA String'],['>Rosalind_ID','DNA String'],...] 
    
    '''
    # need x as string; .txt
    with open(x,'r') as f:
       lines = f.read() # one big string
       # f.readlines() list of strings
       # print(lines)
    
    lines = lines.replace('\n','')
    
     
    seq = []
    
    matches = re.findall(r'>(Rosalind_\d+)(\w+)',lines) 
    # re.findall() returns a list of the CAPTURED GROUPS
    # print(matches)
    # stripped = re.split(r'(>Rosalind_\d{4})',lines) # list of all the >rosalind's
    
    for match in matches:
        seq.append(list(match))
    # print(seq[0][1])
    return seq