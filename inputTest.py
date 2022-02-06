# Import the pygame module
import pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Initialize pygame
pygame.init()

playerDim = (20,20)

# Screen width/Height
SCREEN_WIDTH = playerDim[0]*32
SCREEN_HEIGHT = playerDim[1]*2

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# Variable to keep the main loop running
running = True

# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False
    surf = pygame.Surface((playerDim))
    surf.fill((0, 0, 255))
    rect = surf.get_rect()
    # This line says "Draw surf onto the screen at the center"
    # Put the center of surf at the center of the display
    surf_center = (0,0)

    # Draw surf at the new coordinates
    screen.blit(surf, surf_center)
    pygame.display.flip()
    