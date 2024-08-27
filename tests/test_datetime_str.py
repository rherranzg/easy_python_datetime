from datetime import datetime, timezone

from src.datetime__str import convert_datetime_to_str, convert_str_to_datetime


def test_convert_str_to_datetime():
    input_str = "2024-01-01T00:00:00.000Z"
    output = convert_str_to_datetime(input_str)
    assert output == datetime(2024, 1, 1, 0, 0, 0, 0, tzinfo=timezone.utc)


def test_convert_datetime_to_str():
    dt = datetime(2024, 1, 1, 0, 0, 0, 0, tzinfo=timezone.utc)
    output = convert_datetime_to_str(dt)
    assert output == "2024-01-01T00:00:00.000Z"
