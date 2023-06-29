VERSION = "v1.8"
DEBUG = False

# Wordlist settings
SOURCES = "assets/wordlist-english/sources"
WORDLIST = "assets/wordlist-english/wordlist.txt"

# Heuristic settings
# Work in progress
HEURISTIC = False

# FastAPI settings
HOST = "127.0.0.1"
PORT = 8080

# Swap mode settings
# Make sure you have enough ram memory (and patience) for the selected swap modes
# swap0  (no swap) - Memory:  140 MB - Load:   3 sec - Query:    20 ms (mean)
# swap1 (one swap) - Memory: 1020 MB - Load:  30 sec - Query:  1000 ms (mean)
# swap2 (two swap) - Memory: 3650 MB - Load: 100 sec - Query: 12000 ms (mean)
SWAP = ("swap0", "swap1")
# notice: it is recommended not to activate double swap (swap2)