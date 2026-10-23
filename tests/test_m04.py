from missions.m04_load import load_hold


def test_filters_by_limit():
    assert load_hold([10, 50, 30, 80], 50) == [10, 50, 30]


def test_order_and_empty():
    assert load_hold([], 10) == []
    assert load_hold([99, 100], 50) == []
    assert load_hold([5, 60, 20], 20) == [5, 20]
