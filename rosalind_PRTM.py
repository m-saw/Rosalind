# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 13:31:27 2022

@author: Moogie
"""
'''
Thus, the mass of a protein is the sum of masses of:
all its residues,
    (molecules where rxn = 1 water molecule is removed)
    i.e. every aa in a protein except the leftmost and rightmost ones
    (bc their ends aren't bonded to another aa)

plus the mass of a single water molecule.

monoisotopic mass is computed by using
the principal (most abundant) isotope of each atom in the amino acid
Many applications in proteomics rely on mass spectrometry;
monoisotopic is used > average mass

The standard unit used in mass spectrometry for measuring mass
is the atomic mass unit, which is also called the dalton (Da)

The mass of a protein is the sum of the monoisotopic masses 
of its amino acid residues plus the mass of a single water molecule 
(whose monoisotopic mass is 18.01056 Da).

we are going to avoid the complication of having to distinguish 
between residues and non-residues by only considering peptides 
excised from the middle of the protein.
This is a relatively safe assumption because in practice, 
peptide analysis is often performed in tandem mass spectrometry. 
In this special class of mass spectrometry, a protein is first divided 
into peptides, which are then broken into ions for mass analysis.
-------------------------------------------------------------------
Problem
In a weighted alphabet, every symbol is assigned a positive real number
called a weight. A string formed from a weighted alphabet is called a 
weighted string, and its weight is equal to the sum of the weights 
of its symbols.

The standard weight assigned to each member of the 20-symbol amino acid 
alphabet is the monoisotopic mass of the corresponding amino acid.

Given: A protein string P of length at most 1000 aa.

Return: The total weight of P. Consult the monoisotopic mass table

Sample Dataset
SKADYEK
Sample Output
821.392
-------------------------------------------------------------------
The monoisotopic mass table for amino acids
is a table listing the mass of each possible amino acid residue, 
where the value of the mass used is the monoisotopic mass of each 
residue.
Note: the monoisotopic mass of water:
    is considered 18.01056 Da.

[In Daltons (Da):]
'''
table = '''
A 71.03711
C 103.00919
D 115.02694
E 129.04259
F 147.06841
G 57.02146
H 137.05891
I 113.08406
K 128.09496
L 113.08406
M 131.04049
N 114.04293
P 97.05276
Q 128.05858
R 156.10111
S 87.03203
T 101.04768
V 99.06841
W 186.07931
Y 163.06333
'''
# NOTE: We're calculating WEIGHT of string P, not the monoisotopic mass
# of protein P; I guess that means we do NOT add water mass.
import regex as re

aa = re.findall(r'([A-Z])', table)
weight = re.findall(r'(\d+\.?\d+)', table)
# print(aa)
# print(weight)

# Can also do s/t like this to process table ? 
# mmt = dict(zip(mmt[::2],map(float,mmt[1::2])))

massd = {}

c = 0
for item in aa:
    massd[item] = float(weight[c])
    c += 1
# print(massd)
# print(d['M'])


def PRTM(p):
    total = 0.0
    # for i in p:
    #     total += massd[i]
    total = sum(massd[i] for i in p)
    print(round(total,3))

# PRTM('SKADYEK')
# PRTM('PTFKLWYSRLGELARQVAPSETQRAWGPQERGHVYEGKRDIASAGDRQHWLIDEASVLVSCMRWPFHDWRSSVECDNAPEKCDDHRRTIFACERCMFQCANPAFYAYPLWWFPSICNMGFIDLPCNVEECQQIHAPYARWLEKLCCWITTLMHEAENKNTSVRQKSPPRHEMFRIHCMPKFYRQQKCQGWKADMGQWYFVPVWYACRTIFVWCVLQGHFFLQGTKYEWKEDNIIYGPAMYFAHSFDHCTCQSSMTEMSNASIQVMTFTYTESHVCYLMVWMTNAVDKPHYPMWCRWGGMVIDSPQLGKWLGKNWEYMMTWMGYKSPATPIDPWGKYISNGWAMQFPPPDDTIDTHWPRNLNQHLKPDCHFFFSCNIHSLSSDLGWPGPDRRNLIQHDEFWCVIDMVTCKKWMVCFMPTQMGMVNKSLEGQFGQPQAKNHPPRTDSMECILEVPLNNKPTISEPDKGAMCMMHTFFLYVIQNSCEIQQRLQHTALGEGEPQTWVMLAFGWRKKQNCNKGKLFSMENVMDLLCHPAQNNGMCTVNKSTNQFVMTEHDVRSFWFKDSLHFARCELNMTEPLGCLFDAHKQRVWGYPWAPGKLIPSWMPDVVKQQLKEQCFHPRRFVTMMWQYYDDSWGIHMECMREKPKRKNCRRAVIYYSEYCVDDHHWDDGEDETFYDCSDRTFKMFWGQNVKYYKGFRLWSRGFSGDPFHIFSHRGYPAMRQLFYFWWHQFAFWFGAFQGARRSWTPKPVSFWYSNTGVKCLKGKVFPRHIAAWHQTIQTHCHFMMHCAMVGYKMYLIGVCKVDLCQQLMSCTSSPVFVADVVYQWDQHGYASCGGWEEMSDDVMCLCSRNQQWICQCTRSYWGKGPCYWNPGFHVGVLVKPQGVPCIWSHDRPKIIIEIRKVVNACGEVQQPITQENYLAKNTWYHPYVGVHGRWELYLPAAIQFIVLNYTVWAWTHILAFWYAYSNMPLGDCDNMGDYQYHFCRAGC')


