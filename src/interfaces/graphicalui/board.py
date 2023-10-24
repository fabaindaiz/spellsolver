from abc import abstractmethod
from typing import List, Tuple, Dict

from src.interfaces.baseui import BaseUI
from src.interfaces.graphicalui.boardbutton import BoardButton
from src.interfaces.graphicalui.boardlabel import BoardLabel
from src.interfaces.graphicalui.boardtile import BoardTile
from src.modules.gameboard.resultword import ResultWord
from src.utils.utils import aux_to_indices
from src.config import SWAP


class Board:
    """Represents an abstract board

    Args:
        app (BaseUI): The base user interface for the board.

    Attributes:
        app (BaseUI): The base user interface for the board.
        double_swap (bool): A boolean indicating whether SWAP is greater than or equal to 2.
        buttons (List[BoardButton]): A list of board buttons.
        labels (List[BoardLabel]): A list of board labels.
        tiles (Dict[Tuple[int, int], BoardTile]): A dictionary mapping coordinates to board tiles.
    """

    def __init__(self, app: BaseUI) -> None:
        """Initialize the Board with a BaseUI instance.

        Args:
            app (BaseUI): The base user interface for the board.
        """

        self.app: BaseUI = app
        self.double_swap: bool = SWAP >= 2

        self.buttons: List[BoardButton] = []
        self.labels: List[BoardLabel] = []
        self.tiles: Dict[Tuple[int, int], BoardTile] = {}

        self.initialize_components()

    def initialize_components(self) -> None:
        """Initialize the components of the board: buttons, tiles, and labels."""

        self.initialize_buttons()
        self.initialize_tiles()
        self.initialize_labels()

    def initialize_buttons(self) -> None:
        """Initialize board buttons based on the value of SWAP."""

        swap_options = [0, 1]

        if self.double_swap:
            swap_options.append(2)

        for option in swap_options:
            button = self.create_button(option)

            self.buttons.append(button)

    def create_button(self, swap_count: int) -> BoardButton:
        """Create a board button for a specific swap count.

        Args:
            swap_count (int): The number of swaps represented by the button.

        Returns:
            BoardButton: The created board button.
        """

        return BoardButton(
            parent=self.app,
            double_swap=self.double_swap,
            swap_count=swap_count,
            command=lambda: self.button_command(swap_count),
        )

    def initialize_tiles(self) -> None:
        """Initialize board tiles on the board."""

        for tile_index in range(25):
            coord_index = aux_to_indices(tile_index)

            self.tiles[coord_index] = BoardTile(self, tile_index)

    def initialize_labels(self) -> None:
        """Initialize board labels on the board."""

        for label_index in range(10):
            label = BoardLabel(self, label_index)

            self.labels.append(label)

    def set_results(self, word_list: List[ResultWord]) -> None:
        """Set results on the board labels.

        Args:
            word_list (List[ResultWord]): A list of result words to be displayed on the labels.
        """

        self.reset_labels()
        self.update_labels(word_list)

    def reset_labels(self) -> None:
        """Reset the text on all board labels."""

        for label in self.labels:
            label.reset()

    def update_labels(self, word_list: List[ResultWord]) -> None:
        """Update the text and paths on board labels.

        Args:
            word_list (List[ResultWord]): A list of result words to be displayed on the labels.
        """

        for label, result in zip(self.labels, word_list):
            text = result.text()
            path = result.path

            label.set_hover(text, path)

    @abstractmethod
    def button_command(self, swap: int) -> None:
        """Handle a button click action, to be implemented in subclasses.

        Args:
            swap (int): The number of swaps represented by the clicked button.
        """

        pass
