import pygame

a = int(input())
b = int(input())
pygame.init()

screen = pygame.display.set_mode((a, b - 50))
pygame.display.set_caption('It is Japan')

white = (255, 255, 255)
red = (255, 0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)

    pygame.draw.circle(screen, red, (a * 0.5, b * 0.5), a * 0.1)

    pygame.display.flip()

pygame.quit()
