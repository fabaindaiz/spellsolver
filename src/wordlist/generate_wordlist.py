import os
from utils import valid_word


def generate_wordlist(source_path: str, dest_path: str) -> None:
    """Generate a wordlist files from multiples filesin a source folder"""
    files = [os.path.join(source_path, file) for file in os.listdir(source_path)]

    words = set()
    for file in files:
        with open(file) as f:
            for word in f.readlines():
                word = word[:-1]
                if valid_word(word):
                    words.add(word.lower())

    words = sorted(words)
    with open(dest_path, 'w') as f:
        for word in words:
            f.write("%s\n" % word)
    print("wordlist successfully generated")


if __name__=="__main__":
    generate_wordlist("sources", "wordlist_english.txt")
