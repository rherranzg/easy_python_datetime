from datetime import UTC, datetime


def convert_datetime_to_seconds_timestamp(dt: datetime) -> int:
    return int(dt.timestamp())


def convert_seconds_timestamp_to_datetime(timestamp: int) -> datetime:
    return datetime.fromtimestamp(timestamp, tz=UTC)
