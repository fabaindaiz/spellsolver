import unittest

from utils import aux_to_indices, is_valid_word, get_letter_point_value


class TestFunctions(unittest.TestCase):
    def test_get_coordinate(self):
        self.assertEqual(aux_to_indices(0), (0, 0))
        self.assertEqual(aux_to_indices(5), (0, 1))
        self.assertEqual(aux_to_indices(24), (4, 4))
        self.assertEqual(aux_to_indices(26), (1, 0))

    def test_valid_word(self):
        self.assertTrue(is_valid_word("hello"))
        self.assertTrue(is_valid_word("world"))
        self.assertFalse(is_valid_word("123"))
        self.assertFalse(is_valid_word("abc$"))

    def test_letter_points(self):
        self.assertEqual(get_letter_point_value("a"), 1)
        self.assertEqual(get_letter_point_value("b"), 4)
        self.assertEqual(get_letter_point_value("z"), 8)
        self.assertEqual(get_letter_point_value("q"), 8)
        self.assertEqual(get_letter_point_value("x"), 7)
        self.assertEqual(get_letter_point_value("f"), 5)
        self.assertEqual(get_letter_point_value("1"), 0)


if __name__ == "__main__":
    unittest.main()
