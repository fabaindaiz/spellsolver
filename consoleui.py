from argparse import ArgumentParser, Namespace

from src.config import SWAP
from src.entities import Coordinates
from src.interfaces.baseui import BaseUI, GameSolver
from src.modules.gameboard.resultlist import ResultList


class ConsoleUI(BaseUI):
    """Console UI"""

    def __init__(self) -> None:
        super().__init__()

        self.parser: ArgumentParser = ArgumentParser(
            description="Spellsolver", epilog="Word Finder for Discord Spellcast"
        )

        self.parser.add_argument(
            "game", type=str, default=None, nargs="?", help="gameboard string"
        )
        self.parser.add_argument(
            "--swap", type=int, required=False, help="enable swap mode", default=0
        )

        self.parser.add_argument(
            "--x2", type=str, required=False, help="word multiplier", default=""
        )
        self.parser.add_argument(
            "--dl", type=str, required=False, help="double letter", default=""
        )
        self.parser.add_argument(
            "--tl", type=str, required=False, help="triple letter", default=""
        )

        self.opt = self.parser.parse_args()

        swap = self.opt.swap if self.opt.swap else SWAP
        self.init(swap=swap)

    def mainargs(self, opt: Namespace) -> None:
        """Main loop of the Console UI using arguments"""
        gameboard_string = opt.game
        solver = self.load(gameboard_string)

        X2_string = opt.x2.replace(".", " ")
        DL_string = opt.dl.replace(".", " ")
        TL_string = opt.tl.replace(".", " ")
        solver.set_multipliers(X2_string, DL_string, TL_string)

        swap = opt.swap if opt.swap else SWAP
        results = solver.solve(swap=swap)
        self.print_results(results)

    def maininput(self) -> None:
        """Main loop of the Console UI using inputs"""
        gameboard_string = input("Insert a gameboard: ")
        solver = self.load(gameboard_string)

        X2_string = input("Insert 2x coordinates: ").replace(".", " ")
        DL_string = input("Insert DL coordinates: ").replace(".", " ")
        TL_string = input("Insert TL coordinates: ").replace(".", " ")
        solver.set_multipliers(X2_string, DL_string, TL_string)

        swap = int(input("Use swap?: "))
        results = solver.solve(swap=swap)
        self.print_results(results)

    def mainloop(self) -> bool:
        """Main loop of the Console UI"""
        if self.opt.game:
            self.mainargs(self.opt)
            return False

        try:
            self.maininput()
        except Exception as e:
            print("Exception:", e)

        return True

    @staticmethod
    def print_results(results: ResultList) -> None:
        """Print results to console"""
        sorted_words = results.sorted_words
        results.words_to_text(sorted_words[:10])


if __name__ == "__main__":
    app = ConsoleUI()

    loop = True
    while loop:
        loop = app.mainloop()
