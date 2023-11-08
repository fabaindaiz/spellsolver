from tkinter import ttk
from tkinter.font import Font
from typing import List

from src.modules.gameboard import GameTile


class Label:
    def __init__(self, board, num: int, text: str = "") -> None:
        """
        Initialize a Label object.

        Args:
            board: The game board.
            num (int): The label's number.
            text (str, optional): The text to display on the label.
            Defaults to "".
        """
        self.board = board
        self.app = board.app

        self.text: str = text
        self.label = self.create()
        self.place_label(num)

    def create(self) -> ttk.Label:
        """
        Create a ttk.Label widget with specified attributes.

        Returns:
            ttk.Label: The created label widget.
        """
        label: ttk.Label = ttk.Label(
            master=self.app.window,
            font=Font(family="Consolas", size=16),
            foreground="#333333",
            justify="center",
            text=self.text,
        )

        return label

    def place_label(self, num: int) -> None:
        """
        Place the label on the game board.

        Args:
            num (int): The label's number.
        """
        self.label.place(x=250, y=16 + num * 24, width=350, height=24)

    def _on_hover(self, path) -> None:
        """
        Handle hover behavior for the label.

        Args:
            path: The path information.
        """
        for tile in path:
            self.board.tiles[tile.coordinates].hover(tile.letter, tile.is_swapped)
        self.label.focus_set()

    def _on_unhover(self, path) -> None:
        """
        Handle unhover behavior for the label.

        Args:
            path: The path information.
        """
        for tile in path:
            self.board.tiles[tile.coordinates].unhover()

    def bind_events(self, path) -> None:
        """
        Bind hover and unhover events to the label.

        Args:
            path: The path information.
        """
        self.label.bind("<Enter>", lambda _: self._on_hover(path))
        self.label.bind("<Leave>", lambda _: self._on_unhover(path))

    def reset(self) -> None:
        """
        Reset the label's text to its initial value.
        """
        self.label["text"] = self.text

    def set_text(self, text: str) -> None:
        """
        Set the text of the label to the specified value.

        Args:
            text (str): The new text for the label.
        """
        self.label["text"] = str(text)

    def set_hover(self, text: str, path: List[GameTile]) -> None:
        """
        Set the label's text and bind hover/unhover events.

        Args:
            text (str): The new text for the label.
            path: The path information.
        """
        self.bind_events(path)
        self.label["text"] = str(text)
