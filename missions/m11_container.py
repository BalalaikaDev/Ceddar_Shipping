"""Mission 11 — Pack a container.

Loose cargo is a pain: every port handles it differently. So you pack items into
a standard container — one predictable unit any boat can carry and any port can
stack. (This is the idea behind Docker: package things so they run the same
everywhere.)

Given a list of items, each a dict with a "weight", return a container summary:
    {"units": <how many items>, "weight": <their total weight>}

Concepts: looping over a list of dicts, summing, building a dict to return.
"""


def pack(items: list[dict]) -> dict:
    """Return {"units": count of items, "weight": total of their weights}."""
    # TODO: count the items and add up their "weight" values.
    raise NotImplementedError("Mission 11: return the container summary")
