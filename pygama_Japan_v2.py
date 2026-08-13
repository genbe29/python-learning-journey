import pygame

width = int(input('Enter the width: '))
height = int(input('Enter the height: '))
pygame.init()

screen = pygame.display.set_mode((width, height - 50))
pygame.display.set_caption('It is Japan')

white = (255, 255, 255)
red = (255, 0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)

    pygame.draw.circle(screen, red, (width * 0.5, height * 0.5), width * 0.1)

    pygame.display.flip()

pygame.quit()
