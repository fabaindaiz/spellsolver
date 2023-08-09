import unittest
from src.modules.validate import WordValidate
from src.modules.trie import TrieNode


class Validate(unittest.TestCase):
    """"""

    def setUp(self) -> None:
        self.validate: WordValidate = WordValidate()
        self.validate.load_wordlist()

    def test_(self) -> None:
        """"""
        node = self.validate.trie.get_node("hello")
        self.assertEqual(type(node), TrieNode)
