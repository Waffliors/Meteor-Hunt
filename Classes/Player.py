import pygame

BLACK = (0, 0, 0)

class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """

    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.image.load("./Images/space_ship.png").convert()
        self.image.set_colorkey(BLACK)


    def update(self):
        """ Update the player's position. """
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        return pygame.mouse.get_pos()
































































































