from missions.m07_boat import Boat
from missions.m08_dispatch import available


def test_available():
    fleet = [Boat("Nimbus", 100), Boat("Tug", 30), Boat("Hauler", 500)]
    assert available(fleet, 50) == ["Nimbus", "Hauler"]
    assert available(fleet, 1000) == []
    assert available(fleet, 10) == ["Nimbus", "Tug", "Hauler"]
