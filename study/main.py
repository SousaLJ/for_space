# Example file showing a basic pygame "game loop"
import pygame
from os.path import join
from random import randint

# pygame setup
pygame.init()

LARGURA_TELA = 1280
ALTURA_TELA = 720

display = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA), pygame.SCALED | pygame.RESIZABLE)
pygame.display.set_caption("for_invaders")
pygame.display.set_icon(pygame.image.load(join("images", "logo.png")))
running = True
x = 100

nave_surf = pygame.image.load(join("images", "nave.png")).convert_alpha()
nave_surf = pygame.transform.scale(nave_surf, (100, 100))
nave_rect = nave_surf.get_rect(center = (LARGURA_TELA / 2, ALTURA_TELA / 2))
boss3_surf = pygame.image.load(join("images", "boss3.png")).convert_alpha()
boss3_pos = [(randint(0, LARGURA_TELA), randint(0, ALTURA_TELA)) for i in range(20)]

while running:
    # enquanto o jogo esta rodando procuramos por eventos
    
    for event in pygame.event.get():
        # pygame.QUIT event significa que o usuario fechou a janela no X
        if event.type == pygame.QUIT:
            running = False
        
        # if event.type == pygame.VIDEORESIZE:
        #    new_size = (event.w, event.h)
        #    display = pygame.display.set_mode(new_size, pygame.SCALED + pygame.RESIZABLE)

    # fundo com a cor da for_code
    display.fill("#1E1647")
    
    for pos in boss3_pos:
        display.blit(boss3_surf, pos)
    display.blit(nave_surf, nave_rect)
    nave_rect.left += 1
    
    # RENDER YOUR GAME HERE
    
    # update the display
    pygame.display.update()


pygame.quit()