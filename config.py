import pygame
from button import Button
from os.path import join

LARGURA_TELA = 1280
ALTURA_TELA = 720
display = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA), pygame.SCALED | pygame.RESIZABLE)
pygame.display.set_caption("for_space")
pygame.display.set_icon(pygame.image.load(join("images", "logo.png")))
rows = 5
cols = 13

# Telas
menu_background = pygame.image.load(join('images', 'background_menu_atualizado.png'))
ingame_background = pygame.image.load(join('images', 'universo.png'))
credits_background = pygame.image.load(join('images', 'credits_bg.png'))
game_over_background = pygame.image.load(join('images', 'game_over_screen_sem_botoes.png'))
score_board_background = pygame.image.load(join('images', 'score_board.png'))

# Instanciando botão
play_button = Button('play_button.png', 72.0, 402.7, 1)
scoreboard_button = Button('scoreboard_button.png', 255.8, 487.1, 1)
options_button = Button('options_button.png', 849.4, 487.1, 1)
credits_button = Button('credits_button.png', 1033, 402.7, 1)
back_to_menu_button = Button('back_to_menu_button.png', 20, 20, 1)
play_again_game_over_button = Button('play_again_button.png', 410, 370, 1)
scoreboard_game_over_button = Button('scoreboard_button.png', 720, 293, 1.1)
exit_game_game_over_button = Button('exit_game_button.png', 652, 370, 1)
back_to_menu_game_over_button = Button('back_to_menu_button.png', 330, 295, 1)

player_sprite = pygame.sprite.Group()
invader_group = pygame.sprite.Group()

clock = pygame.time.Clock()
dt = clock.tick(60) / 10      # teste

pause_screen = False