"""Mission 04 — Load the hold.

Loop over the crates and keep the ones that fit.

Concepts: a list, a for-loop, a boolean, .append().
"""


def load_hold(crates: list[int], limit: int) -> list[int]:
    # Step 1 — start with an empty hold (a list).
    loaded = []

    # Step 2 — look at each crate in turn.
    for crate in crates:
        # Step 3 — is this crate within the limit?
        fits = False         # TODO: replace False with  crate <= limit
        if fits:
            loaded.append(crate)   # add it to the hold

    # Step 4 — hand back everything you loaded.
    return loaded
