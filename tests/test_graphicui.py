import unittest
from unittest.mock import MagicMock

from graphicalui import GraphicalUI


class TestGraphicalUI(unittest.TestCase):
    def setUp(self):
        self.ui = GraphicalUI()

    def test_window_title(self):
        self.assertEqual(self.ui.WINDOW_TITLE, "Spellsolver")

    def test_window_dimensions(self):
        self.assertEqual(self.ui.WINDOW_WIDTH, 600)
        self.assertEqual(self.ui.WINDOW_HEIGHT, 300)

    def test_padding_values(self):
        self.assertEqual(self.ui.HORIZONTAL_PADDING, 25)
        self.assertEqual(self.ui.VERTICAL_PADDING, 25)

    def test_get_alignment_string(self):
        self.ui.window.winfo_screenwidth = MagicMock(return_value=1920)
        self.ui.window.winfo_screenheight = MagicMock(return_value=1080)

        alignment_string = self.ui.get_alignment_string()
        self.assertEqual(alignment_string, "600x300+660+390")

        self.ui.window.winfo_screenwidth.assert_called_once()
        self.ui.window.winfo_screenheight.assert_called_once()

    def test_calculate_screen_offset(self):
        self.ui.window.winfo_screenwidth = MagicMock(return_value=1920)
        self.ui.window.winfo_screenheight = MagicMock(return_value=1080)

        horizontal_offset, vertical_offset = self.ui.calculate_screen_offset()
        self.assertEqual(horizontal_offset, 660)
        self.assertEqual(vertical_offset, 390)

        self.ui.window.winfo_screenwidth.assert_called_once()
        self.ui.window.winfo_screenheight.assert_called_once()

    def test_format_alignment_string(self):
        alignment_string = self.ui.format_alignment_string(660, 390)
        self.assertEqual(alignment_string, "600x300+660+390")

    def tearDown(self):
        self.ui.window.destroy()


if __name__ == "__main__":
    unittest.main()
