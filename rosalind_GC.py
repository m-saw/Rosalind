# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 14:33:54 2022

@author: Moogie
"""
# =============================================================================
# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# 
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
# 
# Sample Dataset
# >Rosalind_6404
# CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
# TCCCACTAATAATTCTGAGG
# >Rosalind_5959
# CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
# ATATCCATTTGTCAGCAGACACGC
# >Rosalind_0808
# CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
# TGGGAACCTGCGGGCAGTAGGTGGAAT
#
# Sample Output
# Rosalind_0808
# 60.919540
# =============================================================================

#Dictionaries??? ID's and their DNA strings... 
#Maybe look for ">Rosalind_####" or something??? to add to ID's...
#Count all DNA strings' C and G, divide by length or total number of characters...
#then multiply by 100...Could add GC values to list and then max() ? otherwise must make loop.
#then return ID and % value.

#There's also string.split() or .strip('\n') to separate lines by linebreaks \n
#probably easier to just work with the file...

def GC_content(x):
    with open(x, 'r') as f:
        # print(f.readlines())
        
        # new_lines = []
        string = f.read()
        string = string.replace('\n','')
        # print(string)
        # print(line)
        # n = line.replace('\n','')
        n = string.split('>')# .strip() removes characters, use .replace() for specific words and groupings...
        n = n[1:]
        
        # print(n[1][0:13],n[1][13:])
        
        d = {}
        for lines in n:
            d[lines[0:13]] = lines[13:]
        # print(d)
        # print(new_lines)
        
        # d = {}
        # for x in new_lines[::2]:     # [from start to end, skip 1; interval of 2]
        #     d[x] = new_lines[new_lines.index(x) + 1]
        # print(d)
        
        GC_max = ''     # the key that contains the highest GC_percent
        GC_num_max = 0     # reference for value to find the maximum
        for key, value in d.items():
            # print(value)
           
            GC_sum = value.count('G') + value.count('C')
            Total = len(value)
            GC_percent = (GC_sum/Total)*100
            d[key] = [value, GC_percent]     # make into list [] to add another value to same key
            
            if GC_percent > GC_num_max:
                GC_max = key
                GC_num_max = GC_percent
            
        print(GC_max)
        print(GC_num_max)
        # print(d)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        