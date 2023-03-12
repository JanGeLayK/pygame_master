from pygame.sprite import Sprite
from pygame.image import load
from pygame.transform import scale


class Dor(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.img = load('Sprite/door.png')
        self.image = scale(self.img, (110, 120))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0