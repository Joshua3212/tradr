import datetime

from app.core.settings import Settings

_settings = Settings()


def get_current_date():
    current_date = datetime.datetime.now(datetime.timezone.utc)
    timedelta = datetime.timedelta(minutes=_settings.CURRENT_DATE_OFFSET)
    return (current_date - timedelta).isoformat()


def get_past_date(minutes: int):
    current_date = datetime.datetime.now(datetime.timezone.utc)
    timedelta = datetime.timedelta(minutes=(minutes + _settings.CURRENT_DATE_OFFSET))
    return (current_date - timedelta).isoformat()
