"""Mission 09 — The route network.

Ports are linked by shipping lanes. We store the network as a dictionary mapping
each port to the list of ports it has a direct lane to — an "adjacency list".
This is exactly how a graph database like Neo4j thinks: nodes and the
relationships between them.

Concepts: a dict of lists (nested data), safe lookup.

Example network:
    {"A": ["B", "C"], "B": ["A"], "C": []}
"""


def neighbours(lanes: dict, port: str) -> list:
    """Return the list of ports directly reachable from `port` (or [] if none)."""
    # TODO: look up port in lanes; default to an empty list.
    raise NotImplementedError("Mission 09a: return the neighbours")


def has_lane(lanes: dict, start: str, end: str) -> bool:
    """Return True if there is a direct lane from `start` to `end`."""
    # TODO: is `end` among the neighbours of `start`? (reuse neighbours())
    raise NotImplementedError("Mission 09b: return whether a direct lane exists")
