import pygame
from os.path import join
from utils import surface_load
from pygame.sprite import Sprite
# from window import LARGURA_TELA


class Player(Sprite):
  def __init__(self, x, y, groups):
    super().__init__(groups)
    self.image = surface_load(join("images", "nave.png"), True, (80, 80))
    self.rect = self.image.get_rect(center = (x,y))
    self.speed = 5
    
  def update(self):
    
    self.direcao = pygame.math.Vector2()
    self.keys = pygame.key.get_pressed()
    
    self.direcao.x = int(self.keys[pygame.K_d]) - int(self.keys[pygame.K_a])
    # self.direcao.y = int(self.keys[pygame.K_s]) - int(self.keys[pygame.K_w])

    # self.direcao = self.direcao.normalize() if self.direcao else self.direcao
  
    self.rect.center += self.direcao * self.speed
    if self.rect.left <= 0:
      self.rect.left = 0
    
    if self.rect.right >= 1280:
      self.rect.right = 1280
    
    
  # def fire(self):
  #   current_time = time.time()
  #   if self.keys[pygame.K_SPACE] and current_time - self.tempo_ultimo_tiro >= 1:
  #     print("fire laser")
  #     self.tempo_ultimo_tiro = current_time