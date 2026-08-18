import pygame
import time

pygame.init()

a, b = 800, 600
screen = pygame.display.set_mode((a, b))

pygame.display.set_caption('idk')

white = (255, 255, 255)

red = (255, 0, 0)

blue = (0, 0, 255)

black = (0, 0, 0)

x, y = (a // 2, b // 2)

c, c1, d, d1 = a - 5, b // 2 - 50, a - 5, b // 2 + 50

e, e1, f, f1 = 5, b // 2 - 50, 5, b // 2 + 50


running = True
while running:
    time.sleep(0.01)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x -= 5
        if x < 5:
            x += 5

    if keys[pygame.K_d]:
        x += 5
        if x > a - 65:
            x -= 5

    if keys[pygame.K_w]:
        y -= 5
        if y < 5:
            y += 5

    if keys[pygame.K_s]:
        y += 5
        if y > b - 85:
            y -= 5



    if -5 < x - e < 5 and -50 < y - b // 2 < 50:
        x = a - 70

    if -65 < x - c < 65 and -50 < y - b // 2 < 50:
        x = 10

    screen.fill(white)

    pygame.draw.rect(screen, black, (x, y, 60, 80))

    pygame.draw.line(screen, red, (c, c1), (d, d1), 11)

    pygame.draw.line(screen, blue, (e, e1), (f, f1), 11)

    pygame.display.flip()

pygame.quit()
