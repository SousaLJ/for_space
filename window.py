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

score = 0
def display_score():
    score_surface = font.render(f'Score: {score}', False, 'white')
    score_rect = score_surface.get_rect(topleft = (10, -10))
    display.blit(score_surface, score_rect)


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

        if event.type == INVADERFIRE:
            invaders_fire()
            
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
        display_score()
        invader_group.update()
        invader_group.draw(display)
        check_invader_position()

        invader_fire.update()
        invader_fire.draw(display)
        
        player_sprite.update()
        player_sprite.draw(display)
        
        # Logica do hit no invader
        for fire in player_sprite:
            invader_hit = pygame.sprite.spritecollide(fire, invader_group, True)
            if invader_hit:
                for invader in invader_hit:
                    score += invader.reward
                fire.kill()

        # Logica do hit no player
        # False pois somente o hit vai sumir mas o player permanecerá vivo perdendo HP
        # Precisa implementar ainda algo para validar o HP perdido
        if invader_fire:
            for fire in invader_fire:
                # O modo como a classe Fire foi implementada (recebendo um group como inicializador)
                # parar herdar, vincula um ao outro tornando-os 1 coisa só.
                # Por exemplo, no código abaixo estamos checando cada instancia de tiro criada
                # a partir do click no mouse ou barra de espaço, essa instancia é adicionada
                # ao grupo player_sprite e checa a colisão com invader_group
                # Porem, se analisarmos bem, como o tiro é um player_sprite, 
                # todo tiro gerado a partir da classe invader checa colisão com o tiro do player
                # criando uma mecanica na qual da para anular o tiro do invader com o tiro do player
                # Entao é necessario certificar se a gente vai querer isso ou não no nosso game

                if pygame.sprite.spritecollide(fire, player_sprite, False):
                    fire.kill()

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