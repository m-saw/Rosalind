# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 15:37:49 2022

@author: Moogie
"""

'INCLUDE OVERLAPPING'

import urllib as url
import regex as re

def uniprot_getmotif(s):
    with open(s,'r') as f:
        lines = f.readlines()
        # print(lines)
    for line in lines:
        # print(line.strip('\n'))
        uniprot_searchfasta(line.strip('\n'))
        
def uniprot_searchfasta(i):

    x = url.request.urlopen(r'http://www.uniprot.org/uniprot/'+i+'.fasta')
    # print(x.read())
    x_read = str(x.read())
    # print(x_read)
    
    # print(x_read.split(r'\n'))
    x_read_split = x_read.split(r'\n')
    
    fasta = ''.join(x_read_split[1:-1])
    # print(fasta)
    
    # print(re.findall(r'N[^P][ST][^P]',fasta))
    pattern = re.compile(r'(?=(N[^P][ST][^P]))') # (?=(r'')) includes overlap
    matches = pattern.finditer(fasta)
    # print(list(matches))
    # pprint(dir(matches))
    
    if re.search(pattern, fasta) is None:
        return
    
    print(i) # print ID
    for match in matches:
        print(match.start()+1,end=' ')
    print('')