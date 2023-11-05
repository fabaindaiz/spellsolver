from tkinter import ttk
from typing import Callable


class Button:
    """
    Represents a button on a game board.

    Attributes:
        INITIAL_HORIZONTAL_POSITION (int): The initial horizontal position for buttons.
        INITIAL_VERTICAL_POSITION (int): The initial vertical position for buttons.
        DOUBLE_SWAP_HORIZONTAL_POSITION (int): The horizontal position for buttons when double swapping.
        BUTTON_HEIGHT (int): The height of the button.

    Args:
        parent: The parent widget that contains the button.
        double_swap (bool): Whether it's a double swap button.
        swap_count (int): The number of swaps associated with the button.
        command (Callable): The function to execute when the button is clicked.
    """

    INITIAL_HORIZONTAL_POSITION = 100
    INITIAL_VERTICAL_POSITION = 210
    DOUBLE_SWAP_HORIZONTAL_POSITION = 67
    BUTTON_HEIGHT = 30

    def __init__(self, parent, double_swap: bool, swap_count: int, command: Callable):
        """
        Initializes a Button instance.

        Args:
            parent: The parent widget that contains the button.
            double_swap (bool): Whether it's a double swap button.
            swap_count (int): The number of swaps associated with the button.
            command (Callable): The function to execute when the button is clicked.
        """

        self.parent = parent
        self.double_swap = double_swap
        self.swap_count = swap_count
        self.command = command
        self.button = self.initialize()

    def initialize(self):
        """
        Initializes the button, sets its style, and positions it on the screen.
        Returns:
            ttk.Button: The initialized button.
        """
        master = self.parent.window
        text = self.get_label()
        command = self.command

        button = ttk.Button(master=master, text=text, command=command)

        self.configure_style()
        self.set_position(button)

        return button

    def get_label(self):
        """
        Generates the label text for the button based on the swap count.

        Returns:
            str: The label text.
        """
        return (
            f"{self.swap_count} Swap"
            if self.swap_count == 1
            else f"{self.swap_count} Swaps"
        )

    def set_position(self, button):
        """
        Sets the position of the button on the screen.

        Args:
            button (ttk.Button): The button to position.
        """
        width, height = self.calculate_size()
        horizontal_position, vertical_position = self.calculate_position()

        button.place(
            x=horizontal_position, y=vertical_position, width=width, height=height
        )

    def horizontal_position(self):
        """
        Calculates the horizontal position based on double swap and swap count.

        Returns:
            int: The horizontal position.
        """
        return (
            self.DOUBLE_SWAP_HORIZONTAL_POSITION * self.swap_count
            if self.double_swap
            else self.INITIAL_HORIZONTAL_POSITION * self.swap_count
        )

    def calculate_width(self):
        """
        Calculates the button width based on double swap.

        Returns:
            int: The button width.
        """
        return (
            self.DOUBLE_SWAP_HORIZONTAL_POSITION
            if self.double_swap
            else self.INITIAL_HORIZONTAL_POSITION
        )

    def calculate_size(self):
        """
        Calculates the button size (width and height).

        Returns:
            Tuple[int, int]: The button width and height.
        """
        width = self.calculate_width()
        height = self.BUTTON_HEIGHT

        return width, height

    def calculate_padding(self):
        """
        Calculates the horizontal and vertical padding for button positioning.

        Returns:
            Tuple[int, int]: The horizontal and vertical padding.
        """
        horizontal_padding = self.parent.HORIZONTAL_PADDING
        vertical_padding = self.parent.VERTICAL_PADDING

        return horizontal_padding, vertical_padding

    def calculate_position(self):
        """
        Calculates the position of the button on the screen.

        Returns:
            Tuple[int, int]: The horizontal and vertical position.
        """
        horizontal_padding, vertical_padding = self.calculate_padding()

        horizontal_position = horizontal_padding + self.horizontal_position()
        vertical_position = vertical_padding + self.INITIAL_VERTICAL_POSITION

        return horizontal_position, vertical_position

    @staticmethod
    def configure_style():
        """
        Configures the style of the ttk button.
        """
        style = ttk.Style()
        style.configure(
            style="TButton",
            background="#e9e9ed",
            font=("Times", 12),
            foreground="#000000",
        )
