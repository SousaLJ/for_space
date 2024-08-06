import pygame

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.zoom_scale = 1.2

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        # Verifica se o mouse está sobre o botão
        if self.rect.collidepoint(pos):
            # Tive que pegar os valores novos de largura (referentes a imagem já redimensionada pela função scale)
            width = self.image.get_width()
            height = self.image.get_height()
            hovered_image = pygame.transform.scale(self.image, (int(width * self.zoom_scale), int(height * self.zoom_scale)))
            zoomed_rect = hovered_image.get_rect(center=self.rect.center)

            surface.blit(hovered_image, zoomed_rect.topleft)

            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True
        else:
            surface.blit(self.image, self.rect.topleft)

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action
