import pygame
from pygame.locals import *


def draw_cube(x, y, size):
    pygame.draw.rect(screen, (255, 127, 127), (x, y, size, size))
    pygame.draw.polygon(screen, (255, 149, 149),
                        [(x, y), (x + size / 2, y - size / 2), (x + size * 1.5, y - size / 2), (x + size, y)])
    pygame.draw.polygon(screen, (255, 0, 0),
                        [(x + size, y), (x + size * 1.5, y - size / 2), (x + size * 1.5, y + size / 2), (x + size, y + size)])


def check_input(value):
    try:
        size = int(value)
        if size <= 0:
            raise ValueError
    except ValueError:
        print("Ошибка: неверный формат ввода.")
        return False
    return True


if __name__ == "__main__":
    pygame.init()

    # Ввод размера куба
    while True:
        size_input = input("Введите размер куба: ")
        hue_input = input("Введите оттенок: ")

        if check_input(size_input):
            size = int(size_input)
            break

    # Создание экрана
    screen_size = (300, 300)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Cube")

    cube_x = (screen_size[0] - size * 2) // 2
    cube_y = (screen_size[1] - size * 2) // 2
    draw_cube(cube_x, cube_y, size)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
