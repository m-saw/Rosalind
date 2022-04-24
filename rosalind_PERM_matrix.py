# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 16:28:38 2022

@author: Moogie
"""
'''
Given: A positive integer n≤7.

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
import numpy as np
import math as m

def perm(n):
    
    fn = m.factorial(n)
    mat = np.zeros((fn,n))
    # print(mat)
    
    r = 0
    c = 0
    value = 1
    count = 0
    while count < n:
        for x in range(0,n-1): # Write down first column
            mat[r][0] = value
            r += 1
        value += 1
        count += 1
    # print(mat)
    
    value = 1
    for y in mat[0][0:n]: # Write along first row
        mat[0][c] = value
        value += 1
        c += 1
    # print(mat)
    
    r = 1
    c = 1
    count1 = 1
    while count1 < fn: # while count is < 6 (1-5)
        for z in range(1,4): # (range 1-3)
            if z != mat[r][c-1] and z != mat[r-1][c]: # if z is not the same as number above or to the left
                mat[r][c] = z
            else:
                pass
        count += 1 # begin checks for next row, same column
        r += 1
    print(mat)
        
        