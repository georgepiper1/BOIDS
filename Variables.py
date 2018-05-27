import pygame

# Special Scenarios
Divide = True
Room = False

#Frame Restriction
Frames = 0

# Screen setup
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
w, h = pygame.display.get_surface().get_size()

width=w
height=h
#screen = pygame.display.set_mode((width,height))

# Wrap around Screen:
wrap = False

# Number of boids / goals / leaders
N=57
G=0
L=3
I=0

# Boid speed
s=5

# Weighting factors
C=2             # Cohesion 
A=3             # Alignment 
R=6             # Repulsion
D=2             # Goal-seeking
Dinformed=10    # Goal-seeking for informed boids

S=8             # Leader Strength

# Radii
repulsionradius = 30
alignmentradius = 100
cohesionradius = 200

# Noise amplitude
n=2

# 0,0 vector
zero=pygame.math.Vector2(0,0)

#Sprite Groups
all_sprites=pygame.sprite.Group()
goals=pygame.sprite.Group()
leaders=pygame.sprite.Group()
room=pygame.sprite.Group()
informed=pygame.sprite.Group()

# For two-goal-scenario:
x=width/2
y=height/2
