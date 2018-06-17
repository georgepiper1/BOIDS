#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 22:47:16 2018

@author: bennetwindt
"""

from Variables import *
from Boid import *
from Room import *
import random as rnd

def physicists (Randomise):
    
    if Randomise == False:
        
        p=(width/2-720,height/2-450)
        
        for i in range(0,5): # Comp. Suite
            all_sprites.add(Boid((rnd.randint(1100,1350),rnd.randint(30,220))))
        
        for i in range(0,4): # Annex
            all_sprites.add(Boid((rnd.randint(800,980),rnd.randint(30,230))))
            
        for i in range(0,5): # Main Area
            all_sprites.add(Boid((rnd.randint(410,590),rnd.randint(30,300))))
            
        for i in range(0,2): # Corridor
            all_sprites.add(Boid((rnd.randint(680,810),rnd.randint(280,470))))
        
        all_sprites.add(Boid((570,540)))
        all_sprites.add(Boid((880,420)))
        all_sprites.add(Boid((820,530)))
        all_sprites.add(Boid((570,630)))
        all_sprites.add(Boid((580,710)))
        all_sprites.add(Boid((530,750)))
        all_sprites.add(Boid((840,690)))