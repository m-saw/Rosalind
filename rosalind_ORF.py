# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 09:55:12 2022

@author: Moogie
"""
'''
Given: A DNA string s of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.

Sample Dataset
>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG
# 96 letters ; 32 codons

Sample Output
MLLGSFRLIPKETLIQVAGSSPCNLS # 26 letters
M
MGMTPRLGLESLLE
MTPRLGLESLLE

***INCLUDE REVERSE COMPLEMENT***
'''

# Regex ; pattern r'(?=(M\w*)\*)' ?= for overlap
import rosalind_REVC as REVC
import rosalind_PROT as PROT
import rosalind_REGEX_fileparser as rosparse
import regex as re


def DNA_ORF(s):
    
    RNA = ''
    for char in s:
        if char == 'T':
            RNA += 'U'
        else:
            RNA += char
    # print('Forward: '+RNA) # prints whole string with U replacing T
    
    reverse_RNA = ''
    reverse_RNA = REVC.RNA_REVC(RNA)
    # print('Reverse(L to R): '+reverse_RNA)
    # reverse complement function previously made :)
    
    
    AUG_p = r'(?=(AUG\w*))' # (.{3}) for codons (?=(AUG\w*)\*) for overlap, whole string
    read = re.findall(AUG_p,RNA) # prints list of grouped matches
    # print(read)
    revc_read = re.findall(AUG_p,reverse_RNA)
    # print(revc_read)
    # Overlap search initially looking for strings beginning with AUG.

    # Using ORF Finder to check; Grouping into 3's first is not correct.
    # It seems it's looking at every letter initially, and if the two letters after it
    # make a start codon, then you begin grouping into 3's from there until the stop.
    
    prot_read = []
    prot_revc_read = []
    for FRNA in read:
        prot_read.append(PROT.RNA_protein(FRNA))
    for RRNA in revc_read:
        prot_revc_read.append(PROT.RNA_protein(RRNA))
    # print(prot_read)
    # print(prot_revc_read)
    
    # Make an ORF List ? Prolly have to go thru 3 at a time?
    # Could separate into triplets, findall(.{3}) per string,
    # Then add to new list with loop and break when i == stop codon?
    # Otherwise, for translated proteins:
    Stop_p = re.compile(r'(M\w*)\*')
    
    # re.search returns a match object
    # Can use match.group(0) to return the matched string..
    Proteins = []
    for Fprot in prot_read:
        if Stop_p.search(Fprot):
            # print((Stop_p.search(Fprot)).group(1))
            Proteins.append((Stop_p.search(Fprot)).group(1))

    for Rprot in prot_revc_read:
        if Stop_p.search(Rprot):
            # print((Stop_p.search(Rprot)).group(1))
            Proteins.append((Stop_p.search(Rprot)).group(1))
    
    Proteins = set(Proteins)
    # print(Proteins)
   
    with open('rosalind_ORF_answer.txt', 'w') as f:
        for item in Proteins:
            f.write(item)
            f.write('\n')
    print('rosalind_ORF_answer.txt created!')
#-----------------------------------------------------------    

x = rosparse.fileparse('rosalind_orf.txt')
x = x[0][1]
DNA_ORF(x)
