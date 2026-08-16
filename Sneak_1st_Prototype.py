import pygame

import time

pygame.init()

screen = pygame.display.set_mode((600, 480))

pygame.display.set_caption('Sneak - 1st Prototype')

white = (255, 255, 255)

red = (255, 0, 0)

x, y = 300, 240

running = True
while running:
    time.sleep(0.008)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
          
    keys = pygame.key.get_pressed()
  
    if keys[pygame.K_LEFT]:
      
        x -= 3
      
    if keys[pygame.K_RIGHT]:
      
        x += 3
      
    if keys[pygame.K_UP]:
      
        y -= 3
      
    if keys[pygame.K_DOWN]:
      
        y += 3

    screen.fill(white)

    pygame.draw.rect(screen, red, (x, y, 50, 50))

    pygame.display.flip()

pygame.quit()
