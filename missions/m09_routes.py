"""Mission 09 — The route network.

Ports linked by lanes, stored as a dict of lists (an "adjacency list"). This is
how a graph database like Neo4j thinks: nodes + the links between them.

Concepts: a dict of lists, safe lookup, reusing a function.

Example: {"A": ["B", "C"], "B": ["A"], "C": []}
"""


def neighbours(lanes: dict, port: str) -> list:
    # Step 1 — the ports directly reachable from `port` (empty list if unknown).
    links = []       # TODO: replace [] with  lanes.get(port, [])
    return links


def has_lane(lanes: dict, start: str, end: str) -> bool:
    # Step 1 — get start's neighbours (REUSE the function above).
    links = []       # TODO: replace [] with  neighbours(lanes, start)

    # Step 2 — is `end` one of them?
    return end in links
