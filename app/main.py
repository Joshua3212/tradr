# Initialize Adapter
import time

from alpaca_trade_api import REST, Stream
from alpaca_trade_api.common import URL
from pymongo import MongoClient

from app.core.settings import Settings
from app.utils.logger import Logger

_settings = Settings()

# alpaca connection
_api = REST(
    key_id=_settings.ALPACA_CONFIG["api_key_id"],
    secret_key=_settings.ALPACA_CONFIG["secret_key"],
    base_url=URL(_settings.ALPACA_CONFIG["endpoint"])
)

_stream = Stream(
    key_id=_settings.ALPACA_CONFIG["api_key_id"],
    secret_key=_settings.ALPACA_CONFIG["secret_key"],
    base_url=URL(_settings.ALPACA_CONFIG["endpoint"]),
    data_feed="iex",
    websocket_params={
        "ping_interval": _settings.TIMEFRAME_GAP
    }
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


async def trade_callback(b):
    print(b)


def main():
    for stock in _settings.STOCKS:
        stock = stock.upper()
        _stream.subscribe_trades(
            trade_callback, stock
        )

    time.sleep(3)
    _stream.run()


if __name__ == "__main__":
    main()
