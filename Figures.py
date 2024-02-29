import Rule


class Figure:
    def __init__(self, board, pos, color='w'):
        self.x, self.y = pos
        self.board = board
        self.col = color
        if color == 'w':
            self.image = f"{type(self).__name__}1.png"
        elif color == 'b':
            self.image = f"{type(self).__name__}2.png"
        self.grabbed = False
        if self.board.rule == 'clas' or self.board.rule == 'test' or self.board.rule == 'tes':
            rule = Rule.Classic_Rule()
        elif self.board.rule == 'tot':
            rule = Rule.Total_War()
        self.pawn_start = rule.pawn_start

    def can_move(self, pos2):
        return True

    def check_dest(self, pos2):
        x, y = pos2
        if self.board.rule == 'test' or self.board.rule == 'tes':
            return True
        if ((self.board.board[self.y][self.x].col == self.board.board[y][x].col or self.col != self.board.move)
                or self.board.mated and not type(self.board.board[self.y][self.x]) == King):
            return False
        else:
            return True

    def move(self, pos2):
        # print(self.can_move(pos2), self.check_dest(pos2))
        if self.can_move(pos2) and self.check_dest(pos2) or self.board.rule == 'test':
            board = self.board.board
            board[self.y][self.x], board[pos2[1]][pos2[0]] = Empty(self.board, pos2), board[self.y][self.x]
            if self.col == 'w':
                self.board.move = 'b'
            else:
                self.board.move = 'w'
            self.x = pos2[0]
            self.y = pos2[1]
            return True
        else:
            return False


class Empty(Figure):
    def __init__(self, board, pos2):
        super().__init__(board, pos2)
        self.col = None
        self.image = f"{type(self).__name__}.png"


class Pawn(Figure):
    def can_move(self, pos2):
        x2, y2 = pos2
        x, y = self.x, self.y
        sy1, sy2 = self.pawn_start[0], self.pawn_start[1]
        if (y == sy1 or y == sy2) and abs(y2 - y) == 2 and x2 - x == 0:
            if ((self.col == 'w' and self.board.board[y + 1][x].col != self.col)
                    or (self.col == 'b' and self.board.board[y - 1][x].col != self.col)):
                return True
        elif (y2 - y == 1 and self.col == 'w' or y2 - y == -1 and self.col == 'b') and x2 - x == 0:
            if self.board.board[y2][x2].col is None:
                return True
            else:
                return False
        elif (abs(x2 - x) == 1 and (y2 - y == 1 and self.col == 'w' or y2 - y == -1 and self.col == 'b')
              and self.board.board[y2][x2].col != self.col):
            return True
        else:
            return False


class Rook(Figure):
    def can_move(self, pos2):
        x2, y2 = pos2
        x, y = self.x, self.y
        if x2 == x or y2 == y:
            if x2 == x:
                for y1 in range(min(y, y2) + 1, max(y, y2) + 1):
                    if self.board.board[y1][x].col == self.col:
                        if self.board.board[y1][x] == self:
                            continue
                        print(1)
                        return False
                return True
            elif y2 == y:
                for x1 in range(min(x, x2), max(x, x2)):
                    if self.board.board[y][x1].col == self.col:
                        if self.board.board[y][x1] == self:
                            continue

                        return False
                return True
        else:
            return False


class Knight(Figure):
    def can_move(self, pos2):
        x2, y2 = pos2
        x, y = self.x, self.y
        if abs(x2 - x) == 2 and abs(y2 - y) == 1 or abs(x2 - x) == 1 and abs(y2 - y) == 2:
            return True
        else:
            return False


class Bishop(Figure):
    def can_move(self, pos2):
        x2, y2 = pos2
        x, y = self.x, self.y
        if x2 != x:
            mx = abs(x2 - x) // (x2 - x)
        else:
            mx = 1
        if y2 != y:
            my = abs(y2 - y) // (y2 - y)
        else:
            my = 1
        if abs(x2 - x) == abs(y2 - y):
            for i in range(1, abs(x2 - x)):
                if self.board.board[y + i * my][x + i * mx].col == self.col:
                    return False
            return True
        else:
            return False


class Queen(Figure):
    def can_move(self, pos2):
        x2, y2 = pos2
        x, y = self.x, self.y
        if x2 == x or y2 == y or abs(x2 - x) == abs(y2 - y):
            if x2 == x:
                for y1 in range(min(y, y2) + 1, max(y, y2) + 1):
                    if self.board.board[y1][x].col == self.col:
                        if self.board.board[y1][x] == self:
                            continue
                        return False
                return True
            elif y2 == y:
                for x1 in range(min(x, x2) + 1, max(x, x2) + 1):
                    if self.board.board[y][x1].col == self.col:
                        if self.board.board[y][x1] == self:
                            continue
                        return False
                return True
            elif abs(x2 - x) == abs(y2 - y):
                mx = abs(x2 - x) // (x2 - x)
                my = abs(y2 - y) // (y2 - y)
                for i in range(1, abs(x2 - x)):
                    if type(self.board.board[y + i * my][x + i * mx]) != Empty:
                        return False
                return True
        else:
            return False


class King(Figure):
    def can_move(self, pos2):
        x2, y2 = pos2
        x, y = self.x, self.y
        if (abs(x2 - x) == 1 or x2 == x) and (abs(y2 - y) == 1 or y2 == y):
            return True
        else:
            return False
