from datetime import datetime, timezone

from gspread_models.date_parser import DateParser

def test_generate_timestamp():
    dt = DateParser.generate_timestamp()
    assert isinstance(dt, datetime)
    assert dt.tzinfo == timezone.utc

def test_parse_timestamp():
    example_ts = "2023-03-08 19:59:16.471152+00:00"
    dt = DateParser.parse_timestamp(example_ts)
    assert isinstance(dt, datetime)
    assert dt.year == 2023
    assert dt.month == 3
    assert dt.day == 8
    assert dt.hour == 19
    assert dt.minute == 59
    assert dt.second == 16
    assert dt.tzinfo == timezone.utc

def test_validate_timestamp():
    assert DateParser.validate_timestamp("2023-03-08 19:59:16.471152+00:00") == True
    assert DateParser.validate_timestamp("2023-03-08 19:59:16.471152") == False
    assert DateParser.validate_timestamp("2023-03-08 19:59:16+00:00") == False
    assert DateParser.validate_timestamp("2023-03-08 19:59:16") == False
    assert DateParser.validate_timestamp("2023-03-08") == False
    assert DateParser.validate_timestamp("OOPS") == False
