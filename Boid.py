#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 16:38:21 2018

@author: bennetwindt
"""

# adding this comment as a test of github
import pygame
import random as rnd
import scipy as sp
from Variables import *

class Boid(pygame.sprite.Sprite):
    
    def __init__ (self):                                                        # Define initial variables
        
        pygame.sprite.Sprite.__init__(self)                                         
        self.image = pygame.Surface((20,20),pygame.SRCALPHA,32)                     # Determine size
        self.image = self.image.convert_alpha()                                     # Make background transparent
        pygame.draw.circle(self.image, (0,0,0), (10,10), 10, 0)                        # Determine shape
        
        self.rect = self.image.get_rect()                                           # Determine rect
        self.rect.center = (rnd.randint(10,width-10),rnd.randint(10,height-10))     # Set random initial position
        
        self.vector=pygame.math.Vector2(rnd.randint(-7,7),rnd.randint(-7,7))    # Set initial velocity to zero
        
    def pos (self):                                                             # Define position vector
        
        xpos=self.rect.x+10
        ypos=self.rect.y+10
        
        pos=pygame.math.Vector2(xpos,ypos)
        
        return pos

    def slowness
    
    
    
    def vcoh (self):                                                            # Cohesion function
        
        CoM=pygame.math.Vector2(0,0)
        
        count=0
        
        for sprite in all_sprites:
            
            d=sprite.pos()-self.pos()
            dmag=d.length()
            
            if dmag < cohesionradius:
            
                CoM += sprite.pos()
                count += 1
        
        CoM=CoM/count
    
        CoMv=CoM-self.pos()
        
        if CoMv.length() == 0:
            return zero
        else:
            return CoMv.normalize()
    
    def vrep (self):                                                            # Repulsion funciton
        
        dist=pygame.math.Vector2(0,0)
        
        for sprite in all_sprites:
            
            d=sprite.pos()-self.pos()
            dmag=d.length()
            
            if dmag < repulsionradius:
                if dmag > 0:
                    d=d.normalize()
                    d=(1/dmag)*d
            else:
                d = zero
        
            dist += d
        
        if dist.length() == 0:
            return zero
        else:
            return -dist.normalize()

    def val (self):                                                             # Alignment function
        
        vav=pygame.math.Vector2(0,0)
        count = 0
        
        for sprite in all_sprites:
            
            d=sprite.pos()-self.pos()
            dmag=d.length()
            
            if dmag < alignmentradius:
            
                vav += sprite.vector
                count += 1
        
        vav=vav/count
        
        if vav.length() == 0:
            return zero
        else:
            return vav.normalize()
    """                                 Repulsion Force from borders
    def lrborder (self):
        
        if self.rect.left < 50:
            d=self.rect.left           
            return 1/(d^3)*pygame.math.Vector2(10,0)
        
        elif self.rect.right > width -50:
            d=width - self.rect.right        
            return 1/(d^3)*pygame.math.Vector2(-10,0)
        
        else:
            return zero

    def tbborder (self):
        
        if self.rect.top < 50:
            d=self.rect.top
            return 1/(d^3)*pygame.math.Vector2(0,11)
        
        elif self.rect.bottom > height -50:
            d=height-self.rect.bottom
            return 1/(d^3)*pygame.math.Vector2(0,-10)
        
        else:
            return zero
    """        
    def noise (self):                                                           # Noise generator
        return pygame.math.Vector2(rnd.randint(-n,n),rnd.randint(-n,n))
        
    def update (self):                                                          # Combined movement vector
        
        v=0.25*self.vector+C*self.vcoh()+R*self.vrep()+A*self.val()+self.noise()
        
        self.vector=v
        
        if v.length() == 0:
            v=zero
        else:
            v=v.normalize()*s
        
        self.rect.x += v.x
        self.rect.y += v.y
        
        
        if self.rect.left > width:                                              # Allow movement across screen borders
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = width
        if self.rect.bottom > height:
            self.rect.top = 0
        if self.rect.top < 0:
            self.rect.bottom = height
        
        
