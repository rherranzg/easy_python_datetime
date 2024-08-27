from datetime import datetime

from src.constants import STANDARD_CHOSEN_STRING_FORMAT
from src.datetime__seconds_timestamp import (
    convert_datetime_to_seconds_timestamp,
    convert_seconds_timestamp_to_datetime,
)
from src.datetime__str import convert_datetime_to_str, convert_str_to_datetime

# seconds-timestamp <-> str


def convert_str_to_seconds_timestamp(
    incoming_str_date: str, incoming_date_format: str = STANDARD_CHOSEN_STRING_FORMAT
) -> int:
    """
    In order to convert string into seconds-timestamp,
    we will transform first the string into datetime.
    """

    dt_date = convert_str_to_datetime(incoming_str_date, incoming_date_format)
    return convert_datetime_to_seconds_timestamp(dt_date)


def convert_seconds_timestamp_to_str(
    incoming_timestamp: int, incoming_date_format: str = STANDARD_CHOSEN_STRING_FORMAT
) -> str:
    """
    In order to convert seconds-timestamp into string,
    we will transform first the seconds-timestamp into datetime.
    """

    dt_date = convert_seconds_timestamp_to_datetime(incoming_timestamp)
    return convert_datetime_to_str(dt_date, incoming_date_format)
