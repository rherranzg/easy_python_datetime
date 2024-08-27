from datetime import datetime, timezone

from src.datetime__seconds_timestamp import (
    convert_datetime_to_seconds_timestamp,
    convert_seconds_timestamp_to_datetime,
)


def test_convert_datetime_to_seconds_timestamp():
    # https://www.epochconverter.com/?q=1704067200

    dt = datetime(2024, 1, 1, 0, 0, 0, 0, tzinfo=timezone.utc)
    output = convert_datetime_to_seconds_timestamp(dt)
    assert output == 1704067200


def test_convert_seconds_timestamp_to_datetime():
    # https://www.epochconverter.com/?q=1704067200

    ts = 1704067200
    output = convert_seconds_timestamp_to_datetime(ts)
    assert output == datetime(2024, 1, 1, 0, 0, 0, 0, tzinfo=timezone.utc)
