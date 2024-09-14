import pygame
from musica import *
from pygame import mixer
from player import *
from invaders import *
from sys import exit
from os.path import join
from config import *
from fire import *
from dropdown import *
from obstacles import *

pygame.init()
mixer.init()

score = 0
registrou = False

fps = 60
dropdown.index_selecionado = 1
font_path = 'font\\pixeled.ttf'
font = pygame.font.Font(font_path, 16)
def display_score():
    score_surface = font.render(f'Score: {score}', False, 'white')
    score_rect = score_surface.get_rect(topleft = (10, -10))
    display.blit(score_surface, score_rect)

def collisions():
    global score, lifes_left
    invader_hitted = pygame.sprite.groupcollide(invader_group,player_fire, True, True, pygame.sprite.collide_mask)
    if invader_hitted:
        for invader in invader_hitted:
            score += invader.reward
            explosion_group.add(Explosion(invader.rect.center))
        som_invader_morto.play()

    if pygame.sprite.groupcollide(player_fire, special_invader_group, True, True, pygame.sprite.collide_rect):
        explosion_group.add(Explosion(special_invader.rect.center))
        score += special_invader.reward

    pygame.sprite.groupcollide(obstacle_group, player_fire, True, True)
    pygame.sprite.groupcollide(obstacle_group, invader_fire, True, True, pygame.sprite.collide_rect)

    for fire in invader_fire:
        if pygame.sprite.spritecollide(fire, player_sprite, False, pygame.sprite.collide_mask):
            explosion_group.add(Explosion(fire.rect.center))
            fire.kill()
            lifes_left -= 1

        if pygame.sprite.spritecollide(fire, player_fire, True, pygame.sprite.collide_rect):
            explosion_group.add(Explosion(fire.rect.center))
            fire.kill()

def update_and_draw():
    special_invader_group.update()
    special_invader_group.draw(display)

    invader_group.update()
    invader_group.draw(display)

    invader_fire.update()
    invader_fire.draw(display)
    
    player_sprite.update()
    player_sprite.draw(display)

    player_fire.update()
    player_fire.draw(display)

    explosion_group.update()
    explosion_group.draw(display)
    
    obstacle_group.update()
    obstacle_group.draw(display)

def pause_menu():
    invader_group.draw(display)
    player_sprite.draw(display)
    player_fire.draw(display)
    invader_fire.draw(display)
    special_invader_group.draw(display) 
    explosion_group.draw(display)
    obstacle_group.draw(display)
    
    if ps_play_button.draw(display):
        global pause_screen
        pause_screen = False
    if ps_options.draw(display):
        global game_state
        game_state = 'ps_options'
    if ps_back_to_menu_button.draw(display):
        reset_game()
        game_state = 'menu'
    if ps_exit_game.draw(display):
        pygame.quit()
        exit()

def reset_game():
    global score, lifes_left, pause_screen, registrou
    registrou = False
    score = 0
    lifes_left = 5
    pause_screen = False
    
    invader_fire.empty()
    invader_group.empty()
    create_invaders()

    player_sprite.empty()
    player_fire.empty()
    create_player()
    
    obstacle_group.empty()
    create_obstacles()

def options():
    display.blit(options_background, (0, 0))
    tocar_musica()
    #opções de audio
    musica_text = font.render("Volume da Musica:", True, 'white')
    display.blit(musica_text, (345, 200))

    efeitos_text = font.render("Volume dos Efeitos:", True, 'white')
    display.blit(efeitos_text, (345, 300))

    volume_musica = musica_slider.draw(display)
    volume_efeitos = efeitos_slider.draw(display)

    volume_musica_percent = volume_musica / 100
    mixer.music.set_volume(volume_musica_percent)

    volume_efeitos_percent = volume_efeitos / 100
    som_invader_morto.set_volume(volume_efeitos_percent)
    som_ship_exp.set_volume(volume_efeitos_percent)
    som_shoot.set_volume(volume_efeitos_percent)

    #opções de display
    brilho_text = font.render("Brilho:", True, 'white')
    display.blit(brilho_text, (430, 500))

    brilho = brilho_slider.draw(display)

    fps_text = font.render("Taxa de Atualizaçao:", True, 'white')
    display.blit(fps_text, (345, 400))  

    for evento in eventos:
        dropdown.handle_event(evento)

    dropdown.draw(display)

    if dropdown.index_selecionado == 0:
        fps = 30
        pygame.display.set_caption("Space Invaders - FPS: 30")
    elif dropdown.index_selecionado == 1:
        fps = 60
        pygame.display.set_caption("Space Invaders - FPS: 60")
    elif dropdown.index_selecionado == 2:
        fps = 120
        pygame.display.set_caption("Space Invaders - FPS: 120")
    elif dropdown.index_selecionado == 3:
        fps = 144
        pygame.display.set_caption("Space Invaders - FPS: 240")

