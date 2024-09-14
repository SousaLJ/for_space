import pygame

from config import *
from os.path import join
from pygame.sprite import Sprite

def create_obstacles():
    """Cria os obstáculos e os adiciona ao grupo de sprites"""
    for obstacle in range(4):
        for x in range(0, 180, 5):
            for y in range(0, 60, 5):
                if 463 + y >= 496 and 66 <= 33 + x <= 170:
                    continue
                # Cria um novo obstáculo e adiciona ao grupo
                obs = Obstacle(5, 342 * obstacle + 33 + x, 463 + y)
                obstacle_group.add(obs)

class Obstacle(Sprite):
    """Classe para representar cada obstáculo"""

    def __init__(self, size, x, y):
        """Inicializa o sprite do obstáculo e define sua posição"""
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.obstacles_amount = 4