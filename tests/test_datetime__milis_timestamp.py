from datetime import UTC, datetime

from src.datetime__milis_timestamp import (
    convert_datetime_to_milis_timestamp,
    convert_milis_timestamp_to_datetime,
)


def test_convert_milis_timestamp_to_datetime():
    # https://www.epochconverter.com/?q=1704067200000

    ts = 1704067200000
    output = convert_milis_timestamp_to_datetime(ts)
    assert output == datetime(2024, 1, 1, 0, 0, 0, 0, tzinfo=UTC)


def test_convert_datetime_to_milis_timestamp():
    # https://www.epochconverter.com/?q=1704067200000

    dt = datetime(2024, 1, 1, 0, 0, 0, 0, tzinfo=UTC)
    output = convert_datetime_to_milis_timestamp(dt)
    assert output == 1704067200000
