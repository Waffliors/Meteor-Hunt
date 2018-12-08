import pygame
import Constants

class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """

    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.image.load("./Images/Spaceship/playerShip1_green.png")
        self.rect = self.image.get_rect()
        self.life = 4
        self.control = ""
        self.rect.x = Constants.X / 2
        self.rect.y = Constants.Y / 2
        pygame.mouse.set_pos(Constants.X / 2, Constants.Y / 2)

    def update(self):
        keys = pygame.key.get_pressed()

        if self.control == "Teclado":
            if self.rect.x < 10:
                self.rect.x = 11
            elif self.rect.x > Constants.X - 110:
                self.rect.x = Constants.X - 111
            elif self.rect.y < 10:
                self.rect.y = 11
            elif self.rect.y > Constants.Y - 85:
                self.rect.y = Constants.Y - 86

            if keys[pygame.K_LEFT]:
                self.rect.x -= 15
            if keys[pygame.K_RIGHT]:
                self.rect.x += 15
            if keys[pygame.K_UP]:
                self.rect.y -= 15
            if keys[pygame.K_DOWN]:
                self.rect.y += 15

        elif self.control == "Mouse":
            pos = pygame.mouse.get_pos()
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