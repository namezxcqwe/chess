from src.piece import Piece


class King(Piece):
    castling = True

    def char(self):
        return 'K'

    def can_move(self, board, row: int, col: int, row_1: int, col_1: int) -> bool:
        offsets = [(0, 1), (1, 0), (1, 1)]
        offsets_castling = [(1, 7), (1, 3), (8, 7), (8, 3)]
        offsets_castling_rook = [(1, 8), (1, 1), (8, 8), (8, 1)]
        return (abs(row - row_1), abs(col - col_1)) in offsets

    def can_attack(self, board, row: int, col: int, row_1: int, col_1: int) -> bool:
        return self.can_move(board, row, col, row_1, col_1)