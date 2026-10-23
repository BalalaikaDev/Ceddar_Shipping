"""Mission 10 — Radio the harbour.

The harbour answers with a data packet (a dict inside a dict) — the shape a web
API like FastAPI returns as JSON. Dig out your berth.

A response looks like:
    {"status": "ok", "assignments": {"Nimbus": "B12", "Tug": "A3"}}

Concepts: nested dictionaries, safe lookup with a default.
"""


def berth_for(response: dict, boat_name: str) -> str:
    # Step 1 — reach the assignments dict INSIDE the response.
    assignments = {}      # TODO: replace {} with  response.get("assignments", {})

    # Step 2 — look up this boat's berth; default to "NONE".
    berth = "NONE"        # TODO: replace "NONE" with  assignments.get(boat_name, "NONE")

    return berth
