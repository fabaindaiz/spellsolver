import tkinter as tk
from tkinter.font import Font
from typing import Callable


class BoardButton:
    """Represents a solve button"""

    def __init__(self, board, num, text, command: Callable):
        self.board = board
        app = board.app

        self.button = tk.Button(app.window)
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
