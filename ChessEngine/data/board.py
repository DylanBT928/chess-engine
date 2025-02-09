import pygame

class Board:
    def __init__(self):
        """Creates a chess board."""
        self.board = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
        self.rows = 8
        self.cols = 8


    def draw_board(self, screen: pygame.display):
        """Displays the board onto the screen."""
        for x in range(self.rows):
            for y in range(self.cols):
                color = (237, 242, 239) if (x + y) % 2 == 0 else (97, 155, 138)
                pygame.draw.rect(screen, color, [(x * 64) + 25, (y * 64) + 25, 64, 64])
