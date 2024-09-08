import pygame
from player import *
from invaders import *
from sys import exit
from os.path import join
from config import *
from fire import *

pygame.init()


score = 0
def display_score():
    score_surface = font.render(f'Score: {score}', False, 'white')
    score_rect = score_surface.get_rect(topleft = (10, -10))
    display.blit(score_surface, score_rect)

# Invaders
create_invaders()

# Player
player = create_player()

running = True
clock = pygame.time.Clock()

game_state = 'menu'

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
            display.blit(score_board_background, (0, 0))

            if back_to_menu_button.draw(display):
                game_state = 'menu'
            
        case 'options':
            if back_to_menu_button.draw(display):
                game_state = 'menu'

        case 'credits':
            display.blit(credits_background, (0, 0))

            if back_to_menu_button.draw(display):
                game_state = 'menu'

        case 'playing':
            if lifes_left == 0:
                game_state = 'game_over'

            else:
                display.blit(ingame_background, (0, 0))

                display_score()

                # Exibe as vidas do jogador.
                for i in range(lifes_left):
                    display.blit(lifes_left_image, (coordinate_x - (i*40), 0))

                if pause_screen:
                    invader_group.draw(display)
                    player_sprite.draw(display)
                    invader_fire.draw(display)
                    special_invader_group.draw(display)
                    explosion_group.draw(display)

                    if ps_play_button.draw(display):
                        pause_screen = False

                    if ps_options.draw(display):
                        ...
        
                    if ps_back_to_menu_button.draw(display):
                        game_state = 'menu'
                        score = 0
                        invader_fire.empty()
                        invader_group.empty()
                        player_sprite.empty()
                        player_fire.empty()
                        create_invaders()
                        create_player()
                        pause_screen = False
                        lifes_left = 5

                    if ps_exit_game.draw(display):
                        pygame.quit()
                        exit()
                    
                else:
                    special_invader_group.update()
                    special_invader_group.draw(display)

                    check_invader_position()
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
                    
                    # Logica do hit no invader
                    for fire in player_fire:
                        invader_hitted = pygame.sprite.spritecollide(fire, invader_group, True, pygame.sprite.collide_mask)
                        # special_invader_hitted = pygame.sprite.spritecollide(fire, special_invader_group, True)
                        if invader_hitted:
                            for invader in invader_hitted:
                                score += invader.reward
                                explosion = Explosion(invader.rect.center)
                                explosion_group.add(explosion)
                            # for special_invader in special_invader_hitted:
                            #     score += special_invader.reward
                            #     explosion = Explosion(special_invader.rect.center)
                            #     explosion_group.add(explosion)
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
                            if pygame.sprite.spritecollide(fire, player_sprite, False, pygame.sprite.collide_mask):
                                explosion = Explosion(fire.rect.center)
                                explosion_group.add(explosion)
                                fire.kill()

                                # Retira uma vida do jogador.
                                lifes_left -= 1 
        
    if game_state == 'game_over':
        # Pinta no fundo a tela de fim de jogo.
        display.blit(game_over_background, (0, 0))

        # Reinicia as vidas do jogador.
        lifes_left = 5

        # Verifica se o botão de jogar novamente foi pressionado
        if play_again_game_over_button.draw(display):
            game_state = 'playing'
        
        # Verifica se o botão de voltar para o menu foi pressionado
        elif back_to_menu_game_over_button.draw(display):
            game_state = 'menu'
              
        # Verifica se o botão de mostrar o scoreboard foi pressionado
        elif scoreboard_game_over_button.draw(display):
            game_state = 'scoreboard'
        
        # # Verifica se o botão de sair do jogo foi pressionado
        elif exit_game_game_over_button.draw(display):
            pygame.quit()
            exit()

    else:
        pass

    
    pygame.display.update()