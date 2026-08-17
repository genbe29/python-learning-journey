import pygame

import time

pygame.init()

screen = pygame.display.set_mode((1200, 900))

pygame.display.set_caption('Catch Me!')

white = (255, 255, 255)

red = (255, 0, 0)

blue = (0, 0 ,255)

a, b = 600, 800

x, y = 150, 450

running = True

while running:
    time.sleep(0.01)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if 85 > (x - a) > -85 and 85 > (y - b) > -85:
        print('Blue player wins!')
        break

    else:

        if keys[pygame.K_UP]:
            b -= 3.5
            if b <= 60:
                b += 3.5
        if keys[pygame.K_DOWN]:
            b += 3.5
            if b >= 840:
                b -= 3.5
        if keys[pygame.K_LEFT]:
            a -= 3.5
            if a <= 60:
                a += 3.5
        if keys[pygame.K_RIGHT]:
            a += 3.5
            if a >= 1140:
                a -= 3.5



        if keys[pygame.K_d]:
            x += 5
            if x >= 1140:
                x -= 5
        if keys[pygame.K_a]:
            x -= 5
            if x <= 60:
                x += 5
        if  keys[pygame.K_w]:
            y -= 5
            if y <= 60:
                y += 5
        if keys[pygame.K_s]:
            y += 5
            if y >= 840:
                y -= 5


    screen.fill(white)

    pygame.draw.circle(screen, red, (x, y), 50)

    pygame.draw.circle(screen, blue, (a, b), 50)

    pygame.display.flip()

pygame.quit()
