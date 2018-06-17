import pygame
import random as rnd
import scipy as sp
import matplotlib.pyplot as plt

from Variables import *
from Input import *

from Goals import *
from Boid import *
from Leader import *
from Informed import *
from Physicists import *

from Floorplan import *
from Room import *

from Noise import Va
"""
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
"""
pygame.init()                                           # Initialise game

font = pygame.font.Font(None, 32)
clock = pygame.time.Clock()                             # Set clock

button=Button()

# Check for special scenarios
if Divide == True:                                      # Set up two-goal-scenario
        
    goal_left=Goal_left()
    goals.add(goal_left)
    
    goal_right=Goal_right()
    goals.add(goal_right)

if Randomise == True:
    for i in range(N):                                      # Create boids and add to sprite group
        boid=Boid((0,0))
        all_sprites.add(boid)
  
for i in range(L):                                      # Create leaders and add to sprite group
    leader=Leader()
    leaders.add(leader)

for i in range(G):                                      # Create goals and add to sprite group
    goal=Goal()
    goals.add(goal)
    
for i in range(I):                                      # Create goals and add to sprite group
    informer=Informed((0,0))
    all_sprites.add(informer)

if Blackett == True:
    floorplan=Floorplan()
    background=pygame.sprite.Group()
    background.add(floorplan)
    
cohesion = InputBox(250, 680, 40, 40,C,font)
alignment = InputBox(250, 730, 40, 40,A,font)
repulsion = InputBox(250, 780, 40, 40,R,font)
rcohesion = InputBox(470, 680, 40, 40,cohesionradius,font)
ralignment = InputBox(470, 730, 40, 40,alignmentradius,font)
rrepulsion = InputBox(470, 780, 40, 40,repulsionradius,font)
input_boxes = [cohesion,alignment,repulsion,rcohesion,ralignment,rrepulsion]
    
physicists(Randomise)
roomfunc(Room)
    
count=0                                                 # Set Count
Count=[]
Positionx=[]
Positiony=[]

Boxon=False

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
        if Boxon==True:
            for box in input_boxes:
                box.handle_event(event,font)
        button.handle_event(event)
    
    if button.activate==True:
        Boxon=True
    else:
        Boxon=False
    
    if Boxon==True:          
        for box in input_boxes:
            box.update()
        
        for s in all_sprites:
            s.Coh=cohesion.value
            s.Al=alignment.value
            s.Rep=repulsion.value
            s.RC=rcohesion.value
            s.RA=ralignment.value
            s.RR=rrepulsion.value
            
        for s in informed:
            s.Coh=cohesion.value
            s.Al=alignment.value
            s.Rep=repulsion.value
            s.RC=rcohesion.value
            s.RA=ralignment.value
            s.RR=rrepulsion.value
            
    Positionx.append(pygame.mouse.get_pos()[0])
    Positiony.append(pygame.mouse.get_pos()[1])

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
            
        #for sprite in all_sprites:
            #plt.plot(Count,sprite.memory)
    
    for sprite in all_sprites:                              # Check wall collisions
        sprite.collide(room)
                
    for sprite in leaders:
        sprite.collide(room)
        
    for sprite in informed:
        sprite.collide(room)
    
    all_sprites.update()                                    # Get new movement direction
    leaders.update()
    informed.update()
    
    pygame.display.set_caption("Frame {0}".format(count))   # Frame count as window title
    
    screen.fill((255,255,255))                              # Recolour screen to remove sprite traces
    #screen.blit(TextSurf, TextRect)

    room.draw(screen)
    goals.draw(screen)
    
    if Blackett == True:
        screen.blit(floorplan.image, floorplan.rect)
    
    for box in input_boxes:
        box.draw(screen,Boxon)
        
    if Boxon==True:
        message_display("Cohesion:",140,700)
        message_display("Alignment:",140,750)
        message_display("Repulsion:",140,800)
        message_display("Repulsion:",140,800)
        
        message_display("--Strength--",350,660)
        message_display("--Radius--",565,660)

    screen.blit(button.image, button.rect)
    
    all_sprites.draw(screen)                                # Draw all objects onto the screen
    leaders.draw(screen)
    informed.draw(screen)

    pygame.display.flip()                                   # Update screen
                
pygame.quit()
