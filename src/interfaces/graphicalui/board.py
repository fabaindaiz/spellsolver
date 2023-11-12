from src import SWAP
from src.entities import Coordinates
from src.interfaces import BaseUI
from src.modules.gameboard import ResultWord
from src.utils import aux_to_indices
from .button import Button
from .label import Label
from .menu_handler import MenuHandler
from .tile import Tile


class Board:
    def __init__(self, app: BaseUI) -> None:
        self.app: BaseUI = app
        self.double_swap: bool = SWAP >= 2
        self.buttons: list[Button] = []
        self.timer: Label = None
        self.labels: list[Label] = []
        self.tiles: dict[Coordinates, Tile] = {}
        self.menu: MenuHandler = MenuHandler(self)

        self.initialize_components()

        first_tile_coordinates = Coordinates(0, 0)
        self.tiles[first_tile_coordinates].entry.focus()

    def initialize_components(self) -> None:
        self.initialize_buttons()
        self.initialize_tiles()
        self.initialize_labels()

    def initialize_buttons(self) -> None:
        swap_options = [0, 1]

        if self.double_swap:
            swap_options.append(2)

        for option in swap_options:
            button = self.create_button(option)
            self.buttons.append(button)

    def create_button(self, swap_count: int) -> Button:
        return Button(
            parent=self.app,
            double_swap=self.double_swap,
            swap_count=swap_count,
            command=lambda: self.handle_button_click(swap_count),
        )

    def handle_button_click(self, swap_count: int) -> None:
        self.load_game_board()
        self.set_bonuses()

        results = self.app.solve(swap_count)
        self.update_results(results)

    def initialize_tiles(self) -> None:
        for tile_index in range(25):
            coord_index = aux_to_indices(tile_index)
            self.tiles[coord_index] = Tile(self, tile_index)

    def initialize_labels(self) -> None:
        self.timer = Label(self, 10)

        for label_index in range(10):
            label = Label(self, label_index)
            self.labels.append(label)

    def load_game_board(self) -> None:
        values = self.tiles.values()
        game_board_string = "".join(tile.letter for tile in values)

        self.app.game_board.load(game_board_string)

    def set_bonuses(self) -> None:
        self.set_mult_word()
        self.set_mult_letter()
        self.set_gems()

    def set_mult_word(self) -> None:
        if self.menu.word_coord is not None:
            self.app.game_board.set_mult_word(self.menu.word_coord)

    def set_mult_letter(self) -> None:
        if self.menu.letter_coord is not None:
            self.app.game_board.set_mult_letter(
                self.menu.letter_coord, self.menu.letter_mult
            )

    def set_gems(self) -> None:
        if self.menu.letter_gems is not None:
            self.app.game_board.set_gems(self.menu.letter_gems)

    def update_results(self, results) -> None:
        sorted_words = results.sorted_words
        self.set_timer(results.timer.elapsed_millis)
        self.set_results(sorted_words[:10])

    def set_timer(self, elapsed_millis: int) -> None:
        self.timer.set_text(f"elapsed time: {elapsed_millis} ms")

    def reset_labels(self) -> None:
        for label in self.labels:
            label.reset()

    def update_labels(self, word_list: list[ResultWord]) -> None:
        for label, result in zip(self.labels, word_list):
            text = result.label
            path = result.path
            label.set_hover(text, path)

    def set_results(self, word_list: list[ResultWord]) -> None:
        self.reset_labels()
        self.update_labels(word_list)
