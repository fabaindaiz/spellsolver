
chars = "abcdefghijklmnopqrstuvwxyz"

def valid_word(word):
    word = word[:-1].lower()
    for letter in word:
        if letter not in chars:
            return False
    return True


def get_word_points(path):
        word_points = 0
        word_bonus = 0
        word_mult = 1

        for node in path:
            word_points += node.get_points()
            word_mult *= node.word_mult
        
        if len(path) >= 6:
            word_bonus += 10

        return word_points * word_mult + word_bonus