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
        self.ALPACA_CONFIG = self.config['alpaca_config']

        self.STOCKS = self.config["stocks"]  # a list of stocks to query / buy
        self.BUYING_POWER = self.config["buying_power"]  # in whatever currency
        self.MONGO_URI = self.config["mongo_uri"]

        self.LONG_TERM_GAIN_TIMEFRAME = self.config["long_term_gain_timeframe"]  # in whatever currency
        self.SHORT_TERM_GAIN_TIMEFRAME = self.config["short_term_gain_timeframe"]

        self.TIMEFRAME_GAP = self.config["timeframe_gap"]

        self.CURRENT_DATE_OFFSET = self.config["current_date_offset"]
        self.MIN_STOCK_DROP = self.config["min_stock_drop"]

        try:
            self.TIMEOUT = self.config['timeout']
        except:
            self.TIMEOUT = 5  # default timeout of 5 seconds

    ALPACA_CONFIG: dict
    TIMEOUT: int
    STOCKS: list
    BUYING_POWER: int

    MONGO_URI: str

    LONG_TERM_GAIN_TIMEFRAME: int  # in minutes
    SHORT_TERM_GAIN_TIMEFRAME: int  # in minutes

    TIMEFRAME_GAP: int  # the gap between two bar entries in minutes
    CURRENT_DATE_OFFSET: int  # in minutes

    MIN_STOCK_DROP: int  # in the selected currency