"""Mission 06 — Count the cost.

A constant, a helper function, and one function reusing another.

Concepts: a module constant, variables, calling a function from a function.
"""

FUEL_PRICE = 2   # coins per mile — a constant (a variable we don't change)


def fuel_cost(distance: int) -> int:
    # Step 1 — fuel cost = distance * FUEL_PRICE.
    cost = 0         # TODO: replace 0 with  distance * FUEL_PRICE
    return cost


def profit(cargo_value: int, distance: int) -> int:
    # Step 2 — REUSE fuel_cost() instead of repeating the maths.
    spent = 0        # TODO: replace 0 with  fuel_cost(distance)

    # Step 3 — profit is what's left after fuel.
    return cargo_value - spent
