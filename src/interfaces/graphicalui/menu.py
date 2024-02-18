import tkinter as tk

from src.utils import aux_to_indices


class Menu:
    def __init__(self, parent, aux_cord: int) -> None:
        self.parent = parent
        self.aux_cord = aux_cord
        self.menu: tk.Menu = tk.Menu(self.parent.window, tearoff=0)
        self.initialize()

    def initialize(self):
        self.add_menu_items()
        self.add_separator()
        self.add_remove_menus()

    def add_menu_items(self):
        cord = aux_to_indices(self.aux_cord)

        self.add_menu_item("Gem", lambda: self.parent.menu.set_gem(cord))
        self.add_menu_item("Ice", lambda: self.parent.menu.set_ice(cord))
        self.add_menu_item("2X", lambda: self.parent.menu.set_x2_mult(cord))
        self.add_menu_item("DL", lambda: self.parent.menu.set_dl_mult(cord))
        self.add_menu_item("TL", lambda: self.parent.menu.set_tl_mult(cord))

    def add_remove_menus(self):
        self.add_menu_item("Remove gems", self.parent.menu.remove_gems)
        self.add_menu_item("Remove ices", self.parent.menu.remove_ices)
        self.add_menu_item("Remove bonus", self.parent.menu.remove_mults)

    def add_separator(self):
        self.menu.add_separator()

    def add_menu_item(self, label, command):
        self.menu.add_command(label=label, command=command)

    def popup(self, event) -> None:
        try:
            self.menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.menu.grab_release()
