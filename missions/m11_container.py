"""Mission 11 — Pack a container.

Pack loose items into one standard unit any boat can carry and any port can
stack. (The idea behind Docker: package things so they run the same everywhere.)

Given items like [{"weight": 10}, {"weight": 5}], return:
    {"units": 2, "weight": 15}

Concepts: len(), sum() over a list of dicts, building a dict to return.
"""


def pack(items: list[dict]) -> dict:
    # Step 1 — how many items are there?
    units = 0        # TODO: replace 0 with  len(items)

    # Step 2 — add up their weights.
    weight = 0       # TODO: replace 0 with  sum(i["weight"] for i in items)

    # Step 3 — return the standard container summary (a dict).
    return {"units": units, "weight": weight}
