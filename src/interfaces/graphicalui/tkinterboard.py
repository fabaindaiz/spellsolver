from src.interfaces.baseui import BaseUI
from src.interfaces.graphicalui.multhandler import MenuHandler
from src.interfaces.graphicalui.board import Board


class TkinterBoard(Board):
    def __init__(self, app: BaseUI) -> None:
        super().__init__(app)
        self.menu: MenuHandler = MenuHandler(self)

    def button_command(self, swap: int) -> None:
        gameboard_string = "".join(tile.letter() for tile in self.tiles.values())
        self.app.gameboard.load(gameboard_string)

        if self.menu.word_cord is not None:
            self.app.gameboard.set_mult_word(self.menu.word_cord)
        if self.menu.letter_cord is not None:
            self.app.gameboard.set_mult_letter(
                self.menu.letter_cord, self.menu.letter_mult
            )
        if self.menu.letter_gems is not None:
            self.app.gameboard.set_gems(self.menu.letter_gems)

        results = self.app.solve(swap)
        sorted_words = results.sorted_words()
        self.set_timer(results.timer.elapsed_millis())
        self.set_results(sorted_words[:10])
