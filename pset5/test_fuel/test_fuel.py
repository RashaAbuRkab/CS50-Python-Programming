import pytest
from fuel import convert, gauge

def test_convert_valid_cases():
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("0/1") == 0
    assert convert("1/1") == 100
    assert convert("5/8") == 62  # 62.5 rounded to 63

def test_convert_invalid_cases():
    with pytest.raises(ValueError):
        convert("2/1.5")  # Not an integer
    with pytest.raises(ValueError):
        convert("2/a")  # Not an integer
    with pytest.raises(ValueError):
        convert("3/2")  # Should raise if X > Y
    with pytest.raises(ZeroDivisionError):
        convert("3/0")  # Y cannot be zero

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
