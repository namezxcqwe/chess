from src.piece import Piece


class Bishop(Piece):
    def char(self):
        return 'B'

    def can_move(self, board, row: int, col: int, row_1: int, col_1: int) -> bool:
        return abs(row - row_1) == abs(col - col_1)

    def can_attack(self, board, row: int, col: int, row_1: int, col_1: int) -> bool:
        return self.can_move(board, row, col, row_1, col_1)
