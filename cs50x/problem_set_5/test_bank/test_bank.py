from bank import value


def test_lowercase():
        assert value("hello") == 0
        assert value("hhhhhhelloooo") == 20
        assert value("hi") == 20
        assert value("ahoy there") == 100
        assert value("good morning") == 100

def test_caps():
        assert value("HHHHHELLO") == 20
        assert value("HELLO") == 0
        assert value("HI") == 20
        assert value("AHOY THERE") == 100
        assert value("GOOD MORNING") == 100

def test_combined():
        assert value("hhHhHeLLo") == 20
        assert value("HeLlO") == 0
        assert value("hI") == 20
        assert value("aHOy") == 100
        assert value("gOOd mOrnInG") == 100
        assert value("123413456fdsafdsfds") == 100

