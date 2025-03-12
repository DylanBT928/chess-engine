import pygame

from board import Board

# Window dimensions
SCREEN_WIDTH = 562
SCREEN_HEIGHT = 562

# Load window icon
icon = pygame.image.load('resources/icon.png')

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Chess Engine')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
running = True

# Initialize game
board = Board()

# Prints the starting bitboard and FEN string
print(board.display_bitboard())
print(board.bitboard_to_fen())

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
    board.draw_pieces(screen)

    # Update the display
    pygame.display.flip()

    # Limit FPS to 60
    clock.tick(60)

pygame.quit()
