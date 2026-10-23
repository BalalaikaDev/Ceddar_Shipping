from missions.m10_harbour import berth_for

RESP = {"status": "ok", "assignments": {"Nimbus": "B12", "Tug": "A3"}}


def test_found():
    assert berth_for(RESP, "Nimbus") == "B12"
    assert berth_for(RESP, "Tug") == "A3"


def test_missing_and_empty():
    assert berth_for(RESP, "Hauler") == "NONE"
    assert berth_for({"status": "ok"}, "Nimbus") == "NONE"
