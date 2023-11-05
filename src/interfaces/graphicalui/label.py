import tkinter as tk
from tkinter.font import Font
from typing import List

from src.modules.gameboard.gametile import GameTile


class Label:
    """Represents a result label"""

    def __init__(self, board, num: int, text: str = "") -> None:
        self.board = board
        app = board.app

        self.text: str = text
        self.hover: LabelHover = None

        self.label: tk.Label = tk.Label(app.window)
        self.label["borderwidth"] = "1px"
        self.label["font"] = Font(family="Consolas", size=16)
        self.label["fg"] = "#333333"
        self.label["justify"] = "center"
        self.label["text"] = self.text
        self.label.place(x=250, y=16 + num * 24, width=350, height=24)

    def reset(self) -> None:
        self.hover: LabelHover = None
        self.label["text"] = self.text

    def set_text(self, text: str) -> None:
        """Set text value of the label"""
        self.label["text"] = str(text)

    def set_hover(self, text: str, path: List[GameTile]) -> None:
        """Set hover & text value of the label"""
        self.hover = LabelHover(self.board, self, path)
        self.label["text"] = str(text)


class LabelHover:
    """Represent a hover event handler for result labels"""

    def __init__(self, board, label: Label, path: List[GameTile]) -> None:
        self.board = board
        self.label: Label = label
        self.path: List[GameTile] = path

        self.label.label.bind("<Enter>", lambda _: self._hover())
        self.label.label.bind("<Leave>", lambda _: self._unhover())

    def _hover(self) -> None:
        """Handle hover event in the label"""
        for tile in self.path:
            self.board.tiles[tile.cord].hover(tile.letter, tile.swap)
        self.label.label.focus_set()

    def _unhover(self) -> None:
        """handle unhover event in the label"""
        for tile in self.path:
            self.board.tiles[tile.cord].unhover()
