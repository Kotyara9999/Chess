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

    def can_move(self, pos2):
        return False

    def check_dest(self, pos2):
        x, y = pos2
        if self.board.board[self.y][self.x].col == self.board.board[y][x].col:
            return False
        else:
            return True

    def move(self, pos2):
        if self.can_move(pos2) and self.check_dest(pos2):
            board = self.board.board
            board[self.y][self.x], board[pos2[1]][pos2[0]] = Empty(self.board, pos2), board[self.y][self.x]
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
        if (y == 1 or y == 6) and abs(y2 - y) == 2 and x2 - x == 0:
            return True
        elif abs(y2 - y) == 1 and x2 - x == 0:
            return True
        elif abs(x2 - x) == 1 and y2 - y == 1 and type(self.board.board[y2][x2]) != Empty:
            return True
        else:
            return False


class Rook(Figure):
    def can_move(self, pos2):
        x2, y2 = pos2
        x, y = self.x, self.y
        if x2 == x or y2 == y:
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
        if abs(x2 - x) == abs(y2 - y):
            return True
        else:
            return False


class Queen(Figure):
    def can_move(self, pos2):
        x2, y2 = pos2
        x, y = self.x, self.y
        if x2 == x or y2 == y or abs(x2 - x) == abs(y2 - y):
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
