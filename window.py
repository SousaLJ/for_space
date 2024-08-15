from typing import Any
import pygame
import button
import random
from sys import exit
from os.path import join

class Invaders(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        invader_type = random.randint(0,1)
        if invader_type == 0:
            frame1_invader0 = pygame.image.load(join('images', 'frame1_invader0.png')).convert_alpha()
            frame2_invader0 = pygame.image.load(join('images', 'frame2_invader0.png')).convert_alpha()
            self.frames = [frame1_invader0, frame2_invader0]
            self.x = x
            self.y = y

        else:
            frame1_invader0 = pygame.image.load(join('images', 'frame1_invader0.png')).convert_alpha()
            frame2_invader0 = pygame.image.load(join('images', 'frame2_invader0.png')).convert_alpha()
            self.frames = [frame1_invader0, frame2_invader0]
            self.x = x
            self.y = y

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.direction = 1

    def animation_state(self):
        self.animation_index += 0.02
        if self.animation_index >= len(self.frames): 
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x += self.direction


pygame.init()

clock = pygame.time.Clock()
fps = 60

pygame.display.set_caption("for_invaders")
pygame.display.set_icon(pygame.image.load(join("images", "logo.png")))

LARGURA_TELA = 1280
ALTURA_TELA = 720
display = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA), pygame.SCALED | pygame.RESIZABLE)
rows = 5
cols = 13

# Telas
menu_background = pygame.image.load(join('images', 'logo_redimensionado.png')).convert()
ingame_background = pygame.image.load(join('images', 'universo.png'))
credits_background = pygame.image.load(join('images', 'credits_bg.png'))
game_over_background = pygame.image.load(join('images', 'game_over_screen_sem_botoes.png'))

# Instanciando botão
play_button = button.Button('play.png', 261.93, 335.39, 0.8)
scoreboard_button = button.Button('scoreboard.png', 445.63, 382.39, 0.8)
options_button = button.Button('options.png', 714.67, 377.39, 0.8)
credits_button = button.Button('credits.png', 898.37, 329.39, 0.8)
btm_button = button.Button('btm_img.png', 20, 20, 1)
play_again_game_over_button = button.Button('play_again.png', 410, 370, 1)
back_to_menu_game_over_button = button.Button('back_to_menu.png', 330, 295, 1)
scoreboard_game_over_button = button.Button('scoreboard_game_over.png', 740, 290, 1)
exit_game_game_over_button = button.Button('exit_game.png', 652, 370, 1)

# invaders
invader_group = pygame.sprite.Group()
            
def create_invaders():
    for row in range(rows):
        for item in range(cols):
            invader = Invaders(100 + item * 65, 50 + row * 70)
            invader_group.add(invader)

create_invaders()

def check_invader_position():
    change_direction = False
    all_invaders = invader_group.sprites()
    for invader in all_invaders:
        if invader.rect.right >= LARGURA_TELA or invader.rect.left <= 0:
            change_direction = True
            break

    if change_direction:
        for invader in all_invaders:
            invader.direction *= -1
            invader.rect.y += 10


running = True

game_state = 'menu'

while running:
    clock.tick(fps)
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

        elif options_button.draw(display):
            game_state = 'menu_options'

        elif play_button.draw(display):
            print('clicked')
            game_state = 'playing'

        elif credits_button.draw(display):
            game_state = 'menu_credits'

    elif game_state == 'menu_scoreboard':
        if btm_button.draw(display):
            game_state = 'menu'
        

    elif game_state == 'playing':
        display.blit(ingame_background, (0, 0)) # Comentado com o propósito de testar a tela de fim de jogo
        invader_group.update()
        invader_group.draw(display)
        check_invader_position()


        # Pinta no fundo a tela de fim de jogo.
        # display.blit(game_over_background, (0, 0))

        # Verifica se o botão de jogar novamente foi pressionado
        # if play_again_game_over_button.draw(display):
        #     game_state == 'playing'
        
        # # Verifica se o botão de voltar para o menu foi pressionado
        # elif back_to_menu_game_over_button.draw(display):
        #     game_state = 'menu'
        
        # # Verifica se o botão de mostrar o scoreboard foi pressionado
        # elif scoreboard_game_over_button.draw(display):
        #     game_state = 'menu_scoreboard'
        
        # # Verifica se o botão de sair do jogo foi pressionado
        # elif exit_game_game_over_button.draw(display):
        #     pygame.quit()
        #     exit()

    elif game_state == 'menu_credits':
        display.blit(credits_background, (0, 0))
        if btm_button.draw(display):
            game_state = 'menu'

    else:
        pass

    
    pygame.display.update()