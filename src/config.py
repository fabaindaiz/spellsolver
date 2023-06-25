VERSION = "v1.7"
DEBUG = False

# FastAPI host settings
# Modify the host and port used by webapi.py
HOST = "127.0.0.1"
PORT = 8080

# Swap mode settings
# Make sure you have enough ram memory (and patience) for the selected swap modes
# word0 - Memory:  156 MB - Load:   3 sec - Query:    20 ms (mean)
# word1 - Memory: 1212 MB - Load:  30 sec - Query:  1000 ms (mean)
# word2 - Memory: 5246 MB - Load: 150 sec - Query: 12000 ms (mean)
SWAP = ["word0", "word1"]
# notice: it is recommended not to activate double swap (word2)