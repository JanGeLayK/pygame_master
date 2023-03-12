from pygame.sprite import Sprite
from pygame.image import load


class Banana(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = load('Sprite/ban.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y