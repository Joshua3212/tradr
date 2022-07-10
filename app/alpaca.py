from alpaca_trade_api import REST, TimeFrame, TimeFrameUnit
from alpaca_trade_api.common import URL
from alpaca_trade_api.entity import Trade

from app.core.settings import Settings

_settings = Settings()

_api = REST(
    key_id=_settings.ALPACA_CONFIG["api_key_id"],
    secret_key=_settings.ALPACA_CONFIG["secret_key"],
    base_url=URL(_settings.ALPACA_CONFIG["endpoint"])
)


def get_clock():
    return _api.get_clock()


def get_bars_iter_for_stock(symbol: str, timeframe: TimeFrame = TimeFrame(1, TimeFrameUnit.Hour)) -> [Trade]:
    return _api.get_bars_iter(
        symbol, timeframe, limit=_settings.BARS_LIMIT
    )


def submit_order(stock_id: str, quantity: int, intention: str):
    """

    Note: an intention is either a buy or a sell

    :param stock_id:
    :type stock_id:
    :param quantity:
    :type quantity:
    :param intention:
    :type intention:
    :return:
    :rtype:
    """
    return _api.submit_order(
        stock_id, quantity, intention, "market", "day"
    )


def get_positions(symbol: str = None):
    if symbol:
        return _api.get_position(symbol)
    return _api.list_positions()
