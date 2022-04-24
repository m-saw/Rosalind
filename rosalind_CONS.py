# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 09:16:40 2022

@author: Moogie
"""
'''
A T C C A G C T
G G G C A A C T
A T G G A T C T
A A G C A A C C
T T G G A A C T
A T G C C A T T
A T G C C A C T

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

Sample Dataset
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT

Sample Output
ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6
'''
# Take matrix and turn into one-dimensional vector

import numpy as np
import regex as re

def consensus(x):
    # need x as string; .txt
    with open(x,'r') as f:
       lines = f.read() # one big string
       # f.readlines() list of strings
       # print(lines)
    
    lines = lines.replace('\n','')
    
    # print(lines)
    '''
    n = lines.split('>')
    n = n[1:]
    seq = []
    for lines in n:
          seq.append(lines[13:])
    # print(seq)
    
     for line in lines:
            seq.append(list(line.strip('\n')))
    # print(seq)
    '''   
 
    
    seq = []
    
    matches = re.findall(r'>Rosalind_\d{4}(\w+)',lines) 
    # re.findall() returns a list of the CAPTURED GROUPS
    # print(matches)
    # stripped = re.split(r'(>Rosalind_\d{4})',lines) # list of all the >rosalind's
    
    for match in matches:
        seq.append(list(match))
    # print(seq)

    
    
    m = np.array(seq)
    # print(m.transpose())
    
    # print(m[:][3])
    
    # A,C,G,T = [],[],[],[]
    d = {'A':[],'C':[],'G':[],'T':[]}
    # countA,countC,countG,countT = 0,0,0,0
    
    mylist = []
    max_n = 0
    # max_n_list = []
    for x in m.transpose():
        # new = ''
        # new = new.join(x)
        # d['A'].append(new.count('A')) # returns 0 for some reason
       
        nA = list(x).count('A')
        nC = list(x).count('C')
        nG = list(x).count('G')
        nT = list(x).count('T')
        
        mylist.append(nA)
        mylist.append(nC)
        mylist.append(nG)
        mylist.append(nT)
        
        # max_n_list.append(max(mylist))
        max_n = max(mylist)
        
        if nA == max_n:
            print('A', end='')
        elif nC == max_n:
            print('C', end='')
        elif nG == max_n:
            print('G', end='')
        elif nT == max_n:
            print('T', end='')
        
        mylist = []
        
        d['A'].append(nA)
        d['C'].append(nC)
        d['G'].append(nG)
        d['T'].append(nT)
        
    for k,v in d.items(): 
        # alternatively can just f.write into new file
        print(f'\n{k}: ',end='')
        print(*v, end='')
    
##########################################################          
   # print(d)
   # print(max_n_list)
   # i = 0    
   
   # for k in d.keys():
       
   #     # print(v[i])

   #     if d[k][i] == max_n_list[i]:
   #         print(k)
           
   #     i += 1
            

            
            
            
                        
        
        
        
        
        





