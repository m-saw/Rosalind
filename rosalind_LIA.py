# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 09:16:35 2022

@author: Moogie
"""

import math as m

def Mendel2(k,N):
    '''
    k = generation, <= 7
    N = number of Aa Bb kids, <= 2**k
    
    What is the probability that there will be at least N kids total after gen k?
    
    Sample Dataset: 2, 1
    Output: 0.684
    Pr() that there will be at least 1 Aa Bb kid total after 2 generations
    '''
    # Binomial distribution
    # Pr(Aa Bb) = sum( (n!/s!(n-s)!) * p^s * q^(n-s) )
        # Pr(Aa Bb) = sum( P!/i!*(P-i)! * 0.25**i * 0.75**P-i
    
    # n = # of events = k
    # s = # of times Aa Bb = N
    # n-s = t = # of times result is not Aa Bb
        # t = (2**k) - N
    
    # p = 25% = 0.25
        # p is 0.25 because, mates are always heterozygous, 
        # so chance of hetero is always 4/16, 25%
     # q = 100% - 25% = 0.75   

                                                                        
    
    P = 2**k                                                                       
    probability = 0                                                                
    for i in range(N, P + 1):  
    # why is it range from N to 2**k + 1 ?
    #What does i mean here; is it the chance for hetero each time after the minimum N ?                                                 
        binomial = (m.factorial(P) / (m.factorial(i) * m.factorial(P - i))) * (0.25**i) * (0.75**(P - i))                                                        
        probability += binomial
    print(probability) 


Mendel2(7,35)
    
    # cdf(2^k, (2^k)-n, 0.75)
    # cumulative distribution function
    
    
    
    
    
    
    
    
    
    
    
    
    # Notes
# =============================================================================
#     # Track Aa and Bb separately, then multiply them together?
#     # 2 kids per person in each gen; each person mates with a Aa Bb person.
#     
#     # F0 : Aa Bb X Aa Bb
#     # Pr(Aa X Aa) * Pr(Bb X Bb) = 9 different possible kids.
#     # Aa * Aa:
#         # AA 0.25 ; 1/4
#         # Aa 0.5  ; 2/4
#         # aa 0.25
#     # Bb * Bb:
#         # BB 0.25
#         # Bb 0.5
#         # bb 0.25
#     # total = sum of char in both strings; e.g. 4
#     
#     # F1 : 9 types:
#         # AA BB = Pr(AA) from Aa X Aa * Pr(BB) from Bb X Bb
#             # Pr(AA BB) = 0.25 * 0.25
#         # AA Bb = Pr(AA) * Pr(Bb) and so on
#         # AA bb
#         # Aa BB
#         # Aa Bb:
#             # Pr() = 0.5 * 0.5
#         # Aa bb
#         # aa BB
#         # aa Bb
#         # aa bb
#         
#         # Just A geno:
#             # Aa X Aa:
#                 # AA 0.25
#                 # Aa 0.5
#                 # aa 0.25
#             # Pr_kid1_AA = 0.25 (0.25/2 kids total?);
#             # Pr_kid2_AA = 0.25 ( /2 kids total?)
#             
#             # AA and aa have same Pr
#             
#             # AA X Aa:
#                 # AA 0.5
#                 # Aa 0.5
#             # Aa X Aa:
#                 # AA 0.25
#                 # Aa 0.5
#                 # aa 0.25
#             # aa X Aa:
#                 # aa 0.5
#                 # Aa 0.5
#             # Pr_kid3_AA = 0.25 + 0.5 ? include parent? divide by total?
#             
#             # maybe append each Pr to a list
#             # then multiply them or something?
#             
#     # total_kids = 2^k  # total kids per gen
#     # while i < k:
# =============================================================================
        
            
            