from typing import Tuple, Dict, List, Generator

from src.utils.utils import get_letter_point_value

NEIGHBOR_OFFSETS = [
    (x, y) for x in range(-1, 2) for y in range(-1, 2) if (x, y) != (0, 0)
]


class GameTile:
    def __init__(self, letter: str, cord: Tuple[int, int]) -> None:
        self.letter: str = letter
        self.cord: Tuple[int, int] = cord
        self.swap: bool = False

        self.letter_points: int = get_letter_point_value(letter)
        self.letter_gems: int = 0
        self.letter_mult: int = 1
        self.word_mult: int = 1

        self.neighbors: List[GameTile] = []

    def copy(self, letter: str) -> "GameTile":
        node = GameTile(letter, self.cord)
        node.swap = True

        node.letter_mult = self.letter_mult
        node.word_mult = self.word_mult
        return node

    def points(self) -> int:
        return self.letter_points * self.letter_mult

    def gems(self) -> int:
        return self.letter_gems

    def init_neighbors(self, tiles: Dict[Tuple[int, int], "GameTile"]) -> None:
        x, y = self.cord
        neighbors_cords = (
            (x + dx, y + dy)
            for dx, dy in NEIGHBOR_OFFSETS
            if 0 <= x + dx < 5 and 0 <= y + dy < 5
        )
        self.neighbors.extend(tiles[cord] for cord in neighbors_cords)

    def suggest_tile(self, path: List["GameTile"]) -> Generator["GameTile", None, None]:
        return (tile for tile in self.neighbors if tile not in path)

    def __str__(self) -> str:
        return f"({self.letter} {self.cord})"
