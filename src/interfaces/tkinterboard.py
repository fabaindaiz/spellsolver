from src.interfaces.baseui import BaseUI
from src.interfaces.board import Board
from src.interfaces.multhandler import MultHandler


class TkinterBoard(Board):
    def __init__(self, app: BaseUI) -> None:
        super().__init__(app)
        self.mult: MultHandler = MultHandler(self)

    def button_command(self, swap: int) -> None:
        gameboard_string = "".join(tile.letter() for tile in self.tiles.values())
        self.app.gameboard.load(gameboard_string)

        if self.mult.mult_cord is not None:
            self.app.gameboard.set_mult_word(self.mult.mult_cord)
        if self.mult.letter_cord is not None:
            self.app.gameboard.set_mult_letter(
                self.mult.letter_cord, self.mult.letter_mult
            )

        results = self.app.solve(swap)
        sorted = results.sorted(console=True)
        self.set_results(sorted)
