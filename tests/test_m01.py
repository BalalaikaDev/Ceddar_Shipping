from missions.m01_signon import captain


def test_returns_a_string():
    assert isinstance(captain(), str), "captain() must return a string"


def test_not_empty():
    assert captain().strip() != "", "your captain name can't be empty"


def test_single_lowercase_word():
    name = captain()
    assert name == name.lower(), "keep it lowercase"
    assert " " not in name, "one word — no spaces"
