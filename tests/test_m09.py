from missions.m09_routes import neighbours, has_lane

NET = {"A": ["B", "C"], "B": ["A"], "C": []}


def test_neighbours():
    assert neighbours(NET, "A") == ["B", "C"]
    assert neighbours(NET, "C") == []
    assert neighbours(NET, "Z") == []        # unknown port, no crash


def test_has_lane():
    assert has_lane(NET, "A", "B") is True
    assert has_lane(NET, "A", "Z") is False
    assert has_lane(NET, "C", "A") is False
