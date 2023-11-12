import tkinter as tk

from .entry import Entry
from .menu import Menu


class Tile:
    FONT_HOVER = ("Roboto", 24, tk.font.BOLD)

    def __init__(self, parent, aux_cord: int):
        self.parent = parent

        self.backup_letter = None

        self.string_var = tk.StringVar(master=self.parent.window, value="")
        self.menu = Menu(self.parent, aux_cord)
        self.entry = Entry(self.parent, self.menu, self.string_var, aux_cord)

        self._configure_style()

    @property
    def letter(self) -> str:
        return self.string_var.get()

    def _configure_style(
        self,
        font: tuple[str, int, str] = ("Roboto", 18, tk.font.NORMAL),
        background: str = "white",
        foreground: str = "black",
        highlight_background: str = "black",
        highlight_color: str = "black",
    ) -> None:
        self.entry.entry.configure(
            font=font,
            background=background,
            fg=foreground,
            highlightbackground=highlight_background,
            highlightcolor=highlight_color,
        )

    def multiplier(self, color) -> None:
        self._configure_style(
            highlight_background=color,
            highlight_color=color,
        )

    def hover(self, letter, swap) -> None:
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
        self._configure_style()
        self.string_var.set(self.backup_letter)
        self.parent.menu.unhover_tiles()
