import pygame
import random

pygame.init()
i = int(input())
done = False

pygame.time.Clock()

if __name__ == '__main__':

    screen = pygame.display.set_mode((300, 300))
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill((15, 15, 15))
        k = 300 // i // 2
        for a in range(i):
            pygame.draw.ellipse(screen, (255,255,255), (a * k, 0, 300 - a * k * 2, 300), width=1)
        for b in range(i):
            pygame.draw.ellipse(screen, (255,255,255), (0, b * k, 300, 300 - b * k * 2), width=1)
        pygame.display.flip()

    pygame.quit()