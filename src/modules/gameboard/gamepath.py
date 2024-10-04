from .gametile import GameTile

type GameTileTuple = tuple[GameTile, ...]


class GamePath:

    @staticmethod
    def calculate_points(path: GameTileTuple) -> int:
        long_word_bonus = 10
        min_bonus_length = 6
        word_multiplier = 1

        word_points = sum(node.points for node in path)
        word_bonus = long_word_bonus if len(path) >= min_bonus_length else 0

        for node in path:
            word_multiplier *= node.word_mult

        return word_points * word_multiplier + word_bonus

    @staticmethod
    def calculate_gems(path: GameTileTuple) -> int:
        return sum(node.has_gem for node in path)

    @staticmethod
    def update_path(
        original_path: GameTileTuple, word: str, swapped_indices: tuple[int, ...]
    ) -> GameTileTuple:
        if not swapped_indices:
            return original_path

        updated_path = []

        for index, tile in enumerate(original_path):
            if index in swapped_indices:
                updated_tile = GameTile(word[index], tile.coordinates)
                updated_tile.swapped = True
                updated_path.append(updated_tile)
            else:
                updated_path.append(tile)

        return tuple(updated_path)
