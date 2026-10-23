"""Mission 08 — Dispatch the fleet.

You now command several boats. Given your fleet and a crate weight, return the
NAMES of the boats that can carry it — in fleet order.

Concepts: looping over a list of OBJECTS, calling their methods, building a list.
Reuses the Boat class from Mission 07.
"""
from missions.m07_boat import Boat


def available(fleet: list[Boat], weight: int) -> list[str]:
    """Return the names of boats in `fleet` whose can_carry(weight) is True."""
    # TODO: loop over the fleet; keep the name of each boat that can carry it.
    raise NotImplementedError("Mission 08: return the names of boats that can carry it")
