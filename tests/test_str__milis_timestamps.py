from datetime import datetime

from src.datetime__str import convert_str_to_datetime
from src.str__milis_timestamp import (
    convert_milis_timestamp_to_str,
    convert_str_to_milis_timestamp,
)


def test_convert_str_to_milis_timestamp():
    # https://www.epochconverter.com/?q=1704067200000

    str_date = "2024-01-01T00:00:00.000Z"
    output = convert_str_to_milis_timestamp(str_date)
    assert output == 1704067200000


def test_convert_milis_timestamp_to_str():
    # https://www.epochconverter.com/?q=1704067200000

    ts = 1704067200000
    output = convert_milis_timestamp_to_str(ts)
    assert output == "2024-01-01T00:00:00.000Z"
