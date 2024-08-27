from datetime import UTC, datetime


# datetime <-> milis-timestamp
def convert_milis_timestamp_to_datetime(timestamp: int) -> datetime:
    return datetime.fromtimestamp(timestamp / 1000.0, tz=UTC)


def convert_datetime_to_milis_timestamp(dt: datetime) -> int:
    return int(dt.timestamp() * 1000)
