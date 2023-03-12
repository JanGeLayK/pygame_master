import pygame


class Button:
    """Класс для создания кнопок на экране"""

    def __init__(self, x, y, width, height, color, text=''):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.font = pygame.font.Font(None, height - 10)

    def draw(self, surface, outline=None):
        if outline:
            pygame.draw.rect(surface, outline, self.rect, 2)

        pygame.draw.rect(surface, self.color, self.rect)

        if self.text:
            text = self.font.render(self.text, True, (255, 255, 255))
            text_rect = text.get_rect()
            text_rect.center = self.rect.center
            surface.blit(text, text_rect)

    def is_pressed(self, pos):
        return self.rect.collidepoint(pos)