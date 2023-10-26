import tkinter as tk

from src.utils.utils import aux_to_indices


class BoardMenu:
    """Represents the contextual menu in GUI"""

    def __init__(self, board, aux_cord: int) -> None:
        self.board = board
        app = board.app

        cord = aux_to_indices(aux_cord)

        self.menu: tk.Menu = tk.Menu(app.window, tearoff=0)
        self.menu.add_command(
            label="2X", command=lambda: self.board.menu.set_mult_word(cord)
        )
        self.menu.add_command(
            label="DL", command=lambda: self.board.menu.set_mult_letter(cord, 2)
        )
        self.menu.add_command(
            label="TL", command=lambda: self.board.menu.set_mult_letter(cord, 3)
        )
        self.menu.add_separator()
        self.menu.add_command(
            label="Remove bonus", command=lambda: self.board.menu.remove_mult(cord)
        )
        self.menu.add_command(
            label="Remove all bonus", command=lambda: self.board.menu.remove_mult()
        )
        self.menu.add_separator()
        self.menu.add_command(
            label="Remove bonus", command=lambda: self.board.menu.remove_mult()
        )

    def popup(self, event) -> None:
        """Handle the popup event"""
        try:
            self.menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.menu.grab_release()
