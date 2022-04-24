# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 14:01:22 2022

@author: Moogie
"""

# =============================================================================
# Given: Positive integers n≤40 and k≤5.
# 
# Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
# 
# Sample Dataset
# 5 3
# Sample Output
# 19
# =============================================================================


def total_pairs(n, k):
    
    if n == 1 or n == 2:
            return 1
        
    # mature = 0
    # new = 1
    # total = 1      
    month = 1    
    
    mi = 0
    ni = 1
    mj = 0
    nj = 0
        
    while month < n:
        
        # mature,new = mature + new,mature*k

# or: mi ni mj nj ; mi*3=nj, mi+ni=mj ... values of mj and nj become mi and ni
        
        nj = mi*k
        mj = mi + ni
        
        mi = mj
        ni = nj
        
        month += 1
    # total = mature + new
    total = mj + nj
    return total
      
        
    

        