from missions.m07_boat import Boat


def test_attributes():
    b = Boat("Nimbus", 100)
    assert b.name == "Nimbus"
    assert b.capacity == 100


def test_can_carry():
    b = Boat("Nimbus", 100)
    assert b.can_carry(100) is True
    assert b.can_carry(40) is True
    assert b.can_carry(101) is False
