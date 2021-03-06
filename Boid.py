import pygame
import random as rnd
import scipy as sp
from Variables import *
from Noise import noise
from Goals import *


class Boid(pygame.sprite.Sprite):
    
    def __init__ (self,spawn):                                                        # Define initial variables
        
        pygame.sprite.Sprite.__init__(self)                                         
        self.image = pygame.Surface((14,14),pygame.SRCALPHA,32)                     # Determine size
        self.image = self.image.convert_alpha()                                     # Make background transparent
        
        pygame.draw.circle(self.image, (0,0,0), (7,7), 7, 0)
        
        self.rect = self.image.get_rect()                                           # Determine rect
        
        if Divide == True:                                                          # Set initial positions
            self.rect.center = (rnd.randint(x-100,x+100),rnd.randint(y-100,y+100))
        if Bottleneck == True: 
            self.rect.center = (rnd.randint(x-300,x-100),rnd.randint(y-100,y+100))
        elif Room == True:
            self.rect.center = (rnd.randint(447,993),rnd.randint(height/2-145,height/2+145))
        elif Blackett == True:
            if spawn == (0,0):
                p=(width/2-720,height/2-450)
                self.rect.center = (rnd.randint(p[0]+400,p[0]+690),rnd.randint(p[1]+115,p[1]+340))
            else:
                p=(width/2-720,height/2-450)
                self.rect.center = (p[0]+spawn[0],p[1]+spawn[1])
        else:
            self.rect.center = (rnd.randint(100,width-100),rnd.randint(100,height-100))
        
        self.vector=pygame.math.Vector2(rnd.randint(-7,7),rnd.randint(-7,7))        # Set random initial velocity
        
        self.noisex=noise(7)
        self.noisey=noise(7)
        
        self.stop = False
        self.q=rnd.randint(lowerlimit,100)/100    # Level of emotion
        
        self.E=1    # Expression
        self.d=6    # Openness
        
        self.Coh=C
        self.Al=A
        self.Rep=R
        
        self.RC=cohesionradius
        self.RA=alignmentradius
        self.RR=repulsionradius
        
        self.memory=[self.q]
        
    def noise (self):                                                           # Noise generator
        return pygame.math.Vector2(self.noisex,self.noisey)
    
    
# Panic Mechanism -------------------------------------------------------------                          
    def a (self, sprite):        
         
        d=sprite.pos()-self.pos()
        dmag=d.length()
        
        if dmag==0:
            return 0
        else:
            return 1/dmag**2
    
    def indiv_reception (self, sprite):
        
        y=sprite.E*self.a(sprite)*self.d
        
        return y
        
    def total_reception (self):
        
        total=0
        
        for sprite in all_sprites:
            total += self.indiv_reception(sprite)
        
        return total
    
    def qstar (self):
        
        if self.total_reception() == 0:
            return self.q
        
        else:
            q=0
        
            for sprite in all_sprites:
                q += self.indiv_reception(sprite)/self.total_reception()*sprite.q
    
            return q
