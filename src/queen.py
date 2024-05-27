from src.piece import Piece


class Queen(Piece):
    def char(self):
        return 'Q'

    def can_move(self, board, row: int, col: int, row_1: int, col_1: int) -> bool:
        offsets = [(0, 1), (1, 0), (1, 1)]
        return abs(row - row_1) == abs(col - col_1) or \
            row == row_1 or col == col_1 or \
            (abs(row - row_1), abs(col - col_1)) in offsets

    def can_attack(self, board, row: int, col: int, row_1: int, col_1: int) -> bool:
        return self.can_move(board, row, col, row_1, col_1)