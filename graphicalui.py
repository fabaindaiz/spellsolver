from tkinter import Tk, PhotoImage

from src import VERSION
from src.interfaces import BaseUI
from src.interfaces.graphicalui import Board
from src.utils import resource_path


class GraphicalUI(BaseUI):
    WINDOW_TITLE: str = f"Spellsolver {VERSION}"
    WINDOW_WIDTH: int = 600
    WINDOW_HEIGHT: int = 300

    def __init__(self) -> None:
        super().__init__()

        self.window: Tk = Tk()
        self.interface_board: Board = Board(self)

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
        icon_path = resource_path("assets/icon.png")
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


if __name__ == "__main__":
    application = GraphicalUI()
    application.run()
