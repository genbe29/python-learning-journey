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

    pygame.draw.line(screen, red, (300, 400), (120, 175), 5)
    
    pygame.draw.line(screen, red, (300, 400), (480, 175), 5)
    
    pygame.draw.line(screen, red, (120, 175), (225, 70), 5)
    
    pygame.draw.line(screen, red, (480, 175), (375, 70), 5)
    
    pygame.draw.line(screen, red, (225, 70), (300, 140), 5)
    
    pygame.draw.line(screen, red, (375, 70), (300, 140), 5)
    

    pygame.display.flip()

pygame.quit()
