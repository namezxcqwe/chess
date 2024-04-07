from src.color import Color
from src.pawn import Pawn
from src.knight import Knight
from src.rock import Rock
from src.king import King
from src.queen import Queen
from src.bishop import Bishop


class Board:
    def __init__(self):
        self.__field = []
        self.__color = Color.WHITE
        for _ in range(8):
            self.__field.append([None] * 8)
        self.__fill()

    def __fill(self):
        for col in range(8):
            self.__field[1][col] = Pawn(Color.WHITE)
            self.__field[6][col] = Pawn(Color.BLACK)
        for col in [1, 6]:
            self.__field[0][col] = Knight(Color.WHITE)
            self.__field[7][col] = Knight(Color.BLACK)
        for col in [0, 7]:
            self.__field[0][col] = Rock(Color.WHITE)
            self.__field[7][col] = Rock(Color.BLACK)
        for col in [4]:
            self.__field[0][col] = King(Color.WHITE)
            self.__field[7][col] = King(Color.BLACK)
        for col in [3]:
            self.__field[0][col] = Queen(Color.WHITE)
            self.__field[7][col] = Queen(Color.BLACK)
        for col in [2, 5]:
            self.__field[0][col] = Bishop(Color.WHITE)
            self.__field[7][col] = Bishop(Color.BLACK)

    @property
    def current_player(self):
        return self.__color

    @property
    def field(self):
        return tuple([tuple(row) for row in self.__field])

    def get_piece(self, row: int, col: int):
        if 1 <= row <= 9 and 1 <= col <= 9:
            return self.field[row - 1][col - 1]
        return None