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

# Inicialização do Pygame e Mixer
pygame.init()
mixer.init()

# Configurações iniciais
score = 0
fps = 60
dropdown.index_selecionado = 1
font_path = 'font\\pixeled.ttf'
font = pygame.font.Font(font_path, 16)
clock = pygame.time.Clock()

game_state = 'menu'
pause_screen = False
lifes_left = 5  

# Inicialização da música
mixer.music.play(-1)

def display_score():
    score_surface = font.render(f'Score: {score}', False, 'white')
    score_rect = score_surface.get_rect(topleft=(10, -10))
    display.blit(score_surface, score_rect)

def reset_game():
    global score, lifes_left, pause_screen
    score = 0
    lifes_left = 5
    pause_screen = False
    invader_fire.empty()
    invader_group.empty()
    player_sprite.empty()
    player_fire.empty()
    create_invaders()
    create_player()

def update_and_draw_gameplay():
    # Atualização e desenho dos elementos do jogo
    special_invader_group.update()
    invader_group.update()
    invader_fire.update()
    player_sprite.update()
    player_fire.update()
    explosion_group.update()
    obstacle_group.update()

    special_invader_group.draw(display)
    invader_group.draw(display)
    invader_fire.draw(display)
    player_sprite.draw(display)
    player_fire.draw(display)
    explosion_group.draw(display)
    obstacle_group.draw(display)

    # Verificação de colisões
    handle_collisions()

def handle_collisions():
    global score, lifes_left
    # Colisões de tiros com invasores
    invader_hitted = pygame.sprite.groupcollide(invader_group,player_fire, True, True, pygame.sprite.collide_rect)
    if invader_hitted:
        for invader in invader_hitted:
            score += invader.reward
            explosion_group.add(Explosion(invader.rect.center))
        som_invader_morto.play()

    pygame.sprite.groupcollide(player_fire, special_invader_group, True, True, pygame.sprite.collide_rect)

    # Colisões com obstáculos
    pygame.sprite.groupcollide(obstacle_group, player_fire, True, True)
    pygame.sprite.groupcollide(obstacle_group, invader_fire, True, True, pygame.sprite.collide_rect)

    # Colisões de tiros inimigos com o jogador
    for fire in invader_fire:
        if pygame.sprite.spritecollide(fire, player_sprite, False, pygame.sprite.collide_mask):
            explosion_group.add(Explosion(fire.rect.center))
            fire.kill()
            lifes_left -= 1

        if pygame.sprite.spritecollide(fire, player_fire, True, pygame.sprite.collide_rect):
            explosion_group.add(Explosion(fire.rect.center))
            fire.kill()

    #colisões de jogadores com invasores
    # colisoes_player_aliens = pygame.sprite.groupcollide(player_sprite, invader_group, False, True, pygame.sprite.collide_rect)
    # if colisoes_player_aliens:
    #     for ships, collided_sprites in colisoes_player_aliens.items():
    #         for invaders in collided_sprites:
    #             explosion_group.add(Explosion(ships.rect.center))
    #         lifes_left -= 1

def draw_pause_menu():
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

# Criação de entidades
create_obstacles()
create_invaders()
player = create_player()

# Loop principal do jogo
running = True
while running:
    clock.tick(fps)
    display.fill("#1E1647")  # Fundo da tela
    eventos = pygame.event.get()

    # Eventos gerais
    for event in eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN and game_state == 'playing':
            if event.key == pygame.K_ESCAPE:
                pause_screen = not pause_screen
            elif event.key == pygame.K_0:  # Teste de aumento de taxa de disparo
                player.cooldown = 100

        if event.type == INVADERFIRE and not pause_screen:
            invaders_fire()

        if event.type == SPECIALINVADER:
            special_invader = SpecialInvader(random.choice([0, 1]))
            special_invader_group.add(special_invader)

    # Atualização dos estados do jogo
    match game_state:
        case 'menu':
            tocar_musica()
            display.blit(menu_background, (0, 0))
            if play_button.draw(display): 
                game_state = 'playing'
            elif scoreboard_button.draw(display): 
                game_state = 'scoreboard'
            elif options_button.draw(display): 
                game_state = 'options'
            elif credits_button.draw(display):
                game_state = 'credits'

        case 'scoreboard':
            tocar_musica()
            display.blit(score_board_background, (0, 0))
            with open('scoreboard.txt', 'r') as arquivo:
                lista_argumentos = [linha.strip() for linha in arquivo.readlines()]
            for i, score in enumerate(lista_argumentos):
                points_surface = font.render(f'{score}', False, 'white')
                points_rect = points_surface.get_rect(topleft=((785), (340 + (i * 50))))
                display.blit(points_surface, points_rect)
            if back_to_menu_button.draw(display): game_state = 'menu'

        case 'options':
            display.blit(options_background, (0, 0))
            if back_to_menu_button.draw(display): game_state = 'menu'
            volume_musica = musica_slider.draw(display) / 100
            volume_efeitos = efeitos_slider.draw(display) / 100
            mixer.music.set_volume(volume_musica)
            som_invader_morto.set_volume(volume_efeitos)
            som_ship_exp.set_volume(volume_efeitos)
            som_shoot.set_volume(volume_efeitos)
            brilho = brilho_slider.draw(display)
            fps_text = font.render("Taxa de Atualização:", True, 'white')
            display.blit(fps_text, (345, 400))
            for evento in eventos: dropdown.handle_event(evento)
            dropdown.draw(display)
            fps_options = [30, 60, 120, 144]
            fps = fps_options[dropdown.index_selecionado]
            pygame.display.set_caption(f"Space Invaders - FPS: {fps}")

        case 'playing':
            pygame.mixer_music.stop()
            if lifes_left == 0:
                game_state = 'game_over'
                som_gover.play()
            else:
                display.blit(ingame_background, (0, 0))
                display_score()
                for i in range(lifes_left):
                    display.blit(lifes_left_image, (coordinate_x_lifes - (i * 40), 0))

                if not pause_screen:
                    update_and_draw_gameplay()

                if pause_screen:
                    draw_pause_menu()

        case 'game_over':
            display.blit(game_over_background, (0, 0))
            if play_again_game_over_button.draw(display):
                reset_game()
                game_state = 'playing'
            elif back_to_menu_game_over_button.draw(display): 
                game_state = 'menu'
            elif scoreboard_game_over_button.draw(display): 
                game_state = 'scoreboard'
            elif exit_game_game_over_button.draw(display):
                pygame.quit()
                exit()

    pygame.display.update()
