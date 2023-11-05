from typing import List, Tuple


class MenuHandler:
    def __init__(self, board) -> None:
        """
        Initialize a MenuHandler for managing menu options on the game board.

        Args:
            board: The game board.
        """
        self.board = board

        self.word_cord: Tuple[int, int] = None
        self.letter_cord: Tuple[int, int] = None
        self.letter_mult: int = None

        self.letter_gems: List[Tuple[int, int]] = []

    def set_mult_word(self, cord: tuple) -> None:
        """
        Set a word multiplier at the specified coordinate.

        Args:
            cord (tuple): The coordinate for setting the word multiplier.
        """
        self.remove_mult_cord(cord)
        if self.word_cord is not None:
            self.board.tiles[self.word_cord].multiplier("black")

        self.word_cord = cord
        self.board.tiles[cord].multiplier("deep pink")

    def set_mult_letter(self, cord: tuple, mult: int) -> None:
        """
        Set a letter multiplier at the specified coordinate with a specified multiplier.

        Args:
            cord (tuple): The coordinate for setting the letter multiplier.
            mult (int): The multiplier value.
        """
        self.remove_mult_cord(cord)
        if self.letter_cord is not None:
            self.board.tiles[self.letter_cord].multiplier("black")

        self.letter_mult = mult
        self.letter_cord = cord
        self.board.tiles[cord].multiplier("gold")

    def remove_mult_cord(self, cord: tuple) -> None:
        """
        Remove any multipliers set at the specified coordinate.

        Args:
            cord (tuple): The coordinate for removing multipliers.
        """
        if self.word_cord == cord:
            self.board.tiles[cord].multiplier("black")
            self.word_cord = None
        if self.letter_cord == cord:
            self.board.tiles[cord].multiplier("black")
            self.letter_cord = None

    def remove_mult_all(self) -> None:
        """
        Remove all multipliers set on the board.
        """
        if self.word_cord is not None:
            self.board.tiles[self.word_cord].multiplier("black")
            self.word_cord = None
        if self.letter_cord is not None:
            self.board.tiles[self.letter_cord].multiplier("black")
            self.letter_cord = None

    def set_gem_letter(self, cord: tuple) -> None:
        """
        Set a gem letter at the specified coordinate.

        Args:
            cord (tuple): The coordinate for setting a gem letter.
        """
        self.remove_mult_cord(cord)

        self.letter_gems.append(cord)
        self.board.tiles[cord].multiplier("blue")

    def remove_gem_cord(self, cord: tuple) -> None:
        """
        Remove a gem letter at the specified coordinate.

        Args:
            cord (tuple): The coordinate for removing a gem letter.
        """
        if cord in self.letter_gems:
            self.letter_gems.remove(cord)
            self.board.tiles[cord].multiplier("black")

    def remove_gem_all(self) -> None:
        """
        Remove all gem letters set on the board.
        """
        self.letter_gems = []
        for tile in self.letter_gems:
            self.board.tiles[tile].multiplier("black")

    def unhover_tiles(self) -> None:
        """
        Unhover all tiles with multipliers set.
        """
        if self.word_cord is not None:
            self.board.tiles[self.word_cord].multiplier("deep pink")
        if self.letter_cord is not None:
            self.board.tiles[self.letter_cord].multiplier("gold")
        for tile in self.letter_gems:
            self.board.tiles[tile].multiplier("blue")
