from fuel import convert, gauge
import pytest

def test_convert_ints():
    assert convert("4/5") == 80
    assert convert("5/5") == 100
    assert convert("1/5") == 20

def test_convert_valueerror():
    with pytest.raises(ValueError):
        assert convert("A/F")
        assert convert("$/%")
        assert convert("saddsadsa")
        assert convert("45454")
        assert convert("54")
        assert convert("dd/dd")

def test_convert_zerodivisionerror():
    with pytest.raises(ZeroDivisionError):
        assert convert("4/0")
        assert convert("0/0")




def test_gauge():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(98) == "98%"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(50) == "50%"
    assert gauge(2) == "2%"

