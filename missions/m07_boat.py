"""Mission 07 — Build a boat.

So far you've written loose functions. A class lets you bundle DATA (a boat's
name and capacity) with BEHAVIOUR (whether it can carry a crate) into one thing
you can make many of.

Concepts: class, __init__, self, attributes, a method.

Fill in the two TODOs. `self` is "this particular boat".
"""


class Boat:
    def __init__(self, name: str, capacity: int):
        # TODO: store the two arguments on the boat:
        #   self.name = name
        #   self.capacity = capacity
        raise NotImplementedError("Mission 07a: store name and capacity on self")

    def can_carry(self, weight: int) -> bool:
        # TODO: return True if weight fits within this boat's capacity
        raise NotImplementedError("Mission 07b: return whether weight fits")
