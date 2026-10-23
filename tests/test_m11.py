from missions.m11_container import pack


def test_pack():
    assert pack([{"weight": 10}, {"weight": 5}]) == {"units": 2, "weight": 15}
    assert pack([]) == {"units": 0, "weight": 0}
    assert pack([{"weight": 7}]) == {"units": 1, "weight": 7}
