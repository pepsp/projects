from numb3rs import validate

def test_validate_num():
    assert validate("1.2.3.4") == True
    assert validate("....") == False
    assert validate("5654656") == False
    assert validate("255.256.256.256") == False


def test_validate_letter():
    assert validate("a.b.c.d") == False
    assert validate("....") == False
    assert validate("amogus") == False
