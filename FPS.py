import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))

pygame.display.set_caption('fps')

white = (255, 255, 255)

red = (255, 0, 0)

x, y = (320, 240)

total = 0

speed_x, speed_y = 3, 3

FPS = 60
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                FPS += 5
                print('фпс увеличен с', FPS - 5, 'до', FPS)
            elif event.key == pygame.K_DOWN:
                FPS -= 5
                print('фпс уменьшен с', FPS + 5, 'до', FPS)

    x += speed_x
    y += speed_y

    if x <= 25 or x >= 615:
        speed_x = -speed_x

    if y <= 25 or y >= 455:
        speed_y = -speed_y


    screen.fill(white)

    pygame.draw.circle(screen, red, (x, y), 25)

    pygame.display.flip()

    clock.tick(FPS)

    total += 1

pygame.quit()

print('общее количесто кадров: ', total)
