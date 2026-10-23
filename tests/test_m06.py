from missions.m06_logistics import fuel_cost, profit


def test_fuel_cost():
    assert fuel_cost(10) == 20
    assert fuel_cost(0) == 0


def test_profit_uses_fuel_cost():
    assert profit(100, 10) == 80     # 100 - (10*2)
    assert profit(50, 25) == 0       # 50 - 50
