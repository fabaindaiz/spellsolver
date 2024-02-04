from typing import Optional

from src.entities import Coordinates


class MenuHandler:
    """Class to handle the menu options for the game board tiles"""
    # TODO: Refactor this class

    def __init__(self, parent) -> None:
        self.parent = parent

        self.word_coord: Optional[Coordinates] = None
        self.letter_coord: Optional[Coordinates] = None
        self.letter_mult: Optional[int] = None

        self.letter_gems: list[Coordinates] = []
        self.letter_ices: list[Coordinates] = []

    def set_mult_word(self, coordinates: Coordinates) -> None:
        """Set the word multiplier for the tile"""
        self.remove_mult_cord(coordinates)
        self.remove_gem_cord(coordinates)
        self.remove_ice_cord(coordinates)
        if self.word_coord is not None:
            self.parent.tiles[self.word_coord].multiplier("black")
        
        self.word_coord = coordinates
        self.parent.tiles[coordinates].multiplier("deep pink")

    def set_mult_letter(self, coordinates: Coordinates, mult: int) -> None:
        """Set the letter multiplier for the tile"""
        self.remove_mult_cord(coordinates)
        self.remove_gem_cord(coordinates)
        self.remove_ice_cord(coordinates)
        if self.letter_coord is not None:
            self.parent.tiles[self.letter_coord].multiplier("black")

        self.letter_mult = mult
        self.letter_coord = coordinates
        self.parent.tiles[coordinates].multiplier("gold")

    def remove_mult_cord(self, coordinates: Coordinates) -> None:
        """Remove the multiplier from the tile at the given coordinates"""
        if self.word_coord == coordinates:
            self.parent.tiles[coordinates].multiplier("black")
            self.word_coord = None
        if self.letter_coord == coordinates:
            self.parent.tiles[coordinates].multiplier("black")
            self.letter_coord = None

    def remove_mult_all(self) -> None:
        """Remove all the multipliers from the tiles"""
        if self.word_coord is not None:
            self.parent.tiles[self.word_coord].multiplier("black")
            self.word_coord = None
        if self.letter_coord is not None:
            self.parent.tiles[self.letter_coord].multiplier("black")
            self.letter_coord = None

    def set_gem_letter(self, coordinates: Coordinates) -> None:
        """Set the gem on the tile at the given coordinates"""
        self.remove_mult_cord(coordinates)
        self.remove_ice_cord(coordinates)

        self.letter_gems.append(coordinates)
        self.parent.tiles[coordinates].multiplier("violet")

    def remove_gem_cord(self, coordinates: Coordinates) -> None:
        """Remove the gem from the tile at the given coordinates"""
        if coordinates in self.letter_gems:
            self.letter_gems.remove(coordinates)
            self.parent.tiles[coordinates].multiplier("black")

    def remove_gem_all(self) -> None:
        """Remove all the gems from the tiles"""
        for tile in self.letter_gems:
            self.parent.tiles[tile].multiplier("black")
        self.letter_gems = []
    
    def set_ice_letter(self, coordinates: Coordinates) -> None:
        """Set the ice on the tile at the given coordinates"""
        self.remove_mult_cord(coordinates)
        self.remove_gem_cord(coordinates)

        self.letter_ices.append(coordinates)
        self.parent.tiles[coordinates].multiplier("blue")
    
    def remove_ice_cord(self, coordinates: Coordinates) -> None:
        """Remove the ice from the tile at the given coordinates"""
        if coordinates in self.letter_ices:
            self.letter_ices.remove(coordinates)
            self.parent.tiles[coordinates].multiplier("black")
        
    def remove_ice_all(self) -> None:
        """Remove all the ices from the tiles"""
        for tile in self.letter_ices:
            self.parent.tiles[tile].multiplier("black")
        self.letter_ices = []

    def unhover_tiles(self) -> None:
        """Remove the hover effect from the tiles"""
        if self.word_coord is not None:
            self.parent.tiles[self.word_coord].multiplier("deep pink")
        if self.letter_coord is not None:
            self.parent.tiles[self.letter_coord].multiplier("gold")
        
        for tile in self.letter_gems:
            self.parent.tiles[tile].multiplier("violet")
        for tile in self.letter_ices:
            self.parent.tiles[tile].multiplier("blue")
