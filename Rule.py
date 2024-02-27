import Figures


class Classic_Rule():
    def __init__(self):
        self.board = None
        self.size = 8
        self.cell_size = 90
        self.left = 20
        self.top = 20
        self.max_time = 5 * 60
        self.mw

    def add_figures(self, board):
        self.board = [[Figures.Empty(board, (x, y)) for x in range(self.size)] for y in range(self.size)]
        for i in range(self.size):
            self.board[1][i] = Figures.Pawn(board, (i, 1), 'w')
        self.board[0][0], self.board[0][7] = (Figures.Rook(board, (0, 0), 'w'),
                                              Figures.Rook(board, (7, 0), 'w'))
        self.board[0][1], self.board[0][6] = (Figures.Knight(board, (1, 0), 'w'),
                                              Figures.Knight(board, (6, 0), 'w'))
        self.board[0][2], self.board[0][5] = (Figures.Bishop(board, (2, 0), 'w'),
                                              Figures.Bishop(board, (5, 0), 'w'))
        self.board[0][3], self.board[0][4] = (Figures.Queen(board, (3, 0), 'w'),
                                              Figures.King(board, (4, 0), 'w'))

        for i in range(self.size):
            self.board[6][i] = Figures.Pawn(board, (i, 6), 'b')
        self.board[7][0], self.board[7][7] = (Figures.Rook(board, (0, 7), 'b'),
                                              Figures.Rook(board, (7, 7), 'b'))
        self.board[7][1], self.board[7][6] = (Figures.Knight(board, (1, 7), 'b'),
                                              Figures.Knight(board, (6, 7), 'b'))
        self.board[7][2], self.board[7][5] = (Figures.Bishop(board, (2, 7), 'b'),
                                              Figures.Bishop(board, (5, 7), 'b'))
        self.board[7][3], self.board[7][4] = (Figures.Queen(board, (3, 7), 'b'),
                                              Figures.King(board, (4, 7), 'b'))

        # for i in range(self.size):
        #     for j in range(self.size):
        #         print(self.board[i][j], end=" ")
        #     print()
