import datetime


def get_current_date(current_date_offset: int):
    current_date = datetime.datetime.now(datetime.timezone.utc)
    timedelta = datetime.timedelta(minutes=current_date_offset)
    return (current_date - timedelta).isoformat()


def get_past_date(minutes: int, current_date_offset: int):
    current_date = datetime.datetime.now(datetime.timezone.utc)
    timedelta = datetime.timedelta(minutes=minutes + current_date_offset)
    return (current_date - timedelta).isoformat()
