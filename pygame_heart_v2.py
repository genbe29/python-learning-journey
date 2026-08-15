import pygame

pygame.init()

screen = pygame.display.set_mode((600, 480))

pygame.display.set_caption('Heart')

white = (255, 255, 255)

red = (255, 0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)

    pygame.draw.circle(screen, red, (390, 175), 92)

    pygame.draw.circle(screen, red, (210, 175), 92)

    pygame.draw.polygon(screen, red, [(134, 225), (466, 225), (300, 400)])

    pygame.draw.rect(screen, red, (210, 175, 175, 120))

    pygame.display.flip()

pygame.quit()
