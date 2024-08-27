import pygame
from os.path import join
from utils import surface_load
from pygame.sprite import Sprite
from config import *
from fire import Fire

def create_player():
  return Player((ALTURA_TELA / 2, LARGURA_TELA / 2), player_sprite)
  
class Player(Sprite):
  def __init__(self, pos, groups):
    super().__init__(groups)
    self.image = surface_load(join("images", "nave.png"), True, (80, 80))
    self.rect = self.image.get_rect(center = pos)
    self.speed = 4
    
    # cooldown
    self.can_shoot = True
    self.check_shoot_cooldown = 0
    self.cooldown = 500

  # timer para o tiro, baseado no cooldown
  def fire_timer(self):
    if not self.can_shoot:
      current_time = pygame.time.get_ticks()
      if current_time - self.check_shoot_cooldown >= self.cooldown:   # se concluiu o cooldown
        self.can_shoot = True

  def update(self):
    
    # utilizamos vetores para tratar do movimento do Player
    self.direcao = pygame.math.Vector2()
    
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()
    
    # se D pressionado (1 - 0) = 1, se A pressionado (0 - 1) = -1, se A e D pressionados (1 - 1) = 0
    self.direcao.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
  
    self.rect.center += self.direcao * self.speed * dt        # dt em fase de testes ainda
    
    self.mask = pygame.mask.from_surface(self.image)
    
    if self.rect.left <= 0:
      self.rect.left = 0
    
    if self.rect.right >= LARGURA_TELA:
      self.rect.right = LARGURA_TELA
      
    # fire
    if (keys[pygame.K_SPACE] or mouse[0]) and self.can_shoot:
      player_sprite.add(Fire(self.rect.midtop, 10, player_sprite))
      self.can_shoot = False
      self.check_shoot_cooldown = pygame.time.get_ticks()
      
    self.fire_timer()