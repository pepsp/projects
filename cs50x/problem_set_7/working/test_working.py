from working import convert
import pytest


def test_convert_nominutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 AM to 8:00 AM") == "00:00 to 08:00"
    with pytest.raises(ValueError):
        convert("10 AM 12 PM")
        convert("9:88 AM 5:69 PM")


def test_convert_with_minutes():
    assert convert("10:50 AM to 12:34 PM") == "10:50 to 12:34"
    assert convert("12:59 AM to 11:35 AM") == "00:59 to 11:35"
    with pytest.raises(ValueError):
        convert("10:80 AM to 59:59 PM")
        convert("5:32 4:55")


def test_convert_outta():
    with pytest.raises(ValueError):
        convert("99:99 AM to 99:99 PM")
