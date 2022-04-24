# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 17:43:07 2022

@author: moogie
"""

def fileparse(x):
    # Rosalind is stupid big dummies
    # need x as string; .txt
    with open(x,'r') as f:
       lines = f.read()
    lines = lines.replace('\n','')
    n = lines.split('>')
    n = n[1:]
    seq = []
    for lines in n:
          seq.append(lines[13:])
    return seq