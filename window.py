import pygame
import button
from player import Player
from sys import exit
from os.path import join

pygame.init()

pygame.display.set_caption("for_space")
pygame.display.set_icon(pygame.image.load(join("images", "logo.png")))

LARGURA_TELA = 1280
ALTURA_TELA = 720
display = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA), pygame.SCALED | pygame.RESIZABLE)

# Telas
menu_background = pygame.image.load(join('images', 'background_menu_atualizado.png'))
ingame_background = pygame.image.load(join('images', 'universo.png'))
credits_background = pygame.image.load(join('images', 'credits_bg.png'))
game_over_background = pygame.image.load(join('images', 'game_over_screen_sem_botoes.png'))

# Instanciando botão
play_button = button.Button('play_button.png', 72.0, 402.7, 1)
scoreboard_button = button.Button('scoreboard_button.png', 255.8, 487.1, 1)
options_button = button.Button('options_button.png', 849.4, 487.1, 1)
credits_button = button.Button('credits_button.png', 1033, 402.7, 1)
back_to_menu_button = button.Button('back_to_menu_button.png', 20, 20, 1)
play_again_game_over_button = button.Button('play_again_button.png', 410, 370, 1)
scoreboard_game_over_button = button.Button('scoreboard_button.png', 720, 293, 1.1)
exit_game_game_over_button = button.Button('exit_game_button.png', 652, 370, 1)
back_to_menu_game_over_button = button.Button('back_to_menu_button.png', 330, 295, 1)

running = True
clock = pygame.time.Clock()

game_state = 'menu'
previous_game_state = game_state

player_sprite = pygame.sprite.GroupSingle()
player = Player(ALTURA_TELA // 2, LARGURA_TELA // 2, player_sprite)

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
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and game_state != 'playing':
            game_state = previous_game_state
            
    # background atual será definido apos condição
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

    elif game_state == 'menu_scoreboard' or game_state == 'menu_options':
        if back_to_menu_button.draw(display):
            game_state = 'menu'
        

    elif game_state == 'playing':
        display.blit(ingame_background, (0, 0))
        
        player_sprite.update()
        player_sprite.draw(display)
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and not pause_screen:
            pause_screen = True
            # Pause_Screen()
            print("PAUSE SCREEN")
    
        if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
            pause_screen = False
        
        # if colisao:
        #   game_state = 'game_over'
        
    elif game_state == 'game_over':
        # Pinta no fundo a tela de fim de jogo.
        display.blit(game_over_background, (0, 0))

        # Verifica se o botão de jogar novamente foi pressionado
        if play_again_game_over_button.draw(display):
            game_state = 'playing'
        
        # Verifica se o botão de voltar para o menu foi pressionado
        elif back_to_menu_game_over_button.draw(display):
            previous_game_state = game_state
            game_state = 'menu'
        
        # Verifica se o botão de mostrar o scoreboard foi pressionado
        elif scoreboard_game_over_button.draw(display):
            previous_game_state = game_state
            game_state = 'menu_scoreboard'
        
        # Verifica se o botão de sair do jogo foi pressionado
        elif exit_game_game_over_button.draw(display):
            pygame.quit()
            exit()

    elif game_state == 'menu_credits':
        display.blit(credits_background, (0, 0))
        if back_to_menu_button.draw(display):
            game_state = 'menu'

    else:
        pass

    
    pygame.display.update()