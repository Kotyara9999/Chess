class Figure:
    def __init__(self, board, pos):
        self.x, self.y = pos
        self.board = board
        self.image = f"{type(self).__name__}.png"

    def can_move(self, pos2):
        pass

    def move(self, pos2):
        pass


class Pawn(Figure):
    def __init__(self, board, pos):
        super().__init__(board, pos)

    def can_move(self, pos2):
        x2, y2 = pos2
        x, y = self.x, self.y
        if y == 2:
            if y2 - y == 2 and x2 - x == 0:
                return True
        elif y2 - y == 1 and x2 - x == 0:
            return True
        else:
            return False

    def move(self, pos2):
        if self.can_move(pos2):
            self.x = pos2[0]
            self.y = pos2[1]
            return True
        else:
            return False
        print(pos2)
