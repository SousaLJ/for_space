from pygame.sprite import Sprite
from utils import surface_load
from os.path import join
from config import ALTURA_TELA
import pygame


class Fire(Sprite):
  def __init__(self, pos, speed, groups) -> None:
    super().__init__(groups)
    self.image = surface_load(join("images", "fire.png"), True, (45, 45))
    self.rect = self.image.get_rect(center = pos)
    self.speed = speed
    
  def update(self):
    self.rect.y -= self.speed
    if self.rect.top >= ALTURA_TELA:
      self.kill()
      


class InvaderFire(Sprite):
    def __init__(self, pos, speed):
        super().__init__()
        self.image = surface_load(join('images', 'fire.png'), True, (40, 40))
        self.image = pygame.transform.rotate(self.image, 180)  # Rotaciona a imagem em 180 graus
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed

    def update(self):
       self.rect.y -= self.speed
       if self.rect.y <= -50:
          self.kill()

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