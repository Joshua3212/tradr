from alpaca_trade_api import REST
from alpaca_trade_api.common import URL


class Alpaca:
    def __init__(self, alpaca_config: dict):
        """
        Example Alpaca configuration:

        >>  {
        >>      "endpoint": https://paper-api.alpaca.markets
        >>      "api_key_id": "api_key_id",
        >>      "secret_key": "secret_key",
        >>  }


        :param alpaca_config:
        :type alpaca_config:
        """

        self.alpaca_config = alpaca_config

        self.api = REST(
            key_id=alpaca_config["api_key_id"],
            secret_key=alpaca_config["secret_key"],
            base_url=URL(alpaca_config["endpoint"])
        )

    api: REST
