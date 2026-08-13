import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('It is Japan')

white = (255, 255, 255)
red = (255, 0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)

    pygame.draw.circle(screen, red, (320, 240), 100)

    pygame.display.flip()

pygame.quit()
