VERSION = "v1.11"
DEBUG = False

# Wordlist settings
SOURCES = "assets/wordlist-english/sources"
WORDLIST = "assets/wordlist-english/wordlist.txt"

# FastAPI settings
HOST = "127.0.0.1"
PORT = 8080

# Trie settings
# TRIE = "MARISA"
TRIE = "MARISA"

# Swap mode settings
# Make sure you have enough ram memory (and patience) for the selected swap modes
# SWAP = 0  (no swap) - Memory:  36 MB - Load:  1 sec - Query:    50 ms (mean)
# SWAP = 1 (one swap) - Memory: 150 MB - Load:  5 sec - Query:  2000 ms (mean)
# SWAP = 2 (two swap) - Memory: 650 MB - Load: 25 sec - Query: 30000 ms (mean)
SWAP = 1
