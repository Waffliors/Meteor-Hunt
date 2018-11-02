import pygame
import random
import Constants
import Classes.Bullet as bullet
import Classes.Player as player
import Classes.Meteors as meteor

pygame.init()

clock = pygame.time.Clock()
pygame.display.set_caption("Meteor Hunt")
click_do_mouse = pygame.mixer.Sound("./Sounds/laser5.ogg")
background_position = [0, 0]#-2000
background_image = pygame.image.load("./Images/Background/saturn_family1.jpg").convert()

player = player.Player()

# --- Sprite Lists

# List of every sprite
all_sprites_list = pygame.sprite.Group()

# List of each bullet
bullet_list = pygame.sprite.Group()

# List of each meteor
meteor_list = pygame.sprite.Group()
meteors_hit_list = pygame.sprite.Group()

all_sprites_list.add(player)

done = False

block = meteor.Meteor(Constants.BROWN, 20, 15)

for i in range(50):
    block = meteor.Meteor(Constants.BROWN, 20, 15)

    # Set a random location for the meteor
    block.rect.x = random.randrange(Constants.SCREEN_WIDTH)
    block.rect.y = random.randrange(Constants.SCREEN_HEIGHT)

    # all_sprites_list.add(meteor)
    # Add the meteor to the list of objects
    meteor_list.add(block)

while not done:
    pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_do_mouse.play()
            # Fire a bullet if the user clicks the mouse button
            shot = bullet.Bullet()
            # Set the bullet sp ot os where the player is
            shot.rect.x = pos[0]+48
            shot.rect.y = pos[1]-6
            #Add the bullet to the lists
            all_sprites_list.add(shot)
            bullet_list.add(shot)

    # --- Game Logic
    #Call update method on all the sprites
    all_sprites_list.update()
    meteor_list.update(Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT)
    # Calculate mechanics for each bullet
    for shot in bullet_list:
        #Remove the bullet if it fliees up off the screen
        if shot.rect.y < -40:
            bullet_list.remove(shot)
            all_sprites_list.remove(shot)
        # See if the player block has collided with anything.
        meteors_hit_list = pygame.sprite.spritecollide(shot, meteor_list, True)

        # Check the list of collisions.
        for meteor in meteors_hit_list:
            meteor_list.remove(block)
            bullet_list.remove(shot)


    Constants.screen.blit(background_image, background_position)
    Constants.screen.blit(player.image, pos)

    # Roll the background
    '''if background_position[1] >= 0:
        background_position[1] = -2000
    else:
        background_position[1] += 2'''

    # Draw all the sprites
    bullet_list.draw(Constants.screen)
    meteor_list.draw(Constants.screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
