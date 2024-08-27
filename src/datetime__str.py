# datetime <-> str
from datetime import datetime, timezone
from typing import Union

from src.constants import STANDARD_CHOSEN_STRING_FORMAT

# datetime <-> str


def convert_str_to_datetime(
    incoming_str_date: str, incoming_date_format: str = STANDARD_CHOSEN_STRING_FORMAT
) -> datetime:
    """
    Convert a string to a datetime object
    """

    if not incoming_str_date:
        return None
    dt_date = datetime.strptime(incoming_str_date, incoming_date_format)
    return dt_date.replace(tzinfo=timezone.utc)


def convert_datetime_to_str(
    incoming_datetime: str, incoming_date_format: str = STANDARD_CHOSEN_STRING_FORMAT
) -> Union[str, None]:
    """
    Convert a datetime object to a string
    """

    if not incoming_datetime:
        return None
    return incoming_datetime.strftime(incoming_date_format)[:-4] + "Z"
