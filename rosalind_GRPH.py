# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 12:15:23 2022

@author: Moogie
"""
'''
Problem
A graph whose nodes have all been labeled can be represented by an adjacency list, 
in which each row of the list contains the two node labels corresponding to a unique edge.

For a collection of strings and a positive integer k, 
the overlap graph for the strings is a directed graph Ok in which each string is represented by 
a node, and string s is connected to string t with a directed edge
when there is a length k suffix of s that matches a length k prefix of t, 
as long as s≠t; we demand s≠t to prevent directed loops in the overlap graph 
(although directed cycles may be present).

Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to Overlap of k=3. You may return edges in any order.

Sample Dataset
>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG
Sample Output
Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323
'''

'need last 3 of string1 to match first 3 of string2'

import rosalind_REGEX_fileparser as moogie

def overlap_graph(x):
    collection = moogie.fileparse(x)
    # print(collection)
    
    d = {}
    for items in collection:
        d[items[1]] = items[0]
    # print(d)
    
    sequences = list(d.keys())
    # print(sequences)
    
    t = sequences
    for seq in sequences:   
        for item in t:
            if item == seq:
                pass
            elif seq[-3:] == item[0:3]:
                print(f'{d[seq]} {d[item]}')

    
    
        








