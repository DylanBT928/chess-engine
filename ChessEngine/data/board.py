import pygame

def draw_board(screen: pygame.display):
    for x in range(8):
        for y in range(8):
            color = (237, 242, 239) if (x + y) % 2 == 0 else (97, 155, 138)
            pygame.draw.rect(screen, color, [(x * 64) + 25, (y * 64) + 25, 64, 64])
