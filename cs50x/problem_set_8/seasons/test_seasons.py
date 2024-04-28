from seasons import get_today
from datetime import date

def test_get_today():
    assert get_today() == date.today()
    assert get_today() == date.today()
    assert get_today() == date.today()
    assert get_today() == date.today()
    assert get_today() == date.today()
"""|
today = get_today()

print(today)

"""
