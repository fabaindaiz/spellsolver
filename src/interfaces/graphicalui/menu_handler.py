from src.entities import Coordinates


class MenuHandler:
    def __init__(self, board) -> None:
        """
        Initialize a MenuHandler for managing menu options on the game board.

        Args:
            board: The game board.
        """
        self.board = board

        self.word_coord: Coordinates = None
        self.letter_coord: Coordinates = None
        self.letter_mult: int = None

        self.letter_gems: list[Coordinates] = []

    def set_mult_word(self, coordinates: Coordinates) -> None:
        """
        Set a word multiplier at the specified coordinate.

        Args:
            coordinates (tuple): The coordinate for setting the word multiplier.
        """
        self.remove_mult_cord(coordinates)
        if self.word_coord is not None:
            self.board.tiles[self.word_coord].multiplier("black")

        self.word_coord = coordinates
        self.board.tiles[coordinates].multiplier("deep pink")

    def set_mult_letter(self, coordinates: Coordinates, mult: int) -> None:
        """
        Set a letter multiplier at the specified coordinate with a specified multiplier.

        Args:
            coordinates (tuple): The coordinate for setting the letter multiplier.
            mult (int): The multiplier value.
        """
        self.remove_mult_cord(coordinates)
        if self.letter_coord is not None:
            self.board.tiles[self.letter_coord].multiplier("black")

        self.letter_mult = mult
        self.letter_coord = coordinates
        self.board.tiles[coordinates].multiplier("gold")

    def remove_mult_cord(self, coordinates: Coordinates) -> None:
        """
        Remove any multipliers set at the specified coordinate.

        Args:
            coordinates (tuple): The coordinate for removing multipliers.
        """
        if self.word_coord == coordinates:
            self.board.tiles[coordinates].multiplier("black")
            self.word_coord = None
        if self.letter_coord == coordinates:
            self.board.tiles[coordinates].multiplier("black")
            self.letter_coord = None

    def remove_mult_all(self) -> None:
        """
        Remove all multipliers set on the board.
        """
        if self.word_coord is not None:
            self.board.tiles[self.word_coord].multiplier("black")
            self.word_coord = None
        if self.letter_coord is not None:
            self.board.tiles[self.letter_coord].multiplier("black")
            self.letter_coord = None

    def set_gem_letter(self, coordinates: Coordinates) -> None:
        """
        Set a gem letter at the specified coordinate.

        Args:
            coordinates (tuple): The coordinate for setting a gem letter.
        """
        self.remove_mult_cord(coordinates)

        self.letter_gems.append(coordinates)
        self.board.tiles[coordinates].multiplier("blue")

    def remove_gem_cord(self, coordinates: Coordinates) -> None:
        """
        Remove a gem letter at the specified coordinate.

        Args:
            coordinates (tuple): The coordinate for removing a gem letter.
        """
        if coordinates in self.letter_gems:
            self.letter_gems.remove(coordinates)
            self.board.tiles[coordinates].multiplier("black")

    def remove_gem_all(self) -> None:
        """
        Remove all gem letters set on the board.
        """
        self.letter_gems = []
        for tile in self.letter_gems:
            self.board.tiles[tile].multiplier("black")

    def unhover_tiles(self) -> None:
        """
        Unhover all tiles with multipliers set.
        """
        if self.word_coord is not None:
            self.board.tiles[self.word_coord].multiplier("deep pink")
        if self.letter_coord is not None:
            self.board.tiles[self.letter_coord].multiplier("gold")
        for tile in self.letter_gems:
            self.board.tiles[tile].multiplier("blue")
