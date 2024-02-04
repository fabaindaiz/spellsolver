from typing import Optional

from src.entities import Coordinates


class MenuHandler:
    def __init__(self, parent) -> None:
        self.parent = parent

        self.word_coord: Optional[Coordinates] = None
        self.letter_coord: Optional[Coordinates] = None
        self.letter_mult: Optional[int] = None

        self.letter_gems: list[Coordinates] = []
        self.letter_ices: list[Coordinates] = []

    def set_mult_word(self, coordinates: Coordinates) -> None:
        self.remove_mult_cord(coordinates)
        if self.word_coord is not None:
            self.parent.tiles[self.word_coord].multiplier("black")

        self.word_coord = coordinates
        self.parent.tiles[coordinates].multiplier("deep pink")

    def set_mult_letter(self, coordinates: Coordinates, mult: int) -> None:
        self.remove_mult_cord(coordinates)
        if self.letter_coord is not None:
            self.parent.tiles[self.letter_coord].multiplier("black")

        self.letter_mult = mult
        self.letter_coord = coordinates
        self.parent.tiles[coordinates].multiplier("gold")

    def remove_mult_cord(self, coordinates: Coordinates) -> None:
        if self.word_coord == coordinates:
            self.parent.tiles[coordinates].multiplier("black")
            self.word_coord = None
        if self.letter_coord == coordinates:
            self.parent.tiles[coordinates].multiplier("black")
            self.letter_coord = None

    def remove_mult_all(self) -> None:
        if self.word_coord is not None:
            self.parent.tiles[self.word_coord].multiplier("black")
            self.word_coord = None
        if self.letter_coord is not None:
            self.parent.tiles[self.letter_coord].multiplier("black")
            self.letter_coord = None

    def set_gem_letter(self, coordinates: Coordinates) -> None:
        self.remove_mult_cord(coordinates)

        self.letter_gems.append(coordinates)
        self.parent.tiles[coordinates].multiplier("blue")

    def remove_gem_cord(self, coordinates: Coordinates) -> None:
        if coordinates in self.letter_gems:
            self.letter_gems.remove(coordinates)
            self.parent.tiles[coordinates].multiplier("black")

    def remove_gem_all(self) -> None:
        for tile in self.letter_gems:
            self.parent.tiles[tile].multiplier("black")
        self.letter_gems = []
    
    def set_ice_letter(self, coordinates: Coordinates) -> None:
        self.remove_mult_cord(coordinates)

        self.letter_ices.append(coordinates)
        self.parent.tiles[coordinates].multiplier("violet")
    
    def remove_ice_cord(self, coordinates: Coordinates) -> None:
        if coordinates in self.letter_ices:
            self.letter_ices.remove(coordinates)
            self.parent.tiles[coordinates].multiplier("black")
        
    def remove_ice_all(self) -> None:
        for tile in self.letter_ices:
            self.parent.tiles[tile].multiplier("black")
        self.letter_ices = []

    def unhover_tiles(self) -> None:
        if self.word_coord is not None:
            self.parent.tiles[self.word_coord].multiplier("deep pink")
        if self.letter_coord is not None:
            self.parent.tiles[self.letter_coord].multiplier("gold")
        for tile in self.letter_gems:
            self.parent.tiles[tile].multiplier("blue")
