from src.interfaces.board import Board


class MultHandler:
    def __init__(self, board: Board) -> None:
        self.board: Board = board

        self.mult_cord: tuple = None
        self.letter_mult: int = None
        self.letter_cord: tuple = None

    def set_mult_word(self, cord: tuple) -> None:
        if self.mult_cord is not None:
            self.board.tiles[self.mult_cord].multiplier("black")

        self.mult_cord = cord
        self.configure_mult()

    def set_mult_letter(self, cord: tuple, mult: int) -> None:
        if self.letter_cord is not None:
            self.board.tiles[self.letter_cord].multiplier("black")

        self.letter_mult = mult
        self.letter_cord = cord
        self.configure_mult()

    def configure_mult(self) -> None:
        if self.letter_cord is not None:
            self.board.tiles[self.letter_cord].multiplier("gold")
        if self.mult_cord is not None:
            self.board.tiles[self.mult_cord].multiplier("deep pink")

    def remove_mult(self) -> None:
        if self.letter_cord is not None:
            self.board.tiles[self.letter_cord].multiplier("black")
        if self.mult_cord is not None:
            self.board.tiles[self.mult_cord].multiplier("black")

        self.letter_cord = None
        self.mult_cord = None
