
from utils import valid_word
import os


folder_path = "sources"
files = [os.path.join(folder_path, file) for file in os.listdir(folder_path)]

words = set()
for file in files:
    with open(file) as f:
        for word in f.readlines():
            if valid_word(word):
                words.add(word[:-1].lower())

words = sorted(words)
with open("wordlist_english.txt", 'w') as f:
    for word in words:
        f.write("%s\n" % word)
