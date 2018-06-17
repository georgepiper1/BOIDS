#%%
import pygame
import random as rnd
import scipy as sp
from Variables import *

class left (pygame.sprite.Sprite):
    
    def __init__ (self,p,wi,he,x,y):
        
        pygame.sprite.Sprite.__init__(self)       
        self.image = pygame.Surface((wi,he))
        self.image.fill((0,0,0))
        self.rect=self.image.get_rect()
        #self.rect.center=(430,height/2)
        self.rect.center=(p[0]+x,p[1]+y)
        self.type=1
        
class right (pygame.sprite.Sprite):
    
    def __init__ (self,p,wi,he,x,y):
        
        pygame.sprite.Sprite.__init__(self)       
        self.image = pygame.Surface((wi,he))
        self.image.fill((0,0,0))
        self.rect=self.image.get_rect()
        self.rect.center=(p[0]+x,p[1]+y)
        self.type=2
        
class cright (pygame.sprite.Sprite):
    
    def __init__ (self,p,wi,he,x,y):
        
        pygame.sprite.Sprite.__init__(self)       
        self.image = pygame.Surface((wi,he))
        self.image.fill((0,0,0))
        self.rect=self.image.get_rect()
        self.rect.center=(p[0]+x,p[1]+y)
        self.type=3

class bottom (pygame.sprite.Sprite):
    
    def __init__ (self,p,wi,he,x,y):
        
        pygame.sprite.Sprite.__init__(self)       
        self.image = pygame.Surface((wi,he))
        self.image.fill((0,0,0))
        self.rect=self.image.get_rect()
        self.rect.center=(p[0]+x,p[1]+y)
        self.type=4
        
class top (pygame.sprite.Sprite):
    
    def __init__ (self,p,wi,he,x,y):
        
        pygame.sprite.Sprite.__init__(self)       
        self.image = pygame.Surface((wi,he))
        self.image.fill((0,0,0))
        self.rect=self.image.get_rect()
        self.rect.center=(p[0]+x,p[1]+y)
        self.type=5
        
class cleft (pygame.sprite.Sprite):
    
    def __init__ (self,p,wi,he,x,y):
        
        pygame.sprite.Sprite.__init__(self)       
        self.image = pygame.Surface((wi,he))
        self.image.fill((0,0,0))
        self.rect=self.image.get_rect()
        self.rect.center=(p[0]+x,p[1]+y)
        self.type=6

class Exit_Left (pygame.sprite.Sprite):
    
    def __init__ (self,p,x,y):
        
        pygame.sprite.Sprite.__init__(self)       
        self.image = pygame.Surface((30,20))
        self.image.fill((255,0,0))
        self.rect=self.image.get_rect()
        self.rect.center=(p[0]+x,p[1]+y)
        
        self.pos=pygame.math.Vector2(self.rect.center[0],self.rect.center[1])
        self.number=0

class Exit_Right (pygame.sprite.Sprite):
    
    def __init__ (self,p,x,y):
        
        pygame.sprite.Sprite.__init__(self)       
        self.image = pygame.Surface((20,30))
        self.image.fill((255,0,0))
        self.rect=self.image.get_rect()
        self.rect.center=(p[0]+x,p[1]+y) 
        
        self.pos=pygame.math.Vector2(self.rect.center[0],self.rect.center[1])
        self.number=0

        
        