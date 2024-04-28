from um import count

def test_count():
    assert count("um um um!") == 3
    assert count("UM uM! Um?") == 3
    assert count("yum fum cum clum stun") == 0
