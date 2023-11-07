import tkinter as tk

from .entry import Entry
from .menu import Menu


class Tile:
    """
    Represents a tile in a game board.

    Attributes:
        FONT_HOVER (tuple): The font style for hover state.
    """

    FONT_HOVER = ("Roboto", 24, tk.font.BOLD)

    def __init__(self, board, aux_cord: int):
        """
        Initialize a Tile instance.

        Args:
            board (Board): The game board this tile belongs to.
            aux_cord (int): The auxiliary coordinates of the tile.

        Initializes the Tile with a reference to the board and auxiliary coordinates.
        Also sets up a StringVar for the tile's content, a menu, and an entry.

        """
        self.board = board
        app = board.app

        self.backup_letter = None

        self.string_var = tk.StringVar(app.window, value="")
        self.menu = Menu(self.board, aux_cord)
        self.entry = Entry(self.board, self.menu, self.string_var, aux_cord)

        self._configure_style()

    @property
    def letter(self) -> str:
        """
        Get the letter on the tile.

        Returns:
            str: The letter on the tile in lowercase.
        """
        return self.string_var.get()

    def _configure_style(
        self,
        font: tuple[str, int, str] = ("Roboto", 18, tk.font.NORMAL),
        background: str = "white",
        foreground: str = "black",
        highlight_background: str = "black",
        highlight_color: str = "black",
    ) -> None:
        """
        Configure the visual style of the tile entry widget.

        Args:
            font (tuple): A tuple containing font details.
            background (str): The background color.
            foreground (str): The text color.
            highlight_background (str): The background color for highlighting.
            highlight_color (str): The text color for highlighting.
        """
        self.entry.entry.configure(
            font=font,
            background=background,
            fg=foreground,
            highlightbackground=highlight_background,
            highlightcolor=highlight_color,
        )

    def multiplier(self, color) -> None:
        """
        Apply a multiplier effect to the tile.

        Args:
            color (str): The color of the multiplier effect.

        Applies a multiplier effect to the tile, changing its style based on the given color.
        """
        self._configure_style(
            highlight_background=color,
            highlight_color=color,
        )

    def hover(self, letter, swap) -> None:
        """
        Handle hover state of the tile.

        Args:
            letter (str): The letter to display on hover.
            swap (bool): Whether to swap the tile content.

        Handles the hover state of the tile, changing its style and content based on the input parameters.
        """
        self.backup_letter = self.letter
        self.string_var.set(letter)

        color = "red" if swap else "blue"
        self._configure_style(
            font=self.FONT_HOVER,
            background=color,
            foreground="white",
            highlight_background=color,
            highlight_color=color,
        )

    def unhover(self) -> None:
        """
        Handle when the tile is unhovered.

        Restores the tile's original style and content after being hovered.
        """
        self._configure_style()
        self.string_var.set(self.backup_letter)
        self.board.menu.unhover_tiles()
