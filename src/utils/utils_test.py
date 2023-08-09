import unittest
from utils import get_coordinate, valid_word, letter_points


class TestFunctions(unittest.TestCase):
    def test_get_coordinate(self):
        self.assertEqual(get_coordinate(0), (0, 0))
        self.assertEqual(get_coordinate(5), (0, 1))
        self.assertEqual(get_coordinate(24), (4, 4))
        self.assertEqual(get_coordinate(26), (1, 0))

    def test_valid_word(self):
        self.assertTrue(valid_word("hello"))
        self.assertTrue(valid_word("world"))
        self.assertFalse(valid_word("123"))
        self.assertFalse(valid_word("abc$"))

    def test_letter_points(self):
        self.assertEqual(letter_points("a"), 1)
        self.assertEqual(letter_points("b"), 4)
        self.assertEqual(letter_points("z"), 8)
        self.assertEqual(letter_points("q"), 8)
        self.assertEqual(letter_points("x"), 7)
        self.assertEqual(letter_points("f"), 5)
        self.assertEqual(letter_points("1"), 0)


if __name__ == "__main__":
    unittest.main()
