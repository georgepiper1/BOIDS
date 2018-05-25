#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 20:40:51 2018

@author: bennetwindt
"""

import pygame
import random as rnd
import scipy as sp
from Boid import Boid
from Variables import *

pygame.init()                                       # Initialise game

screen = pygame.display.set_mode((width,height))    # Create screen

clock = pygame.time.Clock()                         # Set clock

for i in range(N):                                  # Create boids and add to sprite group
    boid=Boid()
    all_sprites.add(boid)

mainloop = True                                     # Start running game

while mainloop:
        
    clock.tick(30)                                  # Set FPS
    
    for event in pygame.event.get():                # Quitting mechanism
        # User presses QUIT-button.
        if event.type == pygame.QUIT:
            mainloop = False 
        elif event.type == pygame.KEYDOWN:
            # User presses ESCAPE-Key
            if event.key == pygame.K_ESCAPE:
                mainloop = False
    
    all_sprites.update()                            # Get new movement directions

    screen.fill((255,255,255))                      # Recolour screen to remove sprite traces
    all_sprites.draw(screen)                        # Move boids to new positions

    
    pygame.display.flip()                           # Update screen
                
pygame.quit()