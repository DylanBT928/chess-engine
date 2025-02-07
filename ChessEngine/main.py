import pygame

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Main loop
while running:
    # Poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RENDER GAME

    # Update the display
    pygame.display.flip()

    # Limit FPS to 60
    clock.tick(60)

pygame.quit()
