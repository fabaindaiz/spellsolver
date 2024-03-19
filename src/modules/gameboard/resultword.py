from collections.abc import Generator
from typing import Any

from src import DEBUG, GEMS_MULT, WORD_MULT
from .gamepath import GamePath
from .gametile import GameTile

type StringGenerator = Generator[str, None, None]


# TODO: Refactor this class to use a dataclass
class ResultWord:
    def __init__(
        self,
        word: str,
        path: tuple[GameTile, ...],
        swaps: tuple[int, ...],
    ) -> None:
        self.word: str = word
        self.path: tuple[GameTile, ...] = path
        self.gems: int = GamePath.calculate_gems(self.path)
        self.points: int = GamePath.calculate_points(self.path)
        self.swaps: tuple[int, ...] = swaps

    def _str(self) -> StringGenerator:
        initial_info = self._format_initial_info()
        swaps = self._format_swaps()

        yield from [initial_info, *swaps]

        if not DEBUG:
            return

        yield self._debug_info()

    def _format_initial_info(self) -> str:
        initial_coordinates = self.path[0].coordinates

        return f"{self.points} {self.word} {initial_coordinates}"

    def _format_swaps(self) -> StringGenerator:
        for swap_index in self.swaps:
            word_at_swap = self.word[swap_index]
            coordinates_of_swap = self.path[swap_index].coordinates

            yield f"{word_at_swap} {coordinates_of_swap}"

    def _debug_info(self) -> str:
        debug_info = []

        for tile in self.path:
            tile_str = str(tile)
            debug_info.append(tile_str)

        return str(debug_info)

    @property
    def total_value(self) -> int:
        points_component = self.points * WORD_MULT
        gems_component = self.gems * GEMS_MULT

        return points_component + gems_component

    @property
    def label(self) -> str:
        points_symbol = "🌟"
        gems_symbol = "♦️"
        word_padding = 12

        word_presentation = self.word.ljust(word_padding)
        points_presentation = f"{self.points}{points_symbol}"
        gems_presentation = f"{self.gems}{gems_symbol}"

        return f"{word_presentation} {points_presentation} {gems_presentation}"

    @property
    def text(self) -> str:
        separator = " | "
        string_repr = self._str()
        joined_string = separator.join(string_repr)

        return f"{joined_string}"

    def dict(self) -> dict[str, Any]:
        path_coordinates = []

        for node in self.path:
            node_coords_str = str(node.coordinates)
            path_coordinates.append(node_coords_str)

        return {
            "points": self.points,
            "gems": self.gems,
            "word": self.word,
            "path": path_coordinates,
            "swap": self.swaps,
        }
