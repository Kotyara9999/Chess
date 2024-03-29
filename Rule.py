import Figures


class Classic_Rule():
    def __init__(self):
        self.board = None
        self.size = 8
        self.cell_size = 90
        self.left = 20
        self.top = 20
        self.max_time = 5 * 60
        self.mw = 16
        self.mb = 16
        self.pawn_start = (1, 6)

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


class Total_War():
    def __init__(self):
        self.board = None
        self.size = 13
        self.cell_size = 65
        self.left = 20
        self.top = 20
        self.max_time = 5 * 60
        self.mw = 20
        self.mb = 20
        self.pawn_start = (2, 10)

    def add_figures(self, board):
        self.board = [[Figures.Empty(board, (x, y)) for x in range(self.size)] for y in range(self.size)]
        for i in range(2, self.size - 2):
            self.board[2][i] = Figures.Pawn(board, (i, 2), 'w')
        self.board[1][2], self.board[1][10] = (Figures.Rook(board, (2, 1), 'w'),
                                               Figures.Rook(board, (10, 1), 'w'))
        self.board[1][3], self.board[1][9] = (Figures.Knight(board, (3, 1), 'w'),
                                              Figures.Knight(board, (9, 1), 'w'))
        self.board[1][4], self.board[1][8] = (Figures.Bishop(board, (4, 1), 'w'),
                                              Figures.Bishop(board, (8, 1), 'w'))
        self.board[1][6], self.board[0][6] = (Figures.Queen(board, (6, 1), 'w'),
                                              Figures.King(board, (6, 0), 'w'))

        for i in range(2, self.size - 2):
            self.board[10][i] = Figures.Pawn(board, (i, 10), 'b')
        self.board[11][2], self.board[11][10] = (Figures.Rook(board, (2, 11), 'b'),
                                                 Figures.Rook(board, (10, 11), 'b'))
        self.board[11][3], self.board[11][9] = (Figures.Knight(board, (3, 11), 'b'),
                                                Figures.Knight(board, (9, 11), 'b'))
        self.board[11][4], self.board[11][8] = (Figures.Bishop(board, (4, 11), 'b'),
                                                Figures.Bishop(board, (5, 11), 'b'))
        self.board[11][6], self.board[12][6] = (Figures.Queen(board, (6, 11), 'b'),
                                                Figures.King(board, (6, 12), 'b'))
