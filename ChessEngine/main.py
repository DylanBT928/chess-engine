import pygame

from ChessEngine.data.board import draw_board

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((562, 562))
clock = pygame.time.Clock()
running = True

# Main loop
while running:
    # Poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((36, 35, 37))

    # RENDER GAME
    draw_board(screen)

    # Update the display
    pygame.display.flip()

    # Limit FPS to 60
    clock.tick(60)

pygame.quit()
