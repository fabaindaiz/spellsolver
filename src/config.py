VERSION = "v1.13"
DEBUG = False

# Wordlist settings
SOURCES = "assets/wordlist-english/sources"
WORDLIST = "assets/wordlist-english/wordlist.txt"

# FastAPI settings
HOST = "127.0.0.1"
PORT = 8080

# Spellsolver settings
TRIE = "MARISA"
SWAP = 2

# Make sure you have enough ram memory (and patience) for the selected trie and swap mode

# TRIE = "MARISA"       RECOMMENDED
# SWAP = 0  (no swap) - Memory:   35 MB - Load:   1 sec - Query:   100 ms (mean)
# SWAP = 1 (one swap) - Memory:  150 MB - Load:   5 sec - Query:  3000 ms (mean)
# SWAP = 2 (two swap) - Memory:  650 MB - Load:  25 sec - Query: 40000 ms (mean)

# TRIE = "PREFIX"       NOT RECOMMENDED
# SWAP = 0  (no swap) - Memory:  110 MB - Load:   2 sec - Query:    50 ms (mean)
# SWAP = 1 (one swap) - Memory:  760 MB - Load:  15 sec - Query:  1500 ms (mean)
# SWAP = 2 (two swap) - Memory: 3200 MB - Load:  70 sec - Query: 30000 ms (mean)

# TRIE = "PATRICIA"     NOT RECOMMENDED
# SWAP = 0  (no swap) - Memory:  110 MB - Load:   3 sec - Query:    60 ms (mean)
# SWAP = 1 (one swap) - Memory:  760 MB - Load:  30 sec - Query:  2000 ms (mean)
# SWAP = 2 (two swap) - Memory: 3200 MB - Load: 130 sec - Query: 35000 ms (mean)
