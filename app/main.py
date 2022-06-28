# Initialize Adapter
import time

from pymongo import MongoClient

from app.alpaca import get_trades_iter_for_stock
from app.core.settings import Settings
from app.sanity import make_decision
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


async def trade_callback(b):
    print(b)


def main():
    while True:
        buy = []
        sell = []

        for stock in _settings.STOCKS:
            stock = stock.upper()
            trades_iter = get_trades_iter_for_stock(stock)

            prices = [i.o for i in trades_iter]
            res = make_decision(prices)

            if res == "buy":
                buy.append(stock)
            elif res == "sell":
                sell.append(stock)

            print(stock)
            print(prices)
            print(res)
            print("----")

        time.sleep(_settings.TIMEOUT)


if __name__ == "__main__":
    main()
