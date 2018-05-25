#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 16:48:02 2018

@author: bennetwindt
"""
import pygame



# Dimensions of the screen
width=1080
height=900

# Number of boids
N=35

# Boid speed
s=10

# Weighting factors
C=1         # Cohesion 
A=5         # Alignment 
R=20        # Repulsion

# Radii
repulsionradius = 50
alignmentradius = 120
cohesionradius = 250

# Noise amplitude
n=0



# 0,0 vector
zero=pygame.math.Vector2(0,0)

#Sprite Group
all_sprites=pygame.sprite.Group()

