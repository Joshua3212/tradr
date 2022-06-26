import datetime


def get_current_date():
    current_date = datetime.datetime.today()
    timedelta = datetime.timedelta(days=1)
    return (current_date - timedelta).strftime('%Y-%m-%d')


def get_past_date(seconds: int):
    current_date = datetime.datetime.today()
    timedelta = datetime.timedelta(seconds=seconds)
    return (current_date - timedelta).strftime('%Y-%m-%d')
