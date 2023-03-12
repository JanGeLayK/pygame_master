import pygame
pygame.init()

window = pygame.display.set_mode((200, 200), pygame.RESIZABLE)
virtual_window = pygame.Surface((200, 200))
current_size = window.get_size()
image = pygame.image.load('Sprite/player.png')

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif e.type == pygame.VIDEORESIZE:
            current_size = e.size
    virtual_window.fill((0, 0, 0))
    virtual_window.blit(image, (100, 100))
    scaled_surface = pygame.transform.scale(virtual_window, current_size)
    window.blit(scaled_surface, (0, 0))
    pygame.display.flip()
    pygame.display.update()