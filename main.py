import os
import sys
from random import randint
import string
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
WHITE_CELL_COLOR = (230,206,172)
BLACK_CELL_COLOR = (148,117,89)
BOARD_COLOR = (88,57,29)
ENGLISH = list(string.ascii_uppercase)



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


class Board:
    def __init__(self, x, cell_size, left, top, edge, corner=True):
        self.edge = edge
        self.size = x
        self.cell_size = cell_size
        self.left = left
        self.top = top
        self.board = [[Cell(self, 0, x1, y1) for x1 in range(x)] for y1 in range(x)]
        self.corner = corner

    def render(self, screen):
        #это рендер края доски
        pygame.draw.rect(screen, BOARD_COLOR,
                         (self.left, self.top,
                          self.cell_size * self.size + self.edge * 2,
                          self.cell_size * self.size + self.edge * 2), self.edge)
        #рендер букв и цифр
        for i in range(self.size):
            number = FONT.render(str(i), True, WHITE)
            screen.blit(number, (self.left + (self.edge // 2 - FX // 2),
                                 i * self.cell_size + self.top + self.edge + (self.cell_size // 2 - FY // 2)))

        for i in range(self.size):
            number = FONT.render(ENGLISH[i], True, WHITE)
            screen.blit(number, (i * self.cell_size + self.left + self.edge + (self.cell_size // 2 - FX // 2),
                                 self.top + (self.edge // 2 - FY // 2)))

        #это рендер клеток
        for x in range(self.size):
            for y in range(self.size):
                if self.corner:
                    pygame.draw.rect(screen, (255, 255, 255),
                                     (x * self.cell_size + self.left + self.edge, y * self.cell_size + self.top + self.edge,
                                      self.cell_size, self.cell_size), 1)
                if (x + y) % 2 == 0:
                    color = WHITE_CELL_COLOR
                else:
                    color = BLACK_CELL_COLOR
                pygame.draw.rect(screen, color,
                                 (x * self.cell_size + self.left + self.edge,
                                  y * self.cell_size + self.top + self.edge, self.cell_size, self.cell_size), 0)

                self.board[y][x].render(screen)

    def update(self):
        counter = 0
        for y in range(self.size):
            for x in range(self.size):
                if board[y][x].val != 0:
                    counter += 1
        new = randint(0, counter)


class Cell:
    def __init__(self, board, value, x, y):
        self.val = value
        self.x = x
        self.y = y
        self.cell_size = board.cell_size
        self.left = board.left
        self.top = board.top
        self.edge = board.edge

    def render(self, screen):
        if self.val != 0:
            number = FONT.render(str(self.val), True, RED)
            screen.blit(number, (self.x * self.cell_size + self.left + self.edge + (self.cell_size // 2 - FX // 2),
                                 self.y * self.cell_size + self.top + self.edge + (self.cell_size // 2 - FY // 2)))


if __name__ == "__main__":
    pygame.init()
    FONT = pygame.font.Font(None, 60)
    FX, FY = FONT.render("1", True, WHITE).get_size()
    size = 8
    cell_size = 90
    left = 20
    top = 20
    edge = max(FX,FY)
    screen = pygame.display.set_mode((size * cell_size + (left + edge) * 2,
                                      size * cell_size + (top + edge) * 2,))
    corner = False
    board = Board(size, cell_size, left, top, edge, corner)
    running = True
    board.board[0][0].val = 1

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()

