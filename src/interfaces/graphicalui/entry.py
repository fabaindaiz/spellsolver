import tkinter as tk

from src.entities import Coordinates
from src.utils import aux_to_indices


class Entry(tk.Entry):
    def __init__(self, parent, menu, string_var: tk.StringVar, aux_coord: int) -> None:
        super().__init__(parent.window)

        self.parent = parent
        self.menu = menu
        self.aux_coord = aux_coord

        self.current_coord, self.next_coord = self.calculate_coordinates()
        self.keys = {
            "<Up>": aux_to_indices(self.aux_coord - 5),
            "<Down>": aux_to_indices(self.aux_coord + 5),
            "<Left>": aux_to_indices(self.aux_coord - 1),
            "<Right>": aux_to_indices(self.aux_coord + 1),
        }

        self.entry = self.create_entry(string_var)
        self.place_entry()
        self.bind_events()

    def create_entry(self, string_var: tk.StringVar) -> tk.Entry:
        registration = self.parent.window.register(self.input_handler)

        entry = tk.Entry(
            master=self.parent.window,
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
        x, y = self.current_coord
        horizontal_padding = 25
        vertical_padding = 25

        self.entry.place(
            x=horizontal_padding + 40 * x,
            y=vertical_padding + 40 * y,
            width=40,
            height=40,
        )

    def calculate_coordinates(self) -> tuple[Coordinates, Coordinates]:
        current_coord = aux_to_indices(self.aux_coord)
        next_coord = aux_to_indices(self.aux_coord + 1)

        return current_coord, next_coord

    def bind_events(self) -> None:
        self.entry.bind("<Button-3>", lambda event: self.menu.popup(event))
        self.entry.bind("<Up>", lambda event: self.focus_on_tile(self.keys["<Up>"]))
        self.entry.bind("<Down>", lambda event: self.focus_on_tile(self.keys["<Down>"]))
        self.entry.bind("<Left>", lambda event: self.focus_on_tile(self.keys["<Left>"]))
        self.entry.bind(
            "<Right>", lambda event: self.focus_on_tile(self.keys["<Right>"])
        )

    @staticmethod
    def validate_input(user_input: str) -> bool:
        is_a_single_character = len(user_input) == 1
        is_in_english_alphabet = user_input.isalpha() and user_input.isascii()

        return is_a_single_character and is_in_english_alphabet

    def input_handler(self, user_input: str) -> bool:
        is_valid = self.validate_input(user_input)
        is_occupied = len(user_input) > 1

        if is_occupied:
            self.focus_on_tile(self.current_coord)
            return False

        if is_valid:
            self.focus_on_tile(self.next_coord)

        return True

    def focus_on_tile(self, coordinates: Coordinates) -> None:
        self.parent.tiles[coordinates].entry.focus()

    def focus(self) -> None:
        self.entry.focus_set()
        self.entry.select_range(0, "end")
