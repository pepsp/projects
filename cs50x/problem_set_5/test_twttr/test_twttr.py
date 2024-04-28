from twttr import shorten

def test_lowercase():
    assert shorten("eyes") == "ys"
    assert shorten("a") == ""
    assert shorten("e") == ""


def test_caps():
    assert shorten("EYES") == "YS"
    assert shorten("A") == ""
    assert shorten("E") == ""

def test_num():
    assert shorten("I am 26 years old!") == " m 26 yrs ld!"
    assert shorten("69645 cats") == "69645 cts"

def test_punctuation():
    assert shorten("!@#@$##$.,.,.,.") == "!@#@$##$.,.,.,."
    assert shorten("I'm.called??") == "'m.clld??"

