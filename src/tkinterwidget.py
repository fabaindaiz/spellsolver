import tkinter as tk
from tkinter.font import Font
from src.baseui import BaseUI


class BoardMenu:
    """Represents the contextual menu in GUI"""
    def __init__(self, board: 'TkinterBoard', cord: tuple) -> None:
        self.board = board
        app = board.app

        self.menu = tk.Menu(app.root, tearoff = 0)
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


class LabelHover:
    """Represent a hover event handler for result labels"""
    def __init__(self, board: 'TkinterBoard', label: tk.Label, path: list) -> None:
        self.board = board
        self.label = label
        self.path = path

        self.label.bind('<Enter>', lambda _ : self.hover())
        self.label.bind('<Leave>', lambda _ : self.unhover())

    def hover(self) -> None:
        """Handle hover event in the label"""
        for tile in self.path:
            self.board.tiles[tile.cord].hover(tile.letter, tile.swap)   
        self.label.focus_set()

    def unhover(self) -> None:
        """handle unhover event in the label"""
        for tile in self.path:
            self.board.tiles[tile.cord].unhover()

class TkinterTile:
    def __init__(self, board, cord):
        self.board = board
        app = board.app

        self.input = None
        self.letter = None

        self.menu = BoardMenu(self.board, cord)
        self.stringvar = tk.StringVar(app.root, value='')

        self.entry = BoardEntry(self.board, self.menu, self.stringvar, next_cord)


    def hover(self, letter, swap):
        if swap:
            self.input.configure(
                highlightbackground="red", highlightcolor="red", background="red",
                font=('Roboto', 20, tk.font.BOLD), fg="white")
            self.stringvar.set(letter)
        else:
            self.input.configure(
                highlightbackground="blue", highlightcolor="blue", background="blue",
                font=('Roboto', 20, tk.font.BOLD), fg="white")
    
    def unhover(self) -> None:
        self.input.configure(
            highlightbackground="black", highlightcolor="black", background="white",
            font=('Roboto', 16, tk.font.NORMAL), fg="black")
        self.stringvar.set(self.letter)
        self.board.mult.configure_mult()

class BoardLabel:
    """Represents a result label"""
    def __init__(self, board: 'TkinterBoard', text: str, num: int) -> None:
        self.board = board
        app = board.app

        self.label = tk.Label(app.root)
        self.label["borderwidth"] = "1px"
        self.label["font"] = Font(family='Times',size=14)
        self.label["fg"] = "#333333"
        self.label["justify"] = "center"
        self.label["text"] = text
        self.label.place(x=320,y=10+num*22,width=250,height=25)
    
    def set_text(self, text: str) -> None:
        """Set text value of the label"""
        self.label["text"] = str(text)

class BoardEntry:
    def __init__(self, board: 'TkinterBoard', menu, stringvar, cord: tuple, next_cord: tuple):
        self.board = board
        app = board.app

        def on_validate(input: str) -> bool:
            """Validate the value in the entry"""            
            if len(input) == 1:
                self.board.inputs[next_cord].focus_set()
                self.board.inputs[next_cord].select_range(0, 'end')
            return True
        
        (x, y) = cord

        self.entry: tk.Entry = tk.Entry(app.root, textvariable=stringvar, validate="key", highlightthickness=2)
        self.entry["borderwidth"] = "1px"
        self.entry["font"] = Font(family='Times',size=10)
        self.entry["fg"] = "#333333"
        self.entry["justify"] = "center"
        self.entry['validatecommand'] = (self.entry.register(on_validate), '%P')
        self.entry.place(x=app.xoff+x*32, y=app.yoff+y*32, width=32, height=32)
        self.entry.configure(highlightbackground="black", highlightcolor="black", font=('Roboto', 16))
        self.entry.bind("<Button-3>", lambda event: menu.do_popup(event))

class BoardButton:
    """Represents a solve button"""
    def __init__(self, board: 'TkinterBoard', text: str, num: int, command: callable) -> None:
        self.board = board
        app = board.app

        self.button = tk.Button(app.root)
        self.button["bg"] = "#e9e9ed"
        self.button["font"] = Font(family='Times',size=10)
        self.button["fg"] = "#000000"
        self.button["justify"] = "center"
        self.button["text"] = text
        self.button.place(x=app.xoff+num*80,y=app.yoff+160,width=80,height=25)
        self.button["command"] = command

class TkinterBoard:
    pass

