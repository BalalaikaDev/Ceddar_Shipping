from missions.m01_identify import callsign


def test_returns_a_string():
    assert isinstance(callsign(), str), "callsign() must return a string"


def test_not_empty():
    assert callsign().strip() != "", "your callsign can't be empty"


def test_lowercase_handle():
    cs = callsign()
    assert cs == cs.lower(), "keep your callsign lowercase"
    assert " " not in cs, "a callsign is one word — no spaces"
