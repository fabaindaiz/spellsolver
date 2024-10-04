from tkinter import ttk
from typing import Callable


class Button(ttk.Button):
    INITIAL_HORIZONTAL_POSITION = 100
    INITIAL_VERTICAL_POSITION = 210
    DOUBLE_SWAP_HORIZONTAL_POSITION = 67
    BUTTON_HEIGHT = 30

    def __init__(self, parent, double_swap: bool, swap_count: int, command: Callable):
        super().__init__(parent.window)

        self.parent = parent.window
        self.double_swap = double_swap
        self.swap_count = swap_count
        self.command = command
        self.button = self.initialize()

    def initialize(self):
        master = self.parent
        text = self.get_label()
        command = self.command

        button = ttk.Button(master=master, text=text, command=command)

        self.configure_style()
        self.set_position(button)

        return button

    def get_label(self):
        return (
            f"{self.swap_count} Swap"
            if self.swap_count == 1
            else f"{self.swap_count} Swaps"
        )

    def set_position(self, button):
        width, height = self.calculate_size()
        horizontal_position, vertical_position = self.calculate_position()

        button.place(
            x=horizontal_position, y=vertical_position, width=width, height=height
        )

    def horizontal_position(self):
        return (
            self.DOUBLE_SWAP_HORIZONTAL_POSITION * self.swap_count
            if self.double_swap
            else self.INITIAL_HORIZONTAL_POSITION * self.swap_count
        )

    def calculate_width(self):
        return (
            self.DOUBLE_SWAP_HORIZONTAL_POSITION
            if self.double_swap
            else self.INITIAL_HORIZONTAL_POSITION
        )

    def calculate_size(self):
        width = self.calculate_width()
        height = self.BUTTON_HEIGHT

        return width, height

    def calculate_padding(self):
        horizontal_padding = 25
        vertical_padding = 25

        return horizontal_padding, vertical_padding

    def calculate_position(self):
        horizontal_padding, vertical_padding = self.calculate_padding()

        horizontal_position = horizontal_padding + self.horizontal_position()
        vertical_position = vertical_padding + self.INITIAL_VERTICAL_POSITION

        return horizontal_position, vertical_position

    @staticmethod
    def configure_style():
        style = ttk.Style()
        style.configure(
            style="TButton",
            background="#e9e9ed",
            font=("Times", 12),
            foreground="#000000",
        )
