import pygame
import Classes.Bullet as bullet
import Classes.Player as player
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Aula de sprite")
clock = pygame.time.Clock()
click_do_mouse = pygame.mixer.Sound("./Sounds/laser5.ogg")
background_position = [0, 0]
background_image = pygame.image.load("./Images/Background/saturn_family1.jpg").convert()

player = player.Player()

# --- Sprite Lists

# List of every sprite
all_sprites_list = pygame.sprite.Group()

# List of each bullet
bullet_list = pygame.sprite.Group()

all_sprites_list.add(player)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_do_mouse.play()
            # Fire a bullet if the user clicks the mmouse button
            shot = bullet.Bullet()
            # Set the bullet sp ot os wjere tje player is
            shot.rect.x = player.update()[0]+48
            shot.rect.y = player.update()[1]-4
            #Add the bullet to the lists
            all_sprites_list.add(shot)
            bullet_list.add(shot)

    # --- Game Logic
    #Call update method on all the sprites
    all_sprites_list.update()

    # Calculate mechanics for each bullet
    for shot in bullet_list:
        #Remove the bullet if it fliees up off the screen
        if shot.rect.y < -600:
            print(shot.rect.x, shot.rect.y)
            bullet_list.remove(shot)
            all_sprites_list.remove(shot)

    pos = player.update()

    screen.blit(background_image, background_position)
    screen.blit(player.image, pos)

    # Draw all the sprites
    bullet_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
