VERSION = "v1.9"
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
# SWAP = 0  (no swap) - Memory:  150 MB - Load:   3 sec - Query:    20 ms (mean)
# SWAP = 1 (one swap) - Memory:  990 MB - Load:  30 sec - Query:  1000 ms (mean)
# SWAP = 2 (two swap) - Memory: 3520 MB - Load: 100 sec - Query: 12000 ms (mean)
SWAP = 1
# notice: it is recommended not to activate double swap (SWAP = 2)