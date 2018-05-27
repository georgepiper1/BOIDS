#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 20:40:51 2018

@author: bennetwindt
"""

import pygame
import random as rnd
import scipy as sp

from Variables import *

from Goals import *
from Boid import *

from Noise import Va

from Room import *


pygame.init()                                           # Initialise game

clock = pygame.time.Clock()                             # Set clock

boidfunc(Divide)                                        # Check for special scenarios
roomfunc(Room)
    
count=0                                                 # Set Count
Count=[]
    
mainloop = True                                         # Run game

while mainloop:
        
    clock.tick(30)                                          # Set FPS
    
    for event in pygame.event.get():                        # Quitting mechanism
        if event.type == pygame.QUIT:
            mainloop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False
        if event.type == pygame.KEYDOWN:                    # Screenshot mechanism
            if event.key == pygame.K_s:
                pygame.image.save(screen,"Screenshot.jpg")
    
    count += 1                                              # Count each frame
    Count.append(count)
    
    if len(all_sprites)==0:
        mainloop = False
    
    if Frames != 0:                                         # Automated quitting function
        if count == Frames:                             
            mainloop = False
    if mainloop == False:                                       # Print Frame Count
        print("Total Frame Count: {0}".format ( count ))
        
        for sprite in goals:                                    # Print boids at each goal
            print("Goal at {0}:".format(sprite.rect.x))
            print("{0} boids collected".format (sprite.number))
    
    for sprite in all_sprites:                              # Check wall collisions
        sprite.collide(room)
                
    for sprite in leaders:
        sprite.collide(room)
    
    all_sprites.update()                                    # Get new movement direction
    leaders.update()
    informed.update()
    
    pygame.display.set_caption("Frame {0}".format(count))   # Frame count as window title
    
    screen.fill((255,255,255))                              # Recolour screen to remove sprite traces
    
    all_sprites.draw(screen)                                # Draw all objects onto the screen
    leaders.draw(screen)
    goals.draw(screen)
    room.draw(screen)
    informed.draw(screen)
    
    pygame.display.flip()                                   # Update screen
                
pygame.quit()
