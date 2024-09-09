import pygame
from pygame.locals import *

pygame.init()

font_path = 'font\pixeled.ttf'
font = pygame.font.Font(font_path, 12)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

class Dropdown:
    def __init__(self, x, y, width, height, options, index_selecionado=0):
        self.rect = pygame.Rect(x, y, width, height)
        self.options = options
        self.index_selecionado = index_selecionado
        self.is_open = False

    def draw(self, screen):
        pygame.draw.rect(screen, GRAY if self.is_open else WHITE, self.rect, 0)
        pygame.draw.rect(screen, BLACK, self.rect, 2)

        # Texto da opção selecionada
        text = font.render(self.options[self.index_selecionado], True, BLACK)
        screen.blit(text, (self.rect.x + 5, self.rect.y + 5))

        if self.is_open:
            for i, option in enumerate(self.options):
                option_rect = pygame.Rect(self.rect.x, self.rect.y + (i+1) * self.rect.height, self.rect.width, self.rect.height)
                pygame.draw.rect(screen, WHITE, option_rect, 0)
                pygame.draw.rect(screen, BLACK, option_rect, 2)

                option_text = font.render(option, True, BLACK)
                screen.blit(option_text, (option_rect.x + 5, option_rect.y + 5))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.is_open = not self.is_open
            elif self.is_open:
                for i in range(len(self.options)):
                    option_rect = pygame.Rect(self.rect.x, self.rect.y + (i+1) * self.rect.height, self.rect.width, self.rect.height)
                    if option_rect.collidepoint(event.pos):
                        self.index_selecionado = i
                        self.is_open = False
                        break
                else:
                    self.is_open = False