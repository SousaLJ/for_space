import pygame
from os.path import join

pygame.init()

def surface_load(path: str, transparente: bool = False, size: tuple = (0,0)) -> pygame.Surface:
  """
    Carrega uma imagem e a redimensiona, se necessário.

    str, bool, tuple -> pygame.Surface
    Args:
        path (str): O caminho para o arquivo de imagem.
        transparente (bool): Define se a imagem tem transparência (True) ou não (False).
        size (tuple): Tamanho para redimensionar a imagem (largura, altura). 
                      Se (0, 0), a imagem não será redimensionada.

    Returns:
        pygame.Surface: A superfície da imagem carregada e possivelmente redimensionada.
    """
  if transparente:
    surface = pygame.image.load(path).convert_alpha()
  else:
    surface = pygame.image.load(path).convert()
  
  if size != (0,0):
    surface = pygame.transform.scale(surface, size)
    
  return surface

LARGURA_TELA = 1600
ALTURA_TELA = 900

display_surf = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA), pygame.SCALED | pygame.RESIZABLE)
universo_surf = surface_load(join("images", "universo.png"), size=display_surf.get_size())

player_surf = surface_load(join("images", "nave.png"), True, (80, 80))
player = player_surf.get_rect(center = (LARGURA_TELA / 2, ALTURA_TELA * 0.80))

pygame.display.set_caption("ex rect")
pygame.display.set_icon(pygame.image.load(join("images", "logo.png")))

direcao = 1
running = True

while running:
  for events in pygame.event.get():
    if events.type == pygame.QUIT:
      running = False
  
  display_surf.fill("#1E1647")
  display_surf.blit(universo_surf, (0,0))
  
  display_surf.blit(player_surf, player)
  
  player.x += direcao
  if player.right >= LARGURA_TELA or player.left <= 0:
    direcao *= -1
  
  pygame.display.update()
  
pygame.quit()