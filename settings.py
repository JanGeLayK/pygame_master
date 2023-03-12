import pygame
import pyautogui

(width, height) = (1360, 760)

pl = pygame.Surface((40, 40))
pl.fill((210, 120, 60))
FPS = 60
timer = pygame.time.Clock()
bg = (1, 238, 255)

game_over = 0
sun = pygame.image.load('Sprite/png-transparent-yelow.png')
sun = pygame.transform.scale(sun, (150, 155))
square = pygame.image.load('Sprite/scuare.png')
square = pygame.transform.scale(square, (100, 100))