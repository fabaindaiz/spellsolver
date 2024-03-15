from dataclasses import dataclass
from typing import Iterator


@dataclass
class Coordinates:
    x_coordinate: int
    y_coordinate: int

    @classmethod
    def from_string(cls, coordinates: str) -> "Coordinates":
        x, y = coordinates
        return cls(int(x), int(y))

    @property
    def _as_tuple(self) -> tuple[int, int]:
        return self.x_coordinate, self.y_coordinate

    def __hash__(self) -> int:
        return hash(self._as_tuple)

    def __iter__(self) -> Iterator[int]:
        return iter(self._as_tuple)

    def __str__(self) -> str:
        return f"{self._as_tuple}"
