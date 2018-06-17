#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 13:02:08 2018

@author: bennetwindt
"""

import pygame

from Variables import *
from Room import *

class Floorplan (pygame.sprite.Sprite):
    
    def __init__ (self):                                                        
        
        pygame.sprite.Sprite.__init__(self)                                         
        self.image = pygame.image.load("Floorplan.png").convert()
        self.rect = self.image.get_rect()
        self.rect.top=0
        self.rect.center=(width/2,height/2)
    
def roomfunc (Room):
    
    if Room == True:
        
        p=(0,0)
        room.add(left(p,20,600,width/2-290,height/2))
        room.add(right(p,20,290,width/2+290,height/2+145))
        room.add(bottom(p,600,20,width/2,height/2+290))
        room.add(cright(p,20,270,width/2+290,height/2-165))
        room.add(cleft(p,270,20,width/2+165,height/2-290))
        room.add(top(p,290,20,width/2-145,height/2-290))
        
        goals.add(Exit_Right(p,1030,height/2-15))
        goals.add(Exit_Left(p,width/2+15,140))
        
    if Blackett == True:
        
        p=(width/2-720,height/2-450)
        room.add(top(p,1000,8,880,18))  # Outside
        room.add(left(p,8,320,384,174))
        room.add(top(p,69,8,352,330))
        room.add(left(p,8,90,322,373))
        room.add(bottom(p,334,8,490,414))
        room.add(left(p,8,330,531,577))
        room.add(bottom(p,156,8,613,738))
        room.add(left(p,8,80,695,774))
        room.add(bottom(p,50,8,716,814))
        room.add(bottom(p,174,8,858,770))
        room.add(right(p,8,412,941,568))
        room.add(bottom(p,442,8,1159,365))
        room.add(right(p,8,352,1376,190))
        
        room.add(bottom(p,110,6,883,364))
        room.add(top(p,110,6,883,370))
        
        room.add(right(p,6,142,830,432))
        room.add(left(p,6,130,836,438))
        
        room.add(bottom(p,60,6,803,494))
        room.add(top(p,60,6,803,500))
        
        #room.add(bottom(p,116,6,593,494))
        #room.add(top(p,116,6,593,500))
        
        room.add(right(p,6,80,774,695))
        room.add(left(p,6,68,780,701))
        
        room.add(right(p,6,48,774,791))
        room.add(left(p,6,42,780,794))
        
        room.add(bottom(p,168,6,861,570))
        room.add(top(p,160,6,857,576))
        
        room.add(right(p,4,12,771,497))
        room.add(right(p,4,12,653,497))
        
        room.add(bottom(p,160,6,857,658))
        room.add(top(p,160,6,857,664))
        
        room.add(right(p,6,50,774,592))
        room.add(left(p,6,38,780,597))
        
        room.add(left(p,6,54,654,582))
        room.add(right(p,6,42,648,588))
        
        room.add(bottom(p,116,6,593,558))
        room.add(top(p,116,6,593,564))
        
        room.add(left(p,6,54,654,682))
        room.add(right(p,6,42,648,688))
        
        room.add(bottom(p,116,6,593,658))
        room.add(top(p,116,6,593,664))
        
        room.add(left(p,6,113,654,472))
        room.add(right(p,6,103,648,477))
        
        room.add(top(p,116,6,593,419))
        
        room.add(right(p,6,80,617,60))
        room.add(left(p,6,80,623,60))
        
        room.add(right(p,6,220,767,132))
        room.add(left(p,6,220,773,132))
        
        room.add(right(p,6,110,997,75))
        room.add(left(p,6,110,1003,75))
        
        room.add(right(p,6,80,997,218))
        room.add(left(p,6,80,1003,218))
        
        room.add(top(p,160,6,920,255))
        room.add(bottom(p,160,6,920,249))
        
        room.add(right(p,6,54,837,273))
        room.add(left(p,6,44,843,278))
        
        room.add(top(p,30,6,1315,255))
        room.add(bottom(p,30,6,1315,249))
        
        room.add(right(p,6,54,1300,273))
        room.add(left(p,6,44,1306,278))
        
        room.add(right(p,6,30,837,347))
        room.add(left(p,6,30,843,347))
        
        room.add(right(p,6,30,1300,347))
        room.add(left(p,6,30,1306,347))
        
        room.add(bottom(p,100,6,664,98))
        room.add(top(p,100,6,664,104))
        
        room.add(bottom(p,86,6,1043,180))
        room.add(top(p,86,6,1043,185))
        
        goals.add(Exit_Left(p,756,814))
        goals.add(Exit_Right(p,1380 ,320))
        
    if Bottleneck == True:
        
        p=(0,0)
        room.add(right(p,6,440,700,220))
        room.add(right(p,6,440,700,680))
        
        room.add(top(p,440,6,922,437))
        room.add(bottom(p,440,6,922,463))
        
        goals.add(Exit_Right(p,1100 ,450))