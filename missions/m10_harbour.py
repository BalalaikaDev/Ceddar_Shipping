"""Mission 10 — Radio the harbour.

You radio the harbour and it answers with a data packet (a dictionary) — the
same shape a web API (like FastAPI) sends back as JSON. Dig out the berth your
boat was assigned.

A response looks like:
    {"status": "ok", "assignments": {"Nimbus": "B12", "Tug": "A3"}}

Concepts: reading NESTED dictionaries, safe lookups with defaults.
"""


def berth_for(response: dict, boat_name: str) -> str:
    """Return the berth assigned to boat_name, or "NONE" if it wasn't assigned."""
    # TODO: reach into response["assignments"], then the boat_name, default "NONE".
    # Hint: response.get("assignments", {}).get(boat_name, "NONE")
    raise NotImplementedError("Mission 10: return the assigned berth")
