import tkinter as tk

from src.utils.utils import aux_to_indices


class Menu:
    def __init__(self, board, aux_cord: int) -> None:
        """
        Initialize a Menu for the game board.

        Args:
            board: The game board.
            aux_cord (int): The auxiliary coordinate.
        """
        self.board = board
        self.aux_cord = aux_cord
        self.menu: tk.Menu = tk.Menu(self.board.app.window, tearoff=0)
        self.initialize()

    def initialize(self):
        """
        Initialize the menu by adding menu items and separators.
        """
        self.add_menu_items()
        self.add_separator()
        self.add_remove_menus()

    def add_menu_items(self):
        """
        Add menu items for gem and bonus placement options.
        """
        cord = aux_to_indices(self.aux_cord)

        self.add_menu_item("Gem", lambda: self.board.menu.set_gem_letter(cord))
        self.add_menu_item("2X", lambda: self.board.menu.set_mult_word(cord))
        self.add_menu_item("DL", lambda: self.board.menu.set_mult_letter(cord, 2))
        self.add_menu_item("TL", lambda: self.board.menu.set_mult_letter(cord, 3))

    def add_remove_menus(self):
        """
        Add menu items for removing gems and bonuses.
        """
        self.add_menu_item("Remove gems", self.board.menu.remove_gem_all)
        self.add_menu_item("Remove bonus", self.board.menu.remove_mult_all)

    def add_separator(self):
        """
        Add a separator to the menu.
        """
        self.menu.add_separator()

    def add_menu_item(self, label, command):
        """
        Add a menu item with a label and associated command.

        Args:
            label (str): The label for the menu item.
            command: The command to execute when the menu item is selected.
        """
        self.menu.add_command(label=label, command=command)

    def popup(self, event) -> None:
        """
        Display the menu at the specified event location.

        Args:
            event: The event that triggered the menu popup.
        """
        try:
            self.menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.menu.grab_release()
