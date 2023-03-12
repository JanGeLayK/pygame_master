import pygame
pygame.init()
screen_width, screen_height = 500, 500
bg_color = (0, 128, 128)
clock = pygame.time.Clock()

# Создаем экран
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Menu')

class Button:
    """Класс для создания кнопок на экране"""

    def __init__(self, x, y, width, height, color, text=''):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.font = pygame.font.Font(None, height - 10)

    def draw(self, surface, outline=None):
        if outline:
            pygame.draw.rect(surface, outline, self.rect, 2)

        pygame.draw.rect(surface, self.color, self.rect)

        if self.text:
            text = self.font.render(self.text, True, (255, 255, 255))
            text_rect = text.get_rect()
            text_rect.center = self.rect.center
            surface.blit(text, text_rect)

    def is_pressed(self, pos):
        return self.rect.collidepoint(pos)

# Создаем кнопки
start_btn = Button(100, 100, 100, 50, 'LimeGreen', 'Start')
control_btn = Button(100, 200, 165, 50, '#FF00FF', 'Управление')
exit_btn = Button(100, 300, 100, 50, (255, 0, 0), 'Exit')

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_btn.is_pressed(pygame.mouse.get_pos()):
                print('start game')
            elif control_btn.is_pressed(pygame.mouse.get_pos()):
                print('open controls')
            elif exit_btn.is_pressed(pygame.mouse.get_pos()):
                running = False

    screen.fill(bg_color)
    start_btn.draw(screen, (255, 255, 255))
    control_btn.draw(screen, (255, 255, 255))
    exit_btn.draw(screen, (255, 255, 255))

    pygame.display.update()
    clock.tick(60)

pygame.quit()