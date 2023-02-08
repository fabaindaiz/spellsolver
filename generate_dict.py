
import os

chars = "abcdefghijklmnopqrstuvwxyz"
def valid_word(word):
    word = word[:-1].lower()
    for letter in word:
        if letter not in chars:
            return []
    return [word]

folder_path = "sources"
files = [os.path.join(folder_path, file) for file in os.listdir(folder_path)]

words = []

for file in files:
    with open(file) as f:
        for word in f.readlines():
            words += valid_word(word)

words.sort()

with open("wordlist_english.txt", 'w') as f:
    for word in words:
        f.write("%s\n" % word)
