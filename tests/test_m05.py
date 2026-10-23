from missions.m05_records import lookup

CASE = {"e1": "Alice", "e2": "Bob"}


def test_found():
    assert lookup(CASE, "e1") == "Alice"
    assert lookup(CASE, "e2") == "Bob"


def test_missing_returns_unknown():
    assert lookup(CASE, "e9") == "UNKNOWN"
    assert lookup({}, "e1") == "UNKNOWN"
