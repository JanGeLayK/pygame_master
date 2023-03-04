import pygame
import pyautogui

(width, height) = pyautogui.size()
pl = pygame.Surface((40, 40))
pl.fill((210, 120, 60))
FPS = 60
timer = pygame.time.Clock()
bg = (1, 238, 255)

game_over = 0