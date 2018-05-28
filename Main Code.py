import pygame
import random as rnd
import scipy as sp

from Variables import *

from Goals import *
from Boid import *
from Leader import *
from Informed import *

from Noise import Va

from Room import *

import matplotlib.pyplot as plt

params = {
   'axes.labelsize': 27,
   'font.size': 22,
   'font.family': 'sans-serif', 
   'font.serif': 'Arial', 
   'legend.fontsize': 27,
   'xtick.labelsize': 20,
   'ytick.labelsize': 20, 
   'figure.figsize': [10,8] 
} 
plt.rcParams.update(params)
plt.grid()

plt.xlim(0,250)
plt.ylim(0,1)

plt.ylabel("Level of Emotion")
plt.xlabel("Frame count")


pygame.init()                                           # Initialise game

clock = pygame.time.Clock()                             # Set clock


# Check for special scenarios
if Divide == True:                                      # Set up two-goal-scenario
        
    goal_left=Goal_left()
    goals.add(goal_left)
    
    goal_right=Goal_right()
    goals.add(goal_right)
    
for i in range(N):                                      # Create boids and add to sprite group
    boid=Boid()
    all_sprites.add(boid)
  
for i in range(L):                                      # Create leaders and add to sprite group
    leader=Leader()
    leaders.add(leader)

for i in range(G):                                      # Create goals and add to sprite group
    goal=Goal()
    goals.add(goal)
    
for i in range(I):                                      # Create goals and add to sprite group
    informer=Informed()
    all_sprites.add(informer)
                                                            
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
            
        for sprite in all_sprites:
            plt.plot(Count,sprite.memory)
    
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
