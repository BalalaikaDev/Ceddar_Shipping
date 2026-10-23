from missions.m04_scan import open_ports


def test_filters_even():
    assert open_ports([22, 80, 443, 8080]) == [22, 80, 8080]


def test_keeps_order_and_handles_empty():
    assert open_ports([]) == []
    assert open_ports([1, 3, 5]) == []
    assert open_ports([2, 1, 4, 3]) == [2, 4]
