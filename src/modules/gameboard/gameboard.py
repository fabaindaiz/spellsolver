from src.utils import aux_to_indices, is_valid_word
from .gametile import GameTile

Coordinates = tuple[int, int]


class GameBoard:
    def __init__(self) -> None:
        self.tiles: dict[Coordinates, GameTile] = {}

    def _initialize_tiles(self, game_board_input: str) -> None:
        for aux, letter in enumerate(game_board_input):
            cord = aux_to_indices(aux)
            self.tiles[cord] = GameTile(letter, cord)

    def _initialize_neighbors(self) -> None:
        for node in self.tiles.values():
            node.init_neighbors(self.tiles)

    def get_base_tile(self) -> GameTile:
        base_tile = GameTile("0", (-1, -1))
        tile_values = list(self.tiles.values())
        base_tile.neighbors = tile_values

        return base_tile

    def load(self, game_board_input: str) -> None:
        game_board_input = game_board_input.lower()

        if not is_valid_word(game_board_input) or len(game_board_input) != 25:
            raise ValueError("Invalid game board input")

        self._initialize_tiles(game_board_input)
        self._initialize_neighbors()

    def set_gems(self, gem_coordinates: list[Coordinates]) -> None:
        for coordinate in gem_coordinates:
            self.tiles[coordinate].has_gem = True

    def set_mult_letter(
        self, multiplier_coordinates: Coordinates, multiplier: int
    ) -> None:
        self.tiles[multiplier_coordinates].letter_multiplier = multiplier

    def set_mult_word(self, multiplier_coordinates: Coordinates) -> None:
        self.tiles[multiplier_coordinates].word_multiplier = 2


class GameBoardPrinter:
    def __init__(self, board: GameBoard) -> None:
        self.game_board = board

    def __str__(self) -> str:
        rows = []
        tile_values = list(self.game_board.tiles.values())
        row_count = 5

        for index in range(row_count):
            next_index = index + 1
            row = tile_values[index * row_count : next_index * row_count]
            row_str = " ".join(tile.letter for tile in row)
            rows.append(row_str)

        return "\n".join(rows)


if __name__ == "__main__":
    game_board = GameBoard()

    game_board_string = input("Insert a game board: ")
    game_board.load(game_board_string)

    game_board_printer = GameBoardPrinter(game_board)
    print(game_board_printer)
