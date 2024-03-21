from typing import Generator

from src.entities import Coordinates
from src.utils import get_letter_point_value


class GameTile:
    def __init__(self, letter: str, coordinates: Coordinates):
        self.letter: str = letter
        self.coordinates: Coordinates = coordinates
        self.neighbours: list["GameTile"] = []

        self._points: int = get_letter_point_value(letter)
        self._swapped: bool = False
        self._blocked: bool = False
        self._has_gem: bool = False

        self.tile_mult: int = 1
        self.word_mult: int = 1

    def __str__(self) -> str:
        return f"({self.letter} {self.coordinates})"

    @property
    def points(self) -> int:
        return self._points * self.tile_mult

    @property
    def swapped(self) -> bool:
        return self._swapped

    @property
    def blocked(self) -> bool:
        return self._blocked

    @blocked.setter
    def blocked(self, value: bool) -> None:
        self._blocked = value

    @property
    def has_gem(self) -> bool:
        return self._has_gem

    @has_gem.setter
    def has_gem(self, value: bool) -> None:
        self._has_gem = value

    @swapped.setter
    def swapped(self, value: bool) -> None:
        self._swapped = value

    def init_neighbors(self, tiles: dict[Coordinates, "GameTile"]) -> None:
        x, y = self.coordinates
        grid_size = 5

        neighbor_coordinates = [
            Coordinates(x + dx, y + dy)
            for dx in range(-1, 2)
            for dy in range(-1, 2)
            if (0 <= x + dx < grid_size)
            and (0 <= y + dy < grid_size)
            and (dx, dy) != (0, 0)
        ]

        for coordinates in neighbor_coordinates:
            self.neighbours.append(tiles[coordinates])

    def _validate(self, path: list["GameTile"]) -> bool:
        return (self not in path) and (not self.blocked)

    def suggest_tiles(
        self, path: list["GameTile"]
    ) -> Generator["GameTile", None, None]:
        yield from (tile for tile in self.neighbours if tile._validate(path))
