import tkinter as tk
from tkinter.font import Font
from src.resultlist import ResultWord
from src.gameboard import GameTile
from src.baseui import BaseUI
from src.utils import get_coordinate


class Board:
    """Represents an abstract board"""
    def __init__(self, app: BaseUI) -> None:
        self.app: BaseUI = app

        self.buttons: list[BoardButton] = []
        self.labels: list[BoardLabel] = []
        self.tiles: dict[tuple[int], BoardTile] = {}

        self.buttons += [BoardButton(self, 0, "Normal", lambda: self.button_command(swap=False))]
        self.buttons += [BoardButton(self, 1, "Swap", lambda: self.button_command(swap=True))]

        for num in range(10):
            self.labels += [BoardLabel(self, num)]

        for aux_cord in range(25):
            self.tiles[get_coordinate(aux_cord)] = BoardTile(self, aux_cord)
    
    def set_results(self, word_list):
        """Set spellsolver result"""
        label: BoardLabel
        result: ResultWord
        for label, result in zip(self.labels, word_list):
            label.set_hover(text=result.text(), path=result.path)

class BoardTile:
    """Represents a tile from the board with his logic"""
    def __init__(self, board: Board, aux_cord: int) -> None:
        self.board: Board = board
        app = board.app

        self.stringvar: tk.StringVar = tk.StringVar(app.root, value='')
        self.menu: BoardMenu = BoardMenu(self.board, aux_cord)
        self.entry: BoardEntry = BoardEntry(self.board, self.menu, self.stringvar, aux_cord)

    def letter(self) -> str:
        """Get the letter of the tile in lower case"""
        return self.stringvar.get().lower()
    
    def multiplier(self, color: str) -> None:
        """Set multiplier color in tile"""
        font_config = {
            "highlightbackground": color,
            "highlightcolor": color,
            "background": "white",
            "font": ('Roboto', 16, tk.font.NORMAL),
            "fg": "black"
        }
        self.entry.entry.configure(**font_config)

    def hover(self, letter: str, swap: bool) -> None:
        """Handle hover event on the tile"""
        if swap:
            self.entry.entry.configure(
                highlightbackground="red", highlightcolor="red", background="red",
                font=('Roboto', 20, tk.font.BOLD), fg="white")
            self.stringvar.set(letter)
        else:
            self.entry.entry.configure(
                highlightbackground="blue", highlightcolor="blue", background="blue",
                font=('Roboto', 20, tk.font.BOLD), fg="white")
    
    def unhover(self, cord: tuple) -> None:
        """Handle unhover event on the tile"""
        self.entry.entry.configure(
            highlightbackground="black", highlightcolor="black", background="white",
            font=('Roboto', 16, tk.font.NORMAL), fg="black")
        self.stringvar.set(self.board.app.gameboard.tiles[cord].letter)
        self.board.mult.configure_mult()

class BoardMenu:
    """Represents the contextual menu in GUI"""
    def __init__(self, board: Board, aux_cord: int) -> None:
        self.board: Board = board
        app = board.app

        cord = get_coordinate(aux_cord)

        self.menu: tk.Menu = tk.Menu(app.root, tearoff = 0)
        self.menu.add_command(label="2X", command=lambda: self.board.mult.set_mult_word(cord))
        self.menu.add_command(label="DL", command=lambda: self.board.mult.set_mult_DL(cord))
        self.menu.add_command(label="TL", command=lambda: self.board.mult.set_mult_TL(cord))
        self.menu.add_separator()
        self.menu.add_command(label="Remove bonus", command=lambda: self.board.mult.remove_mult())

    def popup(self, event) -> None:
        """Handle the popup event"""
        try:
            self.menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.menu.grab_release()

class BoardEntry:
    """Represents a square tile in the board"""
    def __init__(self, board: Board, menu: BoardMenu, stringvar: tk.StringVar, aux_cord: int) -> None:
        self.board: Board = board
        app = board.app

        def on_validate(input: str) -> bool:
            """Validate the value in the entry"""
            if len(input) == 1:
                next_cord = get_coordinate((aux_cord + 1) % 25)
                entry: BoardEntry = self.board.tiles[next_cord].entry
                entry.entry.focus_set()
                entry.entry.select_range(0, 'end')
            return True
        
        (x, y) = get_coordinate(aux_cord)

        self.entry: tk.Entry = tk.Entry(app.root, textvariable=stringvar, validate="key", highlightthickness=2)
        self.entry["borderwidth"] = "1px"
        self.entry["font"] = Font(family='Times',size=10)
        self.entry["fg"] = "#333333"
        self.entry["justify"] = "center"
        self.entry['validatecommand'] = (self.entry.register(on_validate), '%P')
        self.entry.place(x=app.xoff+x*32, y=app.yoff+y*32, width=32, height=32)
        self.entry.configure(highlightbackground="black", highlightcolor="black", font=('Roboto', 16))
        self.entry.bind("<Button-3>", lambda event: menu.popup(event))

class BoardButton:
    """Represents a solve button"""
    def __init__(self, board: Board, num: int, text: str, command: callable) -> None:
        self.board: Board = board
        app = board.app

        self.button: tk.Button = tk.Button(app.root)
        self.button["bg"] = "#e9e9ed"
        self.button["font"] = Font(family='Times',size=10)
        self.button["fg"] = "#000000"
        self.button["justify"] = "center"
        self.button["text"] = text
        self.button.place(x=app.xoff+num*80,y=app.yoff+160,width=80,height=25)
        self.button["command"] = command

class BoardLabel:
    """Represents a result label"""
    def __init__(self, board: Board, num: int, text: str="") -> None:
        self.board: Board = board
        app = board.app

        self.hover: LabelHover = None

        self.label: tk.Label = tk.Label(app.root)
        self.label["borderwidth"] = "1px"
        self.label["font"] = Font(family='Times',size=14)
        self.label["fg"] = "#333333"
        self.label["justify"] = "center"
        self.label["text"] = text
        self.label.place(x=320,y=10+num*22,width=250,height=25)
    
    def set_hover(self, text: str, path: list[GameTile]):
        """Set hover & text value of the label"""
        self.hover = LabelHover(self.board, self, path)
        self.label["text"] = str(text)

class LabelHover:
    """Represent a hover event handler for result labels"""
    def __init__(self, board: Board, label: BoardLabel, path: list[GameTile]) -> None:
        self.board: Board = board
        self.label: BoardLabel = label
        self.path: list[GameTile] = path

        self.label.label.bind('<Enter>', lambda _ : self._hover())
        self.label.label.bind('<Leave>', lambda _ : self._unhover())

    def _hover(self) -> None:
        """Handle hover event in the label"""
        for tile in self.path:
            self.board.tiles[tile.cord].hover(tile.letter, tile.swap)   
        self.label.label.focus_set()

    def _unhover(self) -> None:
        """handle unhover event in the label"""
        for tile in self.path:
            self.board.tiles[tile.cord].unhover(tile.cord)
