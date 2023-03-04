import platform
import random

import pygame
from platforms import Platform
from settings import width, height, bg, FPS, timer, game_over
from levels import level_1
from classes import Player, Camera
from functions import camera_func
from enemy import Enemy


pygame.init()

game_over_file = pygame.image.load('Sprite/over.png')
game_over_img = pygame.transform.scale(game_over_file, (255, 250))
pygame.mixer.pre_init(44100, -16, 2, 2048)

pygame.init()

pygame.mixer.init()
pygame.mixer.music.load('music/117244.mp3')
pygame.mixer.music.play(-1)



window = pygame.display.set_mode((width, height))

player = Player(55, 55)

total_level_width = len(level_1[0]) * 40

total_level_height = len(level_1) * 40
camera = Camera(camera_func, total_level_width, total_level_height)



platforms = []
enemys = []

monsters = pygame.sprite.Group()

left = right = up = False

sprite_group = pygame.sprite.Group()
sprite_group.add(player)



x = 0
y = 3

for row in level_1:
    for coll in row:
        if coll == 1:
            pl = Platform(x, y)
            sprite_group.add(pl)
            platforms.append(pl)

        if coll == 2:
            enemy = Enemy(x, y - 20)
            monsters.add(enemy)
            enemys.append(enemy)

        x += 40
    y += 40
    x = 0




run = True
while run:

    timer.tick(FPS)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            quit()

        if game_over == 0:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_a:
                    left = True
                if e.key == pygame.K_d:
                    right = True
                if e.key == pygame.K_SPACE:
                    up = True

            if e.type == pygame.KEYUP:
                if e.key == pygame.K_a:
                    left = False
                if e.key == pygame.K_d:
                    right = False
                if e.key == pygame.K_SPACE:
                    up = False
    window.fill(bg)
    player.update(left, right, platforms, up)
    camera.update(player)
    monsters.update(platforms)

    for i in sprite_group:
        window.blit(i.image, camera.apply(i))
    for i in monsters:
        window.blit(i.image, camera.apply(i))

    pygame.display.update()

    if pygame.sprite.spritecollide(player, enemys, False):
        game_over = -1
        up = False
        left = False
        right = False
        while True:
            pass









