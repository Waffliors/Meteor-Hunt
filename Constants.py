import pygame

# Dimensões da tela
screen = pygame.display.set_mode([0, 0], pygame.FULLSCREEN)
X, Y = screen.get_size()

# Cores
BLACK = (0, 0, 0)
BROWN = (163, 127, 44)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

ASTEROID_MOVE_SPEED = 1
ASTEROID_SUMMON_TIME = 60
BACKGROUND_SPEED = 2
BULLET_SPEED = 10
