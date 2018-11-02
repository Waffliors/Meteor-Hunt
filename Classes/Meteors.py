import pygame
import random

class Meteor(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its size. """

        # Call the parent class (Sprite) constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

    def reposicionar(self, screen_width):
        self.rect.y = random.randrange(-100, -10)
        self.rect.x = random.randrange(0, screen_width)

    def update(self, screen_width,screen_height):
        self.rect.y += 1

        if self.rect.y > screen_height:
            self.reposicionar(screen_width)