def registrar_score():
    with open("scoreboard.txt", 'a') as arquivo:  # Modo 'a' adiciona ao final do arquivo
        arquivo.write(f'{score}' + '\n')
    return True

#Obstacle
create_obstacles()

#Invaders
create_invaders()

#Player
player = create_player()

running = True
clock = pygame.time.Clock()

game_state = 'menu'
pause_screen = False

mixer.music.play(-1)

while running:

    clock.tick(fps)
    # fundo com a cor da for_code
    display.fill("#1E1647")
    # enquanto o jogo esta rodando procuramos por eventos

    eventos = pygame.event.get()

    for event in eventos:
        
        # pygame.QUIT event significa que o usuario fechou a janela no X
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_state == 'playing':
            # esc in-game pausa o jogo e so despausa ao apertar esc novamente
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and not pause_screen:
                print("pause")
                pause_screen = True

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and pause_screen:
                print("saindo do pause")
                pause_screen = False
                
            # increase fire rate test
            if event.type == pygame.KEYDOWN and event.key == pygame.K_0 and game_state == 'playing':
                player.cooldown = 100

            if event.type == INVADERFIRE and not pause_screen:
                invaders_fire()

            if event.type == SPECIALINVADER:
                special_invader = SpecialInvader(random.choice([0, 1]))
                special_invader_group.add(special_invader)

    match game_state:
        case 'menu':
            tocar_musica()
            
            display.blit(menu_background, (0,0))

            if scoreboard_button.draw(display):
                game_state = 'scoreboard'

            elif options_button.draw(display):
                game_state = 'options'

            elif play_button.draw(display):
                game_state = 'playing'

            elif credits_button.draw(display):
                game_state = 'credits'

        case 'scoreboard':
            tocar_musica()
            display.blit(score_board_background, (0, 0))

            with open('scoreboard.txt', 'r') as arquivo:  # Modo 'a' adiciona ao final do arquivo
                lista_argumentos = [linha.strip() for linha in arquivo.readlines()] # Lista que armazena o conteudo do arquivo
                numero_argumentos = len(lista_argumentos)  # Conta o número de linhas/argumentos

            print(lista_argumentos)

            for i in range(numero_argumentos):
                points_surface = font.render(f'{lista_argumentos[i]}', False, 'white')
                points_rect = points_surface.get_rect(topleft = ((785), (340+(i*50))))
                display.blit(points_surface, points_rect)

            if back_to_menu_button.draw(display):
                game_state = 'menu'
            

        case 'options':
            display.blit(options_background, (0, 0))

            options()
            if back_to_menu_button.draw(display):
                game_state = 'menu'
            
        case 'ps_options':
            # pause screen options
            options()
            
            if back_to_game_button.draw(display):
                game_state = 'playing'
                pause_screen = 'false'

        case 'credits':
            display.blit(credits_background, (0, 0))

            if back_to_menu_button.draw(display):
                game_state = 'menu'

        case 'playing':
            if not invader_group:
                game_state = 'game_over'
            pygame.mixer_music.stop()
            if lifes_left == 0:
                game_state = 'game_over'
                som_gover.play()
            else:
                display.blit(ingame_background, (0, 0))
                display_score()

                # Exibe as vidas do jogador.
                for i in range(lifes_left):
                    display.blit(lifes_left_image, (coordinate_x_lifes - (i*40), 0))

                if pause_screen:
                    pause_menu()
                else:
                    update_and_draw()
                    check_invader_position()
                    collisions()

        case 'game_over':
            # Pinta no fundo a tela de fim de jogo.
            display.blit(game_over_background, (0, 0))

            # Reinicia as vidas do jogador.
            # lifes_left = 5
            if not registrou:
                registrou = registrar_score()
            # Verifica se o botão de jogar novamente foi pressionado
            if play_again_game_over_button.draw(display):
                reset_game()
                game_state = 'playing'
            
            # Verifica se o botão de voltar para o menu foi pressionado
            elif back_to_menu_game_over_button.draw(display):
                reset_game()
                game_state = 'menu'
                
            # Verifica se o botão de mostrar o scoreboard foi pressionado
            elif scoreboard_game_over_button.draw(display):
                game_state = 'scoreboard'
            
            # # Verifica se o botão de sair do jogo foi pressionado
            elif exit_game_game_over_button.draw(display):
                pygame.quit()
                exit()

    
    pygame.display.update()