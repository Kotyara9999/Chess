import Figures


class Classic_Rule():
    def __init__(self):
        self.size = 8
        self.cell_size = 90
        self.left = 20
        self.top = 20
        self.board = [[0 for j in range(self.size)] for i in range(self.size)]

    def add_figures(self, board):
        for i in range(self.size):
            self.board[1][i] = Figures.Pawn(board, (i, 1))
        self.board[0][0], self.board[0][7] = Figures.Rook(board, (0, 0)), Figures.Rook(board, (7, 0))
        # for i in range(self.size):
        #     for j in range(self.size):
        #         print(self.board[i][j], end=" ")
        #     print()

