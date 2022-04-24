# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 12:24:42 2022

@author: Moogie
"""
'''
Problem

Figure 4. A figure illustrating the propagation of Fibonacci's rabbits if they die after three months.
Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”, which followed the recurrence relation Fn=Fn−1+Fn−2 and assumed that each pair of rabbits reaches maturity in one month and produces a single pair of offspring (one male, one female) each subsequent month.

Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live for three months (meaning that they reproduce only twice before dying).

Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

Sample Dataset
6 3
Sample Output
4

matrix multiplication using a transformational matrix, where
matrix**n-1 gives the answer


k = 1

'''

import numpy as np
from numpy.linalg import matrix_power
import decimal

def fibd(n,d):
    '''
    Given: Positive integers n≤100 and d≤20.

    Return: The total number of pairs of rabbits that will remain after the n-th month,
    if all rabbits live for d months.
    
    Rabbits die after d months including the month they are young
    '''
    # if n == 1:
        # return 1 
    # first month is always one pair
    
    
    dt = np.dtype(np.dtype(decimal.Decimal)) 
    # Have to import and set to Decimal datatype for precision. 
    # Otherwise, Numbers are too large, and cant be rounded accurately.
    
    # starting on the second month:
    # create array to multiply with matrix; LENGTH OF d:
    # rabbits = [0,1,0]  # respectively: 0 young, 1 mature, 0 md
    rabbits = np.zeros((d),dtype=dt)
    rabbits[0] = 1
    
    # print(rabbits)
    
    # transformational matrix if d = 3 month lifespan
    # age of pairs calculated by rows per column
    # y: young; first column y = 
    # m: mature; second column m = 
    # md: last mature; third column md = 
    
    # could create matrix of 0's;
    m = np.zeros((d,d),dtype=dt)
    
    # print(m)
    
    # Fill first row (row 0):
    m[0] = 1
    m[0][0] = 0
    
    # print(m)
    
    # then fill in the rest using a loop;
    i = 1
    while i < d:
        m[i][i-1] = 1
        i += 1
    
    # print(m.T)
    
    # transpose to get final matrix.
    m = m.T
    
    # multiply rabbits with matrix**n months - 1
    m = matrix_power(m, n-1)
    final_rabbits = rabbits@m
    
    print(final_rabbits)
    
    # Get total:
        # can use vector multiplication:
        # new_v = np.full((d),1)
        # new_v = new_v.T
        # answer = final_rabbits@new_v
        
        # or sum() to add all elements of a vector:
    total = sum(final_rabbits)
    print(int(total))
    
    
    
fibd(100, 20)
    
    
    
    

# =============================================================================
# Solution from http://saradoesbioinformatics.blogspot.com/2016/06/mortal-fibonacci-rabbits.html
#     n = 96                                                                         
# m = 17                                                                         
# bunnies = [1, 1]                                                               
# months = 2                                                                     
# while months < n:                                                              
#     if months < m:                                                             
#         bunnies.append(bunnies[-2] + bunnies[-1])                              
#     elif months == m or count == m + 1:                                        
#         bunnies.append(bunnies[-2] + bunnies[-1] - 1)                          
#     else:                                                                      
#         bunnies.append(bunnies[-2] + bunnies[-1] - bunnies[-(                  
#             m + 1)])                                                           
#     months += 1                                                                
# print(bunnies[-1])   
# 
# =============================================================================
    
    
    