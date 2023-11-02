from typing import List, Tuple

from src.interfaces.graphicalui.board import Board


class MenuHandler:
    def __init__(self, board: Board) -> None:
        self.board: Board = board

        self.word_cord: Tuple[int, int] = None
        self.letter_cord: Tuple[int, int] = None
        self.letter_mult: int = None

        self.letter_gems: List[Tuple[int, int]] = []

    def set_mult_word(self, cord: tuple) -> None:
        self.remove_mult_cord(cord)
        if self.word_cord is not None:
            self.board.tiles[self.word_cord].multiplier("black")

        self.word_cord = cord
        self.board.tiles[cord].multiplier("deep pink")

    def set_mult_letter(self, cord: tuple, mult: int) -> None:
        self.remove_mult_cord(cord)
        if self.letter_cord is not None:
            self.board.tiles[self.letter_cord].multiplier("black")

        self.letter_mult = mult
        self.letter_cord = cord
        self.board.tiles[cord].multiplier("gold")

    def remove_mult_cord(self, cord: tuple) -> None:
        if self.word_cord == cord:
            self.board.tiles[cord].multiplier("black")
            self.word_cord = None
        if self.letter_cord == cord:
            self.board.tiles[cord].multiplier("black")
            self.letter_cord = None
    
    def remove_mult_all(self) -> None:
        if self.word_cord is not None:
            self.board.tiles[self.word_cord].multiplier("black")
            self.word_cord = None
        if self.letter_cord is not None:
            self.board.tiles[self.letter_cord].multiplier("black")
            self.letter_cord = None
    
    
    def set_gem_letter(self, cord: tuple) -> None:
        self.remove_mult_cord(cord)

        self.letter_gems.append(cord)
        self.board.tiles[cord].multiplier("blue")

    def remove_gem_all(self) -> None:
        for tile in self.letter_gems:
            self.board.tiles[tile].multiplier("black")

        self.letter_gems = []


    def unhover_tiles(self) -> None:
        if self.word_cord is not None:
            self.board.tiles[self.word_cord].multiplier("deep pink")
        if self.letter_cord is not None:
            self.board.tiles[self.letter_cord].multiplier("gold")
        for tile in self.letter_gems:
            self.board.tiles[tile].multiplier("blue")
