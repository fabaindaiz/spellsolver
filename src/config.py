VERSION = "v1.14"
CONSOLE = True
DEBUG = False

# Wordlist settings
SOURCES = "assets/wordlist-english/sources"
WORDLIST = "assets/wordlist-english/wordlist.txt"

# Executable settings
SCRIPT = "graphicalui.py"

# FastAPI settings
HOST = "127.0.0.1"
PORT = 8080

# Sortings settings
WORD_MULT = 1
GEMS_MULT = 3

# Spellsolver settings
TRIE = "MARISA"
SWAP = 1

# Make sure you have enough ram memory (and patience) for the selected trie and swap mode

# TRIE = "MARISA"       RECOMMENDED
# SWAP = 0  (no swap) - Memory:   35 MB - Load:   1 sec - Query:   20 ms (mean)
# SWAP = 1 (one swap) - Memory:  150 MB - Load:   4 sec - Query:  600 ms (mean)
# SWAP = 2 (two swap) - Memory:  650 MB - Load:  18 sec - Query: 8000 ms (mean)

# TRIE = "PREFIX"       NOT RECOMMENDED
# SWAP = 0  (no swap) - Memory:  110 MB - Load:   2 sec - Query:   10 ms (mean)
# SWAP = 1 (one swap) - Memory:  760 MB - Load:  15 sec - Query:  300 ms (mean)
# SWAP = 2 (two swap) - Memory: 3200 MB - Load:  65 sec - Query: 6000 ms (mean)

# TRIE = "PATRICIA"     NOT RECOMMENDED
# SWAP = 0  (no swap) - Memory:  110 MB - Load:   3 sec - Query:   10 ms (mean)
# SWAP = 1 (one swap) - Memory:  760 MB - Load:  30 sec - Query:  400 ms (mean)
# SWAP = 2 (two swap) - Memory: 3200 MB - Load: 130 sec - Query: 8000 ms (mean)
