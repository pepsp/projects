from plates import is_valid


def test_twoletters():
    assert is_valid("CS50") == True
    assert is_valid("HELLO") == True
    assert is_valid("A") == False
    assert is_valid("AB") == True


def test_numbers():
    assert is_valid("AB55AB") == False
    assert is_valid("AAA222") == True
    assert is_valid("AAA022") == False
    assert is_valid("AB0222") == False
    assert is_valid("AB3333") == True
    assert is_valid("123213") == False


def test_space_punct():
    assert is_valid(" AB22") == False
    assert is_valid("PU69!") == False
    assert is_valid("@@44") == False
    assert is_valid("##") == False
    assert is_valid("  ") == False
