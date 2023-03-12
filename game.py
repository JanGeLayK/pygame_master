import os
import pickle
import pygame
from banana import Banana
from platforms import Platform, MovingPlatform
from settings import width, height, bg, FPS, timer, game_over, sun
from levels import level_1, level_2, level_3, level_4
from classes import Player, Camera
from functions import camera_func
from enemy import Enemy
from dor import Dor
from button import Button



pygame.init()
pygame.font.init()
pygame.mixer.init()

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.music.load('music/117244.mp3')
pygame.mixer.music.set_volume(0.50)
pygame.mixer.music.play(-1)





window = pygame.display.set_mode((width, height), pygame.FULLSCREEN, pygame.RESIZABLE)
virtual_window = pygame.Surface((width, height))






def draw_text(surface, text, size, x, y, color):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_surface, text_rect)



# Создаем кнопки
start_btn = Button(100, 100, 100, 50, 'LimeGreen', 'Start')
control_btn = Button(100, 200, 165, 50, '#FF00FF', 'Управление')
exit_btn = Button(100, 300, 100, 50, (255, 0, 0), 'Exit')
restart_btn = Button(width//2.5, height//3, 350, 50, (255, 0, 0), 'Играть заново')
reset = Button(100, 400, 250, 50, 'orange', 'Сбросить уровни')

# Основной цикл программы
def menu():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if reset.is_pressed(pygame.mouse.get_pos()):
                    effect = pygame.mixer.Sound('music/button.mp3')
                    effect.play()
                    f = open('data/out.bin', 'w')
                    f.close()
                    f = open('data/banana.bin', 'w')
                    f.close()
                    res = True
                    while res:
                        window.fill(bg)
                        draw_text(window, f'Готово через 5 секунд жми Start', 50, window.get_width() / 2, window.get_height() / 2,
                                  (12, 0, 255))
                        pygame.display.update()
                        pygame.time.delay(3000)
                        res = False


                if start_btn.is_pressed(pygame.mouse.get_pos()):
                    effect = pygame.mixer.Sound('music/button.mp3')
                    effect.play()

                    player = Player(55, 55)


                    total_level_width = len(level_1[0]) * 40

                    total_level_height = len(level_1) * 40


                    camera = Camera(camera_func, total_level_width, total_level_height)

                    platforms = []
                    enemys = []

                    monsters = pygame.sprite.Group()

                    doors = pygame.sprite.Group()
                    doors_list = []
                    banana_group = pygame.sprite.Group()
                    banana_list = []

                    left = right = up = False

                    sprite_group = pygame.sprite.Group()
                    sprite_group.add(player)
                    plat_group = pygame.sprite.Group()

                    level_count = 0
                    level_levels = [level_1, level_2, level_3, level_4]

                    game_over = 0
                    monsters_move = True




                    try:
                        if os.path.exists("data/out.bin"):
                            with open("data/out.bin", "rb") as file:
                                bs = pickle.load(file)
                                level_count = bs
                        else:
                            level_count = level_count

                    except:
                        level_count = level_count


                    try:
                        if os.path.exists("data/banana.bin"):
                            with open("data/banana.bin", "rb") as file:
                                bs = pickle.load(file)
                                player.banana = bs
                        else:
                            player.banana = player.banana

                    except:
                        player.banana = player.banana


                    x = 0
                    y = 0

                    for row in level_levels[level_count]:
                        for coll in row:
                            if coll == 1:
                                pl = Platform(x, y)
                                sprite_group.add(pl)
                                platforms.append(pl)

                            if coll == 2:
                                pl1 = MovingPlatform(x, y)
                                plat_group.add(pl1)
                                platforms.append(pl1)


                            if coll == 3:
                                enemy = Enemy(x, y - 20)
                                monsters.add(enemy)
                                enemys.append(enemy)

                            if coll == 4:
                                banana = Banana(x, y)
                                banana_group.add(banana)
                                banana_list.append(banana)

                            if coll == 10:
                                door = Dor(x - 30, y - 75)
                                doors.add(door)
                                doors_list.append(door)

                            x += 40
                        y += 40
                        x = 0

                    current_size = window.get_size()

                    run = True
                    while run:

                        timer.tick(FPS)

                        for e in pygame.event.get():
                            if e.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                            if e.type == pygame.VIDEORESIZE:
                                current_size = e.size


                            if game_over == 0:
                                if e.type == pygame.KEYDOWN:
                                    if e.key == pygame.K_ESCAPE:
                                        menu()
                                    if e.key == pygame.K_a:
                                        left = True
                                    if e.key == pygame.K_d:
                                        right = True
                                    if e.key == pygame.K_SPACE:
                                        up = True

                                        effect = pygame.mixer.Sound('music/jump.mp3')
                                        effect.play()

                                if e.type == pygame.KEYUP:
                                    if e.key == pygame.K_a:
                                        left = False
                                    if e.key == pygame.K_d:
                                        right = False
                                    if e.key == pygame.K_SPACE:
                                        up = False
                        virtual_window.fill(bg)

                        virtual_window.blit(sun, (width - 150, 30))

                        player.update(left, right, platforms, up)
                        camera.update(player)
                        monsters.update(monsters_move)
                        plat_group.update()

                        if player.rect.x <= 100:
                            draw_text(virtual_window, f'Уровень {level_count + 1}', 50, window.get_width() / 2,
                                      window.get_height() / 5,
                                      (12, 0, 255))

                        for i in sprite_group:
                            virtual_window.blit(i.image, camera.apply(i))
                        for i in plat_group:
                            virtual_window.blit(i.image, camera.apply(i))
                        for i in monsters:
                            virtual_window.blit(i.image, camera.apply(i))
                        if not banana_list:
                            for i in doors:
                                virtual_window.blit(i.image, camera.apply(i))




                        for i in banana_list:
                            virtual_window.blit(i.image, camera.apply(i))
                        draw_text(virtual_window, f'Бананы: {player.banana}', 30, 100, 50,
                                  (12, 0, 255))
                        scaled_surface = pygame.transform.scale(virtual_window, current_size)
                        window.blit(scaled_surface, (0, 0))

                        pygame.display.update()



                        if pygame.sprite.spritecollide(player, enemys, False):
                            effect = pygame.mixer.Sound('music/game_over.mp3')
                            effect.play()
                            pygame.mixer.music.set_volume(0)
                            game_over = -1
                            monsters_move = False
                            left = right = up = False

                            draw_text(virtual_window, f'Game over', 50, window.get_width() / 2, window.get_height() / 2,
                                      (12, 0, 255))
                            scaled_surface = pygame.transform.scale(virtual_window, current_size)
                            window.blit(scaled_surface, (0, 0))
                            pygame.display.update()

                            pygame.time.delay(2500)
                            menu()

                        else:
                            pygame.mixer.music.set_volume(0.50)




                        if pygame.sprite.spritecollide(player, banana_group, False):
                            collided_bananas = pygame.sprite.spritecollide(player, banana_group, False)
                            for banana in collided_bananas:
                                if banana in banana_list:
                                    banana_list.remove(banana)
                                    player.banana += 1
                                    effect = pygame.mixer.Sound('music/banana.mp3')
                                    effect.play()
                            draw_text(virtual_window, f'Бананы: {player.banana}', 30, 100, 50,
                                      (12, 0, 255))




                        if not banana_list and pygame.sprite.spritecollide(player, doors, False):

                            up = False
                            left = False
                            right = False
                            level_count += 1
                            with open("data/out.bin", "wb") as file:
                                pickle.dump(level_count, file)
                            with open("data/banana.bin", "wb") as file:
                                pickle.dump(player.banana, file)

                            player.rect.x = 55
                            player.rect.y = 55

                            monsters = pygame.sprite.Group()
                            plat_group = pygame.sprite.Group()
                            sprite_group = pygame.sprite.Group()
                            banana_group = pygame.sprite.Group()
                            enemys = []
                            banana_list = []
                            platforms = []
                            sprite_group.add(player)


                            ''' заменяешь на нужный уровень '''
                            if level_count < len(level_levels):
                                x = 0
                                y = 0
                                for row in level_levels[level_count]:
                                    for coll in row:
                                        if coll == 1:
                                            pl = Platform(x, y)
                                            sprite_group.add(pl)
                                            platforms.append(pl)

                                        if coll == 2:
                                            pl1 = MovingPlatform(x, y)
                                            plat_group.add(pl1)
                                            platforms.append(pl1)

                                        if coll == 3:
                                            enemy = Enemy(x, y - 20)
                                            monsters.add(enemy)
                                            enemys.append(enemy)

                                        if coll == 4:
                                            banana = Banana(x, y)
                                            banana_group.add(banana)
                                            banana_list.append(banana)

                                        if coll == 10:
                                            door = Dor(x - 30, y - 75)
                                            doors.add(door)
                                            doors_list.append(door)

                                        x += 40
                                    y += 40
                                    x = 0
                            else:
                                restart_btn = Button(width // 3, height // 3, 350, 50, (255, 0, 0),
                                                     'Вернуться в menu')
                                current_size = window.get_size()
                                run_controls = True
                                while run_controls:
                                    for e in pygame.event.get():
                                        if e.type == pygame.QUIT:
                                            pygame.quit()
                                            quit()
                                        if e.type == pygame.VIDEORESIZE:
                                            current_size = e.size
                                        if e.type == pygame.MOUSEBUTTONUP and event.button == 1:
                                            if restart_btn.is_pressed(pygame.mouse.get_pos()):
                                                effect = pygame.mixer.Sound('music/button.mp3')
                                                effect.play()
                                                f = open('data/out.bin', 'w')
                                                f.close()
                                                f = open('data/banana.bin', 'w')
                                                f.close()
                                                run_controls = False
                                                menu()
                                    virtual_window.fill((bg))
                                    draw_text(virtual_window, 'Поздравляю Вы побидили!!!', 50, width//2.1, height//2,
                                              (12, 0, 255))
                                    scaled_surface = pygame.transform.scale(virtual_window, current_size)
                                    window.blit(scaled_surface, (0, 0))
                                    restart_btn.draw(window, (255, 255, 255))

                                    pygame.display.update()


                elif control_btn.is_pressed(pygame.mouse.get_pos()):
                    effect = pygame.mixer.Sound('music/button.mp3')
                    effect.play()
                    print('open controls')
                    restart_btn = Button(width // 2.5, height // 3, 350, 50, (255, 0, 0), 'Вернуться в menu')
                    current_size = window.get_size()
                    run_controls = True
                    while run_controls:
                        for e in pygame.event.get():
                            if e.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                            if e.type == pygame.VIDEORESIZE:
                                current_size = e.size
                            if e.type == pygame.MOUSEBUTTONUP and event.button == 1:
                                if restart_btn.is_pressed(pygame.mouse.get_pos()):
                                    effect = pygame.mixer.Sound('music/button.mp3')
                                    effect.play()
                                    run_controls = False
                        virtual_window.fill((bg))
                        draw_text(virtual_window, 'a: ', 50, 125, 50,
                                      (12, 0, 255))
                        draw_text(virtual_window, 'Движение в лево', 50, 320, 50,
                                      (12, 0, 255))
                        draw_text(virtual_window, 'd: ', 50, 125, 100,
                                      (12, 0, 255))
                        draw_text(virtual_window, ' Движение в право', 50, 320, 100,
                                      (12, 0, 255))
                        draw_text(virtual_window, 'Пробел: ', 50, 75, 150,
                                      (12, 0, 255))
                        draw_text(virtual_window, 'Прыжок', 50, 245, 150,
                                      (12, 0, 255))
                        scaled_surface = pygame.transform.scale(virtual_window, current_size)
                        window.blit(scaled_surface, (0, 0))
                        restart_btn.draw(window, (255, 255, 255))

                        pygame.display.update()

                elif exit_btn.is_pressed(pygame.mouse.get_pos()):
                    effect = pygame.mixer.Sound('music/button.mp3')
                    effect.play()
                    running = False
                    pygame.quit()
                    quit()


        window.fill(bg)
        start_btn.draw(window, (255, 255, 255))
        control_btn.draw(window, (255, 255, 255))
        exit_btn.draw(window, (255, 255, 255))
        reset.draw(window, (255, 255, 255))



        pygame.display.update()
        timer.tick(60)

    pygame.quit()

menu()


















