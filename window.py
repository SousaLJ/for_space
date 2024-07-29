import pygame
from os.path import join

pygame.init()

LARGURA_TELA = 1280
ALTURA_TELA = 720

display = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA), pygame.SCALED | pygame.RESIZABLE)
pygame.display.set_caption("for_invaders")
pygame.display.set_icon(pygame.image.load(join("images", "logo.png")))
running = True

while running:
    # enquanto o jogo esta rodando procuramos por eventos
    
    for event in pygame.event.get():
        # pygame.QUIT event significa que o usuario fechou a janela no X
        if event.type == pygame.QUIT:
            running = False

    # fundo com a cor da for_code
    display.fill("#1E1647")

    pygame.display.update()

pygame.quit()