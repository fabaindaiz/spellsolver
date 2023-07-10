import yaml
from src.settings.interfaces import Settings


class SettingsLoader:
    """"""
    def __init__(self) -> None:
        with open("config.json") as file:
            Settings.update_forward_refs()
            config_dict = yaml.load(file)
            self.config: Settings = Settings(**config_dict)

    def load(self) -> Settings:
        """Load config file"""
        #with open("config.json") as file:
        #    config_json = json.load(file)
        #    self.config = Config(**config_json)
        #self.config.parse_file("config.json")
        return Settings
