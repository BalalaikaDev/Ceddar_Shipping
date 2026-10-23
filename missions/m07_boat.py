"""Mission 07 — Build a boat.

Your first class: data (name, capacity) + behaviour (can_carry) in one object.

Concepts: class, __init__, self, attributes, a method.
"""


class Boat:
    def __init__(self, name: str, capacity: int):
        # Step 1 — store the two values on THIS boat. `self` means this boat.
        self.name = "???"    # TODO: replace "???" with  name
        self.capacity = 0    # TODO: replace 0 with  capacity

    def can_carry(self, weight: int) -> bool:
        # Step 2 — can this boat take `weight`? Compare to its own capacity.
        return False         # TODO: replace False with  weight <= self.capacity
