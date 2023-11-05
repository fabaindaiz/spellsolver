from typing import List, Tuple, Dict

from src.config import SWAP
from src.interfaces.baseui import BaseUI
from src.interfaces.graphicalui.button import Button
from src.interfaces.graphicalui.label import Label
from src.interfaces.graphicalui.tile import Tile
from src.interfaces.graphicalui.menu_handler import MenuHandler
from src.modules.gameboard.resultword import ResultWord
from src.utils.utils import aux_to_indices


class Board:
    """
    The `Board` class represents the graphical user interface for a word game.

    Args:
        app (BaseUI): The parent application's user interface.

    Attributes:
        app (BaseUI): The parent application's user interface.
        double_swap (bool): A boolean indicating if double swapping is allowed.
        buttons (List[Button]): List of swap buttons for different swap options.
        timer (Label): Label to display the elapsed time.
        labels (List[BoardLabel]): List of labels to display word results.
        tiles (Dict[Tuple[int, int], Tile]): Dictionary of game tiles on the board.
        menu (MenuHandler): Handler for menu options.
    """

    def __init__(self, app: BaseUI) -> None:
        self.app: BaseUI = app
        self.double_swap: bool = SWAP >= 2

        self.buttons: List[Button] = []
        self.timer: Label = None
        self.labels: List[Label] = []
        self.tiles: Dict[Tuple[int, int], Tile] = {}
        self.menu: MenuHandler = MenuHandler(self)

        self.initialize_components()

    def initialize_components(self) -> None:
        """
        Initialize UI components: buttons, tiles, labels, and menu handler.
        """
        self.initialize_buttons()
        self.initialize_tiles()
        self.initialize_labels()

    def initialize_buttons(self) -> None:
        """
        Initialize swap buttons based on the swap options available.
        """
        swap_options = [0, 1]

        if self.double_swap:
            swap_options.append(2)

        for option in swap_options:
            button = self.create_button(option)

            self.buttons.append(button)

    def create_button(self, swap_count: int) -> Button:
        """
        Create a swap button.

        Args:
            swap_count (int): The number of swaps associated with the button.

        Returns:
            Button: The created swap button.
        """
        return Button(
            parent=self.app,
            double_swap=self.double_swap,
            swap_count=swap_count,
            command=lambda: self.button_command(swap_count),
        )

    def initialize_tiles(self) -> None:
        """
        Initialize game tiles on the board.
        """
        for tile_index in range(25):
            coord_index = aux_to_indices(tile_index)

            self.tiles[coord_index] = Tile(self, tile_index)

    def initialize_labels(self) -> None:
        """
        Initialize labels for displaying word results and the timer.
        """
        self.timer = Label(self, 10)

        for label_index in range(10):
            label = Label(self, label_index)

            self.labels.append(label)

    def set_timer(self, elapsed_millis: int) -> None:
        """
        Set and update the timer label with the elapsed time.

        Args:
            elapsed_millis (int): The elapsed time in milliseconds.
        """
        self.update_timer(elapsed_millis)

    def set_results(self, word_list: List[ResultWord]) -> None:
        """
        Set and update the word result labels.

        Args:
            word_list (List[ResultWord]): List of word results to display.
        """
        self.reset_labels()
        self.update_labels(word_list)

    def reset_labels(self) -> None:
        """
        Reset word result labels.
        """
        for label in self.labels:
            label.reset()

    def update_timer(self, elapsed_millis: int) -> None:
        """
        Update the timer label with the elapsed time.

        Args:
            elapsed_millis (int): The elapsed time in milliseconds.
        """
        self.timer.set_text(f"elapsed time: {elapsed_millis} ms")

    def update_labels(self, word_list: List[ResultWord]) -> None:
        """
        Update word result labels with word text and paths.

        Args:
            word_list (List[ResultWord]): List of word results to display.
        """
        for label, result in zip(self.labels, word_list):
            text = result.label()
            path = result.path

            label.set_hover(text, path)

    def button_command(self, swap: int) -> None:
        """
        Handle button click event and perform game actions based on the selected swap option.

        Args:
            swap (int): The number of swaps to perform.
        """
        gameboard_string = "".join(tile.letter() for tile in self.tiles.values())
        self.app.gameboard.load(gameboard_string)

        if self.menu.word_cord is not None:
            self.app.gameboard.set_mult_word(self.menu.word_cord)
        if self.menu.letter_cord is not None:
            self.app.gameboard.set_mult_letter(
                self.menu.letter_cord, self.menu.letter_mult
            )
        if self.menu.letter_gems is not None:
            self.app.gameboard.set_gems(self.menu.letter_gems)

        results = self.app.solve(swap)
        sorted_words = results.sorted_words()
        self.set_timer(results.timer.elapsed_millis())
        self.set_results(sorted_words[:10])
