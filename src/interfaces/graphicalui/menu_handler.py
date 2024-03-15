from src.entities import Coordinates


class MenuHandler:
    """Class to handle the menu options for the game board tiles"""

    # TODO: Refactor this class

    def __init__(self, parent) -> None:
        self.parent = parent

        self.gems: list[Coordinates] = []
        self.ices: list[Coordinates] = []

        self.x2_mult: list[Coordinates] = []
        self.dl_mult: list[Coordinates] = []
        self.tl_mult: list[Coordinates] = []

    def set_gem(self, coordinates: Coordinates) -> None:
        self.gems.append(coordinates)
        self.parent.tiles[coordinates].multiplier("violet")

    def set_ice(self, coordinates: Coordinates) -> None:
        self.ices.append(coordinates)
        self.parent.tiles[coordinates].multiplier("blue")

    def set_x2_mult(self, coordinates: Coordinates) -> None:
        self.x2_mult.append(coordinates)
        self.parent.tiles[coordinates].multiplier("deep pink")

    def set_dl_mult(self, coordinates: Coordinates) -> None:
        self.dl_mult.append(coordinates)
        self.parent.tiles[coordinates].multiplier("gold")

    def set_tl_mult(self, coordinates: Coordinates) -> None:
        self.tl_mult.append(coordinates)
        self.parent.tiles[coordinates].multiplier("gold")

    def remove_gems(self) -> None:
        self.gems = []
        self.unhover_tiles()

    def remove_ices(self) -> None:
        self.ices = []
        self.unhover_tiles()

    def remove_mults(self) -> None:
        self.x2_mult = []
        self.dl_mult = []
        self.tl_mult = []
        self.unhover_tiles()

    def unhover_tiles(self) -> None:
        """Remove the hover effect from the tiles"""
        for tile in self.parent.tiles.values():
            tile.multiplier("black")
        for gem in self.gems:
            self.parent.tiles[gem].multiplier("violet")
        for ice in self.ices:
            self.parent.tiles[ice].multiplier("blue")
        for x2 in self.x2_mult:
            self.parent.tiles[x2].multiplier("deep pink")
        for dl in self.dl_mult:
            self.parent.tiles[dl].multiplier("gold")
        for tl in self.tl_mult:
            self.parent.tiles[tl].multiplier("gold")
