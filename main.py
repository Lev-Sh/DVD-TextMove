import pygame
import random

pygame.init()
i = list(map(int, input().split()))
SIZE = (i[0], i[1])
WIDTH = i[0]
HEIGHT = i[1]
vel_x = 0.5
vel_y = 1
done = False

pygame.time.Clock()

if __name__ == '__main__':

    screen = pygame.display.set_mode(SIZE)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill((15, 15, 15))
        rect = pygame.draw.rect(screen, (255, 0, 0), ((1, 1), (WIDTH - 1, HEIGHT - 1)))
        pygame.display.flip()

    pygame.quit()
