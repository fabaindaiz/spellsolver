from typing import Dict, Tuple

from src.utils import (
    aux_to_indices,
    is_valid_word,
)
from .gametile import GameTile


class GameBoard:
    """Represents a Spellcast gameboard"""

    def __init__(self) -> None:
        self.tiles: Dict[Tuple[int, int], GameTile] = {}

    def load(self, gameboard: str) -> None:
        gameboard = gameboard.lower()

        if not is_valid_word(gameboard) or len(gameboard) != 25:
            raise Exception("Gameboard init error")

        for aux, letter in enumerate(gameboard):
            cord = aux_to_indices(aux)
            self.tiles[cord] = GameTile(letter, cord)

        for node in self.tiles.values():
            node.init_neighbors(self.tiles)

    def set_mult_word(self, mult_cord: int) -> None:
        """Set a mult_word in a tile"""
        self.tiles[mult_cord].word_mult = 2

    def set_mult_letter(self, mult_cord: tuple, mult: int) -> None:
        """Set a mult_letter in a tile"""
        self.tiles[mult_cord].letter_mult = mult

    def set_gems(self, gem_cord: Tuple[Tuple[int, int], ...]) -> None:
        """Set a list of gems in the board"""
        for cord in gem_cord:
            self.tiles[cord].letter_gems = 1

    def get_base_tile(self) -> GameTile:
        """Get the base tile"""
        base_tile = GameTile("0", (-1, -1))
        base_tile.neighbors = list(self.tiles.values())
        return base_tile


if __name__ == "__main__":
    gameboard = GameBoard()

    gameboard_string = input("Insert a gameboard: ")
    gameboard.load(gameboard_string)

    def print_gameboard(gameboard: GameBoard):
        """Return a string representation of a GameBoard"""
        r = tuple(gameboard.tiles.values())
        return "\n".join(
            " ".join(l.letter for l in r[i * 5 : (i + 1) * 5]) for i in range(5)
        )

    print(print_gameboard(gameboard))
