from missions.m02_course import eta_hours


def test_basic():
    assert eta_hours(100, 10) == 10
    assert eta_hours(50, 25) == 2


def test_fractional():
    assert eta_hours(30, 4) == 7.5
