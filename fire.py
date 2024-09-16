from pygame.sprite import Sprite
from utils import surface_load
from os.path import join
from config import ALTURA_TELA
import pygame


class Fire(Sprite):
  def __init__(self, pos, speed, groups) -> None:
    super().__init__(groups)
    self.image = surface_load(join("images", "fire.png"), True, (30, 30))
    # fiz dessa forma pois unica diferença de tiro é o "speed"
    # que, quando positivo = player, negativo = invader
    if speed < 0:
      self.image = pygame.transform.rotate(self.image, 180)

    self.rect = self.image.get_rect(center = pos)
    self.speed = speed
    
  def destroy(self):
     if self.rect.y <= -50 or self.rect.y >= ALTURA_TELA + 50:
        self.kill()

  def update(self):
    self.rect.y -= self.speed
    self.destroy()

class Explosion(Sprite):
    def __init__(self, position):
      super().__init__()
      self.image = pygame.image.load(join('images', 'lil_explosion.png'))
      self.rect = self.image.get_rect(center=(position))
      self.counter = 0

    def update(self):
      self.counter += 1
      if self.counter > 15:
        self.kill()
        self.counter = 0