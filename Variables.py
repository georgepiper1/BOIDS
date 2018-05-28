import pygame

# Special Scenarios
Divide = False
Room = False

#Frame Restriction
Frames = 250

# Screen setup
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
w, h = pygame.display.get_surface().get_size()

width=w
height=h
#screen = pygame.display.set_mode((width,height))

# Wrap around Screen:
wrap = False

# Number of boids / goals / leaders
N=20
G=0
L=0
I=0

# Boid speed
s=5

# Weighting factors
C=2             # Cohesion 
A=3             # Alignment 
R=6             # Repulsion
D=3             # Goal-seeking
Dinformed=4    # Goal-seeking for informed boids

S=12             # Leader Strength

# Radii
repulsionradius = 30
alignmentradius = 100
cohesionradius = 200

# Noise amplitude
n=2
lowerlimit=0

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
