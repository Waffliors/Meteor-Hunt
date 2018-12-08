import pygame
import pickle
import Constants
import Classes.Bullet as bullet
import Classes.Damage as damage
import Classes.Player as player
import Classes.Meteors as meteor
import Classes.TextInput as textInput
import Score as Score

# gameState = -1 = game over
# gameState = 0 = menu principal
# gameState = 1 = jogo rodando
# gameState = 2 = option
# gameState = 3 = pontuações
# gameState = 4 = deleta pontuações
# gameState = 5 = seleciona controles

pygame.init()

chamaMetodoDoScore = Score.Ranking(" ", 0)
# Traz a lista de scores salvos pro main
listaDeRankings = pickle.load(open('save.pkl', 'rb'))

clock = pygame.time.Clock()
pygame.display.set_caption("Meteor Hunt")
click_do_mouse = pygame.mixer.Sound("./Sounds/sfx_laser2.ogg")
pygame.mixer.music.load("./Musics/Fundo.ogg")
pygame.mixer.music.play(-1)
option_volume = 5
option_volume_number = 50
slide_volume = 0
volume_green_slide = 505
volume_white_slide = 0
volume_green_size = 230
volume_white_size = 250
background_position = [0, -1280]
loop_game = 0
image = ""
tempo = 0
keyboard_image = ""
mouse_image = ""

#Sound
sound_image = "Images/UI/Active.png"
active_sound_image = pygame.image.load(sound_image)

volume_active = "on"
volume_porcent = 5
volume_image_button = "Images/UI/Volume_" + volume_active + "_" + str(volume_porcent) + ".png"
volume_image_button_image = pygame.image.load(volume_image_button)


