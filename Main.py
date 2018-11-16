import pygame
import Constants
import Classes.Bullet as bullet
import Classes.Damage as damage
import Classes.Player as player
import Classes.Meteors as meteor
import Classes.TextInput as textInput
import Classes.Score as score

# gameState = -1 = game over/ inserção de rank
# gameState = 0 = menu principal
# gameState = 1 = jogo rodando
# gameState = 2 = pause


pygame.init()

clock = pygame.time.Clock()
pygame.display.set_caption("Meteor Hunt")
click_do_mouse = pygame.mixer.Sound("./Sounds/sfx_laser2.ogg")
background_position = [0, -1280]
loop_game = 0
image = ""
title_image = ""
pygame.mouse.set_visible(False)
score = 0
font = pygame.font.Font("./Fonts/kenvector_future_thin.ttf", 36)
cursor_porcent_X = 50
cursor_porcent_Y = 75
cursor_loop = 0
cursor_side = "L"
textinput = textInput.TextInput()
pause = False
bulletDelay = 0
bulletDelayLoop = False

player = player.Player()
damage = damage.Damage()

# --- Sprite Lists

# List of every sprite
all_sprites_list = pygame.sprite.Group()

# List of each bullet
bullet_list = pygame.sprite.Group()

# List of each meteor
meteor_list = pygame.sprite.Group()
meteors_hit_list = pygame.sprite.Group()

all_sprites_list.add(player, damage)

gameLoop = False
gameState = 0

