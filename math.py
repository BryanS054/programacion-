# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 12:21:06 2020

@author: Bryan
"""
import math

def sin(x):
    if 2*x==pi:
        return 0.99999999
    else:
        return None
    
pi=3.14
print(sin(pi/2))
print(math.sin(math.pi/2))
