from pygame.sprite import Sprite
from pygame.image import load



class Enemy(Sprite):
    def __init__(self, x, y):
        super(Enemy, self).__init__()
        self.image = load('Sprite/der.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0



    def update(self, monster):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if monster == True:
            if abs(self.move_counter) > 50:
                self.move_direction *= -1
                self.move_counter *= -1
        else:
            self.move_direction = 0
            self.move_counter = 0