while not gameLoop:
    if pause == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameState = -5
                gameLoop = True
            elif event.type == pygame.KEYDOWN:
                if gameState == 1 and (event.key == pygame.K_p or event.key == pygame.K_ESCAPE):
                    pause = True
                elif gameState != 1 and event.key == pygame.K_ESCAPE:
                    gameState = -5
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
                    if cursor_Y > Constants.Y / 100 * 75 and  cursor_Y <= Constants.Y / 100 * 90:
                        cursor_porcent_Y -= 5
                        if cursor_porcent_Y == 75:
                            cursor_porcent_X = 50
                        elif cursor_porcent_Y == 80:
                            cursor_porcent_X = 50
                        elif cursor_porcent_Y == 85:
                            cursor_porcent_X = 100
                        elif cursor_porcent_Y == 90:
                            cursor_porcent_X = 130

            if event.type == pygame.MOUSEBUTTONDOWN and gameState == 1:
                bulletDelay = True
                bulletDelayLoop = 0
            elif event.type == pygame.MOUSEBUTTONUP and gameState == 1:
                bulletDelay = False
                bulletDelayLoop = 0


        # Game Over
        if gameState == -1:
            #Background Image
            if image != "Images/Background/lightBlue.png":
                image = "Images/Background/lightBlue.png"
                background_image = pygame.image.load(image)
                enterScore = False
            while not enterScore:
                if (pygame.key.get_pressed()[pygame.K_ESCAPE]):
                    gameState = -5
                    gameLoop = True
                    enterScore = True
                elif (pygame.key.get_pressed()[pygame.K_RETURN]):
                    gameState = 0
                    score = 0
                    enterScore = True
                    all_sprites_list.add(player, damage)
                    background_position[1] = -1280
                    Constants.ASTEROID_MOVE_SPEED = 1
                    Constants.ASTEROID_SUMMON_TIME = 60
                    player.life = 4
                    damage.damageSprite = 0

                Constants.screen.blit(background_image, [0, 0])
                texto1 = font.render("Fim de jogo! Seu score final foi: " + str(score), True, Constants.WHITE)
                Constants.screen.blit(texto1, [Constants.X / 2 - texto1.get_rect().size[0] / 2, Constants.Y/3])
                texto2 = font.render("Insira seu nome!", True, Constants.WHITE)
                Constants.screen.blit(texto2, [Constants.X / 2 - texto2.get_rect().size[0] / 2, Constants.Y/2])
                texto3 = font.render("Aperte ENTER quando terminar!", True, Constants.WHITE)
                Constants.screen.blit(texto3, [Constants.X / 2 - texto3.get_rect().size[0] / 2, Constants.Y/1.80])

                # Feed it with events every frame
                textinput.update(pygame.event.get())
                # Blit its surface onto the screen
                Constants.screen.blit(textinput.get_surface(), [Constants.X / 2 - textinput.get_surface().get_rect().size[0] / 2, Constants.Y/1.60])
                pygame.display.update()

        # Menu
        if gameState == 0:
            #Background Image
            if image != "Images/Background/lightBlue.png":
                image = "Images/Background/lightBlue.png"
                background_image = pygame.image.load(image)
            Constants.screen.blit(background_image, [0, 0])

            # Title Image
            if Constants.X >= 800 and Constants.X < 1200 and title_image == "":
                title_image = "Images/UI/Title-(800_600).png"
                title = pygame.image.load(title_image)
            elif Constants.X >= 1200 and Constants.X < 1600 and title_image == "":
                title_image = "Images/UI/Title-(1200_900).png"
                title = pygame.image.load(title_image)
            elif Constants.X >= 1600 and Constants.X < 1920 and title_image == "":
                title_image = "Images/UI/Title-(1650_1080).png"
                title = pygame.image.load(title_image)
            elif Constants.X >= 1920 and title_image == "":
                title_image = "Images/UI/Title-(1920_1080).png"
                title = pygame.image.load(title_image)
            Constants.screen.blit(title, (0, 0))

            # Menu Texts
            menu_start = font.render("Iníciar Jogo", True, Constants.BLACK)
            Constants.screen.blit(menu_start, (Constants.X / 2 - menu_start.get_rect().size[0] / 2, Constants.Y / 100 * 75))
            menu_ranking = font.render("Pontuações", True, Constants.BLACK)
            Constants.screen.blit(menu_ranking, (Constants.X / 2 - menu_ranking.get_rect().size[0] / 2, Constants.Y / 100 * 80))
            menu_option = font.render("Opções", True, Constants.BLACK)
            Constants.screen.blit(menu_option, (Constants.X / 2 - menu_option.get_rect().size[0] / 2, Constants.Y / 100 * 85))
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

        # Game Running
        if gameState == 1:
            if image != "Images/Background/Full_Background.png":
                image = "Images/Background/Full_Background.png"
                background_image = pygame.image.load(image).convert()

            if bulletDelay == True:
                if bulletDelayLoop % 15 == 0 and bulletDelayLoop != 0:
                    click_do_mouse.play()
                    # Fire a bullet if the user clicks the mouse button
                    shot = bullet.Bullet()
                    # Set the bullet to where the player is
                    shot.rect.x = pos[0]+44
                    shot.rect.y = pos[1]-60
                    #Add the bullet to the lists
                    all_sprites_list.add(shot)
                    bullet_list.add(shot)
                    bulletDelayLoop = 0
                bulletDelayLoop +=1

            pos = pygame.mouse.get_pos()

            Constants.screen.blit(background_image, background_position)
            scoreText = font.render("SCORE: " + str(score), True, Constants.WHITE)

            lifeText = font.render("Vidas: " + str(player.life), True, Constants.WHITE)

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
                player.life -= 1
                damage.damageSprite += 1
                Constants.screen.blit(damage.image, pos)
                if player.life == 0:
                    Constants.ASTEROID_MOVE_SPEED = 1
                    Constants.ASTEROID_SUMMON_TIME = 60
                    Constants.BACKGROUND_SPEED = 2
                    all_sprites_list.remove(player, damage)
                    for shot in bullet_list:
                        bullet_list.remove(shot)
                        all_sprites_list.remove(shot)
                    for asteroid in meteor_list:
                        meteor_list.remove(asteroid)
                        all_sprites_list.remove(asteroid)
                    gameState = -1
            else:
                Constants.screen.blit(player.image, pos)
            if score >= 20 and Constants.ASTEROID_MOVE_SPEED == 1:
                background_position[1] = -3840
                Constants.ASTEROID_MOVE_SPEED = 3
                Constants.ASTEROID_SUMMON_TIME = 60
                Constants.BACKGROUND_SPEED = 5
            elif score >= 50 and Constants.ASTEROID_MOVE_SPEED == 3:
                background_position[1] = -6400
                Constants.ASTEROID_MOVE_SPEED = 5
                Constants.ASTEROID_SUMMON_TIME = 30
                Constants.BACKGROUND_SPEED = 10
            elif score >= 100 and Constants.ASTEROID_MOVE_SPEED == 5:
                background_position[1] = -8960
                Constants.ASTEROID_MOVE_SPEED = 10
                Constants.ASTEROID_SUMMON_TIME = 20
                Constants.BACKGROUND_SPEED = 20

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
            Constants.screen.blit(scoreText, [10, 10])
            Constants.screen.blit(lifeText, [Constants.X - 200, 10])


    else:
        if pause == True:
            pauseText = font.render("Pause!", True, Constants.WHITE)
            Constants.screen.blit(pauseText, [Constants.X / 2 - pauseText.get_rect().size[0] / 2, Constants.Y/2])

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if gameState == 1 and (event.key == pygame.K_p or event.key == pygame.K_ESCAPE):
                    pygame.mouse.set_pos(pos)
                    pause = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
