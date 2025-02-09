import pygame

from ChessEngine.data.board import Board

SCREEN_WIDTH = 562
SCREEN_HEIGHT = 562

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Chess Engine')
clock = pygame.time.Clock()
running = True

# Initialize game
board = Board()

# Main loop
while running:
    # Poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill((36, 35, 37))

    # RENDER GAME
    board.draw_board(screen)

    # Update the display
    pygame.display.flip()

    # Limit FPS to 60
    clock.tick(60)

pygame.quit()
