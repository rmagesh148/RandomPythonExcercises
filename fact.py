# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 14:35:58 2016

@author: MaGesh
"""

def factorial(n):
    if n < 1:
        return 1
    else:
        number = n * factorial(n-1)
        return number
        
print factorial(5)