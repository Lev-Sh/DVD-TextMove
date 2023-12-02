import pygame
import random

pygame.init()
i = input().split()
WIDTH = int(i[0])
HEIGHT = int(i[1])
SIZE = (WIDTH, HEIGHT)

vel_x = 0.5
vel_y = 1
done = False

if __name__ == '__main__':
    pygame.display.set_caption('Крест')
    screen = pygame.display.set_mode(SIZE)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill((30, 30, 30))

        line1 = pygame.draw.line(screen, (255, 255, 255), (0, 0), (WIDTH, HEIGHT), width=1)
        line2 = pygame.draw.line(screen, (255, 255, 255), (WIDTH, 0), (0, HEIGHT), width=1)
        pygame.display.flip()

    pygame.quit()
