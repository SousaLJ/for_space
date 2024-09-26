import pygame
from os.path import join
from utils import surface_load
from pygame.sprite import Sprite
from config import *
from fire import Fire

def create_player():
  return Player((ALTURA_TELA-80, LARGURA_TELA / 2), player_sprite)
  
class Player(Sprite):
  def __init__(self, pos, groups):
    super().__init__(groups)
    self.image = surface_load(join("images", "nave.png"), True, (80, 80))
    self.rect = self.image.get_rect(center = pos)
    self.speed = 8
    
    # cooldown
    self.can_shoot = True
    self.check_shoot_cooldown = 0
    self.cooldown = 350

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
    
    # se D (ou -->) pressionado (1 - 0) = 1, se A (ou <--) pressionado (0 - 1) = -1, se A (ou <--) e D (ou -->) pressionados (1 - 1) = 0
    self.direcao[0] = (int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])) or (int(keys[pygame.K_d]) - int(keys[pygame.K_a]))

    # Semelhante à linha anterior, porém é necessário que o valor retornado tenha o sinal trocado, a fim de que a movimentação não fique invertida.
    self.direcao[1] = -((int(keys[pygame.K_UP]) - int(keys[pygame.K_DOWN])) or int(keys[pygame.K_w]) - int(keys[pygame.K_s]))
  
    self.rect.center += self.direcao * self.speed      # dt em fase de testes ainda
    
    self.mask = pygame.mask.from_surface(self.image)
    
    if self.rect.left <= 0:
      self.rect.left = 0
    
    if self.rect.right >= LARGURA_TELA:
      self.rect.right = LARGURA_TELA
    
    if self.rect.bottom >= ALTURA_TELA:
      self.rect.bottom = ALTURA_TELA

    if self.rect.top <= 0:
      self.rect.top = 0
      
    # fire
    if (keys[pygame.K_SPACE]) and self.can_shoot:
      Fire(self.rect.midtop, 10, player_fire)
      som_shoot.play()
      self.can_shoot = False
      self.check_shoot_cooldown = pygame.time.get_ticks()
      
    self.fire_timer()