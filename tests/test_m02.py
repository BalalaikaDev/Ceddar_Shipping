from missions.m02_triangulate import midpoint


def test_basic():
    assert midpoint(0, 10) == 5
    assert midpoint(4, 4) == 4


def test_negatives_and_floats():
    assert midpoint(-2, 2) == 0
    assert midpoint(1, 2) == 1.5
