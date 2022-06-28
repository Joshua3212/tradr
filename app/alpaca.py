from alpaca_trade_api import REST, TimeFrame, TimeFrameUnit
from alpaca_trade_api.common import URL
from alpaca_trade_api.entity import Trade

from app.core.settings import Settings
from app.utils.dates import get_past_date, get_current_date

_settings = Settings()

_api = REST(
    key_id=_settings.ALPACA_CONFIG["api_key_id"],
    secret_key=_settings.ALPACA_CONFIG["secret_key"],
    base_url=URL(_settings.ALPACA_CONFIG["endpoint"])
)


def get_price_of_stocks(stocks: list) -> int:
    total_price = 0

    for stock in stocks:
        bars = _api.get_bars(
            stock,
            TimeFrame.Minute,
            get_current_date(),
            get_current_date()
        )

        if len(bars) > 0:
            total_price += bars[0].p


def get_trades_iter_for_stock(stock_id: str) -> [Trade]:
    return _api.get_bars_iter(stock_id, TimeFrame(1, TimeFrameUnit.Hour),
                              get_past_date(_settings.TRADE_CHANGE_TIMEFRAME),
                              get_current_date())


def submit_order(stock_id: str, quantity: int, intension: str):
    """

    Note: an intension is either a buy or a sell

    :param stock_id:
    :type stock_id:
    :param quantity:
    :type quantity:
    :param intension:
    :type intension:
    :return:
    :rtype:
    """
    return _api.submit_order(
        stock_id, quantity, intension, "market", "day"
    )
