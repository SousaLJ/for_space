import pygame
import random
from config import *
from os.path import join
from fire import Fire

def create_invaders(nivel):
    for row in range(rows):
        for item in range(cols):
            invader = Invaders(100 + item * 65, 100 + row * 70, nivel)
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

def invaders_fire(attack_speed):
    if invader_group.sprites():
        random_invader = random.choice(invader_group.sprites())
        fire = Fire(random_invader.rect.center, attack_speed, invader_fire)
        invader_fire.add(fire)

class Invaders(pygame.sprite.Sprite):
    def __init__(self, x, y, nivel):
        super().__init__()

        invader_type = random.randint(0,1)
        if invader_type == 0:
            frame1 = pygame.image.load(join('images', 'frame1_invader0.png')).convert_alpha()
            frame2 = pygame.image.load(join('images', 'frame2_invader0.png')).convert_alpha()
            self.frames = [frame1, frame2]
            self.x = x
            self.y = y

        else:
            frame1 = pygame.image.load(join('images', 'frame1_invader1.png')).convert_alpha()
            frame2 = pygame.image.load(join('images', 'frame2_invader1.png')).convert_alpha()
            self.frames = [frame1, frame2]
            self.x = x
            self.y = y

        self.reward = 100 if invader_type == 0 else 200 if invader_type == 1 else 0
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.direction = nivel

    def animation_state(self):
        self.animation_index += 0.04
        if self.animation_index >= len(self.frames): 
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)] 

    def update(self):
        self.animation_state()
        self.rect.x += self.direction

class SpecialInvader(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(join('images', 'frame1_invader1.png')).convert_alpha()
        
        self.reward = random.choice([150, 200, 250])
        screen_side = random.choice([LARGURA_TELA + 30, -30])
        if screen_side > 0:
            self.speed = -5
        else:
            self.speed = 5
        
        self.rect = self.image.get_rect(topleft=(screen_side, 50))

    def update(self):
        self.rect.x += self.speed