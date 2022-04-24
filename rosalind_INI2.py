# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 09:22:00 2022

@author: Moogie
"""
# =============================================================================
# Given: Two positive integers a and b, each less than 1000.
# 
# Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.
# 
# Sample Dataset
# 3 5
# Sample Output
# 34
# pythagorean: a^2 + b^2 = c^2
# =============================================================================
# =============================================================================
# Addition: 2 + 3 == 5
# Subtraction: 5 - 2 == 3
# Multiplication: 3 * 4 == 12
# Division: 15 / 3 == 5
# Division remainder: 18 % 5 == 3
# Exponentiation: 2 ** 3 == 8
# Root: 4 ** (1/2 or 0.5) [Square root] 4 ** (1/3) [Cube root]
# =============================================================================

def square_hyp(a, b):
    ans = (a**2) + (b**2)
    return ans