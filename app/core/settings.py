import json


class Settings:
    """
    This settings config can be used to retrieve settings from the local.config.json file.
    """

    def __init__(self):
        """
        Initialize the settings class with the local.config.json file.
        """
        try:
            with open('local.config.json') as config_file:
                self.config = json.load(config_file)
        except Exception:
            with open('config.json') as config_file:
                self.config = json.load(config_file)

        # initialize variables
        self.ALPACA_CONFIG = self.config['alpaca_config']

        self.STOCKS = self.config["stocks"]  # a list of stocks to query / buy
        self.BUYING_POWER = self.config["buying_power"]  # in whatever currency
        self.MONGO_URI = self.config["mongo_uri"]

        self.TRADE_CHANGE_TIMEFRAME = self.config["trade_change_timeframe"]  # in whatever currency

        self.DATE_OFFSET = self.config["date_offset"]
        self.MIN_TREND_SIMILARITY = self.config["min_trend_similarity"]
        self.TRENDS = self.config["trends"]
        self.BARS_LIMIT = self.config["bars_limit"]

        try:
            self.TIMEOUT = self.config['timeout']
        except:
            self.TIMEOUT = 5  # default timeout of 5 seconds

    ALPACA_CONFIG: dict
    TIMEOUT: int
    STOCKS: list
    BUYING_POWER: int

    MONGO_URI: str

    TRADE_CHANGE_TIMEFRAME: int  # in minutes

    DATE_OFFSET: int  # in minutes

    MIN_TREND_SIMILARITY: int  # in the selected currency
    TRENDS: dict
    BARS_LIMIT: int
