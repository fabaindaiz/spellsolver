import tkinter as tk
from src.tkinterboard import TkinterBoard
from src.baseui import BaseUI
        

class GraphicUI(BaseUI):
    """Graphic UI"""
    def __init__(self) -> None:
        super().__init__()
        
        self.root: tk.Tk = tk.Tk()
        self.root.title("Spellsolver")

        width = 600
        height = 256
        self.xoff, self.yoff = 25, 25
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()

        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)

        self.board: TkinterBoard = TkinterBoard(self)
    
    def mainloop(self) -> bool:
        """Mainloop of the Graphic UI"""
        self.root.mainloop()
        return False


if __name__ == "__main__":
    app = GraphicUI()
    
    loop = True
    while(loop):
        loop = app.mainloop()
