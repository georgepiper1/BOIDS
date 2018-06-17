import pygame

# Special Scenarios
Divide = False
Room = False
Blackett = False

Bottleneck = False

Randomise = False

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
N=25
G=0
L=0
I=0

# Boid speed
max_speed=5
normal_speed = 3

# Weighting factors
C=2             # Cohesion 
A=3             # Alignment 
R=6             # Repulsion
D=2             # Goal-seeking
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
ihat=pygame.math.Vector2(1,0)
jhat=pygame.math.Vector2(0,1)

#Sprite Groups
all_sprites=pygame.sprite.Group()
goals=pygame.sprite.Group()
leaders=pygame.sprite.Group()
room=pygame.sprite.Group()
informed=pygame.sprite.Group()
slides=pygame.sprite.Group()

# For two-goal-scenario:
x=width/2
y=height/2
