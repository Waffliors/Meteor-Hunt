import pygame

GREEN = (0, 201, 3)
RED = (255, 0, 0)

class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """

    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.image.load("Images/Lasers/laserGreen10.png")
        self.rect = self.image.get_rect()

    def update(self):
        """ Move the bullet. """
        self.rect.y -= 3