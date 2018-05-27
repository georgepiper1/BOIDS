#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 23:05:23 2018

@author: bennetwindt
"""

#%%
import pygame
import random as rnd
import scipy as sp
from Variables import *

class Left_wall (pygame.sprite.Sprite):
    
    def __init__ (self):
        
        pygame.sprite.Sprite.__init__(self)       
        self.image = pygame.Surface((20,600))
        self.image.fill((0,0,0))
        self.rect=self.image.get_rect()
        self.rect.center=(430,height/2)
        self.type=1
        
class Right_wall (pygame.sprite.Sprite):
    
    def __init__ (self):
        
        pygame.sprite.Sprite.__init__(self)       
        self.image = pygame.Surface((20,290))
        self.image.fill((0,0,0))
        self.rect=self.image.get_rect()
        self.rect.center=(1010,height/2+145)
        self.type=2
        
class Corner_Right (pygame.sprite.Sprite):
    
    def __init__ (self):
        
        pygame.sprite.Sprite.__init__(self)       
        self.image = pygame.Surface((20,270))
        self.image.fill((0,0,0))
        self.rect=self.image.get_rect()
        self.rect.center=(1010,height/2-165)
        self.type=3

class Bottom_wall (pygame.sprite.Sprite):
    
    def __init__ (self):
        
        pygame.sprite.Sprite.__init__(self)       
        self.image = pygame.Surface((600,20))
        self.image.fill((0,0,0))
        self.rect=self.image.get_rect()
        self.rect.center=(width/2,740)
        self.type=4
        
class Top_wall (pygame.sprite.Sprite):
    
    def __init__ (self):
        
        pygame.sprite.Sprite.__init__(self)       
        self.image = pygame.Surface((290,20))
        self.image.fill((0,0,0))
        self.rect=self.image.get_rect()
        self.rect.center=(width/2-145,160)
        self.type=5
        
class Corner_Left (pygame.sprite.Sprite):
    
    def __init__ (self):
        
        pygame.sprite.Sprite.__init__(self)       
        self.image = pygame.Surface((270,20))
        self.image.fill((0,0,0))
        self.rect=self.image.get_rect()
        self.rect.center=(width/2+165,160)
        self.type=6

class Exit_Left (pygame.sprite.Sprite):
    
    def __init__ (self):
        
        pygame.sprite.Sprite.__init__(self)       
        self.image = pygame.Surface((30,20))
        self.image.fill((255,0,0))
        self.rect=self.image.get_rect()
        self.rect.center=(width/2+15,140)
        
        self.pos=pygame.math.Vector2(self.rect.center[0],self.rect.center[1])
        self.number=0

class Exit_Right (pygame.sprite.Sprite):
    
    def __init__ (self):
        
        pygame.sprite.Sprite.__init__(self)       
        self.image = pygame.Surface((20,30))
        self.image.fill((255,0,0))
        self.rect=self.image.get_rect()
        self.rect.center=(1030,height/2-15) 
        
        self.pos=pygame.math.Vector2(self.rect.center[0],self.rect.center[1])
        self.number=0

def roomfunc (Room):
    
    if Room == True:
        left_wall=Left_wall()
        room.add(left_wall)
        
        right_wall=Right_wall()
        room.add(right_wall)
        
        bottom_wall=Bottom_wall()
        room.add(bottom_wall)
        
        right_corner=Corner_Right()
        room.add(right_corner)
    
        left_corner=Corner_Left()
        room.add(left_corner)
        
        top_wall=Top_wall()
        room.add(top_wall)
    
        lexit=Exit_Left()
        goals.add(lexit)
        
        rexit=Exit_Right()
        goals.add(rexit)
        