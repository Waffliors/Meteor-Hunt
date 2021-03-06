import pygame
import random
import Constants

class Meteor(pygame.sprite.Sprite):

    def __init__(self):
        """ Constructor. Pass in the color of the block,
        and its size. """

        # Call the parent class (Sprite) constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.image.load("Images/Meteors/meteorBrown_big1.png")
        self.loop_asteroid = 0
        self.value = 3

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

    def reposicionar(self, screen_width):
        self.rect.y = random.randrange(-200, -150)
        self.rect.x = random.randrange(50, screen_width - 130)

    def update(self, screen_width, screen_height, asteroid_speed):
        self.rect.y += asteroid_speed

        if self.rect.y > screen_height:
            self.reposicionar(screen_width)
