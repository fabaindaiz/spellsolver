from tkinter import Tk, PhotoImage

from src import SWAP, VERSION
from src.entities import Coordinates
from src.interfaces import BaseUI
from src.interfaces.graphicalui import Button, Label, Tile, MenuHandler
from src.modules.gameboard import ResultWord
from src.utils import aux_to_indices, resource_path


class GraphicalUI(BaseUI):
    WINDOW_TITLE: str = f"Spellsolver {VERSION}"
    WINDOW_WIDTH: int = 600
    WINDOW_HEIGHT: int = 300

    def __init__(self) -> None:
        super().__init__()

        self.window: Tk = Tk()

        self.double_swap: bool = SWAP >= 2
        self.buttons: list[Button] = []
        self.label: Label = Label(self, 10)
        self.labels: list[Label] = []
        self.tiles: dict[Coordinates, Tile] = {}
        self.menu: MenuHandler = MenuHandler(self)

        self.initialize_components()

        first_tile_coordinates = Coordinates(0, 0)
        self.tiles[first_tile_coordinates].entry.focus()

        self.app_initialize()

    @property
    def _window_position(self) -> str:
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x_position = (screen_width - self.WINDOW_WIDTH) // 2
        y_position = (screen_height - self.WINDOW_HEIGHT) // 2

        return f"{x_position}+{y_position}"

    @property
    def _window_size(self) -> str:
        return f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}"

    def _icon_initialize(self) -> None:
        icon_path = resource_path("assets/spellsolver.png")
        photo_image = PhotoImage(file=icon_path)

        self.window.iconphoto(True, photo_image)

    def _window_configure(self) -> None:
        self.window.title(self.WINDOW_TITLE)
        self.window.resizable(width=False, height=False)
        self._icon_initialize()

    def _window_place(self):
        window_size = self._window_size
        window_position = self._window_position

        self.window.geometry(f"{window_size}+{window_position}")

    def app_initialize(self) -> None:
        self._window_configure()
        self._window_place()
        self.init_spellsolver()

    def run(self) -> None:
        self.window.mainloop()

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
            parent=self,
            double_swap=self.double_swap,
            swap_count=swap_count,
            command=lambda: self.handle_button_click(swap_count),
        )

    def handle_button_click(self, swap_count: int) -> None:
        self.load_game_board()
        self.set_bonuses()

        results = self.solve(swap_count)
        self.update_results(results)

    def initialize_tiles(self) -> None:
        for tile_index in range(25):
            coord_index = aux_to_indices(tile_index)
            self.tiles[coord_index] = Tile(self, tile_index)

    def initialize_labels(self) -> None:
        for label_index in range(10):
            label = Label(self, label_index)
            self.labels.append(label)

    def load_game_board(self) -> None:
        values = self.tiles.values()
        game_board_string = "".join(tile.letter for tile in values)

        self.game_board.load(game_board_string)

    def set_bonuses(self) -> None:
        self.set_mult_word()
        self.set_mult_letter()
        self.set_gems()
        self.set_ices()

    def set_mult_word(self) -> None:
        if self.menu.word_coord is not None:
            self.game_board.set_mult_word(self.menu.word_coord)

    def set_mult_letter(self) -> None:
        if self.menu.letter_coord is not None:
            self.game_board.set_mult_letter(
                self.menu.letter_coord, self.menu.letter_mult
            )

    def set_gems(self) -> None:
        if self.menu.letter_gems is not None:
            self.game_board.set_gems(self.menu.letter_gems)
    
    def set_ices(self) -> None:
        if self.menu.letter_ices is not None:
            self.game_board.set_ices(self.menu.letter_ices)

    def update_results(self, results) -> None:
        sorted_words = results.sorted_words
        self.set_results(sorted_words[:10])

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


if __name__ == "__main__":
    application = GraphicalUI()
    application.run()
