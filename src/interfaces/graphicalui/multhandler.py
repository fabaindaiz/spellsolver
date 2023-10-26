from typing import List, Tuple

from src.interfaces.graphicalui.board import Board


class MenuHandler:
    def __init__(self, board: Board) -> None:
        self.board: Board = board

        self.mult_cord: Tuple[int, int] = None
        self.letter_mult: Tuple[int, int] = None
        self.letter_cord: Tuple[int, int] = None
        self.letter_gems: List[Tuple[int, int]] = None

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

    def remove_mult(self, cord: tuple) -> None:
        if self.letter_cord is not None:
            self.board.tiles[self.letter_cord].multiplier("black")
        if self.mult_cord is not None:
            self.board.tiles[self.mult_cord].multiplier("black")

        self.letter_cord = None
        self.mult_cord = None
    
    def set_gems_letter(self) -> None:
        pass
    
    def configure_gems(self) -> None:
        pass

    def remove_gems(self, cord: tuple) -> None:
        pass
