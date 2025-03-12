from operator import invert

import pygame
import chess


# Define window dimensions
SCREEN_WIDTH = 562
SCREEN_HEIGHT = 562


# Define board colors
LIGHT_SQUARE = (207, 182, 190) # Light gray
DARK_SQUARE = (97, 155, 138) # Green


def invert_color(img: pygame.Surface) -> pygame.Surface:
    """Invert only the RBG of an image."""
    width = img.get_width()
    height = img.get_height()
    img.lock()

    for x in range(width):
        for y in range(height):
            rgba = img.get_at((x, y))
            for i in range(3):
                rgba[i] = 255 - rgba[i]
            img.set_at((x, y), rgba)

    img.unlock()
    return img


# Load icon
icon = pygame.image.load('resources/icon.png')
white_pieces = {
    chess.PAWN: pygame.image.load('resources/pawn.png'),
    chess.ROOK: pygame.image.load('resources/rook.png'),
    chess.KNIGHT: pygame.image.load('resources/knight.png'),
    chess.BISHOP: pygame.image.load('resources/bishop.png'),
    chess.QUEEN: pygame.image.load('resources/queen.png'),
    chess.KING: pygame.image.load('resources/king.png')
}
black_pieces = {
    chess.PAWN: invert_color(white_pieces[chess.PAWN].copy()),
    chess.ROOK: invert_color(white_pieces[chess.ROOK].copy()),
    chess.KNIGHT: invert_color(white_pieces[chess.KNIGHT].copy()),
    chess.BISHOP: invert_color(white_pieces[chess.BISHOP].copy()),
    chess.QUEEN: invert_color(white_pieces[chess.QUEEN].copy()),
    chess.KING: invert_color(white_pieces[chess.KING].copy())
}
piece_images = {
    chess.WHITE: white_pieces,
    chess.BLACK: black_pieces
}


# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Chess Engine')
pygame.display.set_icon(icon)
running = True


# Initialize chess board
board = chess.Board()


def draw_board() -> None:
    """Draws the board to the Pygame window."""
    offset = 25
    for rank in range(8):
        for file in range(8):
            # Draw board
            color = LIGHT_SQUARE if (rank + file) % 2 == 0 else DARK_SQUARE
            rect = pygame.Rect(file * 64 + offset, rank * 64 + offset, 64, 64)
            pygame.draw.rect(screen, color, rect)

            # Draw pieces
            square = chess.square(file, 7 - rank)
            piece = board.piece_at(square)
            if piece:
                piece_image = piece_images[piece.color][piece.piece_type]
                piece_image = pygame.transform.scale(piece_image, (64, 64))
                screen.blit(piece_image, rect.topleft)


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
    draw_board()

    # Update the display
    pygame.display.flip()

pygame.quit()
