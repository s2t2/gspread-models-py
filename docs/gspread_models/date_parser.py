
from datetime import datetime, timezone


# see: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
DATE_FORMAT = "%Y-%m-%d %H:%M:%S.%f%z" # consider allowing customization


class DateParser:
    """Mixin for date parsing / interfacing with google sheets date formatting."""

    @staticmethod
    def generate_timestamp():
        """Generates a new timestamp of the current time in UTC timezone.
            Returns a datetime object.
        """
        return datetime.now(tz=timezone.utc)

    @staticmethod
    def parse_timestamp(ts:str) -> datetime:
        """Converts a timestamp string to a datetime object as necessary.
            Ensures you are working with a datetime object.

            Params:
                ts (str) : a timestamp string in format provided by google sheets

            Example: DateParser.parse_timestamp('2023-03-08 19:59:16.471152+00:00')

            Returns a datetime object.
        """
        if isinstance(ts, datetime):
            return ts
        elif isinstance(ts, str):
            return datetime.strptime(ts, DATE_FORMAT)
        #else:
        #    # something went wrong! use original value. consider raising error
        #    return ts

    @staticmethod
    def validate_timestamp(ts:str):
        try:
            datetime.strptime(ts, DATE_FORMAT)
            return True
        except:
            return False
