import pygame

pygame.init()

screen = pygame.display.set_mode((600, 480))

pygame.display.set_caption('Sounds Damn Complicated, But I Will Try')

white = (255, 255, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print('Left arrow key pressed')
            elif event.key == pygame.K_RIGHT:
                print('Right arrow key pressed')

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                print('Left arrow key released')
            elif event.key == pygame.K_RIGHT:
                print('Right arrow key released')

    screen.fill(white)

    pygame.display.flip()

pygame.quit()