meteorExplosionSound = pygame.mixer.Sound("Sounds/MeteorExplosion.wav")
meteorExplosionSound.set_volume(0.2)
playerExplosionSound = pygame.mixer.Sound("Sounds/PlayerExplosion.wav")
playerExplosionSound.set_volume(1.0)
playerHitSound = pygame.mixer.Sound("Sounds/PlayerHit.wav")
playerHitSound.set_volume(1.0)
optionSelectionSound = pygame.mixer.Sound("Sounds/OptionSelection.wav")
optionSelectionSound.set_volume(1.0)
musica = "Musics/MenuMusic.ogg"
pygame.mixer.music.load(musica)
pygame.mixer.music.play(-1)
musicaLigada = True
#Sound

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
teclado = False

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
                gameLoop = True
            elif event.type == pygame.KEYDOWN:
                if gameState == 1 and (event.key == pygame.K_p or event.key == pygame.K_ESCAPE):
                    optionSelectionSound.play()
                    pause = True
                elif gameState != 1 and event.key == pygame.K_ESCAPE:
                    optionSelectionSound.play()
                    gameState = -5
                    gameLoop = True
                elif event.key == pygame.K_RETURN and gameState == 0 and cursor_Y == Constants.Y / 100 * 75:
                    optionSelectionSound.play()
                    gameState = 5
                    cursor_porcent_Y = 50
                    cursor_porcent_X = -500
                elif event.key == pygame.K_RIGHT and gameState == 5 and cursor_porcent_Y == 50:
                    optionSelectionSound.play()
                    cursor_porcent_X = 200
                elif event.key == pygame.K_LEFT and gameState == 5 and cursor_porcent_Y == 50:
                    optionSelectionSound.play()
                    cursor_porcent_X = -500
                elif event.key == pygame.K_DOWN and gameState == 5 and cursor_porcent_Y == 50:
                    optionSelectionSound.play()
                    cursor_porcent_Y = 90
                    cursor_porcent_X = 0
                elif event.key == pygame.K_UP and gameState == 5 and cursor_porcent_Y == 90:
                    optionSelectionSound.play()
                    cursor_porcent_Y = 50
                    cursor_porcent_X = -500
                elif event.key == pygame.K_RETURN and gameState == 5 and cursor_porcent_Y == 90:
                    optionSelectionSound.play()
                    cursor_porcent_X = 50
                    cursor_porcent_Y = 75
                    gameState = 0
                elif event.key == pygame.K_RETURN and gameState == 5 and cursor_porcent_Y == 50 and cursor_porcent_X > 150 and cursor_porcent_X < 250:
                    gameState = 1
                    player.control = "Mouse"
                    damage.control = "Mouse"
                    bulletDelay = 0
                    bulletDelayLoop = False
                elif event.key == pygame.K_RETURN and gameState == 5 and cursor_porcent_Y == 50 and cursor_porcent_X > -550 and cursor_porcent_X < -450:
                    gameState = 1
                    bulletDelay = 0
                    bulletDelayLoop = False
                    player.control = "Teclado"
                    damage.control = "Teclado"
                elif event.key == pygame.K_RETURN and gameState == 0 and cursor_Y == Constants.Y / 100 * 85:
                    optionSelectionSound.play()
                    gameState = 2
                    cursor_porcent_Y = 40
                    cursor_porcent_X = -425
                elif event.key == pygame.K_RETURN and gameState == 0 and cursor_Y == Constants.Y / 100 * 80:
                    optionSelectionSound.play()
                    gameState = 3
                    cursor_porcent_Y = 90
                    cursor_porcent_X = 0
                elif event.key == pygame.K_RETURN and gameState == 0 and cursor_Y == Constants.Y / 100 * 90:
                    optionSelectionSound.play()
                    gameLoop = True
                elif event.key == pygame.K_RETURN and gameState == 2 and cursor_Y == Constants.Y / 100 * 90:
                    optionSelectionSound.play()
                    gameState = 0
                    cursor_porcent_X = 130
                elif event.key == pygame.K_RETURN and gameState == 3 and cursor_Y == Constants.Y / 100 * 90:
                    optionSelectionSound.play()
                    gameState = 0
                    cursor_porcent_X = 130
                elif event.key == pygame.K_RETURN and gameState == 3 and cursor_Y == Constants.Y / 100 * 80:
                    optionSelectionSound.play()
                    gameState = 4
                    cursor_porcent_Y = 65
                    cursor_porcent_X = 50
                elif event.key == pygame.K_RETURN and gameState == 4 and cursor_Y == Constants.Y / 100 * 55:
                    optionSelectionSound.play()
                    listaDeRankings = chamaMetodoDoScore.resetSave(listaDeRankings)
                    gameState = 3
                    cursor_porcent_Y = 90
                    cursor_porcent_X = 0
                elif event.key == pygame.K_RETURN and gameState == 4 and cursor_Y == Constants.Y / 100 * 65:
                    optionSelectionSound.play()
                    gameState = 3
                    cursor_porcent_Y = 90
                    cursor_porcent_X = 0
                elif gameState == 0 and event.key == pygame.K_DOWN:
                    optionSelectionSound.play()
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
                    optionSelectionSound.play()
                    cursor_loop = 0
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
                elif gameState == 2 and event.key == pygame.K_DOWN:
                    optionSelectionSound.play()
                    cursor_loop = 0
                    if cursor_porcent_Y == 60:
                        cursor_porcent_Y = 90
                        cursor_porcent_X = 0
                    if cursor_porcent_Y == 40:
                        cursor_porcent_Y = 60
                        cursor_porcent_X = -425
                elif gameState == 2 and event.key == pygame.K_UP:
                    optionSelectionSound.play()
                    cursor_loop = 0
                    if cursor_porcent_Y == 60:
                        cursor_porcent_Y = 40
                        cursor_porcent_X = -425
                    if cursor_porcent_Y == 90:
                        cursor_porcent_Y = 60
                        cursor_porcent_X = -425
                elif gameState == 3 and event.key == pygame.K_DOWN:
                    optionSelectionSound.play()
                    cursor_loop = 0
                    if cursor_porcent_Y == 80:
                        cursor_porcent_Y = 90
                        cursor_porcent_X = 0
                elif gameState == 3 and event.key == pygame.K_UP:
                    optionSelectionSound.play()
                    cursor_loop = 0
                    if cursor_porcent_Y == 90:
                        cursor_porcent_Y = 80
                        cursor_porcent_X = -130
                elif gameState == 4 and event.key == pygame.K_DOWN:
                    optionSelectionSound.play()
                    cursor_loop = 0
                    if cursor_porcent_Y == 55:
                        cursor_porcent_Y = 65
                        cursor_porcent_X = 50
                elif gameState == 4 and event.key == pygame.K_UP:
                    optionSelectionSound.play()
                    cursor_loop = 0
                    if cursor_porcent_Y == 65:
                        cursor_porcent_Y = 55
                        cursor_porcent_X = 50
                elif event.key == pygame.K_LEFT and gameState == 2 and cursor_porcent_Y == 40:
                    optionSelectionSound.play()
                    # Sound Image
                    sound_image = "Images/UI/Deactive.png"
                    volume_active = "off"
                    active_sound_image = pygame.image.load(sound_image)
                    volume_image_button = "Images/UI/Volume_" + volume_active + "_" + str(volume_porcent) + ".png"
                    volume_image_button_image = pygame.image.load(volume_image_button)
                    pygame.mixer.music.set_volume(0.0)
                    musicaLigada = False
                    click_do_mouse.set_volume(0.0)
                    meteorExplosionSound.set_volume(0.0)
                    playerHitSound.set_volume(0.0)
                    playerExplosionSound.set_volume(0.0)
                    optionSelectionSound.set_volume(0.0)
                elif event.key == pygame.K_RIGHT and gameState == 2 and cursor_porcent_Y == 40:
                    optionSelectionSound.play()
                    # Sound Image
                    sound_image = "Images/UI/Active.png"
                    volume_active = "on"
                    active_sound_image = pygame.image.load(sound_image)
                    volume_image_button = "Images/UI/Volume_" + volume_active + "_" + str(volume_porcent) + ".png"
                    volume_image_button_image = pygame.image.load(volume_image_button)
                    pygame.mixer.music.set_volume(1.0)
                    musicaLigada = True
                    click_do_mouse.set_volume(1.0)
                    meteorExplosionSound.set_volume(0.5)
                    playerHitSound.set_volume(1.0)
                    playerExplosionSound.set_volume(1.0)
                    optionSelectionSound.set_volume(1.0)
                elif event.key == pygame.K_LEFT and gameState == 2 and cursor_porcent_Y == 60 and sound_image == "Images/UI/Active.png":
                    if volume_porcent > 0:
                        volume_porcent -= 1
                        volume_image_button = "Images/UI/Volume_" + volume_active + "_" + str(volume_porcent) + ".png"
                        volume_image_button_image = pygame.image.load(volume_image_button)
                    if option_volume == 1:
                        option_volume = 0
                        pygame.mixer.music.set_volume(0.0)
                        option_volume_number = 0
                        click_do_mouse.set_volume(0.0)
                        meteorExplosionSound.set_volume(0.0)
                        playerHitSound.set_volume(0.0)
                        playerExplosionSound.set_volume(0.0)
                        optionSelectionSound.set_volume(0.0)
                        optionSelectionSound.play()
                    elif option_volume == 2:
                        option_volume = 1
                        pygame.mixer.music.set_volume(0.1)
                        option_volume_number = 10
                        click_do_mouse.set_volume(0.1)
                        meteorExplosionSound.set_volume(0.1)
                        playerHitSound.set_volume(0.1)
                        playerExplosionSound.set_volume(0.1)
                        optionSelectionSound.set_volume(0.1)
                        optionSelectionSound.play()
                    elif option_volume == 3:
                        option_volume = 2
                        pygame.mixer.music.set_volume(0.2)
                        click_do_mouse.set_volume(0.2)
                        meteorExplosionSound.set_volume(0.2)
                        playerHitSound.set_volume(0.2)
                        playerExplosionSound.set_volume(0.2)
                        optionSelectionSound.set_volume(0.2)
                        optionSelectionSound.play()
                        option_volume_number = 20
                    elif option_volume == 4:
                        option_volume = 3
                        pygame.mixer.music.set_volume(0.3)
                        click_do_mouse.set_volume(0.3)
                        meteorExplosionSound.set_volume(0.3)
                        playerHitSound.set_volume(0.3)
                        playerExplosionSound.set_volume(0.3)
                        optionSelectionSound.set_volume(0.3)
                        optionSelectionSound.play()
                        option_volume_number = 30
                    elif option_volume == 5:
                        option_volume = 4
                        pygame.mixer.music.set_volume(0.4)
                        option_volume_number = 40
                        click_do_mouse.set_volume(0.4)
                        meteorExplosionSound.set_volume(0.4)
                        playerHitSound.set_volume(0.4)
                        playerExplosionSound.set_volume(0.4)
                        optionSelectionSound.set_volume(0.4)
                        optionSelectionSound.play()
                    elif option_volume == 6:
                        option_volume = 5
                        pygame.mixer.music.set_volume(0.5)
                        option_volume_number = 50
                        click_do_mouse.set_volume(0.5)
                        meteorExplosionSound.set_volume(0.5)
                        playerHitSound.set_volume(0.5)
                        playerExplosionSound.set_volume(0.5)
                        optionSelectionSound.set_volume(0.5)
                        optionSelectionSound.play()
                    elif option_volume == 7:
                        option_volume = 6
                        pygame.mixer.music.set_volume(0.6)
                        option_volume_number = 60
                        click_do_mouse.set_volume(0.6)
                        meteorExplosionSound.set_volume(0.6)
                        playerHitSound.set_volume(0.6)
                        playerExplosionSound.set_volume(0.6)
                        optionSelectionSound.set_volume(0.6)
                        optionSelectionSound.play()
                    elif option_volume == 8:
                        option_volume = 7
                        pygame.mixer.music.set_volume(0.7)
                        option_volume_number = 70
                        click_do_mouse.set_volume(0.7)
                        meteorExplosionSound.set_volume(0.7)
                        playerHitSound.set_volume(0.7)
                        playerExplosionSound.set_volume(0.7)
                        optionSelectionSound.set_volume(0.7)
                        optionSelectionSound.play()
                    elif option_volume == 9:
                        option_volume = 8
                        pygame.mixer.music.set_volume(0.8)
                        option_volume_number = 80
                        click_do_mouse.set_volume(0.8)
                        meteorExplosionSound.set_volume(0.8)
                        playerHitSound.set_volume(0.8)
                        playerExplosionSound.set_volume(0.8)
                        optionSelectionSound.set_volume(0.8)
                        optionSelectionSound.play()
                    elif option_volume == 10:
                        option_volume = 9
                        pygame.mixer.music.set_volume(0.9)
                        option_volume_number = 90
                        click_do_mouse.set_volume(0.9)
                        meteorExplosionSound.set_volume(0.9)
                        playerHitSound.set_volume(0.9)
                        playerExplosionSound.set_volume(0.9)
                        optionSelectionSound.set_volume(0.9)
                        optionSelectionSound.play()
                elif event.key == pygame.K_RIGHT and gameState == 2 and cursor_porcent_Y == 60 and sound_image == "Images/UI/Active.png":
                    if volume_porcent < 10:
                        volume_porcent += 1
                        volume_image_button = "Images/UI/Volume_" + volume_active + "_" + str(volume_porcent) + ".png"
                        volume_image_button_image = pygame.image.load(volume_image_button)
                    if option_volume == 9:
                        option_volume = 10
                        pygame.mixer.music.set_volume(1.0)
                        option_volume_number = 100
                        click_do_mouse.set_volume(1.0)
                        meteorExplosionSound.set_volume(1.0)
                        playerHitSound.set_volume(1.0)
                        playerExplosionSound.set_volume(1.0)
                        optionSelectionSound.set_volume(1.0)
                        optionSelectionSound.play()
                    elif option_volume == 8:
                        option_volume = 9
                        pygame.mixer.music.set_volume(0.9)
                        option_volume_number = 90
                        click_do_mouse.set_volume(0.9)
                        meteorExplosionSound.set_volume(0.9)
                        playerHitSound.set_volume(0.9)
                        playerExplosionSound.set_volume(0.9)
                        optionSelectionSound.set_volume(0.9)
                        optionSelectionSound.play()
                    elif option_volume == 7:
                        option_volume = 8
                        pygame.mixer.music.set_volume(0.8)
                        option_volume_number = 80
                        click_do_mouse.set_volume(0.8)
                        meteorExplosionSound.set_volume(0.8)
                        playerHitSound.set_volume(0.8)
                        playerExplosionSound.set_volume(0.8)
                        optionSelectionSound.set_volume(0.8)
                        optionSelectionSound.play()
                    elif option_volume == 6:
                        option_volume = 7
                        pygame.mixer.music.set_volume(0.7)
                        option_volume_number = 70
                        click_do_mouse.set_volume(0.7)
                        meteorExplosionSound.set_volume(0.7)
                        playerHitSound.set_volume(0.7)
                        playerExplosionSound.set_volume(0.7)
                        optionSelectionSound.set_volume(0.7)
                        optionSelectionSound.play()
                    elif option_volume == 5:
                        option_volume = 6
                        pygame.mixer.music.set_volume(0.6)
                        option_volume_number = 60
                        click_do_mouse.set_volume(0.6)
                        meteorExplosionSound.set_volume(0.6)
                        playerHitSound.set_volume(0.6)
                        playerExplosionSound.set_volume(0.6)
                        optionSelectionSound.set_volume(0.6)
                        optionSelectionSound.play()
                    elif option_volume == 4:
                        option_volume = 5
                        pygame.mixer.music.set_volume(0.5)
                        option_volume_number = 50
                        click_do_mouse.set_volume(0.5)
                        meteorExplosionSound.set_volume(0.5)
                        playerHitSound.set_volume(0.5)
                        playerExplosionSound.set_volume(0.5)
                        optionSelectionSound.set_volume(0.5)
                        optionSelectionSound.play()
                    elif option_volume == 3:
                        option_volume = 4
                        pygame.mixer.music.set_volume(0.4)
                        option_volume_number = 40
                        click_do_mouse.set_volume(0.4)
                        meteorExplosionSound.set_volume(0.4)
                        playerHitSound.set_volume(0.4)
                        playerExplosionSound.set_volume(0.4)
                        optionSelectionSound.set_volume(0.4)
                        optionSelectionSound.play()
                    elif option_volume == 2:
                        option_volume = 3
                        pygame.mixer.music.set_volume(0.3)
                        option_volume_number = 30
                        click_do_mouse.set_volume(0.3)
                        meteorExplosionSound.set_volume(0.3)
                        playerHitSound.set_volume(0.3)
                        playerExplosionSound.set_volume(0.3)
                        optionSelectionSound.set_volume(0.3)
                        optionSelectionSound.play()
                    elif option_volume == 1:
                        option_volume = 2
                        pygame.mixer.music.set_volume(0.2)
                        option_volume_number = 20
                        click_do_mouse.set_volume(0.2)
                        meteorExplosionSound.set_volume(0.2)
                        playerHitSound.set_volume(0.2)
                        playerExplosionSound.set_volume(0.2)
                        optionSelectionSound.set_volume(0.2)
                        optionSelectionSound.play()
                    elif option_volume == 0:
                        option_volume = 1
                        pygame.mixer.music.set_volume(0.1)
                        option_volume_number = 10
                        click_do_mouse.set_volume(0.1)
                        meteorExplosionSound.set_volume(0.1)
                        playerHitSound.set_volume(0.1)
                        playerExplosionSound.set_volume(0.1)
                        optionSelectionSound.set_volume(0.1)
                        optionSelectionSound.play()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and gameState == 1 and player.control == "Teclado":
                    bulletDelay = True
                    bulletDelayLoop = 0
                    teclado = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE and gameState == 1 and player.control == "Teclado":
                    bulletDelay = False
                    bulletDelayLoop = 0
                    teclado = False

            if event.type == pygame.MOUSEBUTTONDOWN and gameState == 1 and player.control == "Mouse":
                bulletDelay = True
                bulletDelayLoop = 0
            elif event.type == pygame.MOUSEBUTTONUP and gameState == 1 and player.control == "Mouse":
                bulletDelay = False
                bulletDelayLoop = 0

        # Game Over
        if gameState == -1:
            if musica != "Musics/ScoreMusic.ogg" and musicaLigada == True:
                musica = "Musics/ScoreMusic.ogg"
                pygame.mixer.music.load(musica)
                pygame.mixer.music.play(-1)
            #Background Image
            if image != "Images/Background/lightBlue.png":
                image = "Images/Background/lightBlue.png"
                background_image = pygame.image.load(image)
                enterScore = False
            while not enterScore:
                if (pygame.key.get_pressed()[pygame.K_ESCAPE]):
                    optionSelectionSound.play
                    gameState = -5
                    gameLoop = True
                    enterScore = True
                elif (pygame.key.get_pressed()[pygame.K_RETURN]):

                    optionSelectionSound.play
                    rank = Score.Ranking(textinput.get_text(), score)
                    rank.poeNaLista(listaDeRankings)
                    listaDeRankings = chamaMetodoDoScore.arrumaLista(listaDeRankings)

                    gameState = 0
                    score = 0
                    enterScore = True
                    all_sprites_list.add(player, damage)
                    background_position[1] = -1280
                    Constants.ASTEROID_MOVE_SPEED = 1
                    Constants.ASTEROID_SUMMON_TIME = 60
                    player.life = 4
                    damage.damageSprite = 0
                    cursor_porcent_X = 50
                    cursor_porcent_Y = 75

                Constants.screen.blit(background_image, [0, 0])
                texto1 = font.render("Fim de jogo! Sua pontuação final foi: " + str(score), True, Constants.WHITE)
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
            if musica != "Musics/MenuMusic.ogg" and musicaLigada == True:
                musica = "Musics/MenuMusic.ogg"
                pygame.mixer.music.load(musica)
                pygame.mixer.music.play(-1)
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
            menu_start = font.render("Iniciar Jogo", True, Constants.BLACK)
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
                cursor = "Images/Spaceship/playerShip2_green.png"

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
            if musica != "Musics/GameMusic.ogg" and musicaLigada == True:
                musica = "Musics/GameMusic.ogg"
                pygame.mixer.music.load(musica)
                pygame.mixer.music.play(-1)
            if image != "Images/Background/Full_Background.png":
                image = "Images/Background/Full_Background.png"
                background_image = pygame.image.load(image).convert()

            if bulletDelay == True and teclado == True and player.control == "Teclado":
                if bulletDelayLoop % 15 == 0 and bulletDelayLoop != 0:
                    click_do_mouse.play()
                    # Fire a bullet if the user clicks the mouse button
                    shot = bullet.Bullet()
                    # Set the bullet to where the player is
                    shot.rect.x = player.rect.x + 44
                    shot.rect.y = player.rect.y - 60
                    #Add the bullet to the lists
                    all_sprites_list.add(shot)
                    bullet_list.add(shot)
                    bulletDelayLoop = 0
                bulletDelayLoop +=1

            elif bulletDelay == True and player.control == "Mouse":
                if bulletDelayLoop % 15 == 0 and bulletDelayLoop != 0:
                    click_do_mouse.play()
                    # Fire a bullet if the user clicks the mouse button
                    shot = bullet.Bullet()
                    # Set the bullet to where the player is
                    shot.rect.x = player.rect.x + 44
                    shot.rect.y = player.rect.y - 60
                    #Add the bullet to the lists
                    all_sprites_list.add(shot)
                    bullet_list.add(shot)
                    bulletDelayLoop = 0
                bulletDelayLoop +=1

            Constants.screen.blit(background_image, background_position)

            scoreText = font.render("SCORE: " + str(score), True, Constants.WHITE)

            lifeText = font.render("Vidas: " + str(player.life), True, Constants.WHITE)

            if player.control == "Teclado" and tempo < 300:
                control_image = "Images/UI/Arrows.png"
                control_image = pygame.image.load(control_image)
                Constants.screen.blit(control_image, (Constants.X - 400, Constants.Y - 300))
            elif player.control == "Mouse" and tempo < 300:
                control_image = "Images/UI/Mouse.png"
                control_image = pygame.image.load(control_image)
                Constants.screen.blit(control_image, (Constants.X - 300, Constants.Y - 300))

            # Summon meteors
            if tempo > 300:
                if loop_game % Constants.ASTEROID_SUMMON_TIME == 0:
                    asteroid = meteor.Meteor()
                    asteroid.reposicionar(Constants.X)
                    meteor_list.add(asteroid)
                loop_game += 1
            if tempo <= 300:
                tempo += 1

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
                    meteorExplosionSound.play()

            #Remove player if he was hit
            player_hit_list = pygame.sprite.spritecollide(player, meteor_list, True)

            if player_hit_list:
                player.life -= 1
                damage.damageSprite += 1
                Constants.screen.blit(damage.image, (player.rect.x, player.rect.y))
                playerHitSound.play()
                if player.life == 0:
                    Constants.ASTEROID_MOVE_SPEED = 1
                    Constants.ASTEROID_SUMMON_TIME = 60
                    Constants.BACKGROUND_SPEED = 2
                    all_sprites_list.remove(player, damage)
                    playerExplosionSound.play()
                    for shot in bullet_list:
                        bullet_list.remove(shot)
                        all_sprites_list.remove(shot)
                    for asteroid in meteor_list:
                        meteor_list.remove(asteroid)
                        all_sprites_list.remove(asteroid)
                    gameState = -1
            else:
                Constants.screen.blit(player.image, (player.rect.x, player.rect.y))

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

        # Option
        if gameState == 2:
            # Background Image
            if image != "Images/Background/lightBlue.png":
                image = "Images/Background/lightBlue.png"
                background_image = pygame.image.load(image)
            Constants.screen.blit(background_image, [0, 0])

            # Option Texts
            opcoes = font.render("Opções", True, Constants.WHITE)
            Constants.screen.blit(opcoes, (Constants.X / 2 - opcoes.get_rect().size[0] / 2, 70))
            som = font.render("Som:", True, Constants.BLACK)
            Constants.screen.blit(som, (Constants.X / 2 - 500, Constants.Y / 100 * 40))
            Constants.screen.blit(active_sound_image, [Constants.X / 2 - 450 + som.get_rect().size[0], Constants.Y / 100 * 39])
            volume = font.render("Volume:", True, Constants.BLACK)
            Constants.screen.blit(volume, (Constants.X / 2 - 500, Constants.Y / 100 * 60))
            Constants.screen.blit(volume_image_button_image, [Constants.X / 2 - 775 + volume_image_button_image.get_rect().size[0], Constants.Y / 100 * 59])
            volume_number = font.render(str(option_volume_number) + "%", True, Constants.WHITE)
            Constants.screen.blit(volume_number, (Constants.X / 2 - 250 + volume_image_button_image.get_rect().size[0], Constants.Y / 100 * 60))
            voltar = font.render("Voltar", True, Constants.BLACK)
            Constants.screen.blit(voltar, (Constants.X / 2 - voltar.get_rect().size[0] / 2, Constants.Y / 100 * 90))

            cursor_X = Constants.X / 2 - voltar.get_rect().size[0] + cursor_porcent_X
            cursor_Y = Constants.Y / 100 * cursor_porcent_Y
            cursor_image = pygame.image.load("Images/Spaceship/playerShip2_green.png").convert()
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

        # Score
        if gameState == 3:
            # Background Image
            if image != "Images/Background/lightBlue.png":
                image = "Images/Background/lightBlue.png"
                background_image = pygame.image.load(image)
            Constants.screen.blit(background_image, [0, 0])

            # Option Texts
            opcoes = font.render("Pontuações", True, Constants.WHITE)
            Constants.screen.blit(opcoes, (Constants.X / 2 - opcoes.get_rect().size[0] / 2, 70))

            score1 = font.render("1.", True, Constants.WHITE)
            Constants.screen.blit(score1, (Constants.X / 2 - 300, Constants.Y / 100 * 20))
            score1_nome = font.render(str(listaDeRankings[0]), True, Constants.WHITE)
            Constants.screen.blit(score1_nome, (Constants.X / 2 - 250, Constants.Y / 100 * 20))

            score2 = font.render("2.", True, Constants.WHITE)
            Constants.screen.blit(score2, (Constants.X / 2 - 300, Constants.Y / 100 * 30))
            score2_nome = font.render(str(listaDeRankings[1]), True, Constants.WHITE)
            Constants.screen.blit(score2_nome, (Constants.X / 2 - 250, Constants.Y / 100 * 30))

            score3 = font.render("3.", True, Constants.WHITE)
            Constants.screen.blit(score3, (Constants.X / 2 - 300, Constants.Y / 100 * 40))
            score3_nome = font.render(str(listaDeRankings[2]), True, Constants.WHITE)
            Constants.screen.blit(score3_nome, (Constants.X / 2 - 250, Constants.Y / 100 * 40))

            score4 = font.render("4.", True, Constants.WHITE)
            Constants.screen.blit(score4, (Constants.X / 2 - 300, Constants.Y / 100 * 50))
            score4_nome = font.render(str(listaDeRankings[3]), True, Constants.WHITE)
            Constants.screen.blit(score4_nome, (Constants.X / 2 - 250, Constants.Y / 100 * 50))

            score5 = font.render("5.", True, Constants.WHITE)
            Constants.screen.blit(score5, (Constants.X / 2 - 300, Constants.Y / 100 * 60))
            score5_nome = font.render(str(listaDeRankings[4]), True, Constants.WHITE)
            Constants.screen.blit(score5_nome, (Constants.X / 2 - 250, Constants.Y / 100 * 60))

            reset = font.render("Resetar Pontuações", True, Constants.BLACK)
            Constants.screen.blit(reset, (Constants.X / 2 - reset.get_rect().size[0] / 2, Constants.Y / 100 * 80))
            voltar = font.render("Voltar", True, Constants.BLACK)
            Constants.screen.blit(voltar, (Constants.X / 2 - voltar.get_rect().size[0] / 2, Constants.Y / 100 * 90))

            # Menu Cursor
            if cursor_porcent_Y == 80:
                cursor = "Images/Spaceship/playerShip2_red.png"
            else:
                cursor = "Images/Spaceship/playerShip2_green.png"


            cursor_X = Constants.X / 2 - voltar.get_rect().size[0] + cursor_porcent_X
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

        # Delete Score
        if gameState == 4:
            # Background Image
            if image != "Images/Background/lightBlue.png":
                image = "Images/Background/lightBlue.png"
                background_image = pygame.image.load(image)
            Constants.screen.blit(background_image, [0, 0])

            # Option Texts
            opcoes = font.render("Pontuações", True, Constants.WHITE)
            Constants.screen.blit(opcoes, (Constants.X / 2 - opcoes.get_rect().size[0] / 2, 70))

            reset = font.render("Deseja realmente apagar todas as pontuações?", True, Constants.RED)
            Constants.screen.blit(reset, (Constants.X / 2 - reset.get_rect().size[0] / 2, Constants.Y / 100 * 40))
            yes = font.render("Sim", True, Constants.BLACK)
            Constants.screen.blit(yes, (Constants.X / 2 - yes.get_rect().size[0] / 2, Constants.Y / 100 * 55))
            no = font.render("Não", True, Constants.BLACK)
            Constants.screen.blit(no, (Constants.X / 2 - no.get_rect().size[0] / 2, Constants.Y / 100 * 65))

            # Menu Cursor
            if cursor_porcent_Y == 55:
                cursor = "Images/Spaceship/playerShip2_red.png"
            else:
                cursor = "Images/Spaceship/playerShip2_green.png"


            cursor_X = Constants.X / 2 - voltar.get_rect().size[0] + cursor_porcent_X
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

        # Controls
        if gameState == 5:
            # Background Image
            if image != "Images/Background/lightBlue.png":
                image = "Images/Background/lightBlue.png"
                background_image = pygame.image.load(image)
            Constants.screen.blit(background_image, [0, 0])

            # Control Image
            if keyboard_image != "Images/UI/Arrows.png":
                keyboard_image = "Images/UI/Arrows.png"
                k_image = pygame.image.load(keyboard_image)
            Constants.screen.blit(k_image, [Constants.X / 2 - 500, Constants.Y / 2 - k_image.get_rect().size[0] / 2])
            if mouse_image != "Images/UI/Mouse.png":
                mouse_image = "Images/UI/Mouse.png"
                m_image = pygame.image.load(mouse_image)
            Constants.screen.blit(m_image, [Constants.X / 2 + 150, Constants.Y / 2 - m_image.get_rect().size[0] / 2])

            # Option Texts
            controles = font.render("Controles", True, Constants.WHITE)
            Constants.screen.blit(controles, (Constants.X / 2 - controles.get_rect().size[0] / 2, 70))

            voltar = font.render("Voltar", True, Constants.BLACK)
            Constants.screen.blit(voltar, (Constants.X / 2 - voltar.get_rect().size[0] / 2, Constants.Y / 100 * 90))

            cursor = "Images/Spaceship/playerShip2_green.png"


            cursor_X = Constants.X / 2 - voltar.get_rect().size[0] + cursor_porcent_X
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

    else:
        if pause == True:
            pauseText = font.render("Pause!", True, Constants.WHITE)
            Constants.screen.blit(pauseText, [Constants.X / 2 - pauseText.get_rect().size[0] / 2, Constants.Y/2])


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if gameState == 1 and event.key == pygame.K_p:
                    pygame.mouse.set_pos([player.rect.x, player.rect.y])
                    pause = False
                if gameState == 1 and pause == True and event.key == pygame.K_ESCAPE:
                    gameLoop = True

    pygame.display.update()
    clock.tick(60)

pygame.quit()
