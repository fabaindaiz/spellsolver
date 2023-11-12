from tkinter import ttk
from tkinter.font import Font

from src.modules.gameboard import GameTile


class Label:
    def __init__(self, parent, order: int, text: str = "") -> None:
        self.parent = parent

        self.text: str = text
        self.label = self.create()
        self.place_label(order)

    def create(self) -> ttk.Label:
        label: ttk.Label = ttk.Label(
            master=self.parent.window,
            font=Font(family="Consolas", size=16),
            foreground="#333333",
            justify="center",
            text=self.text,
        )

        return label

    def place_label(self, num: int) -> None:
        self.label.place(x=250, y=16 + num * 24, width=350, height=24)

    def _on_hover(self, path) -> None:
        for tile in path:
            self.parent.tiles[tile.coordinates].hover(tile.letter, tile.is_swapped)
        self.label.focus_set()

    def _on_unhover(self, path) -> None:
        for tile in path:
            self.parent.tiles[tile.coordinates].unhover()

    def bind_events(self, path) -> None:
        self.label.bind("<Enter>", lambda _: self._on_hover(path))
        self.label.bind("<Leave>", lambda _: self._on_unhover(path))

    def reset(self) -> None:
        self.label["text"] = self.text

    def set_text(self, text: str) -> None:
        self.label["text"] = str(text)

    def set_hover(self, text: str, path: tuple[GameTile, ...]) -> None:
        self.bind_events(path)
        self.label["text"] = str(text)
