import pygame

import time

pygame.init()

screen = pygame.display.set_mode((1000, 800))

pygame.display.set_caption('<3')

color = (143, 165, 228)

blue = (72, 112, 223)

red = (223, 72, 72)

a, b = 589, 325

x, y = 333, 400

running = True
while running:
    time.sleep(0.01)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
          
    keys = pygame.key.get_pressed()
  
    if keys[pygame.K_a]:
        x -= 5
    if keys[pygame.K_d]:
        x += 5
    if keys[pygame.K_w]:
        y -= 5
    if keys[pygame.K_s]:
        y += 5

    if keys[pygame.K_LEFT]:
        a -= 5
    if keys[pygame.K_RIGHT]:
        a += 5
    if keys[pygame.K_UP]:
        b -= 5
    if keys[pygame.K_DOWN]:
        b += 5

    screen.fill(color)

    pygame.draw.circle(screen, blue, (x, y), 75)

    pygame.draw.rect(screen, red, (a, b, 150, 150))

    pygame.display.flip()

pygame.quit()
