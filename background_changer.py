import pygame

pygame.init()

screen = pygame.display.set_mode((600, 480))

pygame.display.set_caption('background changer')

white = (255, 255, 255)

red = (255, 0, 0)

green = (0, 255, 0)

blue = (0, 0, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_w:

                screen.fill(white)

            elif event.key == pygame.K_r:

                screen.fill(red)

            elif event.key == pygame.K_g:

                screen.fill(green)

            elif event.key == pygame.K_b:

                screen.fill(blue)

    pygame.display.flip()

pygame.quit()
