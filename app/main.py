# Initialize Adapter
import time

from alpaca_trade_api import REST, TimeFrame, TimeFrameUnit
from alpaca_trade_api.common import URL
from pymongo import MongoClient

from app.core.settings import Settings
from app.utils.dates import get_current_date, get_past_date
from app.utils.logger import Logger

_settings = Settings()

# alpaca connection
_api = REST(
    key_id=_settings.ALPACA_CONFIG["api_key_id"],
    secret_key=_settings.ALPACA_CONFIG["secret_key"],
    base_url=URL(_settings.ALPACA_CONFIG["endpoint"])
)

_db = MongoClient(_settings.MONGO_URI)
_logger = Logger(_db)

"""
Main loop that runs until stopped

"""

_logger.log("""
___________                  .___       
\__    ___/___________     __| _/______ 
  |    |  \_  __ \__  \   / __ |\_  __ \\
  |    |   |  | \// __ \_/ /_/ | |  | \/
  |____|   |__|  (____  /\____ | |__|   
                      \/      \/        
""")
_logger.log("Tradr started successfully ✅")
_logger.log(f"Timeout is set to {_settings.TIMEOUT} seconds")
_logger.log(f"Buying power is set to {_settings.BUYING_POWER}")
_logger.log(f"Stocks is set to {','.join(_settings.STOCKS)}")

while True:
    for stock in _settings.STOCKS:
        # get data for long_term_gain_timeframe

        bar_iter = _api.get_bars(stock, TimeFrame(_settings.TIMEFRAME_GAP, TimeFrameUnit.Minute),
                                 get_past_date(_settings.LONG_TERM_GAIN_TIMEFRAME),
                                 get_current_date(),
                                 adjustment="raw")
        for bar in bar_iter:
            print(bar)
    time.sleep(
        _settings.TIMEOUT
    )
