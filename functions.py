import pygame
from settings import width, height


def camera_func(camera, target_rect):
    l = -target_rect.x + width / 2
    t = -target_rect.y + height / 2
    w, h = camera.width, camera.height
    l = min(0, l)
    l = max(-(camera.width - width), l)
    t = max(-(camera.height - height), t)
    t = min(0, t)
    return pygame.Rect(l, t, w, h)








