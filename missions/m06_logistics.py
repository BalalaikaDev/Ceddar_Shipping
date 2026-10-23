"""Mission 06 — Count the cost.

Every run burns fuel. Fuel costs FUEL_PRICE coins per mile. Profit is what the
cargo is worth minus the fuel it took to carry it.

Concepts: a module constant, a helper function, and one function CALLING another.
"""

FUEL_PRICE = 2   # coins per mile


def fuel_cost(distance: int) -> int:
    """Return the fuel cost for a trip: distance * FUEL_PRICE."""
    # TODO: return distance * FUEL_PRICE
    raise NotImplementedError("Mission 06a: return the fuel cost")


def profit(cargo_value: int, distance: int) -> int:
    """Return cargo_value minus the fuel cost. Reuse fuel_cost() — don't repeat it."""
    # TODO: return cargo_value - fuel_cost(distance)
    raise NotImplementedError("Mission 06b: return the profit")
