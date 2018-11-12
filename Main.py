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
background_image = pygame.image.load("Images/Background/full.png").convert()
loop_game = 0
pygame.mouse.set_visible(False)
score = 0
font = pygame.font.Font("./Fonts/kenvector_future_thin.ttf", 36)
textinput = textInput.TextInput()
cursor_porcent_Y = 75
cursor_porcent_X = 50
cursor_loop = 0
cursor_side = "L"
title_image = ""
image = ""

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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameLoop = True
            elif event.key == pygame.K_RETURN and gameState == 0 and cursor_Y == Constants.Y / 100 * 75:
                gameState = 1
            elif event.key == pygame.K_RETURN and gameState == 0 and cursor_Y == Constants.Y / 100 * 90:
                gameState = -5
                gameLoop = True
            elif gameState == 0 and event.key == pygame.K_DOWN:
                Constants.screen.blit(background_image, background_position)
                cursor_loop = 0
                if cursor_Y >= Constants.Y / 100 * 75 and  cursor_Y < Constants.Y / 100 * 90:
                    cursor_porcent_Y += 5
                    if cursor_porcent_Y == 75:
                        cursor_porcent_X = 50
                    elif cursor_porcent_Y == 80:
                        cursor_porcent_X = 50
                    elif cursor_porcent_Y == 85:
                        cursor_porcent_X = 100
                    elif cursor_porcent_Y == 90:
                        cursor_porcent_X = 130
            elif gameState == 0 and event.key == pygame.K_UP:
                cursor_loop = 0
                Constants.screen.blit(background_image, background_position)
                if cursor_Y > Constants.Y / 100 * 75 and cursor_Y <= Constants.Y / 100 * 90:
                    cursor_porcent_Y -= 5
                    if cursor_porcent_Y == 75:
                        cursor_porcent_X = 50
                    elif cursor_porcent_Y == 80:
                        cursor_porcent_X = 50
                    elif cursor_porcent_Y == 85:
                        cursor_porcent_X = 100
                    elif cursor_porcent_Y == 90:
                        cursor_porcent_X = 130

    # Menu
    if gameState == 0:
        # Background Image
        if image != "Images/Background/lightBlue.png":
            image = "Images/Background/lightBlue.png"
            background_image = pygame.image.load(image)
        Constants.screen.blit(background_image, background_position)

        # Title Image
        if Constants.X >= 800 and Constants.X < 1200 and title_image == "":
            title_image = "Images/UI/Title-(800_600).png"
            title = pygame.image.load(title_image)
        elif Constants.X >= 1200 and Constants.X < 1600 and title_image == "":
            title_image = "Images/UI/Title-(1200_900).png"
            title = pygame.image.load(title_image)
        elif Constants.X >= 1600 and title_image == "":
            title_image = "Images/UI/Title-(1650_1080).png"
            title = pygame.image.load(title_image)
        Constants.screen.blit(title, (0, 0))

        # Menu Texts
        menu_start = font.render("Iníciar Jogo", True, Constants.BLACK)
        Constants.screen.blit(menu_start, (Constants.X / 2 - menu_start.get_rect().size[0] / 2, Constants.Y / 100 * 75))
        menu_ranking = font.render("Pontuações", True, Constants.BLACK)
        Constants.screen.blit(menu_ranking,
                              (Constants.X / 2 - menu_ranking.get_rect().size[0] / 2, Constants.Y / 100 * 80))
        menu_option = font.render("Opções", True, Constants.BLACK)
        Constants.screen.blit(menu_option,
                              (Constants.X / 2 - menu_option.get_rect().size[0] / 2, Constants.Y / 100 * 85))
        menu_exit = font.render("Sair", True, Constants.BLACK)
        Constants.screen.blit(menu_exit, (Constants.X / 2 - menu_exit.get_rect().size[0] / 2, Constants.Y / 100 * 90))

        # Menu Cursor
        if cursor_porcent_Y == 90:
            cursor = "Images/Spaceship/playerShip2_red.png"
        else:
            cursor = "Images/Spaceship/playerShip2_blue.png"

        cursor_X = Constants.X / 2 - menu_start.get_rect().size[0] + cursor_porcent_X
        cursor_Y = Constants.Y / 100 * cursor_porcent_Y
        cursor_image = pygame.image.load(cursor).convert()
        cursor_image.set_colorkey(Constants.BLACK)
        cursor_image = pygame.transform.scale(cursor_image, (44, 32))
        cursor_image = pygame.transform.rotate(cursor_image, -90)
        Constants.screen.blit(cursor_image, (cursor_X, cursor_Y))

        if cursor_side == "R" and cursor_loop <= 7:
            cursor_porcent_X -= 1
            if cursor_loop == 7:
                cursor_side = "L"
                cursor_loop = 0
        elif cursor_side == "L" and cursor_loop <= 7:
            cursor_porcent_X += 1
            if cursor_loop == 7:
                cursor_side = "R"
                cursor_loop = 0
        cursor_loop += 1

    # Game Over
    if gameState == -1:
        Constants.screen.fill(Constants.BLACK)
        texto1 = font.render("Fim de jogo! Seu score final foi: " + str(score), True, Constants.WHITE)
        Constants.screen.blit(texto1, [Constants.X/4, Constants.Y/3])
        texto2 = font.render("Insira seu nome! Máximo de 3 caracteres!", True, Constants.WHITE)
        Constants.screen.blit(texto2, [Constants.X/5, Constants.Y/2.5])
        texto3 = font.render("Aperte ENTER quando terminar!", True, Constants.WHITE)
        Constants.screen.blit(texto3, [Constants.X /3.75, Constants.Y/2.15])

        # Feed it with events every frame
        textinput.update(pygame.event.get())
        # Blit its surface onto the screen
        Constants.screen.blit(textinput.get_surface(), (Constants.X/2, Constants.Y/1.70))
        pygame.display.update()

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
pygame.quit()
