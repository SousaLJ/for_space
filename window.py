import pygame
from player import Player
from invaders import *
from sys import exit
from os.path import join
from config import *

pygame.init()

# Invaders   
create_invaders()
# Player
player = Player((ALTURA_TELA / 2, LARGURA_TELA / 2), player_sprite)

running = True
clock = pygame.time.Clock()

game_state = 'menu'
previous_game_state = game_state

pause_screen = False

while running:
    clock.tick(60)
    # fundo com a cor da for_code
    display.fill("#1E1647")
    # enquanto o jogo esta rodando procuramos por eventos

    for event in pygame.event.get():
        # pygame.QUIT event significa que o usuario fechou a janela no X
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # esc retorna ao game_state antigo
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and game_state != 'playing':
            game_state = previous_game_state
        
        # esc in-game pausa o jogo e so despausa ao apertar esc novamente
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and not pause_screen and game_state == 'playing':
            print("pause")
            pause_screen = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and pause_screen and game_state == 'playing':
            print("saindo do pause")
            pause_screen = False
            
        # increase fire rate test
        if event.type == pygame.KEYDOWN and event.key == pygame.K_0 and game_state == 'playing':
            player.cooldown = 100
            
    if game_state == 'menu':
        display.blit(menu_background, (0,0))

        if scoreboard_button.draw(display):
            previous_game_state = game_state
            game_state = 'menu_scoreboard'

        elif options_button.draw(display):
            previous_game_state = game_state
            game_state = 'menu_options'

        elif play_button.draw(display):
            previous_game_state = game_state
            game_state = 'playing'

        elif credits_button.draw(display):
            previous_game_state = game_state
            game_state = 'menu_credits'

    elif game_state == 'menu_scoreboard':
        display.blit(score_board_background, (0, 0))
        if back_to_menu_button.draw(display):
            game_state = 'menu'
            
    elif game_state == 'menu_options':
        if back_to_menu_button.draw(display):
            game_state = 'menu'


    elif game_state == 'playing':
        display.blit(ingame_background, (0, 0))
        invader_group.update()
        invader_group.draw(display)
        check_invader_position()
        
        player_sprite.update()
        player_sprite.draw(display)
        
        # if colisao:
        #   game_state = 'game_over'
        
    elif game_state == 'game_over':
        # Pinta no fundo a tela de fim de jogo.
        # display.blit(game_over_background, (0, 0))

        # Verifica se o botão de jogar novamente foi pressionado
        if play_again_game_over_button.draw(display):
            game_state = 'playing'
        # if play_again_game_over_button.draw(display):
        #     game_state == 'playing'
        
        # Verifica se o botão de voltar para o menu foi pressionado
        elif back_to_menu_game_over_button.draw(display):
            previous_game_state = game_state
            game_state = 'menu'
        # # Verifica se o botão de voltar para o menu foi pressionado
        # elif back_to_menu_game_over_button.draw(display):
        #     game_state = 'menu'
        
        # Verifica se o botão de mostrar o scoreboard foi pressionado
        elif scoreboard_game_over_button.draw(display):
            previous_game_state = game_state
            game_state = 'menu_scoreboard'
        # # Verifica se o botão de mostrar o scoreboard foi pressionado
        # elif scoreboard_game_over_button.draw(display):
        #     game_state = 'menu_scoreboard'
        
        # # Verifica se o botão de sair do jogo foi pressionado
        # elif exit_game_game_over_button.draw(display):
        #     pygame.quit()
        #     exit()

    elif game_state == 'menu_credits':
        display.blit(credits_background, (0, 0))
        if back_to_menu_button.draw(display):
            game_state = 'menu'

    else:
        pass

    
    pygame.display.update()