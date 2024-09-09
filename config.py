import pygame
from dropdown import *
from button import Button
from slider import *
from os.path import join
from random import randint

''' Para uma futura opção de colocar em tela cheia.
display = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
LARGURA_TELA = display.get_rect().width
ALTURA_TELA = display.get_rect().height'''

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
options_background = pygame.image.load(join('images', 'options_bg.png'))

# Instanciando botão
play_button = Button('play_button.png', 72.0, 402.7, 1)
scoreboard_button = Button('scoreboard_button.png', 255.8, 487.1, 1)
options_button = Button('options_button.png', 849.4, 487.1, 1)
credits_button = Button('credits_button.png', 1033, 402.7, 1)
back_to_menu_button = Button('back_to_menu_button.png', 20, 20, 1)
back_to_game_button = Button('back_to_game.png', 20, 20, 1)
play_again_game_over_button = Button('play_again_button.png', 430, 390, 1)
scoreboard_game_over_button = Button('scoreboard_button.png', 740, 310, 1)
exit_game_game_over_button = Button('exit_game_button.png', 675, 390, 1)
back_to_menu_game_over_button = Button('back_to_menu_button.png', 350, 310, 1)

# Definir os sliders e botões no início do código
musica_slider = Slider(650, 215, 300, 0, 100, 50)
efeitos_slider = Slider(650, 315, 300, 0, 100, 50)
brilho_slider = Slider(650, 535, 300, 0, 100, 50)

# Inicializar valores padrão
volume_music = 50
volume_effects = 50
brightness = 50
fps = 60  # Definido inicialmente para 60Hz

#dropdown de seleção para a taxa de atualização	
dropdown_options = ['30 hz', '60 hz', '120 hz', '144 hz']
dropdown = Dropdown(695, 405, 150, 40, dropdown_options)

# Pause Screen button (ps)
ps_play_button = Button('play_button.png', 520, 200, 0.8)
ps_options = Button('options_button.png', 520, 300, 0.8)
ps_back_to_menu_button = Button('back_to_menu_button.png', 515, 400, 0.8)
ps_exit_game = Button('exit_game_button.png', 520, 500, 0.8)

player_sprite = pygame.sprite.Group()
invader_group = pygame.sprite.Group()
invader_fire = pygame.sprite.Group()
player_fire = pygame.sprite.Group()
special_invader_group = pygame.sprite.GroupSingle()
explosion_group = pygame.sprite.Group()

# Eventos
INVADERFIRE = pygame.USEREVENT + 1
pygame.time.set_timer(INVADERFIRE, 1000) # frequencia de tiros dos invaders em millisegundos 

SPECIALINVADER = pygame.USEREVENT + 2
pygame.time.set_timer(SPECIALINVADER, randint(5000, 20000))

clock = pygame.time.Clock()

pause_screen = False

pygame.font.init()
font = pygame.font.Font(join('font', 'pixeled.ttf'), 20)

# Configurações das vidas do jogador.
lifes_left = 5
lifes_left_image = pygame.image.load(join('images', 'vida_coracao.png')).convert_alpha()
coordinate_x_lifes = 1240

# Configurações dos obstáculos.
coordinate_x_obstacles = 1050