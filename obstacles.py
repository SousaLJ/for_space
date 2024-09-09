import pygame

from os.path import join
from pygame.sprite import Sprite

class Obstacles(Sprite):
    """Classe para representar cada obstáculo"""

    def __init__(self, coordinate_x, coordinate_y):
        """Inicializa o obstáculo e define sua posição inicial"""
        super().__init__()
        
        # Carrega a imagem do obstáculo e define seu atributo rect
        self.image = pygame.image.load(join('images', 'obstaculos.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (coordinate_x, coordinate_y)