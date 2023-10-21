import tkinter as tk

from src.interfaces.boardentry import BoardEntry
from src.interfaces.boardmenu import BoardMenu


class BoardTile:
    """Represents a tile from the board with its logic"""

    def __init__(self, board, aux_cord):
        self.board = board
        app = board.app

        self.backup_letter = None

        self.stringvar = tk.StringVar(app.window, value="")
        self.menu = BoardMenu(self.board, aux_cord)
        self.entry = BoardEntry(self.board, self.menu, self.stringvar, aux_cord)

        self.entry.entry.configure(
            highlightbackground="black",
            highlightcolor="black",
            background="white",
            font=("Roboto", 18, tk.font.NORMAL),
            fg="black",
        )

    def letter(self):
        """Get the letter of the tile in lower case"""
        return self.stringvar.get().lower()

    def multiplier(self, color):
        """Set multiplier color in tile"""
        font_config = {
            "highlightbackground": color,
            "highlightcolor": color,
            "background": "white",
            "font": ("Roboto", 18, tk.font.NORMAL),
            "fg": "black",
        }
        self.entry.entry.configure(**font_config)

    def hover(self, letter, swap):
        """Handle hover event on the tile"""
        self.backup_letter = self.letter()
        self.stringvar.set(letter)

        color = "red" if swap else "blue"
        self.entry.entry.configure(
            highlightbackground=color,
            highlightcolor=color,
            background=color,
            font=("Roboto", 24, tk.font.BOLD),
            fg="white",
        )

    def unhover(self):
        """Handle unhover event on the tile"""
        self.entry.entry.configure(
            highlightbackground="black",
            highlightcolor="black",
            background="white",
            font=("Roboto", 18, tk.font.NORMAL),
            fg="black",
        )
        self.stringvar.set(self.backup_letter)
        self.board.mult.configure_mult()
