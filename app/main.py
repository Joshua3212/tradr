# Initialize Adapter
import time

from app.adapters.alpaca import Alpaca
from app.core.settings import Settings

_settings = Settings()
_adapter = Alpaca(alpaca_config=_settings.ADAPTER_CONFIG)

"""
Main loop that runs until stopped

"""

while True:
    # run

    time.sleep(
        _settings.TIMEOUT
    )
