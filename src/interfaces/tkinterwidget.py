import tkinter as tk
from tkinter.font import Font
from typing import Callable, Dict, List, Tuple
from src.modules.resultlist import ResultWord
from src.modules.gameboard import GameTile
from src.interfaces.baseui import BaseUI
from src.utils.utils import auxiliary_coordinate_to_indices
from src.config import SWAP


class Board:
    """Represents an abstract board"""

    def __init__(self, app: BaseUI) -> None:
        self.app: BaseUI = app

        self.tiles: Dict[Tuple[int], BoardTile] = {}
        self.buttons: List[BoardButton] = []
        self.labels: List[BoardLabel] = []

        self.double_swap: bool = SWAP >= 2

        for aux_cord in range(25):
            self.tiles[auxiliary_coordinate_to_indices(aux_cord)] = BoardTile(
                self, aux_cord
            )

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


class BoardTile:
    """Represents a tile from the board with his logic"""

    def __init__(self, board: Board, aux_cord: int) -> None:
        self.board: Board = board
        app = board.app

        self.backup_letter: str = None

        self.stringvar: tk.StringVar = tk.StringVar(app.window, value="")
        self.menu: BoardMenu = BoardMenu(self.board, aux_cord)
        self.entry: BoardEntry = BoardEntry(
            self.board, self.menu, self.stringvar, aux_cord
        )

        self.entry.entry.configure(
            highlightbackground="black",
            highlightcolor="black",
            background="white",
            font=("Roboto", 18, tk.font.NORMAL),
            fg="black",
        )

    def letter(self) -> str:
        """Get the letter of the tile in lower case"""
        return self.stringvar.get().lower()

    def multiplier(self, color: str) -> None:
        """Set multiplier color in tile"""
        font_config = {
            "highlightbackground": color,
            "highlightcolor": color,
            "background": "white",
            "font": ("Roboto", 18, tk.font.NORMAL),
            "fg": "black",
        }
        self.entry.entry.configure(**font_config)

    def hover(self, letter: str, swap: bool) -> None:
        """Handle hover event on the tile"""
        self.backup_letter = self.letter()
        self.stringvar.set(letter)

        color = "red" if swap else "blue"
        self.entry.entry.configure(
            highlightbackground=color,
            highlightcolor=color,
            background=color,
            font=("Roboto", 24, tk.font.BOLD),
            fg="white",
        )

    def unhover(self) -> None:
        """Handle unhover event on the tile"""
        self.entry.entry.configure(
            highlightbackground="black",
            highlightcolor="black",
            background="white",
            font=("Roboto", 18, tk.font.NORMAL),
            fg="black",
        )
        self.stringvar.set(self.backup_letter)
        self.board.mult.configure_mult()


class BoardMenu:
    """Represents the contextual menu in GUI"""

    def __init__(self, board: Board, aux_cord: int) -> None:
        self.board: Board = board
        app = board.app

        cord = auxiliary_coordinate_to_indices(aux_cord)

        self.menu: tk.Menu = tk.Menu(app.window, tearoff=0)
        self.menu.add_command(
            label="2X", command=lambda: self.board.mult.set_mult_word(cord)
        )
        self.menu.add_command(
            label="DL", command=lambda: self.board.mult.set_mult_letter(cord, 2)
        )
        self.menu.add_command(
            label="TL", command=lambda: self.board.mult.set_mult_letter(cord, 3)
        )
        self.menu.add_separator()
        self.menu.add_command(
            label="Remove bonus", command=lambda: self.board.mult.remove_mult()
        )

    def popup(self, event) -> None:
        """Handle the popup event"""
        try:
            self.menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.menu.grab_release()


class BoardEntry:
    """Represents a square tile in the board"""

    def __init__(
        self, board: Board, menu: BoardMenu, stringvar: tk.StringVar, aux_cord: int
    ) -> None:
        self.board: Board = board
        app = board.app

        cord = auxiliary_coordinate_to_indices(aux_cord)
        next = auxiliary_coordinate_to_indices(aux_cord + 1)
        x, y = cord

        def on_validate(input: str) -> bool:
            """Validate the value in the entry"""
            if len(input) > 1:
                self.board.tiles[cord].entry.focus()
                return False
            if len(input) == 1:
                self.board.tiles[next].entry.focus()
            return True

        self.entry: tk.Entry = tk.Entry(
            app.window,
            textvariable=stringvar,
            validate="key",
            highlightthickness=2,
        )
        self.entry["borderwidth"] = "1px"
        self.entry["fg"] = "#333333"
        self.entry["justify"] = "center"
        self.entry["validatecommand"] = (self.entry.register(on_validate), "%P")
        self.entry.bind("<Button-3>", lambda event: menu.popup(event))
        self.entry.place(
            x=app.HORIZONTAL_PADDING + 40 * x,
            y=app.VERTICAL_PADDING + 40 * y,
            width=40,
            height=40,
        )

    def focus(self) -> None:
        """Set the focus on the entry"""
        self.entry.focus_set()
        self.entry.select_range(0, "end")


class BoardButton:
    """Represents a solve button"""

    def __init__(self, board: Board, num: int, text: str, command: Callable) -> None:
        self.board: Board = board
        app = board.app

        self.button: tk.Button = tk.Button(app.window)
        self.button["bg"] = "#e9e9ed"
        self.button["font"] = Font(family="Times", size=12)
        self.button["fg"] = "#000000"
        self.button["justify"] = "center"
        self.button["text"] = text
        self.button["command"] = command

        if self.board.double_swap:
            self.button.place(
                x=app.HORIZONTAL_PADDING + 67 * num,
                y=app.VERTICAL_PADDING + 210,
                width=67,
                height=30,
            )
        else:
            self.button.place(
                x=app.HORIZONTAL_PADDING + 100 * num,
                y=app.VERTICAL_PADDING + 210,
                width=100,
                height=30,
            )


class BoardLabel:
    """Represents a result label"""

    def __init__(self, board: Board, num: int, text: str = "") -> None:
        self.board: Board = board
        app = board.app

        self.text: str = text
        self.hover: LabelHover = None

        self.label: tk.Label = tk.Label(app.window)
        self.label["borderwidth"] = "1px"
        self.label["font"] = Font(family="Times", size=18)
        self.label["fg"] = "#333333"
        self.label["justify"] = "center"
        self.label["text"] = self.text
        self.label.place(x=300, y=20 + num * 25, width=250, height=25)

    def reset(self) -> None:
        self.hover: LabelHover = None
        self.label["text"] = self.text

    def set_hover(self, text: str, path: List[GameTile]) -> None:
        """Set hover & text value of the label"""
        self.hover = LabelHover(self.board, self, path)
        self.label["text"] = str(text)


class LabelHover:
    """Represent a hover event handler for result labels"""

    def __init__(self, board: Board, label: BoardLabel, path: List[GameTile]) -> None:
        self.board: Board = board
        self.label: BoardLabel = label
        self.path: List[GameTile] = path

        self.label.label.bind("<Enter>", lambda _: self._hover())
        self.label.label.bind("<Leave>", lambda _: self._unhover())

    def _hover(self) -> None:
        """Handle hover event in the label"""
        for tile in self.path:
            self.board.tiles[tile.cord].hover(tile.letter, tile.swap)
        self.label.label.focus_set()

    def _unhover(self) -> None:
        """handle unhover event in the label"""
        for tile in self.path:
            self.board.tiles[tile.cord].unhover()
