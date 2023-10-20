import tkinter as tk

from src.utils.utils import aux_to_indices


class BoardEntry:
    """Represents a square tile in the board"""

    def __init__(self, board, menu, stringvar: tk.StringVar, aux_cord: int) -> None:
        self.board = board
        app = board.app

        cord = aux_to_indices(aux_cord)
        next = aux_to_indices(aux_cord + 1)
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
