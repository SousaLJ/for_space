import pygame

class Slider():
    def __init__(self, x, y, width, min_val, max_val, initial_val):
        # Cria uma superfície para o slider, mas o fundo será desenhado diretamente no surface passado
        self.rect = pygame.Rect(x, y, width, 20)
        self.min_val = min_val
        self.max_val = max_val
        self.current_val = initial_val

        # Calcula a posição inicial do slider com base em initial_val
        initial_pos = (initial_val - self.min_val) / (self.max_val - self.min_val) * (self.rect.width - 10)
        self.slider_rect = pygame.Rect(x + initial_pos, y - 5, 10, 30)  # Ajusta a posição do slider
        self.grabbed = False

    def draw(self, surface):
        # Desenha o fundo branco e a parte do slider no surface
        pygame.draw.rect(surface, 'white', self.rect)  # Fundo branco
        pygame.draw.rect(surface, 'white', (self.rect.x, self.rect.y + 10, self.rect.width, 10))  # Linha branca do slider
        pygame.draw.rect(surface, 'purple', self.slider_rect)  # Slider roxo
        
        # Verifica se o mouse está sobre o slider
        mouse_pos = pygame.mouse.get_pos()
        if self.slider_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            self.grabbed = True
        elif not pygame.mouse.get_pressed()[0]:
            self.grabbed = False

        # Atualiza a posição do slider se estiver sendo arrastado
        if self.grabbed:
            self.slider_rect.x = min(max(mouse_pos[0] - 5, self.rect.x), self.rect.x + self.rect.width - 10)
            self.current_val = self.min_val + ((self.slider_rect.x - self.rect.x) / (self.rect.width - 10)) * (self.max_val - self.min_val)

        return self.current_val

