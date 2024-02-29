import os
import sys
import string
import pygame
import Figures
import Rule

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
WHITE_CELL_COLOR = (230, 206, 172)
BLACK_CELL_COLOR = (148, 117, 89)
BOARD_COLOR = (88, 57, 29)
ENGLISH = list(string.ascii_uppercase)
FPS = 60
STOP = False


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


class Start:
    def terminate(self):
        pygame.quit()
        sys.exit()

    def render(self):
        screen.fill(WHITE)

        intro_text = ["Шахматы", "",
                      "В этих шахматах есть три режима",
                      "Классический, Total War, Improved", "",
                      "В режиме Total War, доска увеличивается и увеличивается количество фигур", "",
                      "В Improved, иногда на поле будут появляться усиления,",
                      "которые могут перевернуть игру"]

        fon = pygame.transform.scale(load_image('fon.jpg'), (650, 650))
        screen.blit(fon, (300, 250))
        font = pygame.font.Font(None, 30)
        text_coord = 50
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('black'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        font = pygame.font.Font(None, 35)

        text = "Классический"
        text = font.render(text, True, BLACK)
        pygame.draw.rect(screen, BLACK_CELL_COLOR, (30, 390, 190, 44))
        screen.blit(text, (40, 400))

        text = "Total War"
        text = font.render(text, True, BLACK)

        pygame.draw.rect(screen, BLACK_CELL_COLOR, (30, 490, 131, 44))
        screen.blit(text, (40, 500))

        text = "Improved"
        text = font.render(text, True, BLACK)
        pygame.draw.rect(screen, BLACK_CELL_COLOR, (30, 590, 128, 44))
        screen.blit(text, (40, 600))

    def start_screen(self):
        global MODE
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                elif event.type == pygame.MOUSEBUTTONUP:
                    x, y = event.pos
                    if x in range(30, 30 + 190) and y in range(390, 390 + 44):
                        MODE = 'clas'
                        return
                    elif x in range(30, 30 + 190) and y in range(490, 490 + 44):
                        MODE = 'tot'
                        return

            self.render()
            pygame.display.flip()
            clock.tick(FPS)


class Board:
    def __init__(self, x, cell_size, left, top, edge, max_time, rule='test', corner=True):
        self.edge = edge
        self.size = x
        self.cell_size = cell_size
        self.left = left
        self.top = top
        self.tw = max_time
        self.tb = max_time
        self.mw = 1
        self.mb = 1
        self.cw = 0
        self.cb = 0
        self.move = 'w'
        self.rule = rule
        self.board = [[Figures.Empty(self, (x1, y1)) for x1 in range(x)] for y1 in range(x)]
        self.corner = corner
        self.mated = ''

    def render_player_action(self, screen):
        for x in range(self.size):
            for y in range(self.size):
                try:
                    if self.board[y][x].grabbed:
                        image = load_image(self.board[y][x].image)
                        image = pygame.transform.scale(image, (self.cell_size, self.cell_size))
                        mx, my = pygame.mouse.get_pos()
                        mx -= self.cell_size // 2
                        my -= self.cell_size // 2
                        screen.blit(image, (mx, my))
                except AttributeError:
                    print(x, y)

    def render_figures(self, screen, pos):
        x, y = pos
        if self.board[y][x] != 0:
            if not self.board[y][x].grabbed:
                image = load_image(self.board[y][x].image)
                image = pygame.transform.scale(image, (self.cell_size, self.cell_size))
                screen.blit(image, (x * self.cell_size + self.left + self.edge,
                                    y * self.cell_size + self.top + self.edge))

    def render(self, screen):
        # это рендер края доски
        pygame.draw.rect(screen, BOARD_COLOR,
                         (self.left, self.top,
                          self.cell_size * self.size + self.edge * 2,
                          self.cell_size * self.size + self.edge * 2), self.edge)
        # рендер букв и цифр
        for i in range(self.size):
            number = FONT.render(str(i), True, WHITE)
            screen.blit(number, (self.left + (self.edge // 2 - FX // 2),
                                 i * self.cell_size + self.top + self.edge + (self.cell_size // 2 - FY // 2)))

        for i in range(self.size):
            number = FONT.render(ENGLISH[i], True, WHITE)
            screen.blit(number, (i * self.cell_size + self.left + self.edge + (self.cell_size // 2 - FX // 2),
                                 self.top + (self.edge // 2 - FY // 2)))

        # это рендер клеток
        for x in range(self.size):
            for y in range(self.size):
                if self.corner:
                    pygame.draw.rect(screen, (255, 255, 255),
                                     (x * self.cell_size + self.left + self.edge,
                                      y * self.cell_size + self.top + self.edge,
                                      self.cell_size, self.cell_size), 1)
                if (x + y) % 2 == 0:
                    color = WHITE_CELL_COLOR
                else:
                    color = BLACK_CELL_COLOR
                pygame.draw.rect(screen, color,
                                 (x * self.cell_size + self.left + self.edge,
                                  y * self.cell_size + self.top + self.edge, self.cell_size, self.cell_size), 0)

                self.render_figures(screen, (x, y))
        self.render_player_action(screen)
        # рендер времени
        t = str(self.tw // 60) + ":" + str(self.tw % 60)
        number = FONT.render(t, True, WHITE)
        screen.blit(number, (self.size * self.cell_size + (self.edge + self.left) * 2, self.top + self.edge,
                             100, 100))

        t = str(self.tb // 60) + ":" + str(self.tb % 60)
        number = FONT.render(t, True, WHITE)
        screen.blit(number, (self.size * self.cell_size + (self.edge + self.left) * 2,
                             self.size * self.cell_size, 100, 100))

        # рендер счёта
        w, b = self.counter()
        t = str(MB - b)
        number = FONT.render(t, True, WHITE)
        screen.blit(number, (self.size * self.cell_size + (self.edge + self.left) * 2,
                             self.size * self.cell_size // 2 - self.top - self.edge,
                             100, 100))

        t = str(MW - w)
        number = FONT.render(t, True, WHITE)
        screen.blit(number, (self.size * self.cell_size + (self.edge + self.left) * 2,
                             self.size * self.cell_size // 2 + self.top + self.edge,
                             100, 100))

    def mat(self):
        global STOP
        kingw = (0, 0)
        kingb = (0, 0)
        for y in range(self.size):
            for x in range(self.size):
                if type(self.board[y][x]) == Figures.King:
                    if self.board[y][x].col == 'w':
                        kingw = (x, y)
                    elif self.board[y][x].col == 'b':
                        kingb = (x, y)
        for y in range(self.size):
            for x in range(self.size):
                if self.board[y][x].col == 'w':
                    if self.board[y][x].can_move(kingb):
                        self.mated = 'b'
                        STOP = True
                elif self.board[y][x].col == 'b':
                    if self.board[y][x].can_move(kingw):
                        self.mated = 'w'
                        STOP = True

    def end(self):
        t = 'WINS'
        y = 0
        if self.tw == 0:
            y = self.size * self.cell_size // 2 - self.top - self.edge - 100
        elif self.tb == 0:
            y = self.size * self.cell_size // 2 - self.top - self.edge + 100

        elif self.tw >= 0 and self.tb >= 0:
            pass

        else:
            t = 'WTF'

            t = FONT.render(t, True, WHITE)
            y = self.size * self.cell_size // 2 - self.top - self.edge - 50
            screen.blit(t, (self.size * self.cell_size + (self.edge + self.left) * 2,
                            y, 100, 100))
            y = self.size * self.cell_size // 2 - self.top - self.edge + 50
            screen.blit(t, (self.size * self.cell_size + (self.edge + self.left) * 2,
                            y, 100, 100))
            return
        m = self.mated
        if m:
            if m == 'w':
                y = self.size * self.cell_size // 2 - self.top - self.edge + 100
            elif m == 'b':
                y = self.size * self.cell_size // 2 - self.top - self.edge - 70
            else:
                t = 'Pat'
                t = FONT.render(t, True, WHITE)
                y = self.size * self.cell_size // 2 - self.top - self.edge - 50
                screen.blit(t, (self.size * self.cell_size + (self.edge + self.left) * 2,
                                y,
                                100, 100))
                y = self.size * self.cell_size // 2 - self.top - self.edge + 50
                screen.blit(t, (self.size * self.cell_size + (self.edge + self.left) * 2,
                                y,
                                100, 100))
                return
        if y:
            t = FONT.render(t, True, WHITE)
            screen.blit(t, (self.size * self.cell_size + (self.edge + self.left) * 2 - 10,
                            y,
                            100, 100))

    def get_cell(self, x, y):
        x = (x - self.left - self.edge) // self.cell_size
        y = (y - self.top - self.edge) // self.cell_size
        return x, y

    def counter(self):
        w = 0
        b = 0
        for y in range(self.size):
            for x in range(self.size):
                if self.board[y][x].col == 'w':
                    w += 1
                elif self.board[y][x].col == 'b':
                    b += 1
        return w, b


if __name__ == "__main__":
    pygame.init()
    FONT = pygame.font.Font(None, 60)
    FX, FY = FONT.render("1", True, WHITE).get_size()
    INF_SIZE = 100
    screen = pygame.display.set_mode((850, 850))
    clock = pygame.time.Clock()
    win1 = Start()
    win1.start_screen()
    # MODE = 'tes'
    if MODE == 'clas' or MODE == 'test' or MODE == 'tes':
        rule = Rule.Classic_Rule()
    elif MODE == 'tot':
        rule = Rule.Total_War()
    size = rule.size
    cell_size = rule.cell_size
    left = rule.left
    top = rule.top
    MW, MB = rule.mw, rule.mb
    max_time = rule.max_time
    edge = max(FX, FY)
    WIDTH = size * cell_size + (left + edge) * 2
    HEIGHT = size * cell_size + (top + edge) * 2
    screen = pygame.display.set_mode((size * cell_size + (left + edge) * 2,
                                      size * cell_size + (top + edge) * 2,))
    corner = False
    board = Board(size, cell_size, left, top, edge, max_time, rule=MODE, corner=corner)
    rule.add_figures(board)
    board.board = rule.board

    running = True
    frame = 0

    screen = pygame.display.set_mode((size * cell_size + (left + edge) * 2 + INF_SIZE,
                                      size * cell_size + (top + edge) * 2,))
    while running:
        frame += 1
        if frame == 60 and not STOP:
            frame = 0
            if board.move == 'w':
                board.tw -= 1
            else:
                board.tb -= 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.dict['pos']
                x, y = pos
                x1, y1 = board.get_cell(x, y)
                if 0 <= x1 < size and 0 <= y1 < size:
                    board.board[y1][x1].grabbed = True
            if event.type == pygame.MOUSEBUTTONUP:
                pos = event.dict['pos']
                x, y = pos
                x2, y2 = board.get_cell(x, y)
                if 0 <= x1 < size and 0 <= y1 < size:
                    board.board[y1][x1].grabbed = False
                if 0 <= x2 < size and 0 <= y2 < size:
                    board.board[y1][x1].move((x2, y2))
        screen.fill((0, 0, 0))
        board.render(screen)
        board.mat()
        board.end()
        clock.tick(FPS)
        pygame.display.flip()
