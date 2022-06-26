import json


class Settings:
    """
    This settings config can be used to retrieve settings from the config.json file.
    """

    def __init__(self):
        """
        Initialize the settings class with the config.json file.
        """
        with open('config.json') as config_file:
            self.config = json.load(config_file)

        # initialize variables
        self.ADAPTER_CONFIG = self.config['adapter_config']

    ADAPTER_CONFIG: str
