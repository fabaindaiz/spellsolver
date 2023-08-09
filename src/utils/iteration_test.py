import unittest
from iteration import pairwise


class TestPairwiseFunction(unittest.TestCase):
    def test_empty_input(self):
        result = list(pairwise([]))
        self.assertEqual(result, [])

    def test_single_element_input(self):
        result = list(pairwise([1]))
        self.assertEqual(result, [])

    def test_normal_input(self):
        result = list(pairwise([1, 2, 3, 4, 5]))
        self.assertEqual(result, [(1, 2), (2, 3), (3, 4), (4, 5)])

    def test_string_input(self):
        result = list(pairwise("ABCDEFG"))
        self.assertEqual(
            result,
            [("A", "B"), ("B", "C"), ("C", "D"), ("D", "E"), ("E", "F"), ("F", "G")],
        )


if __name__ == "__main__":
    unittest.main()
