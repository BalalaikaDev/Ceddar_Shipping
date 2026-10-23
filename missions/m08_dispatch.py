"""Mission 08 — Dispatch the fleet.

Loop over a fleet of Boat objects; keep the names that can carry the cargo.

Concepts: looping over objects, calling a method, building a list.
"""
from missions.m07_boat import Boat


def available(fleet: list[Boat], weight: int) -> list[str]:
    # Step 1 — start an empty list of names.
    names = []

    # Step 2 — check each boat in the fleet.
    for boat in fleet:
        # Step 3 — can this boat carry the weight?
        can = False          # TODO: replace False with  boat.can_carry(weight)
        if can:
            names.append(boat.name)

    return names
