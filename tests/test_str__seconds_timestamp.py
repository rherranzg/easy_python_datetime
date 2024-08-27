from src.str__seconds_timestamp import (
    convert_seconds_timestamp_to_str,
    convert_str_to_seconds_timestamp,
)


def test_convert_str_to_seconds_timestamp():
    input_str = "2024-01-01T00:00:00.000Z"
    output = convert_str_to_seconds_timestamp(input_str)
    assert output == 1704067200


def test_convert_seconds_timestamp_to_str():
    ts = 1704067200
    output = convert_seconds_timestamp_to_str(ts)
    assert output == "2024-01-01T00:00:00.000Z"
