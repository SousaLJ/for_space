import pygame, time
from utils import *
from os.path import join
from pygame.sprite import Sprite

class Game:
  LARGURA_TELA = 1280
  ALTURA_TELA = 720
  
  def __init__(self) -> None:
    pygame.init()
    
    
    self.display = pygame.display.set_mode((self.LARGURA_TELA, self.ALTURA_TELA), pygame.SCALED | pygame.RESIZABLE)
    self.fundo = surface_load(join("images", "universo.png"), size= self.display.get_size())
    

    
    pygame.display.set_caption("studying classes")
    pygame.display.set_icon(pygame.image.load(join("images", "logo.png")))
    
    pygame.mouse.set_visible(True)

    self.clock = pygame.time.Clock()
        

    self.running = True
    self.tempo_ultimo_tiro = 0
    

  # def atirar_player(self):
  #   current_time = time.time()
  #   if self.keys[pygame.K_SPACE] and current_time - self.tempo_ultimo_tiro >= 1:
  #     print("fire laser")
  #     self.tempo_ultimo_tiro = current_time

  def desenhar_fundo(self):
    self.display.fill("#1E1647")
    self.display.blit(self.fundo, (0,0))

  def run(self):

    while self.running:
      self.dt = self.clock.tick()

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False

      self.desenhar_fundo()
      self.player.movimento_player()
      pygame.display.update()
    pygame.quit()

class Player(Sprite):
  def __init__(self, ) -> None:
    super().__init__()
    self.image = surface_load(join("images", "nave.png"), True, (80,80))
    self.rect = self.image.get_rect(center= ())
    self.speed = 0.5

  def movimento_player(self):
    self.direcao = pygame.math.Vector2()
    self.keys = pygame.key.get_pressed()
    
    self.direcao.x = int(self.keys[pygame.K_d]) - int(self.keys[pygame.K_a])
    self.direcao.y = int(self.keys[pygame.K_s]) - int(self.keys[pygame.K_w])

    self.direcao = self.direcao.normalize() if self.direcao else self.direcao
  
    self.rect.center += self.direcao * self.speed * self.dt
    

if __name__ == "__main__":
  jogo = Game()
  jogo.run()