from src.entities import Coordinates
from src.utils import aux_to_indices, is_valid_word
from .gametile import GameTile


class GameBoard:
    def __init__(self) -> None:
        self.tiles: dict[Coordinates, GameTile] = {}
    
    def _init_tiles(self, game_board_input: str) -> None:
        for aux, letter in enumerate(game_board_input):
            coordinates = aux_to_indices(aux)
            self.tiles[coordinates] = GameTile(letter, coordinates)
    
    def _init_neighbours(self) -> None:
        for tile in self.tiles.values():
            tile.init_neighbors(self.tiles)
    
    def init_gameboard(self, game_board_input: str) -> None:
        game_board_input = game_board_input.lower()
        if len(game_board_input) != 25 or not is_valid_word(game_board_input):
            raise ValueError("Invalid game board input")
    
        self._init_tiles(game_board_input)
        self._init_neighbours()
    
    @property
    def base_tile(self) -> GameTile:
        base_tile = GameTile("0", Coordinates(-1, -1))
        base_tile.neighbours = list(self.tiles.values())
        return base_tile

    def set_blocked(self, coordinates: list[Coordinates]) -> None:
        for coordinate in coordinates:
            self.tiles[coordinate].blocked = True
    
    def set_gems(self, tiles: dict[Coordinates, int]) -> None:
        for coordinate, value in tiles.items():
            self.tiles[coordinate].gems = value
    
    def set_tile_mult(self, tiles: dict[Coordinates, int]) -> None:
        for coordinate, value in tiles.items():
            self.tiles[coordinate].tile_mult = value
    
    def set_word_mult(self, tiles: dict[Coordinates, int]) -> None:
        for coordinate, value in tiles.items():
            self.tiles[coordinate].word_mult = value


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
    game_board.init_gameboard(game_board_string)

    game_board_printer = GameBoardPrinter(game_board)
    print(game_board_printer)
