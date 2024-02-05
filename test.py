import os
import sys

import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    fontName = pygame.font.get_default_font()
    size = 70
    font = pygame.font.Font(None, size)
    text = "8"
    ant = True
    color = (255, 255, 255)
    surface = font.render(f"{text}", ant, color)
    print(surface.get_size())
    pygame.display.flip()
    running = True

    image = load_image("Chess.jpg")
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(surface, (300, 100))
        screen.blit(image, (50, 50, 100, 100))
        pygame.display.update()
    pygame.quit()
