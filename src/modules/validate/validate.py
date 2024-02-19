from src import TRIE
from src.modules.trie import Trie, TrieQuery
from .wordlist import WordList

trie: Trie
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

    def init(self, swap: int) -> None:
        self.trie.insert(self.wordlist, swap)

    def get_trie(self) -> TrieQuery:
        return self.trie.query()
    
    def base_node(self) -> TrieQuery:
        return self.get_trie().get_root()