#------------------------------------------------------------------------------        
    def pos (self):                                                             # Define position vector
        
        xpos=self.rect.x+7
        ypos=self.rect.y+7
        
        pos=pygame.math.Vector2(xpos,ypos)
        
        return pos

    def vcoh (self):                                                            # Cohesion function
        
        CoM=pygame.math.Vector2(0,0)
    
        count=0
        
        for sprite in all_sprites:
            
            d=sprite.pos()-self.pos()
            dmag=d.length()
            
            if dmag < float(self.RC):
  
                CoM += sprite.pos()
                count += 1
        
        if count != 0:
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
            
            if dmag < float(self.RR):
                if dmag > 0:
                    d=d.normalize()
                    d=1/dmag*d
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
            
            if dmag < float(self.RA):
                
                vav += sprite.vector
                count += 1
        
        if count != 0:
            vav=vav/count
        
        if vav.length() == 0:
            return zero
        else:
            return vav.normalize()

    def direct (self):                                                          # Goalseeking Function

        direct=pygame.math.Vector2(0,0)
        
        directcount=0
        
        for sprite in goals:
            
            directcount += 1
            d=sprite.pos-self.pos()
            dmag=d.length()
            dweight=dmag**5
            
            if dmag < 25:
                if self in all_sprites:
                    self.kill()
                    sprite.number += 1
                if self in informed:
                    self.kill()
                    sprite.number += 1
                if self in leaders:
                    self.stop = True
            else:
                direct += 1/dweight*d  
        
        if directcount != 0:  
            direct=direct/directcount
        else:
            direct=zero
        
        if direct.length() == 0:
            return zero
        else:
            return direct.normalize()

    def noise (self):                                                           # Noise generator
        return pygame.math.Vector2(self.noisex,self.noisey)
    
    def leader (self):                                                          # Leadership
        
        vav=pygame.math.Vector2(0,0)
        count = 0
        
        for sprite in leaders:
            
            d=sprite.pos()-self.pos()
            dmag=d.length()
            
            if dmag < float(self.RA):
                
                vav += sprite.vector
                count += 1
        
        if count != 0:
            vav=vav/count
        
        if vav.length() == 0:
            vav =zero
        else:
            vav =vav.normalize()
            
        
        CoM=pygame.math.Vector2(0,0)
        count=0
        
        for sprite in leaders:
            
            d=sprite.pos()-self.pos()
            dmag=d.length()
            
            if dmag < float(self.RC):
  
                CoM += sprite.pos()
                count += 1

        if count != 0:
            CoM=CoM/count
        CoMv=CoM-self.pos()
        
        if CoMv.length() == 0:
            CoMv= zero
        else:
            CoMv= CoMv.normalize()
            
        return A*vav+C*CoMv
    
    
    def collide (self,group):                                                   # Wall collision
        for sprite in group:
            if pygame.sprite.collide_rect(self,sprite):
                if sprite.type == 1:
                    self.rect.left = sprite.rect.right
                if sprite.type == 2:    # R Wall
                    if self.rect.right > sprite.rect.left:
                        if self.rect.bottom > sprite.rect.top:
                            self.rect.right = sprite.rect.left
                if sprite.type == 3:    # R Corner
                    if self.rect.right > sprite.rect.left:
                        if self.rect.top < sprite.rect.bottom:
                            self.rect.right = sprite.rect.left
                if sprite.type == 4:
                    self.rect.bottom = sprite.rect.top
                if sprite.type == 5:    # T Wall
                    if self.rect.top < sprite.rect.bottom:
                        if self.rect.left < sprite.rect.right:
                            self.rect.top = sprite.rect.bottom
                if sprite.type == 6:    # L Corner
                    if self.rect.top < sprite.rect.bottom:
                        if self.rect.right > sprite.rect.left:
                            self.rect.top = sprite.rect.bottom

    def update (self):           
    # Combined movement vector
    
        desired_vector = N/(N+L)*(float(self.Coh)*self.vcoh()+float(self.Al)*self.val())+float(self.Rep)*self.vrep()+n*self.q*self.noise() + D*self.direct() + S*L/(N+L)*self.leader()
        new_vector = self.vector + desired_vector
    
        if new_vector.length() == 0:
            new_vector=zero
        else:
            new_vector=new_vector.normalize()
            
        self.memory.append(self.q)
        
        self.q += self.total_reception()*(self.qstar()-self.q)
        
        new_vector *= normal_speed + self.q* max_speed
        
        self.rect.x += new_vector.x
        self.rect.y += new_vector.y
        
        self.vector=new_vector
        
        if wrap == True:
            if self.rect.left > width:                                              # Allow movement across screen borders
                self.rect.right = 0
            if self.rect.right < 0:
                self.rect.left = width
            if self.rect.bottom > height:
                self.rect.top = 0
            if self.rect.top < 0:
                self.rect.bottom = height
        else:
            if self.rect.right > width:
                self.rect.right = width
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.bottom > height:
                self.rect.bottom = height
            if self.rect.top < 0:
                self.rect.top = 0
                
        self.noisex=noise(7)
        self.noisey=noise(7)
        
    
def boidfunc (Divide):                                                          # Grouping for different scenarios
    
    if Divide == True:                                      # Set up two-goal-scenario
        
        goal_left=Goal_left()
        goals.add(goal_left)
    
        goal_right=Goal_right()
        goals.add(goal_right)
    
    for i in range(N):                                      # Create boids and add to sprite group
        boid=Boid()
        all_sprites.add(boid)
  
    for i in range(L):                                      # Create leaders and add to sprite group
        leader=Boid()
        leaders.add(leader)
    
    for i in range(G):                                      # Create goals and add to sprite group
        goal=Goal()
        goals.add(goal)
        
    for i in range(I):                                      # Create goals and add to sprite group
        informer=Boid()
        informed.add(informer)
