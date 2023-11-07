import tkinter as tk

from src.utils import aux_to_indices


class Entry:
    """
    A class representing an input entry in a board.

    Args:
        board (Board): The board to which this entry belongs.
        menu (Menu): The menu associated with the board.
        string_var (tk.StringVar): The StringVar to store the entry's text.
        aux_coord (int): The auxiliary coordinate of the entry.

    Attributes:
        board (Board): The board to which this entry belongs.
        app (Application): The application associated with the board.
        menu (Menu): The menu associated with the board.
        aux_coord (int): The auxiliary coordinate of the entry.
        current_coord (tuple[int, int]): The current (x, y) coordinates of the entry.
        next_coord (tuple[int, int]): The (x, y) coordinates of the next entry.

    """

    def __init__(self, board, menu, string_var: tk.StringVar, aux_coord: int) -> None:
        self.board = board
        self.app = board.app
        self.menu = menu
        self.aux_coord = aux_coord
        self.current_coord, self.next_coord = self.calculate_coordinates()

        self.entry = self.create_entry(string_var)
        self.place_entry()
        self.bind_events()

    def create_entry(self, string_var: tk.StringVar) -> tk.Entry:
        """
        Create and configure the Tkinter Entry widget for the input.

        Args:
            string_var (tk.StringVar): The StringVar to store the entry's text.

        Returns:
            tk.Entry: The configured Entry widget.
        """
        registration = self.app.window.register(self.input_handler)

        entry = tk.Entry(
            master=self.app.window,
            textvariable=string_var,
            validate="key",
            highlightthickness=2,
            borderwidth=1,
            fg="#333333",
            justify="center",
            validatecommand=(registration, "%P"),
        )

        return entry

    def place_entry(self) -> None:
        """
        Place the Entry widget on the board.
        """
        x, y = self.current_coord
        horizontal_padding = self.app.HORIZONTAL_PADDING
        vertical_padding = self.app.VERTICAL_PADDING

        self.entry.place(
            x=horizontal_padding + 40 * x,
            y=vertical_padding + 40 * y,
            width=40,
            height=40,
        )

    def calculate_coordinates(self) -> tuple:
        """
        Calculate the current and next (x, y) coordinates based on aux_coord.

        Returns:
            tuple: A tuple containing the current and next (x, y) coordinates.
        """
        current_coord = aux_to_indices(self.aux_coord)
        next_coord = aux_to_indices(self.aux_coord + 1)

        return current_coord, next_coord

    def bind_events(self) -> None:
        """
        Bind events to the Entry widget.
        """
        self.entry.bind("<Button-3>", lambda event: self.menu.popup(event))

    @staticmethod
    def validate_input(user_input: str) -> bool:
        """
        Validate user input for the Entry.

        Args:
            user_input (str): The user's input.

        Returns:
            bool: True if the input is a single English character, False otherwise.
        """
        is_a_single_character = len(user_input) == 1
        is_in_english_alphabet = user_input.isalpha() and user_input.isascii()

        return is_a_single_character and is_in_english_alphabet

    def input_handler(self, user_input: str) -> bool:
        """
        Handle user input events and validation.

        Args:
            user_input (str): The user's input.

        Returns:
            bool: True if the input is valid and should be accepted, False otherwise.
        """
        is_valid = self.validate_input(user_input)
        is_occupied = len(user_input) > 1

        if is_occupied:
            self.focus_on_tile(self.current_coord)
            return False

        if is_valid:
            self.focus_on_tile(self.next_coord)

        return True

    def focus_on_tile(self, coordinates: tuple[int, int]) -> None:
        """
        Set focus to the Entry of the tile at the specified coordinates.

        Args:
            coordinates (tuple[int, int]): The (x, y) coordinates of the target tile.
        """
        self.board.tiles[coordinates].entry.focus()

    def focus(self) -> None:
        """
        Set focus on the Entry and select its text.
        """
        self.entry.focus_set()
        self.entry.select_range(0, "end")
