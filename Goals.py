#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 00:44:17 2018

@author: bennetwindt
"""

import pygame
import random as rnd
import scipy as sp
from Variables import *

# General Goal class
class Goal(pygame.sprite.Sprite):
    
    def __init__ (self):                                                        
        
        pygame.sprite.Sprite.__init__(self)                                         
        self.image = pygame.Surface((50,50),pygame.SRCALPHA,32)                        
        self.image = self.image.convert_alpha()                                         
        pygame.draw.circle(self.image, (255,0,0), (25,25), 25, 0)                         
        
        self.rect = self.image.get_rect()                                               
        self.rect.center = (rnd.randint(10,width-10),rnd.randint(10,height-10))         
        
        xpos=self.rect.x+25
        ypos=self.rect.y+25
        
        self.pos=pygame.math.Vector2(xpos,ypos)

        self.number = 0


# Two-Goal-Scenario goals
class Goal_left(pygame.sprite.Sprite):
    
    def __init__ (self):                                                       
        
        pygame.sprite.Sprite.__init__(self)                                         
        self.image = pygame.Surface((50,50),pygame.SRCALPHA,32)                         
        self.image = self.image.convert_alpha()                                         
        pygame.draw.circle(self.image, (255,0,0), (25,25), 25, 0)                          
        
        self.rect = self.image.get_rect()          
                                     
        self.rect.center = (width/8,height/2)                                   
        xpos=self.rect.x+25
        ypos=self.rect.y+25
        
        self.pos=pygame.math.Vector2(xpos,ypos)

        self.number = 0


class Goal_right(pygame.sprite.Sprite):
    
    def __init__ (self):                                                       
        
        pygame.sprite.Sprite.__init__(self)                                         
        self.image = pygame.Surface((50,50),pygame.SRCALPHA,32)                         
        self.image = self.image.convert_alpha()                                         
        pygame.draw.circle(self.image, (255,0,0), (25,25), 25, 0)                          
        
        self.rect = self.image.get_rect()          
                                     
        self.rect.center = (7*width/8,height/2)                                   
        xpos=self.rect.x+25
        ypos=self.rect.y+25
        
        self.pos=pygame.math.Vector2(xpos,ypos)

        self.number = 0
