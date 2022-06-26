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

        self.stocks = self.config["stocks"]  # a list of stocks to query / buy
        self.buying_power = self.config["buying_power"]  # in whatever currency

        try:
            self.TIMEOUT = self.config['timeout']
        except:
            self.TIMEOUT = 5  # default timeout of 5 seconds

    ADAPTER_CONFIG: dict
    TIMEOUT: int
    STOCKS: list
    BUYING_POWER: int
