import pygame
import Constants
import Classes.Bullet as bullet
import Classes.Player as player
import Classes.Meteors as meteor
import Classes.TextInput as textInput

# gameState = -1 = game over/ inserção de rank
# gameState = 0 = menu principal
# gameState = 1 = jogo rodando
# gameState = 2 = pause


pygame.init()

clock = pygame.time.Clock()
pygame.display.set_caption("Meteor Hunt")
click_do_mouse = pygame.mixer.Sound("./Sounds/laser5.ogg")
background_position = [0, -1280]
background_image = pygame.image.load("Images/Background/Full_Background.png").convert()
loop_game = 0
pygame.mouse.set_visible(False)
score = 0
font = pygame.font.Font("./Fonts/kenvector_future_thin.ttf", 36)

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

gameLoop = False
gameState = 0
while not gameLoop:

    # Game Running
    while gameState == 1:
        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameState = -5
                gameLoop = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameState = -5
                    gameLoop = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click_do_mouse.play()
                # Fire a bullet if the user clicks the mouse button
                shot = bullet.Bullet()
                # Set the bullet to where the player is
                shot.rect.x = pos[0]+44
                shot.rect.y = pos[1]-60
                #Add the bullet to the lists
                all_sprites_list.add(shot)
                bullet_list.add(shot)

        texto = font.render("SCORE: " + str(score), True, Constants.WHITE)


        # Summon meteors
        if loop_game % Constants.ASTEROID_SUMMON_TIME == 0:
            asteroid = meteor.Meteor()
            asteroid.reposicionar(Constants.X)
            meteor_list.add(asteroid)
        loop_game += 1

        # --- Game Logic

        #Call update method on all the sprites
        all_sprites_list.update()
        meteor_list.update(Constants.X, Constants.Y, Constants.ASTEROID_MOVE_SPEED)
        bullet_list.update()
        # Calculate mechanics for each bullet
        for shot in bullet_list:
            #Remove the bullet if it flies up off the screen
            if shot.rect.y < -40:
                bullet_list.remove(shot)
                all_sprites_list.remove(shot)
            # See if the player block has collided with anything.
            meteors_hit_list = pygame.sprite.spritecollide(shot, meteor_list, True)

            # Check the list of collisions.
            for asteroid in meteors_hit_list:
                score = score + asteroid.value
                meteor_list.remove(asteroid)
                bullet_list.remove(shot)
                all_sprites_list.remove(shot)

        #Remove player if he was hit
        player_hit_list = pygame.sprite.spritecollide(player, meteor_list, True)

        if player_hit_list:
            all_sprites_list.remove(player)
            gameState = -1
        else:
            Constants.screen.blit(player.image, pos)

        Constants.screen.blit(background_image, background_position)

        if score >= 20 and Constants.ASTEROID_MOVE_SPEED == 1:
            background_position[1] = -3840
            Constants.ASTEROID_MOVE_SPEED = 3
            Constants.ASTEROID_SUMMON_TIME = 60
        elif score >= 50 and Constants.ASTEROID_MOVE_SPEED == 3:
            background_position[1] = -6400
            Constants.ASTEROID_MOVE_SPEED = 5
            Constants.ASTEROID_SUMMON_TIME = 30
        elif score >= 100 and Constants.ASTEROID_MOVE_SPEED == 5:
            background_position[1] = -8960
            Constants.ASTEROID_MOVE_SPEED = 10
            Constants.ASTEROID_SUMMON_TIME = 20

        # Roll the background
        if background_position[1] >= -1280 and background_position[1] <= 0:
            if background_position[1] >= 0:
                background_position[1] = -1280
            else:
                background_position[1] += Constants.BACKGROUND_SPEED
        elif background_position[1] >= -3840 and background_position[1] <= -2560:
            if background_position[1] >= -2560:
                background_position[1] = -3840
            else:
                background_position[1] += Constants.BACKGROUND_SPEED
        elif background_position[1] >= -6400 and background_position[1] <= -5120:
            if background_position[1] >= -5120:
                background_position[1] = -6400
            else:
                background_position[1] += Constants.BACKGROUND_SPEED
        elif background_position[1] >= -8960 and background_position[1] <= -7680:
            if background_position[1] >= -7680:
                background_position[1] = -8960
            else:
                background_position[1] += Constants.BACKGROUND_SPEED

        # Draw all the sprites
        all_sprites_list.draw(Constants.screen)
        meteor_list.draw(Constants.screen)
        bullet_list.draw(Constants.screen)
        Constants.screen.blit(texto, [10, 10])

        pygame.display.update()

        clock.tick(60)

    # Menu
    while gameState == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameState = -5
                gameLoop = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameState = -5
                    gameLoop = True
        Constants.screen.fill(Constants.BLACK)
        texto1 = font.render("Fim de jogo! Seu score final foi: " + str(score), True, Constants.WHITE)
        Constants.screen.blit(texto1, [Constants.X/4, Constants.Y/3])
        texto2 = font.render("Insira seu nome! Máximo de 3 caracteres!", True, Constants.WHITE)
        Constants.screen.blit(texto2, [Constants.X/5, Constants.Y/2])
        texto3 = font.render("Aperte ENTER quando terminar!", True, Constants.WHITE)
        Constants.screen.blit(texto3, [Constants.X /3.75, Constants.Y/1.80])
        pygame.display.update()
        nome = textInput.TextInput()

    # Game Over
    while gameState == -1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameState = -5
                gameLoop = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameState = -5
                    gameLoop = True
        Constants.screen.fill(Constants.BLACK)
        texto1 = font.render("Fim de jogo! Seu score final foi: " + str(score), True, Constants.WHITE)
        Constants.screen.blit(texto1, [Constants.X/4, Constants.Y/3])
        texto2 = font.render("Insira seu nome! Máximo de 3 caracteres!", True, Constants.WHITE)
        Constants.screen.blit(texto2, [Constants.X/5, Constants.Y/2])
        texto3 = font.render("Aperte ENTER quando terminar!", True, Constants.WHITE)
        Constants.screen.blit(texto3, [Constants.X /3.75, Constants.Y/1.80])
        pygame.display.update()
        nome = textInput.TextInput()

        enterApertado = 0
        while enterApertado == 0:
            if pygame.event.get() == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    enterApertado = 1

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()

            # Feed it with events every frame
            nome.update(events)
            # Blit its surface onto the screen
            Constants.screen.blit(nome.get_surface(), (10, 10))



pygame.quit()
