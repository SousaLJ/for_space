import pygame
import button
from sys import exit
from os.path import join

pygame.init()

pygame.display.set_caption("for_invaders")
pygame.display.set_icon(pygame.image.load(join("images", "logo.png")))

LARGURA_TELA = 1280
ALTURA_TELA = 720
display = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA), pygame.SCALED | pygame.RESIZABLE)

# Telas
menu_background = pygame.image.load(join('images', 'logo_redimensionado.png')).convert()
ingame_background = pygame.image.load(join('images', 'universo.png'))
credits_background = pygame.image.load(join('images', 'credits_bg.png'))
game_over_background = pygame.image.load(join('images', 'game_over_screen_sem_botoes.png'))

# Botões
play_img = pygame.image.load(join('images', 'buttons', 'play.png')).convert_alpha()
options_img = pygame.image.load(join('images', 'buttons', 'options.png')).convert_alpha()
scoreboard_img = pygame.image.load(join('images', 'buttons', 'scoreboard.png')).convert_alpha()
credits_img = pygame.image.load(join('images', 'buttons', 'credits.png')).convert_alpha()
btm_img = pygame.image.load(join('images', 'buttons','btm_img.png')).convert_alpha()
play_again_game_over_img = pygame.image.load(join('images', 'buttons','play_again.png')).convert_alpha()
back_to_menu_game_over_img = pygame.image.load(join('images', 'buttons','back_to_menu.png')).convert_alpha()
scoreboard_game_over_img = pygame.image.load(join('images', 'buttons','scoreboard_game_over.png')).convert_alpha()
exit_game_game_over_img = pygame.image.load(join('images', 'buttons','exit_game.png')).convert_alpha()

play_button = button.Button(261.93, 335.39, play_img, 0.8)
scoreboard_button = button.Button(445.63, 382.39, scoreboard_img, 0.8)
options_button = button.Button(714.67, 377.39, options_img, 0.8)
credits_button = button.Button(898.37, 329.39, credits_img, 0.8)
btm_button = button.Button(20, 20, btm_img, 1)
play_again_game_over_button = button.Button(410, 370, play_again_game_over_img, 1)
back_to_menu_game_over_button = button.Button(330, 295, back_to_menu_game_over_img, 1)
scoreboard_game_over_button = button.Button(740, 290, scoreboard_game_over_img, 1)
exit_game_game_over_button = button.Button(652, 370, exit_game_game_over_img, 1)

running = True

game_state = 'menu'

while running:

    # fundo com a cor da for_code
    display.fill("#1E1647")

    # enquanto o jogo esta rodando procuramos por eventos

    for event in pygame.event.get():
        # pygame.QUIT event significa que o usuario fechou a janela no X
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # background atual será definido apos condição
    if game_state == 'menu':
        display.blit(menu_background, (280,0))

        if scoreboard_button.draw(display):
            game_state = 'menu_scoreboard'

        if options_button.draw(display):
            game_state = 'menu_options'

        if play_button.draw(display):
            print('clicked')
            game_state = 'playing'

        if credits_button.draw(display):
            game_state = 'menu_credits'

    elif game_state == 'playing':
        #display.blit(ingame_background, (0, 0)) Comentado com o propósito de testar a tela de fim de jogo
        
        # Pinta no fundo a tela de fim de jogo.
        display.blit(game_over_background, (0, 0))

        # Verifica se o botão de jogar novamente foi pressionado
        if play_again_game_over_button.draw(display):
            game_state == 'playing'
        
        # Verifica se o botão de voltar para o menu foi pressionado
        elif back_to_menu_game_over_button.draw(display):
            game_state = 'menu'
        
        # Verifica se o botão de mostrar o scoreboard foi pressionado
        elif scoreboard_game_over_button.draw(display):
            game_state = 'menu_scoreboard'
        
        # Verifica se o botão de sair do jogo foi pressionado
        elif exit_game_game_over_button.draw(display):
            pygame.quit()
            exit()

    elif game_state == 'menu_credits':
        display.blit(credits_background, (0, 0))
        if btm_button.draw(display):
            game_state = 'menu'

    else:
        pass

    
    pygame.display.update()