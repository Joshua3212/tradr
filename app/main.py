# Initialize Adapter
import time

from alpaca_trade_api import REST
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

_db = MongoClient(_settings.MONGO_URI)
_logger = Logger(_db)

"""
Main loop that runs until stopped

"""

_logger.log("""
___________                  .___       
\__    ___/___________     __| _/______ 
  |    |  \_  __ \__  \   / __ |\_  __ \
  |    |   |  | \// __ \_/ /_/ | |  | \/
  |____|   |__|  (____  /\____ | |__|   
                      \/      \/        
""")
_logger.log("Tradr started")

while True:
    # run

    time.sleep(
        _settings.TIMEOUT
    )
