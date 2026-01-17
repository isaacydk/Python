import pytest
from working import convert


# -------------------------
# Valid conversions
# -------------------------

def test_convert_basic():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("5 PM to 9 AM") == "17:00 to 09:00"


def test_convert_with_minutes():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:30 AM to 8:50 PM") == "10:30 to 20:50"
    assert convert("5:15 PM to 9:45 AM") == "17:15 to 09:45"


def test_convert_missing_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 AM to 1 PM") == "00:00 to 13:00"
    assert convert("11 PM to 12 AM") == "23:00 to 00:00"


def test_convert_edge_cases():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("1 AM to 12 PM") == "01:00 to 12:00"


# -------------------------
# Invalid input tests
# -------------------------

def test_convert_invalid_format():
    with pytest.raises(ValueError):
        convert("9 to 5 PM")

    with pytest.raises(ValueError):
        convert("9AM - 5PM")

    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")

    with pytest.raises(ValueError):
        convert("9:99 AM to 5 PM")

    with pytest.raises(ValueError):
        convert("9 AM 5 PM")


def test_convert_invalid_text():
    with pytest.raises(ValueError):
        convert("hello world")

    with pytest.raises(ValueError):
        convert("AM to PM")
