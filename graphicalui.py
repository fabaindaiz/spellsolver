import tkinter as tk
from typing import Tuple

from src.config import SWAP, VERSION
from src.interfaces.baseui import BaseUI
from src.interfaces.graphicalui.board import Board
from src.utils.resources import resource_path


class GraphicalUI(BaseUI):
    """
    Graphical user interface for the Spellsolver application.

    This class extends the BaseUI class to create a graphical interface using the Tkinter library.

    Attributes:
        WINDOW_TITLE (str): The title of the application window.
        WINDOW_WIDTH (int): The width of the application window.
        WINDOW_HEIGHT (int): The height of the application window.
        HORIZONTAL_PADDING (int): Horizontal padding for the application window.
        VERTICAL_PADDING (int): Vertical padding for the application window.
    """

    WINDOW_TITLE: str = f"Spellsolver {VERSION}"
    WINDOW_WIDTH: int = 600
    WINDOW_HEIGHT: int = 300

    HORIZONTAL_PADDING: int = 25
    VERTICAL_PADDING: int = 25

    def __init__(self) -> None:
        """
        Initialize the GraphicalUI class.

        This constructor initializes the Tkinter window and the TkinterBoard interface.

        Returns:
            None
        """
        super().__init__()

        self.window: tk.Tk = tk.Tk()
        self.window.iconphoto(
            True, tk.PhotoImage(file=resource_path("assets/spellsolver.png"))
        )

        self.window.resizable(width=False, height=False)
        self.window.title(self.WINDOW_TITLE)

        alignment_string = self.get_alignment_string()
        self.window.geometry(alignment_string)

        self.loading: tk.Label = None
        self.loading_screen()

        self.init_spellsolver(swap=SWAP)
        self.loading.destroy()

        self.interface_board: Board = Board(self)

    def loading_screen(self) -> None:
        """
        Initialize the loading screen.

        This method initializes the loading screen for the application.

        Returns:
            None
        """
        self.loading = tk.Label(
            self.window,
            text="Loading spellsolver, this will take several seconds...",
            font=("Helvetica", 16),
        )
        self.loading.pack(pady=100, padx=20)
        self.window.update()

    def get_alignment_string(self) -> str:
        """
        Get the alignment string for the window geometry.

        This method calculates the horizontal and vertical screen offsets and returns the alignment string.

        Returns:
            str: The alignment string in the format "WIDTH x HEIGHT + HORIZONTAL_OFFSET + VERTICAL_OFFSET".
        """

        screen_offset = self.calculate_screen_offset()

        return self.format_alignment_string(*screen_offset)

    def calculate_screen_offset(self) -> Tuple[int, int]:
        """
        Calculate the screen offset for window alignment.

        This method calculates the horizontal and vertical offsets for centering the window on the screen.

        Returns:
            Tuple[int, int]: A tuple containing the horizontal and vertical screen offsets.
        """

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        horizontal_offset = (screen_width - self.WINDOW_WIDTH) // 2
        vertical_offset = (screen_height - self.WINDOW_HEIGHT) // 2

        return horizontal_offset, vertical_offset

    def format_alignment_string(
        self, screen_horizontal_offset, screen_vertical_offset
    ) -> str:
        """
        Format the alignment string for window geometry.

        This method formats the alignment string in the format "WIDTH x HEIGHT + HORIZONTAL_OFFSET + VERTICAL_OFFSET".

        Args:
            screen_horizontal_offset (int): The horizontal screen offset.
            screen_vertical_offset (int): The vertical screen offset.

        Returns:
            str: The alignment string for window geometry.
        """

        window_size = f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}"
        screen_offset = f"{screen_horizontal_offset}+{screen_vertical_offset}"

        return f"{window_size}+{screen_offset}"

    def main_execution_loop(self) -> None:
        """
        Start the main execution loop for the Tkinter application.

        This method starts the Tkinter main loop, which handles user interactions and events.

        Returns:
            None
        """

        self.window.mainloop()


if __name__ == "__main__":
    app = GraphicalUI()
    app.main_execution_loop()
