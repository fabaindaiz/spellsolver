from datetime import datetime


chars = "abcdefghijklmnopqrstuvwxyz"

def valid_word(word: str) -> bool:
    """Verify if a word is a valid word"""
    for letter in word:
        if letter not in chars:
            return False
    return True


points = {'a': 1, 'b': 4, 'c': 5, 'd': 3, 'e': 1, 'f': 5, 'g': 3, 'h': 4, 'i': 1, 'j': 7, 'k': 6, 'l': 3, 'm': 4,
    'n': 2, 'o': 1, 'p': 4, 'q': 8, 'r': 2, 's': 2, 't': 2, 'u': 4, 'v': 5, 'w': 5, 'x': 7, 'y': 4, 'z': 8, '': 0}

def letter_points(letter: str) -> int:
    "Gets points value of a letter"
    return points[letter]


class Timer:
    """Represents a timer taht can measure elapsed times"""
    def __init__(self) -> None:
        self.reset_timer()
    
    def reset_timer(self) -> None:
        """Reset starting time to now"""
        self.start_time = datetime.now()
    
    def elapsed_seconds(self) -> float:
        """Get elapsed time in seconds"""
        end_time = datetime.now()
        elapsed_time = (end_time - self.start_time).total_seconds()
        return round(elapsed_time, 2)
    
    def elapsed_millis(self) -> float:
        """Get elapsed time in milliseconds"""
        end_time = datetime.now()
        elapsed_time = (end_time - self.start_time).total_seconds() * 1000
        return round(elapsed_time, 0)
