from project import (
    main,
    get_word,
    select_difficulty,
    previous_guess
)
from hangman_data import difficulty
from unittest.mock import patch



def test_get_word():
    assert get_word(1) in difficulty["easy"]
    assert get_word(2) in difficulty["hard"]

@patch("builtins.input", side_effect=["perro"])
def test_get_word_custom(mock_input):
    assert get_word(3) == "perro"

def test_select_difficulty():
    input_values = ["1"]
    assert select_difficulty(lambda _: input_values.pop(0)) in [1, 2, 3, 0]


def test_previous_guess():
    assert previous_guess(['a', 'b', 'c']) == "\n↓↓ Previously guessed letters ↓↓\n a b c "
