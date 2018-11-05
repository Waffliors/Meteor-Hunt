import pygame

# Dimensões da tela
screen = pygame.display.set_mode([0, 0], pygame.FULLSCREEN)
X, Y = screen.get_size();

# Cores
BLACK = (0, 0, 0)
BROWN = (163, 127, 44)
WHITE = (255, 255, 255)

ASTEROID_ANIMATION_SPEED = 5
ASTEROID_MOVE_SPEED = 3
ASTEROID_SUMMON_TIME = 120
BULLET_SPEED = 10