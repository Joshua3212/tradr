# Initialize Adapter
import time

from pymongo import MongoClient

from app.alpaca import get_trades_iter_for_stock
from app.core.settings import Settings
from app.predict import get_difference
from app.utils.logger import Logger

_settings = Settings()

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


def main():
    while True:
        buy = []
        sell = []

        for stock in _settings.STOCKS:
            stock = stock.upper()
            trades_iter = get_trades_iter_for_stock(stock)

            prices = [i.o for i in trades_iter]

            res = 0
            for i in _settings.TRENDS["buy"]:
                res = get_difference(prices, i)

            for i in _settings.TRENDS["sell"]:
                res = get_difference(prices, i)

            if res is not None:
                if res <= _settings.MIN_TREND_SIMILARITY:
                    buy.append(stock)

                elif res >= _settings.MIN_TREND_SIMILARITY:
                    sell.append(stock)

            print(stock)
            print(prices)
            print(res)
            print("----")

        time.sleep(_settings.TIMEOUT)


if __name__ == "__main__":
    main()
