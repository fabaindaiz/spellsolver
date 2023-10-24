from src.modules.trie.base import Trie, TrieQuery
from src.modules.validate.wordlist import WordList
from src.config import TRIE

if TRIE == "MARISA":
    from src.modules.trie.marisa import MarisaTrie
    trie = MarisaTrie()
elif TRIE == "PREFIX":
    from src.modules.trie.prefix import PrefixTrie
    trie = PrefixTrie()
elif TRIE == "PATRICIA":
    from src.modules.trie.patricia import PatriciaTrie
    trie = PatriciaTrie()
else:
    raise NotImplementedError()


class WordValidate:
    """Validate a word using a trie"""

    def __init__(self) -> None:
        self.wordlist: WordList = WordList()
        self.trie: Trie = trie
    
    def init_trie(self) -> None:
        self.trie.insert_trie(self.wordlist)

    def get_trie(self) -> TrieQuery:
        return self.trie.query_trie()
