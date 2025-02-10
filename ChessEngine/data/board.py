import pygame

class Board:
    def __init__(self):
        """Creates a chess board."""
        self.ranks = 8
        self.files = 8
        self.tile_size = 64
        self.offset = 25
        self.bitboards = {
            'white_pawns': 0x000000000000FF00,  # Rank 2
            'black_pawns': 0x00FF000000000000,  # Rank 7
            'white_rooks': 0x0000000000000081,  # A1, H1
            'black_rooks': 0x8100000000000000,  # A8, H8
            'white_knights': 0x0000000000000042,  # B1, G1
            'black_knights': 0x4200000000000000,  # B8, G8
            'white_bishops': 0x0000000000000024,  # C1, F1
            'black_bishops': 0x2400000000000000,  # C8, F8
            'white_queens': 0x0000000000000010,  # D1
            'black_queens': 0x1000000000000000,  # D8
            'white_kings': 0x0000000000000008,  # E1
            'black_kings': 0x0800000000000000,  # E8
        }
        self.turn = 'w'
        self.castling_rights = 'KQkq'
        self.en_passant = '-'
        self.halfmove_clock = 0
        self.fullmove_number = 1


    def draw_board(self, screen: pygame.display) -> None:
        """Displays the board onto the screen."""
        colors = [(207, 182, 190), (97, 155, 138)] # Light tile, dark tile

        for x in range(self.ranks):
            for y in range(self.files):
                color = colors[(x + y) % 2]
                pygame.draw.rect(screen, color, [x * self.tile_size + self.offset,
                                                 y * self.tile_size + self.offset, 64, 64])


    def create_bitboard(self) -> list:
        """Creates a list of the all the bitboards together."""
        # Create an empty board representation (8x8)
        board = [['.' for _ in range(8)] for _ in range(8)]

        # FEN symbols for pieces
        piece_symbols = {
            'white_pawns': 'P', 'black_pawns': 'p',
            'white_knights': 'N', 'black_knights': 'n',
            'white_bishops': 'B', 'black_bishops': 'b',
            'white_rooks': 'R', 'black_rooks': 'r',
            'white_queens': 'Q', 'black_queens': 'q',
            'white_kings': 'K', 'black_kings': 'k'
        }

        # Populate the board from bitboards
        for piece, bb in self.bitboards.items():
            piece_symbol = piece_symbols[piece]
            for tile in range(64):
                if (bb >> tile) & 1:
                    rank, file = divmod(tile, 8)
                    board[7 - rank][file] = piece_symbol

        return board


    def display_bitboard(self) -> str:
        """Displays the bitboard list in the format of a chess board."""
        bitboard = self.create_bitboard()
        board = ''

        for rank in range(8):
            for field in range(8):
                board += ' ' + bitboard[rank][field] + ' '
            board += '\n'

        return board


    def bitboard_to_fen(self):
        """Converts the bitboard list into a FEN string."""
        # Display piece placement of each rank in FEN
        bitboard = self.create_bitboard()
        pieces = []

        for rank in bitboard:
            empty_count = 0
            piece = ''

            for tile in rank:
                if tile == '.':
                    empty_count += 1
                else:
                    if empty_count > 0:
                        piece += str(empty_count)
                        empty_count = 0
                    piece += tile

            if empty_count > 0:
                piece += str(empty_count)
            pieces.append(piece)

        # Join ranks with '/'
        piece_placement = '/'.join(pieces)

        # Create FEN string
        fen_string = (f'{piece_placement} {self.turn} {self.castling_rights} '
                      f'{self.en_passant} {self.halfmove_clock} {self.fullmove_number}')

        return fen_string
