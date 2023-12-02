import pygame
import random

pygame.init()
SIZE, WIDTH, HEIGHT = (800, 600), 800, 600

vel_x = 0.5
vel_y = 1
done = False

pygame.time.Clock()

gradient = 1
gradient_color = 0
def draw(screen):
    screen.fill((0, 0, 0))
def random_color(a: int, gradient_color=int, gradient=int) -> tuple:
    if a == 0:
        return (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
        )
    if a == 1:
        a = [100, 100, 100]
        a[gradient_color] = gradient
        if(gradient_color == 2):
            a[0] = 255 - gradient
        else:
            a[gradient_color + 1] = 255 - gradient

        b = (a[0], a[1], a[2])
        return b


if __name__ == '__main__':

    screen = pygame.display.set_mode(SIZE)
    draw(screen)
    font = pygame.font.Font(None, 30)
    text = font.render("MMMMMMMMMM", True, (100, 130, 200))
    x = 100
    y = 100
    gradient = 1
    gradient_color = 0
    screen.blit(text, (x + x, y + y))
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        pygame.display.flip()
        x += vel_x
        y += vel_y
        if(gradient >= 255):
            gradient = 100
            if(gradient_color >= 2):
                gradient_color = 0
            gradient_color += 1
        gradient += 0.1

        ontext = "ПОХУЙ"
        if x >= (WIDTH // 2) - len(ontext) ** 2 or x <= 0:
            vel_x *= -1
            text = font.render(ontext, True, random_color(0, gradient_color=gradient_color, gradient=gradient))

        if y >= (HEIGHT // 2) - len(ontext) or y <= 0:
            vel_y *= -1
            text = font.render(ontext, True, random_color(0, gradient_color=gradient_color, gradient=gradient))

        screen.fill((15, 15, 15))

        screen.blit(text, (x + x, y + y))
    pygame.quit()
