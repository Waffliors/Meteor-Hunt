import pygame
import Constants

BLACK = (0, 0, 0)

class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """

    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.image.load("./Images/Spaceship/playerShip1_green.png").convert()
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()

    def update(self):
        """ Update the player's position. """
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()
        # Set the player x position to the mouse x position]
        if self.rect.x < 10:
            pygame.mouse.set_pos(11, pos[1])
            self.rect.x = pos[0]
            self.rect.y = pos[1]
        elif self.rect.x > Constants.X - 110:
            pygame.mouse.set_pos(Constants.X - 111, pos[1])
            self.rect.x = pos[0]
            self.rect.y = pos[1]
        elif self.rect.y < 10:
            pygame.mouse.set_pos(pos[0], 11)
            self.rect.x = pos[0]
            self.rect.y = pos[1]
        elif self.rect.y > Constants.Y - 85:
            pygame.mouse.set_pos(pos[0], Constants.Y - 86)
            self.rect.x = pos[0]
            self.rect.y = pos[1]
        else:
            self.rect.x = pos[0]
            self.rect.y = pos[1]































































































