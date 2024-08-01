import pygame
import button
from sys import exit
from os.path import join

pygame.init()

pygame.display.set_caption("for_invaders")
pygame.display.set_icon(pygame.image.load(join("images", "logo.png")))

LARGURA_TELA = 1080
ALTURA_TELA = 720
display = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA), pygame.SCALED | pygame.RESIZABLE)

# Telas
menu_background = pygame.image.load(join('images', 'logo_redimensionado.png')).convert()
ingame_background = pygame.image.load(join('images', 'universo.png'))

# Botões
play_img = pygame.image.load(join('images', 'buttons', 'play.png')).convert_alpha()
options_img = pygame.image.load(join('images', 'buttons', 'options.png')).convert_alpha()
scoreboard_img = pygame.image.load(join('images', 'buttons', 'scoreboard.png')).convert_alpha()
credits_img = pygame.image.load(join('images', 'buttons', 'credits.png')).convert_alpha()

play_button = button.Button(221, 366, play_img, 0.8)
scoreboard_button = button.Button(376, 413, scoreboard_img, 0.8)
options_button = button.Button(603, 408, options_img, 0.8)
credits_button = button.Button(758, 357, credits_img, 0.8)

running = True
game_paused = True

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
        display.blit(menu_background, (180,0))

        if scoreboard_button.draw(display):
            game_state = 'menu_scoreboard'

        if options_button.draw(display):
            game_state = 'menu_options'

        if play_button.draw(display):
            print('clicked')
            game_state = 'playing'

        if credits_button.draw(display):
            game_state = 'menu_credits'

    if game_state == 'playing':
        display.blit(ingame_background, (0, 0))

    
    pygame.display.update()
