from typing import Dict, List, Tuple

from src.config import SWAP
from src.interfaces.baseui import BaseUI
from src.interfaces.boardbutton import BoardButton
from src.interfaces.boardlabel import BoardLabel
from src.interfaces.boardtile import BoardTile
from src.modules.resultlist import ResultWord
from src.utils.utils import aux_to_indices


class Board:
    """Represents an abstract board"""

    def __init__(self, app: BaseUI) -> None:
        self.app: BaseUI = app

        self.tiles: Dict[Tuple[int], BoardTile] = {}
        self.buttons: List[BoardButton] = []
        self.labels: List[BoardLabel] = []

        self.double_swap: bool = SWAP >= 2

        for aux_cord in range(25):
            self.tiles[aux_to_indices(aux_cord)] = BoardTile(self, aux_cord)

        self.buttons.append(
            BoardButton(self, 0, "Normal", lambda: self.button_command(swap=0))
        )
        self.buttons.append(
            BoardButton(self, 1, "1 Swap", lambda: self.button_command(swap=1))
        )
        if self.double_swap:
            self.buttons.append(
                BoardButton(self, 2, "2 Swap", lambda: self.button_command(swap=2))
            )

        self.labels = [BoardLabel(self, num) for num in range(10)]

    def set_results(self, word_list: List[ResultWord]):
        """Set spellsolver result"""
        if len(word_list) < 10:
            for label in self.labels:
                label.reset()

        for label, result in zip(self.labels, word_list):
            label.set_hover(text=result.text(), path=result.path)

    def button_command(self, swap: int) -> None:
        raise NotImplementedError()
