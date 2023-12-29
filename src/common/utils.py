from datetime import datetime


def get_duration(start:float, end:float) -> float:
    return end - start


def get_timestamp() -> datetime:
    return datetime.now()
