from missions.m03_threatcheck import classify


def test_flag():
    assert classify(70) == "FLAG"
    assert classify(95) == "FLAG"


def test_clear():
    assert classify(69) == "CLEAR"
    assert classify(0) == "CLEAR"
