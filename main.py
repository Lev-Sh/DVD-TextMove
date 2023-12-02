import pygame
import random

pygame.init()
done = False

if __name__ == '__main__':
    brick_size = [30, 15]
    rect = pygame.Rect(0, 0, brick_size[0], brick_size[1])
    cell = 3

    screen = pygame.display.set_mode((300, 200))
    screen.fill((255, 255, 255))

    for row in range(12):
        for col in range(12):
            if row % 2 == 0:
                screen.fill((255, 0, 0), rect.move(32 * col, 17 * row))
                print(row)

            else:
                screen.fill((255, 0, 0), rect.move(32 * col - 15, 17 * row))
                pygame.draw.line(screen, (255, 255, 255), (15, col * 33.5), (15, col * 33.5 - 16), width=2)

    screen.fill((255, 0, 0), rect.move(0, 0))

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        pygame.display.flip()

    pygame.quit()
