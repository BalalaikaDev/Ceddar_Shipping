"""Mission 03 — Weigh the cargo.

Decide with a boolean, then choose the label with if/else.

Concepts: a boolean (True/False), comparison, if/else.
"""


def decide(weight: int, capacity: int) -> str:
    # Step 1 — does it fit? A comparison gives a boolean (True or False).
    fits = False     # TODO: replace False with  weight <= capacity

    # Step 2 — choose the label (this part is done for you).
    if fits:
        return "LOAD"
    else:
        return "LEAVE BEHIND"
