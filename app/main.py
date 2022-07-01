# Initialize Adapter
import time

from app.alpaca import get_bars_iter_for_stock, get_clock
from app.core.settings import Settings
from app.predict import get_difference
from app.utils.logger import Logger

_settings = Settings()

_logger = Logger()

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

        if get_clock().is_open:  # only queue orders if the market is open / ready
            for stock in _settings.STOCKS:
                stock = stock.upper()
                trades_iter = get_bars_iter_for_stock(stock)

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

            _logger.log(
                f"Evaluation completed successfully", "DEBUG"
            )
            _logger.log(
                f"Results: buy={','.join(buy)} sell={','.join(sell)}", "INFO"
            )

            # send out orders

            _logger.log(
                f"Sending out orders", "DEBUG"
            )



        else:

            _logger.log(
                f"Market is closed", "INFO"
            )
        time.sleep(_settings.TIMEOUT)


if __name__ == "__main__":
    main()
