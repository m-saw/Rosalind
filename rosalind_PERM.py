# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 17:50:53 2022

@author: Moogie
"""
'''
Given: A positive integer n ≤ 7.

Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).

Sample Dataset
3
Sample Output
6
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
'''
import math as math
from itertools import permutations

def perm(x):
    with open('rosalind_PERM_answer.txt','w') as f:

        fact_x = math.factorial(x) # x! total number, not list
        f.write(str(fact_x) + '\n')
        # print(fact_x)
        p = []
        i = 1
        while i < x+1:
            p.append(i)
            i += 1
        # print(p) # Ex: x = 3; [3,2,1]
        
        p_list = list(permutations(p))
        # permutations(p): 
        # This method takes a list as an input 
        # and returns an object list of tuples 
        # that contain all permutations in a list form. 
        # Can also specify length of permutations,
        # e.g. every permutation of 5! as len of 2
    
        for i in p_list: # type(i) = tuple
            for j in i:
            # print(*i) # unpacks; no commas/brackets
                f.write(str(j) + ' ') # Rosalind is ok with space at end
            
            f.write('\n')
         # fp.write('\n'.join(f'{} {}') for i in p_list))
                
        print('file created')

    
