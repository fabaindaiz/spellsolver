

chars = "abcdefghijklmnopqrstuvwxyz"

def valid_word(word: str) -> bool:
    """Verify if a word is a valid word"""
    word = word[:-1].lower()
    for letter in word:
        if letter not in chars:
            return False
    return True
