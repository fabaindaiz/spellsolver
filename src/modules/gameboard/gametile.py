from src.utils import get_letter_point_value

Coordinates = tuple[int, int]


class GameTile:
    def __init__(self, letter: str, coordinates: Coordinates) -> None:
        self.coordinates: Coordinates = coordinates
        self.neighbors: list["GameTile"] = []

        self._has_gem: bool = False
        self.letter: str = letter
        self.letter_multiplier: int = 1
        self.word_multiplier: int = 1

        self.is_swapped: bool = False

    def __str__(self) -> str:
        return f"({self.letter} {self.coordinates})"

    @property
    def has_gem(self) -> bool:
        return self._has_gem

    @has_gem.setter
    def has_gem(self, value: bool) -> None:
        self._has_gem = value

    @property
    def letter_points(self) -> int:
        return get_letter_point_value(self.letter)

    @property
    def points(self) -> int:
        return self.letter_points * self.letter_multiplier

    def copy(self, letter: str) -> "GameTile":
        node = GameTile(letter, self.coordinates)
        node.letter_multiplier = self.letter_multiplier
        node.word_multiplier = self.word_multiplier
        node.is_swapped = True

        return node

    def init_neighbors(self, tiles: dict[Coordinates, "GameTile"]) -> None:
        x, y = self.coordinates
        grid_size = 5

        neighbor_coordinates = [
            (x + dx, y + dy)
            for dx in range(-1, 2)
            for dy in range(-1, 2)
            if (0 <= x + dx < grid_size)
            and (0 <= y + dy < grid_size)
            and (dx, dy) != (0, 0)
        ]

        for coordinate in neighbor_coordinates:
            tile = tiles.get(coordinate)

            if tile:
                self.neighbors.append(tile)

    def suggest_tile(self, path):
        suggested_tiles = [tile for tile in self.neighbors if tile not in path]

        yield from suggested_tiles
