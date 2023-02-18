
import tkinter as tk
from tkinter.font import Font
from gameboard import GameBoard
from validate import WordValidate
from spellsolver import SpellSolver
from utils import valid_word


class BoardMenu:

    def __init__(self, board, entry):
        self.board = board
        app = board.app
        
        self.menu = tk.Menu(app.root, tearoff = 0)

        def mult_word():
            self.board.mult.set_mult_word(entry.cord)

        def mult_DL():
            self.board.mult.set_mult_DL(entry.cord)

        def mult_TL():
            self.board.mult.set_mult_TL(entry.cord)

        def remove_mult():
            self.board.mult.remove_mult()

        self.menu.add_command(label="2X", command=mult_word)
        self.menu.add_command(label="DL", command=mult_DL)
        self.menu.add_command(label="TL", command=mult_TL)
        self.menu.add_separator()
        self.menu.add_command(label="Remove bonus", command=remove_mult)


class BoardEntry:

    def __init__(self, board, aux_cord):
        self.board = board
        app = board.app

        x, y = aux_cord % 5, aux_cord // 5
        self.cord = (x, y)
        self.menu = BoardMenu(board, self)

        def on_validate(p, aux_cord):
            aux_cord = int(aux_cord) % 25
            cord = (aux_cord % 5, aux_cord // 5)
            
            if len(p) == 1:
                board.inputs[cord].focus_set()
                board.inputs[cord].select_range(0, 'end')
            
            return True
        
        def do_popup(event):
            try:
                self.menu.menu.tk_popup(event.x_root, event.y_root)
            finally:
                self.menu.menu.grab_release()

        board.tiles[self.cord] = tk.StringVar(app.root, value='')

        entry = tk.Entry(app.root, textvariable=board.tiles[self.cord], validate="key", highlightthickness=2)
        entry["borderwidth"] = "1px"
        entry["font"] = Font(family='Times',size=10)
        entry["fg"] = "#333333"
        entry["justify"] = "center"
        entry['validatecommand'] = (entry.register(on_validate), '%P', aux_cord+1)
        entry.place(x=app.xoff+x*32,y=app.yoff+y*32,width=32,height=32)
        entry.configure(highlightbackground="black", highlightcolor="black", font=('Roboto', 16))
        entry.bind("<Button-3>", do_popup)

        board.inputs[self.cord] = entry


class BoardLabel:

    def __init__(self, board, num):
        self.board = board
        app = board.app

        self.label = tk.Label(app.root)
        self.label["borderwidth"] = "1px"
        self.label["font"] = Font(family='Times',size=14)
        self.label["fg"] = "#333333"
        self.label["justify"] = "center"
        self.label["text"] = f""
        self.label.place(x=320,y=10+num*22,width=250,height=25)
    
    def set_text(self, text):
        self.label["text"] = str(text)


class BoardButton:

    def __init__(self, board, text, num, command):
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
        

class LabelHover:

    def __init__(self, board, label, path):
        self.board = board
        self.label = label
        self.path = path

        self.label.label.bind('<Enter>', lambda _ : self.hover())
        self.label.label.bind('<Leave>', lambda _ : self.unhover())

    def hover(self):
        for tile in self.path:
            if tile.swap:
                self.board.inputs[tile.cord].configure(highlightbackground="red", highlightcolor="red", background="red", font=('Roboto', 20, tk.font.BOLD), fg="white")
                self.board.tiles[tile.cord].set(tile.letter)
            else:
                self.board.inputs[tile.cord].configure(highlightbackground="blue", highlightcolor="blue", background="blue", font=('Roboto', 20, tk.font.BOLD), fg="white")
        self.label.label.focus_set()

    def unhover(self):
        for tile in self.path:
            self.board.inputs[tile.cord].configure(highlightbackground="black", highlightcolor="black", background="white", font=('Roboto', 16, tk.font.NORMAL), fg="black")
            self.board.tiles[tile.cord].set(self.board.gameboard.tiles[tile.cord].letter)
            self.board.mult.configure_mult()


class MultHandler:

    def __init__(self, board):
        self.board = board

        self.mult_cord = None
        self.DL_cord = None
        self.TL_cord = None
    
    def set_mult_word(self, cord):
        if self.mult_cord != None:
            self.board.inputs[self.mult_cord].configure(highlightbackground="black", highlightcolor="black", background="white", font=('Roboto', 16, tk.font.NORMAL), fg="black")

        self.mult_cord = cord
        self.board.inputs[self.mult_cord].configure(highlightbackground="deep pink", highlightcolor="deep pink", background="white", font=('Roboto', 16, tk.font.NORMAL), fg="black")

    def set_mult_DL(self, cord):
        if self.DL_cord != None:
            self.board.inputs[self.DL_cord].configure(highlightbackground="black", highlightcolor="black", background="white", font=('Roboto', 16, tk.font.NORMAL), fg="black")
        
        self.DL_cord = cord
        self.board.inputs[self.DL_cord].configure(highlightbackground="gold", highlightcolor="gold", background="white", font=('Roboto', 16, tk.font.NORMAL), fg="black")

    def set_mult_TL(self, cord):
        if self.TL_cord != None:
            self.board.inputs[self.TL_cord].configure(highlightbackground="black", highlightcolor="black", background="white", font=('Roboto', 16, tk.font.NORMAL), fg="black")
        
        self.TL_cord = cord
        self.board.inputs[self.TL_cord].configure(highlightbackground="gold", highlightcolor="gold", background="white", font=('Roboto', 16, tk.font.NORMAL), fg="black")

    def configure_mult(self):
        if self.mult_cord != None:
            self.board.inputs[self.mult_cord].configure(highlightbackground="deep pink", highlightcolor="deep pink", background="white", font=('Roboto', 16, tk.font.NORMAL), fg="black")
        if self.DL_cord != None:
            self.board.inputs[self.DL_cord].configure(highlightbackground="gold", highlightcolor="gold", background="white", font=('Roboto', 16, tk.font.NORMAL), fg="black")
        if self.TL_cord != None:
            self.board.inputs[self.TL_cord].configure(highlightbackground="gold", highlightcolor="gold", background="white", font=('Roboto', 16, tk.font.NORMAL), fg="black")
        
    def remove_mult(self):
        if self.mult_cord != None:
            self.board.inputs[self.mult_cord].configure(highlightbackground="black", highlightcolor="black", background="white", font=('Roboto', 16, tk.font.NORMAL), fg="black")
        if self.DL_cord != None:
            self.board.inputs[self.DL_cord].configure(highlightbackground="black", highlightcolor="black", background="white", font=('Roboto', 16, tk.font.NORMAL), fg="black")
        if self.TL_cord != None:
            self.board.inputs[self.TL_cord].configure(highlightbackground="black", highlightcolor="black", background="white", font=('Roboto', 16, tk.font.NORMAL), fg="black")
        
        self.mult_cord = None
        self.DL_cord = None
        self.TL_cord = None


class Board:

    def __init__(self, app, validate):
        self.validate = validate
        self.app = app

        self.mult = MultHandler(self)

        self.entry = []
        self.labels = []
        self.buttons = []
        
        self.inputs = {}
        self.tiles = {}
        
        for aux_cord in range(25):
            self.entry += [BoardEntry(self, aux_cord)]
        
        for num in range(10):
            self.labels += [BoardLabel(self, num)]
        
        self.buttons += [BoardButton(self, "Normal", 0, lambda: self.button_command(swap=""))]
        self.buttons += [BoardButton(self, "Swap", 1, lambda: self.button_command(swap="1"))]
    

    def button_command(self, swap):
        gameboard_string = "".join([t.get().lower() for t in self.tiles.values()])
        if not valid_word(gameboard_string) or len(gameboard_string) != 25:
            return

        self.gameboard = GameBoard()
        self.gameboard.init_nodes(gameboard_string)

        if self.mult.mult_cord != None:
            self.gameboard.set_mult_word(self.mult.mult_cord)
        if self.mult.DL_cord != None:
            self.gameboard.set_mult_letter(self.mult.DL_cord, 2)
        if self.mult.TL_cord != None:
            self.gameboard.set_mult_letter(self.mult.TL_cord, 3)

        spellsolver = SpellSolver(self.validate, self.gameboard)
        word_list = spellsolver.get_word_list(swap)

        for i, result in enumerate(word_list):
            if i >= len(self.labels):
                break
            self.labels[i].set_text(result[:2])
            LabelHover(self, self.labels[i], result[-1])
        

class GraphicUI:
    
    def __init__(self, root, validate):

        self.xoff, self.yoff = 25, 25
        self.root = root

        root.title("Spellsolver")
        width = 600
        height = 256
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.board = Board(self, validate)


if __name__ == "__main__":
    validate = WordValidate()
    validate.from_file("wordlist_english.txt", swap=True)

    print("Init GraphicUI")
    root = tk.Tk()
    app = GraphicUI(root, validate)
    root.mainloop()
