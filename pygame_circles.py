import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption('UwU')

white = (255, 255, 255)

black = (0, 0, 0)

screen.fill(white)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.circle(screen, black, (event.pos), 50)



    pygame.display.flip()

pygame.quit()
