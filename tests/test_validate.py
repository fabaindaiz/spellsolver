import unittest

from src.modules.validate import WordValidate


class Validate(unittest.TestCase):
    def setUp(self) -> None:
        self.validate: WordValidate = WordValidate()
        self.validate.init_trie()

    def test_(self) -> None:
        """"""
        trie = self.validate.trie.query()
        self.assertTrue(trie.get_key("epidemic"))
        self.assertFalse(trie.get_key("abcdefg"))
