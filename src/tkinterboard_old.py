import tkinter as tk
from tkinter.font import Font
from src.baseui import BaseUI



class BoardEntry:
    """Represents a square tile in GUI"""
    def __init__(self, board: 'TkinterBoard', aux_cord: int) -> None:
        self.board = board
        app = board.app

        
        
        

        stringvar = tk.StringVar(app.root, value='')

        self.board.tiles[self.cord] = stringvar
        self.board.inputs[self.cord] = self.entry



        



class MultHandler:
    """Handle Spellcast word & letter multipliers"""
    def __init__(self, board: 'TkinterBoard') -> None:
        self.board: TkinterBoard = board
        app = board.app

        self.mult_cord: tuple = None
        self.DL_cord: tuple = None
        self.TL_cord: tuple = None
    
    def font_conf(self, color: str) -> dict:
        """Get default font configuration"""
        return {
            "highlightbackground": color,
            "highlightcolor": color,
            "background": "white",
            "font": ('Roboto', 16, tk.font.NORMAL),
            "fg": "black"
        }
    
    def set_mult_word(self, cord: tuple) -> None:
        """Set a mult_word in a tile"""
        if self.mult_cord != None:
            self.board.inputs[self.mult_cord].configure(**self.font_conf("black"))

        self.mult_cord = cord
        self.board.inputs[self.mult_cord].configure(**self.font_conf("deep pink"))

    def set_mult_DL(self, cord: tuple) -> None:
        """Set a mult_DL in a tile"""
        if self.DL_cord != None:
            self.board.inputs[self.DL_cord].configure(**self.font_conf("black"))
        
        self.DL_cord = cord
        self.board.inputs[self.DL_cord].configure(**self.font_conf("gold"))

    def set_mult_TL(self, cord: tuple) -> None:
        """Set a mult_TL in a tile"""
        if self.TL_cord != None:
            self.board.inputs[self.TL_cord].configure(**self.font_conf("black"))
        
        self.TL_cord = cord
        self.board.inputs[self.TL_cord].configure(**self.font_conf("gold"))

    def configure_mult(self) -> None:
        """Change colors of a tile based in the multipliers"""
        if self.mult_cord != None:
            self.board.inputs[self.mult_cord].configure(**self.font_conf("deep pink"))
        if self.DL_cord != None:
            self.board.inputs[self.DL_cord].configure(**self.font_conf("gold"))
        if self.TL_cord != None:
            self.board.inputs[self.TL_cord].configure(**self.font_conf("gold"))
        
    def remove_mult(self) -> None:
        """Remove colors of a tile"""
        if self.mult_cord != None:
            self.board.inputs[self.mult_cord].configure(**self.font_conf("black"))
        if self.DL_cord != None:
            self.board.inputs[self.DL_cord].configure(**self.font_conf("black"))
        if self.TL_cord != None:
            self.board.inputs[self.TL_cord].configure(**self.font_conf("black"))
        
        self.mult_cord = None
        self.DL_cord = None
        self.TL_cord = None


class TkinterBoard:
    """Represents a Tkinter Board with his logic"""
    def __init__(self, app: BaseUI) -> None:
        self.app: BaseUI = app
        self.mult: MultHandler = MultHandler(self)

        self.entry: list = []
        self.labels: list = []
        self.buttons: list = []
        
        self.inputs: dict = {}
        self.tiles: dict = {}
        
        for aux_cord in range(25):
            self.entry += [BoardEntry(self, aux_cord)]

        for num in range(10):
            self.labels += [BoardLabel(self, num)]
        
        self.buttons += [BoardButton(self, "Normal", 0, lambda: self.button_command(swap=False))]
        self.buttons += [BoardButton(self, "Swap", 1, lambda: self.button_command(swap=True))]
    
    def button_command(self, swap: bool) -> None:
        """Execute SpellSolver when a button is pressed"""
        gameboard_string = "".join([t.get().lower() for t in self.tiles.values()])
        self.app.gameboard.load(gameboard_string)

        if self.mult.mult_cord != None:
            self.app.gameboard.set_mult_word(self.mult.mult_cord)
        if self.mult.DL_cord != None:
            self.app.gameboard.set_mult_letter(self.mult.DL_cord, 2)
        if self.mult.TL_cord != None:
            self.app.gameboard.set_mult_letter(self.mult.TL_cord, 3)
        
        word_list = self.app.solve(swap)
        for label, result in zip(self.labels, word_list):
            label.set_text(result[:2])
            LabelHover(self, label, result[-1])
