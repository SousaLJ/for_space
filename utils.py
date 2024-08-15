import pygame

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