import unittest
import graphicui


class GraphicUI(unittest.TestCase):
    """"""

    def setUp(self) -> None:
        self.graphicui: graphicui.GraphicUI = graphicui.GraphicUI()

    def test_graphicui(self) -> None:
        self.graphicui.root.destroy()
