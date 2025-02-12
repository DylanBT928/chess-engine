import pygame


def load_piece(piece) -> pygame.Surface:
    """Loads the image of the wanted chess piece."""
    img = pygame.image.load(f'resources/{piece.lower()}.png')

    if piece.islower():
        invert_color(img)

    return img


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
