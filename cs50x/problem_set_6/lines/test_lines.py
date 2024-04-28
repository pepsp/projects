from lines import command_check, get_file
import pytest

def test_command_check():
    with pytest.raises(ValueError):
        assert command_check(["lines.py", "lol.txt"])
        assert command_check(["lines.py", "source_file.txt"])
        assert command_check(["lines.py", "sourcefilepy"])
        assert command_check(["lines.py", "sdaDSADSadsadsadsadsa"])
    with pytest.raises(IndexError):
        assert command_check(["lines.py"])
        assert command_check(["lines.py", "source_file.py", "XD"])

def test_get_file():
    assert get_file("garbage.py") == 7
    assert get_file("hello.py") == 3



