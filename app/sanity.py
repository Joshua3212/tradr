# literally checking whether a buy/sell action is sensible
from app.core.settings import Settings

_settings = Settings()


def make_decision(prices: list):
    result = None

    latest_price = prices[len(prices) - 1]

    max_price = max(prices)
    min_price = min(prices)
    min_index = prices.index(min_price)
    max_index = prices.index(max_price)

    prices_before_min_price = prices[0:min_index]
    avg_prices_before_min_price = 0
    for price in prices_before_min_price:
        avg_prices_before_min_price += price
    if min_index != 0:
        avg_prices_before_min_price = avg_prices_before_min_price / min_index

    prices_before_max_price = prices[0:max_index]
    avg_prices_before_max_price = 0
    for price in prices_before_max_price:
        avg_prices_before_max_price += price
    if max_index != 0:
        avg_prices_before_max_price = avg_prices_before_max_price / max_index

    if latest_price > min_price and latest_price + _settings.MIN_STOCK_DROP < avg_prices_before_min_price:
        """
            buy it I guess
        """
        result = "buy"

    if latest_price < max_price and latest_price - _settings.MIN_STOCK_DROP < avg_prices_before_max_price:
        """
            sell it I guess
        """
        result = "sell"

    if not result:
        result = "wait"

    return result
