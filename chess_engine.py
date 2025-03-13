import pygame
import chess


# Define window dimensions
SCREEN_WIDTH = 512
SCREEN_HEIGHT = 512


# Define board colors
LIGHT_SQUARE = (207, 182, 190) # Light gray
DARK_SQUARE = (97, 155, 138) # Green
HIGHLIGHT_COLOR = (255, 255, 0) # Yellow


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
selected_square = None
legal_moves = []


def draw_board() -> None:
    """Draws the board to the Pygame window."""
    for rank in range(8):
        for file in range(8):
            # Draw board
            color = LIGHT_SQUARE if (rank + file) % 2 == 0 else DARK_SQUARE
            rect = pygame.Rect(file * 64, rank * 64, 64, 64)
            pygame.draw.rect(screen, color, rect)

            # Draw pieces
            square = chess.square(file, 7 - rank)
            piece = board.piece_at(square)
            if piece:
                piece_image = piece_images[piece.color][piece.piece_type]
                piece_image = pygame.transform.scale(piece_image, (64, 64))
                screen.blit(piece_image, rect.topleft)


def draw_highlights() -> None:
    """Draws the highlights of the selected piece and legal moves."""
    if selected_square is not None:
        file = chess.square_file(selected_square)
        rank = 7 - chess.square_rank(selected_square)
        rect = pygame.Rect(file * 64, rank * 64, 64, 64)
        pygame.draw.rect(screen, HIGHLIGHT_COLOR, rect, 4)

        for move in legal_moves:
            if move.from_square == selected_square:
                file = chess.square_file(move.to_square)
                rank = 7 - chess.square_rank(move.to_square)
                rect = pygame.Rect(file * 64, rank * 64, 64, 64)
                pygame.draw.circle(screen, HIGHLIGHT_COLOR, rect.center, 10)



def get_square(pos: tuple) -> int:
    """Gets the chess square from the mouse position."""
    x, y = pos
    file = x // 64
    rank = 7 - (y // 64)
    return chess.square(file, rank)


# Main loop
while running:

    # Poll for events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            square = get_square(pos)

            if selected_square is not None:
                move = chess.Move(selected_square, square)

                if move in legal_moves:
                    board.push(move)
                    selected_square = None
                    legal_moves = []
                else:
                    selected_square = square if board.piece_at(square) else None
                    legal_moves = [m for m in board.legal_moves if m.from_square == selected_square]

            else:
                if board.piece_at(square) and board.piece_at(square).color == board.turn:
                    selected_square = square
                    legal_moves = [m for m in board.legal_moves if m.from_square == selected_square]
                else:
                    selected_square = None
                    legal_moves = []


    screen.fill((36, 35, 37))

    # RENDER GAME
    draw_board()
    draw_highlights()

    # Update the display
    pygame.display.flip()

    # Check game over
    if board.is_game_over():
        print('Game Over!')
        print(f'Result: {board.result()}')
        running = False

pygame.quit()
