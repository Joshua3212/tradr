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
