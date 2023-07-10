import unittest
from src.settings.settings import SettingsLoader


class Config(unittest.TestCase):
    """"""
    def setUp(self) -> None:
        pass
    
    def test_(self) -> None:
        loader = SettingsLoader()
        version = loader.load().version
        self.assertIsNone(version)
