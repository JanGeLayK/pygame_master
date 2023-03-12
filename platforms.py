from pygame.sprite import Sprite
from pygame.image import load


class Platform(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = load('Sprite/pl.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class MovingPlatform(Platform):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = load('Sprite/pl.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 200:
            self.move_direction *= -1
            self.move_counter *= -1



