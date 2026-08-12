import pygame
import time

print('Choose one of the available levels:', 'Level 1', 'Level 2', 'Level 3', sep='\n')

pygame.init()

level = input()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Level', level)

print('The program was executed successfully')

time.sleep(5)

pygame.quit()
