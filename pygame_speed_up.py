import pygame

import time

pygame.init()

screen = pygame.display.set_mode((600, 480))

pygame.display.set_caption('speed up')

white = (255, 255, 255)

black = (0, 0, 0)

x, y = 300, 240

k = 2

running = True

while running:
    time.sleep(0.01)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                k = 2
            if event.key == pygame.K_a:
                k = 2
            if event.key == pygame.K_d:
                k = 2
            if event.key == pygame.K_s:
                k = 2


    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x -= k
        k *= 1.04
    if keys[pygame.K_d]:
        x += k
        k *= 1.04
    if keys[pygame.K_w]:
        y -= k
        k *= 1.04
    if keys[pygame.K_s]:
        y += k
        k *= 1.04

    screen.fill(white)

    pygame.draw.rect(screen, black, (x, y, 50, 50))

    pygame.display.flip()

pygame.quit()
