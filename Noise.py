#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 20:38:20 2018

@author: bennetwindt
"""

#%%
import random as rnd
import scipy as sp
from Variables import *

# Box-Müller Transform:

def noise (eta):
   
    u1 = rnd.random()
    u2 = rnd.random()

    x=sp.sqrt(-2*sp.log(u1))*sp.cos(2*sp.pi*u2)
    
    return x

# Measuring mean speed

def Va (N):
    
    vectorsum = zero
        
    for sprite in all_sprites:
        vectorsum += sprite.vector
    
    return vectorsum/(N*s)

