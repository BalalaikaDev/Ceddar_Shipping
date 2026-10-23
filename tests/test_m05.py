from missions.m05_manifest import value_of

MANIFEST = {"c1": 100, "c2": 250}


def test_found():
    assert value_of(MANIFEST, "c1") == 100
    assert value_of(MANIFEST, "c2") == 250


def test_missing_returns_zero():
    assert value_of(MANIFEST, "c9") == 0
    assert value_of({}, "c1") == 0
