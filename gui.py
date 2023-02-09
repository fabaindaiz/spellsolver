
import tkinter as tk
from tkinter.font import Font
from gameboard import GameBoard
from validate import WordValidate
from spellsolver import SpellSolver
from utils import valid_word


class App:
    def __init__(self, root, validate):
        self.validate = validate

        self.tiles = {}
        self.inputs = {}
        
        self.labels = []
        
        root.title("Spellsolver")
        width = 600
        height = 256
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        def on_validate(p, aux_cord):
            aux_cord = int(aux_cord) % 25
            cord = (aux_cord % 5, aux_cord // 5)

            if len(p) == 1:
                self.inputs[cord].focus_set()
                self.inputs[cord].select_range(0, 'end')
            return True

        xoff, yoff = 25, 25
        aux_cord = 0

        for __ in range(25):
            x = aux_cord % 5
            y = aux_cord // 5
            aux_cord += 1

            self.tiles[(x, y)] = tk.StringVar(root, value='')

            entry = tk.Entry(root, textvariable=self.tiles[(x, y)], validate="key", highlightthickness=2)
            entry["borderwidth"] = "1px"
            entry["font"] = Font(family='Times',size=10)
            entry["fg"] = "#333333"
            entry["justify"] = "center"
            entry['validatecommand'] = (entry.register(on_validate), '%P', aux_cord)
            entry.place(x=xoff+x*32,y=yoff+y*32,width=32,height=32)
            entry.configure(highlightbackground="black", highlightcolor="black", font=('Roboto', 16))

            self.inputs[(x, y)] = entry

        for i in range(10):
            label = tk.Label(root)
            label["font"] = Font(family='Times',size=10)
            label["fg"] = "#333333"
            label["justify"] = "center"
            label["text"] = f""
            label.place(x=320,y=10+i*20,width=250,height=25)

            self.labels += [label]
        
        self.button = tk.Button(root)
        self.button["bg"] = "#e9e9ed"
        self.button["font"] = Font(family='Times',size=10)
        self.button["fg"] = "#000000"
        self.button["justify"] = "center"
        self.button["text"] = "Generate Words"
        self.button.place(x=xoff,y=yoff+160,width=160,height=25)
        self.button["command"] = self.button_command
    

    class lblHover:
        def __init__(self, gameboard, label, path, inputs, vals):
            self.gameboard = gameboard
            self.label = label
            self.path = path

            self.inputs = inputs
            self.vals = vals

            self.label.bind('<Enter>', lambda _ : self.hover())
            self.label.bind('<Leave>', lambda _ : self.unhover())
            
        def hover(self):
            for tile in self.path:
                if tile.swap:
                    self.inputs[tile.cord].configure(highlightbackground="red", highlightcolor="red", background="red", font=('Roboto', 20, tk.font.BOLD), fg="white")
                    self.vals[tile.cord].set(tile.letter)
                else:
                    self.inputs[tile.cord].configure(highlightbackground="blue", highlightcolor="blue", background="blue", font=('Roboto', 20, tk.font.BOLD), fg="white")

        def unhover(self):
            for tile in self.path:
                self.inputs[tile.cord].configure(highlightbackground="black", highlightcolor="black", background="white", font=('Roboto', 16, tk.font.NORMAL), fg="black")
                self.vals[tile.cord].set(self.gameboard.tiles[tile.cord].letter)

    def button_command(self):
        gameboard_string = "".join([t.get().lower() for t in self.tiles.values()])
        if not valid_word(gameboard_string) or len(gameboard_string) != 25:
            return

        self.gameboard = GameBoard()
        self.gameboard.init_nodes(gameboard_string)

        spellsolver = SpellSolver(self.validate, self.gameboard)
        word_list = spellsolver.get_word_list(swap="1")

        for i, result in enumerate(word_list):
            if i >= len(self.labels):
                break
            word = "".join([n.letter for n in result[-1]])
            self.labels[i]["text"] = str(result[0:3])
            self.lblHover(self.gameboard, self.labels[i], result[-1], self.inputs, self.tiles)


if __name__ == "__main__":
    print("Init WordValidate")
    validate = WordValidate()
    validate.from_file("wordlist_english.txt", swap=True)

    print("Init Gui")
    root = tk.Tk()
    app = App(root, validate)
    root.mainloop()