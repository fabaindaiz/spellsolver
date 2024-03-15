import tkinter as tk

from src.utils import aux_to_indices


class Menu(tk.Menu):
    def __init__(self, parent, aux_cord: int) -> None:
        super().__init__(parent.window)

        self.parent = parent
        self.aux_cord = aux_cord
        self.menu: tk.Menu = tk.Menu(self.parent.window, tearoff=0)
        self.initialize()

    def _menu_items(self):
        cord = aux_to_indices(self.aux_cord)

        self.menu.add_command(
            label="Gem", command=lambda: self.parent.menu.set_gem(cord)
        )
        self.menu.add_command(
            label="Ice", command=lambda: self.parent.menu.set_ice(cord)
        )
        self.menu.add_command(
            label="2X", command=lambda: self.parent.menu.set_x2_mult(cord)
        )
        self.menu.add_command(
            label="DL", command=lambda: self.parent.menu.set_dl_mult(cord)
        )
        self.menu.add_command(
            label="TL", command=lambda: self.parent.menu.set_tl_mult(cord)
        )

    def _menu_remove(self):
        self.menu.add_command(label="Remove gems", command=self.parent.menu.remove_gems)
        self.menu.add_command(label="Remove ices", command=self.parent.menu.remove_ices)
        self.menu.add_command(
            label="Remove bonus", command=self.parent.menu.remove_mults
        )

    def _separator(self):
        self.menu.add_separator()

    def initialize(self):
        self._menu_items()
        self._separator()
        self._menu_remove()

    def popup(self, event) -> None:
        try:
            self.menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.menu.grab_release()
