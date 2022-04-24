# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 08:49:10 2022

@author: Moogie
"""

'''
Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:

1. AA-AA ; 1
2. AA-Aa ; 1
3. AA-aa ; 1
4. Aa-Aa ; 0.75
5. Aa-aa ; 0.5
6. aa-aa ; 0
Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.

Sample Dataset
1 0 0 1 0 1
Sample Output
3.5

Multiply couples * probabilities * 2 (offspring) and add them?

'''

def expected_offspring(a,b,c,d,e,f):
    '''
    Takes # of couples per corresponding Mendelian genotype-pairings
    Returns # (float) of expected offspring to have dominant phenotype
    '''
    A = 1
    B = 1
    C = 1
    D = 0.75
    E = 0.5
    # respective probabilities of dominant phenotype
    
    # Sum of (Number of couples*corresponding probability*Number of offspring)
    return float((a*A*2)+(b*B*2)+(c*C*2)+(d*D*2)+(e*E*2))