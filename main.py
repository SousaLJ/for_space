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

fps = 60
dropdown.index_selecionado = 1
font_path = 'font\pixeled.ttf'
font = pygame.font.Font(font_path, 16)
def display_score():
    score_surface = font.render(f'Score: {score}', False, 'white')
    score_rect = score_surface.get_rect(topleft = (10, -10))
    display.blit(score_surface, score_rect)

# Obstacles.
obstacles_group = pygame.sprite.Group()
for i in range(4):
    obstacle = Obstacles(coordinate_x_obstacles - (i*345), 450)
    obstacles_group.add(obstacle)

# Invaders
create_invaders()

# Player
player = create_player()

running = True
clock = pygame.time.Clock()

game_state = 'menu'
pause_screen = False

#carregando musicas e efeitos sonoros

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

            if back_to_menu_button.draw(display):
                game_state = 'menu'
            

        case 'options':
            display.blit(options_background, (0, 0))

            #opções de audio
            if back_to_menu_button.draw(display):
                game_state = 'menu'

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
            
            if back_to_menu_button.draw(display):
                game_state = 'menu'

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
            
        case 'ps_options':
            # pause screen options
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
            
            if back_to_game_button.draw(display):
                game_state = 'playing'
                pause_screen = 'false'

        case 'credits':
            display.blit(credits_background, (0, 0))

            if back_to_menu_button.draw(display):
                game_state = 'menu'

        case 'playing':
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

                # Exibe os obstáculos.
                obstacles_group.draw(display)

                if pause_screen:
                    invader_group.draw(display)
                    player_sprite.draw(display)
                    player_fire.draw(display)
                    invader_fire.draw(display)
                    special_invader_group.draw(display)
                    explosion_group.draw(display)
                    
                    if ps_play_button.draw(display):
                        pause_screen = False

                    if ps_options.draw(display):
                        game_state = 'ps_options'
        
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
                    
                    for obstacle in obstacles_group:
                        for invader in invader_group:
                            invader_collision = pygame.sprite.collide_rect(obstacle, invader)
                        
                        for ship in player_sprite:
                            ship_collision = pygame.sprite.collide_rect(obstacle, ship)
                        for fire in player_fire:
                            if pygame.sprite.collide_rect(obstacle, fire):
                                fire.kill()

                        for fire in invader_fire:
                            if pygame.sprite.collide_rect(obstacle, fire):
                                fire.kill()                 

                    # Logica do hit no invader
                    for fire in player_fire:
                        
                        invader_hitted = pygame.sprite.spritecollide(fire, invader_group, True, pygame.sprite.collide_mask)
                        # special_invader_hitted = pygame.sprite.spritecollide(fire, special_invader_group, True)
                        if invader_hitted:
                            for invader in invader_hitted:
                                score += invader.reward
                                explosion = Explosion(invader.rect.center)
                                explosion_group.add(explosion)

                                som_invader_morto.play()
                                
                                

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
                            
                    # Se houver colisões, destacar os sprites e calcular a área de colisão.
                    colisoes_player_aliens = pygame.sprite.groupcollide(player_sprite, invader_group, False, True, pygame.sprite.collide_mask)
                    if colisoes_player_aliens:
                        for ships, collided_sprites in colisoes_player_aliens.items():
                            for invaders in collided_sprites:
                                # Calcular a área de interseção da colisão.
                                area_colisao = ships.rect.clip(invaders.rect)
                        
                        # Exibe uma imagem de explosão na coordenada (x, y) da colisão e retira uma vida do jogador.
                        explosion = Explosion(area_colisao.center)
                        explosion_group.add(explosion)
                        lifes_left -= 1     

    if game_state == 'game_over':
        
        # Pinta no fundo a tela de fim de jogo.
        display.blit(game_over_background, (0, 0))

        # Reinicia as vidas do jogador.
        lifes_left = 5

        # Verifica se o botão de jogar novamente foi pressionado
        if play_again_game_over_button.draw(display):
            score = 0
            invader_fire.empty()
            invader_group.empty()
            player_sprite.empty()
            player_fire.empty()
            create_invaders()
            create_player()
            pause_screen = False
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