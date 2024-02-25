class Figure:
    def __init__(self, board, pos):
        self.x, self.y = pos
        self.board = board
        self.image = f"{type(self).__name__}.png"
        self.grabbed = False

    def can_move(self, pos2):
        pass

    def move(self, pos2):
        if self.can_move(pos2):
            self.x = pos2[0]
            self.y = pos2[1]
            return True
        else:
            return False


class Pawn(Figure):
    def can_move(self, pos2):
        x2, y2 = pos2
        x, y = self.x, self.y
        if y == 1 and y2 - y == 2 and x2 - x == 0:
            return True
        elif y2 - y == 1 and x2 - x == 0:
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

