# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 10:47:49 2022

@author: Moogie
"""
# =============================================================================


#An event is simply a collection of outcomes. Because outcomes are distinct, the probability of an event can be written as the sum of the probabilities of its constituent outcomes. For our colored ball example, let A be the event "Y is blue." Pr(A) is equal to the sum of the probabilities of two different outcomes: Pr(X=blue and Y=blue)+Pr(X=red and Y=blue), or 3/10 + 1/10 = 2/5 ... where 3/10 and 1/10 are at the 'ends' of the probability tree diagram.



# Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
# 
# Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
# 
# Sample Dataset
# 2 2 2
# Sample Output
# 0.78333
# =============================================================================

# d = YY
# h = Yy
# r = yy
def Mendel(d,h,r):
    total = d+h+r
    # first choice prob
    Pr_d1 = d/total
    Pr_h1 = h/total
    Pr_r1 = r/total
    # second choice prob, w/o replacing first, assuming first choice was same
    Pr_d2 = (d-1)/(total-1)
    Pr_h2 = (h-1)/(total-1)
    Pr_r2 = (r-1)/(total-1)
    
    
    Pr_dd = Pr_d1 * Pr_d2 * 1
    Pr_dh = Pr_d1 * (h/(total-1)) * 1
    Pr_dr = Pr_d1 * (r/(total-1)) * 1
    
    Pr_hd = Pr_h1 * (d/(total-1)) * 1
    Pr_hh = Pr_h1 * Pr_h2 * 0.75
    Pr_hr = Pr_h1 * (r/(total-1)) * 0.50
    
    Pr_rd = Pr_r1 * (d/(total-1)) * 1
    Pr_rh = Pr_r1 * (h/(total-1)) * 0.50
    Pr_rr = Pr_r1 * Pr_r2 * 0 
    
    Dom_Pr = Pr_dd + Pr_dh + Pr_dr + Pr_hd + Pr_hh + Pr_hr + Pr_rd + Pr_rh + Pr_rr
    return Dom_Pr

    