import pygame
import random
from config import *
from os.path import join

def create_invaders():
    for row in range(rows):
        for item in range(cols):
            invader = Invaders(100 + item * 65, 50 + row * 70)
            invader_group.add(invader)

def check_invader_position():
    change_direction = False
    all_invaders = invader_group.sprites()
    for invader in all_invaders:
        if invader.rect.right >= LARGURA_TELA or invader.rect.left <= 0:
            change_direction = True
            break

    if change_direction:
        for invader in all_invaders:
            invader.direction *= -1
            invader.rect.y += 10
 
class Invaders(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        invader_type = random.randint(0,1)
        if invader_type == 0:
            frame1_invader0 = pygame.image.load(join('images', 'frame1_invader0.png')).convert_alpha()
            frame2_invader0 = pygame.image.load(join('images', 'frame2_invader0.png')).convert_alpha()
            self.frames = [frame1_invader0, frame2_invader0]
            self.x = x
            self.y = y

        else:
            frame1_invader0 = pygame.image.load(join('images', 'frame1_invader0.png')).convert_alpha()
            frame2_invader0 = pygame.image.load(join('images', 'frame2_invader0.png')).convert_alpha()
            self.frames = [frame1_invader0, frame2_invader0]
            self.x = x
            self.y = y

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.direction = 1

    def animation_state(self):
        self.animation_index += 0.02
        if self.animation_index >= len(self.frames): 
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x += self.direction