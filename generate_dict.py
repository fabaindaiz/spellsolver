
import os

folder_path = "sources"
files = [os.path.join(folder_path, file) for file in os.listdir(folder_path)]

words = []

for file in files:
    with open(file) as f:
        for word in f.readlines():
            if "'" not in word:
                words += [word[:-1].lower()]

words.sort()

with open("wordlist_english.txt", 'w') as f:
    for word in words:
        f.write("%s\n" % word)