import random

import pygame
from pygame.sprite import Sprite, collide_rect
from pygame import Surface
import pyganim

MOVE_SPEED = 7
GRAVITY = 0.4
JUMP_POWER = 10
ANIMATION_DELAY = 100

ANIMATION_STAY = [('Sprite/idle.png', ANIMATION_DELAY)]

ANIMATION_RIGHT = ['Sprite/right_1.png',
                   'Sprite/right_2.png',
                   'Sprite/right_3.png',
                   'Sprite/right_4.png',
                   'Sprite/right_5.png',
                   'Sprite/right_6.png'
                   ]

ANIMATION_LEFT = ['Sprite/left_1.png',
                   'Sprite/left_2.png',
                   'Sprite/left_3.png',
                   'Sprite/left_4.png',
                   'Sprite/left_5.png',
                   'Sprite/left_6.png'
                   ]



class Player(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = Surface((60, 71))
        self.x_vel = 0
        self.y_vel = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.banana = 0
        self.onGround = False
        self.image.set_colorkey((1, 238, 255))
        self.boltAnimStay = pyganim.PygAnimation(ANIMATION_STAY)
        self.boltAnimStay.play()

        self.stay_counter = 0
        boltAnimRight = []
        for anim in ANIMATION_RIGHT:
            boltAnimRight.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnimRight)
        self.boltAnimRight.play()
        boltAnimLeft = []
        for anim in ANIMATION_LEFT:
            boltAnimLeft.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnimLeft)
        self.boltAnimLeft.play()

    def update(self, left, right, platforms, up):
        if left:
            self.x_vel = -MOVE_SPEED
            self.image.fill((1, 238, 255))
            self.boltAnimLeft.blit(self.image, (0, 0))
        if right:
            self.x_vel = MOVE_SPEED
            self.image.fill((1, 238, 255))
            self.boltAnimRight.blit(self.image, (0, 0))
        if not (left or right):
            self.x_vel = 0
            if not up:
                self.image.fill((1, 238, 255))
                self.boltAnimStay.blit(self.image, (0, 0))



        if not self.onGround:
            self.y_vel += GRAVITY
        if up:
            if self.onGround:
                self.y_vel = -JUMP_POWER
        self.onGround = False
        self.rect.x += self.x_vel
        self.collide(self.x_vel, 0, platforms)
        self.rect.y += self.y_vel
        self.collide(0, self.y_vel, platforms)



    def collide(self, x_vel, y_vel, platforms):
        for pl in platforms:
            if collide_rect(self, pl):
                if x_vel > 0:
                    self.rect.right = pl.rect.left
                if x_vel < 0:
                    self.rect.left = pl.rect.right
                if y_vel > 0:
                    self.rect.bottom = pl.rect.top
                    self.onGround = True
                    self.y_vel = 0
                if y_vel < 0:
                    self.rect.top = pl.rect.bottom
                    self.y_vel = 0


class Camera:
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)









