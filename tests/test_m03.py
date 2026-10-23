from missions.m03_weigh import decide


def test_load_when_it_fits():
    assert decide(10, 20) == "LOAD"
    assert decide(20, 20) == "LOAD"      # exactly full still fits


def test_leave_when_too_heavy():
    assert decide(21, 20) == "LEAVE BEHIND"
    assert decide(100, 5) == "LEAVE BEHIND"
