from dataclasses import dataclass
from typing import Iterator


@dataclass
class Coordinates:
    def __init__(self, x_coordinate: int, y_coordinate: int) -> None:
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

        self._coordinates = (self.x_coordinate, self.y_coordinate)

    def __hash__(self) -> int:
        return hash(self._coordinates)

    def __iter__(self) -> Iterator[int]:
        return iter(self._coordinates)

    def __str__(self) -> str:
        return f"{self._coordinates}"
