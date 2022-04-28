import pygame
from object import *

WIDTH = 360  # ширина игрового окна
HEIGHT = 480 # высота игрового окна
FPS = 30 # частота кадров в секунду

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

sonic=Object(100,100)

running = True
while running:
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.draw.circle(
                    screen, RED, event.pos, 20)
                pygame.display.update()
            elif event.button == 3:
                pygame.draw.circle(
                    screen, BLUE, event.pos, 20)
                pygame.draw.rect(
                    screen, GREEN,
                    (event.pos[0] - 10,
                     event.pos[1] - 10,
                     20, 20))
                pygame.display.update()
            elif event.button == 2:
                screen.fill(WHITE)
                pygame.display.update()

    '''#Рендеринг
    screen.fill(WHITE)

    screen.blit(sonic.image,sonic.rect)

    # после отрисовки всего, переворачиваем экран
    pygame.display.flip()'''

    clock.tick(FPS)




