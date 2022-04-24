# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 15:41:48 2022

@author: Harrison
"""

import numpy as np 

class allele : 
    
    def __init__(self,char): 
        if char == char.lower() : 
            self.v = 'a'
        else : 
            self.v = 'A'
            
        
    def __mul__(self,other):
        return self.v + other.v
    
    def __str__(self): 
        return self.v

class person : 


    
    def __init__(self,first,second):
        self.f = allele(first)
        self.s = allele(second)
    

    

        
    def __str__ (self): 
        return self.f.v+self.s.v
    
    def __add__(self,other) :
        x = np.array([[self.f],[self.s]],dtype=allele)
        y = np.array([[other.f,other.s]],dtype=allele)
        
        z = np.dot(x,y)
        a = np.count_nonzero(z == 'AA') 
        b = np.count_nonzero(z == 'Aa') + np.count_nonzero(z == 'Aa')
        c = np.count_nonzero(z == 'aa')
        
        print(z)
        return (np.array([a,b,c])/4)
        
    
Harrison = person('a','B') 
Marianne = person('A','a')

print(Harrison + Marianne)




    



    

    