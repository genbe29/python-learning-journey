import pygame
import sys

# Initialize all imported pygame modules
pygame.init()

# Set up the game window dimensions (Width, Height)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Entangled Spaces - Prototype")

# Game status flag
is_running = True

# Main Game Loop
while is_running:
    # Check for user actions (events)
    for event in pygame.event.get():
        # If user clicks the close button (X), stop the game
        if event.type == pygame.QUIT:
            is_running = False

    # Fill the screen with a dark gray color (RGB format)
    screen.fill((40, 40, 40))

    # Update the full display Surface to the screen
    pygame.display.flip()

# Clean up and close the game properly
pygame.quit()
sys.exit()
