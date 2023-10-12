from typing import Generator, Dict, List, Tuple
from src.utils.utils import get_coordinate, letter_points, valid_word

NEIGHBOR_OFFSETS = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


class GameTile:
    """Respresents a Spellcast tile"""

    def __init__(self, letter: str, cord: Tuple[int, int]) -> None:
        self.letter: str = letter
        self.cord: Tuple[int, int] = cord
        self.swap: bool = False

        self.letter_points: int = letter_points(letter)
        self.letter_mult: int = 1
        self.word_mult: int = 1

        self.neighbors: List[GameTile] = []

    def copy(self, letter: str) -> "GameTile":
        """Makes a copy of a Gametile"""
        node = GameTile(letter, self.cord)
        node.swap = True

        node.letter_mult = self.letter_mult
        node.word_mult = self.word_mult
        return node

    def points(self) -> int:
        """Gets points value of actual tile"""
        return self.letter_points * self.letter_mult

    def init_neighbors(self, tiles: Dict[Tuple[int, int], "GameTile"]) -> None:
        """Init neighbors of actual tile"""
        x, y = self.cord
        neighbors_cords = (
            (x + dx, y + dy) for dx, dy in NEIGHBOR_OFFSETS if 0 <= x + dx < 5 and 0 <= y + dy < 5
        )
        self.neighbors.extend(tiles[cord] for cord in neighbors_cords)

    def suggest_tile(self, path: List["GameTile"]) -> Generator["GameTile", None, None]:
        """Get all nodes in neighbors that are not in path"""
        return (tile for tile in self.neighbors if tile not in path)


class GameBoard:
    """Represents a Spellcast gameboard"""

    def __init__(self) -> None:
        self.tiles: Dict[Tuple[int, int], GameTile] = {}

    def load(self, gameboard: str) -> None:
        gameboard = gameboard.lower()

        if not valid_word(gameboard) or len(gameboard) != 25:
            raise Exception("Gameboard init error")

        for aux, letter in enumerate(gameboard):
            cord = get_coordinate(aux)
            self.tiles[cord] = GameTile(letter, cord)

        for node in self.tiles.values():
            node.init_neighbors(self.tiles)

    def set_mult_word(self, mult_cord: int) -> None:
        """Set a mult_word in a tile"""
        self.tiles[mult_cord].word_mult = 2

    def set_mult_letter(self, mult_cord: tuple, mult: int) -> None:
        """Set a mult_letter in a tile"""
        self.tiles[mult_cord].letter_mult = mult


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
