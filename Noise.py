#%%
import random as rnd
import scipy as sp
from Variables import *

# Box-Muller Transform:

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

