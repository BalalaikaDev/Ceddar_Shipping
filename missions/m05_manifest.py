"""Mission 05 — Read the manifest.

Look up a crate's value safely.

Concepts: a dictionary, .get() with a default.
"""


def value_of(manifest: dict, crate_id: str) -> int:
    # Step 1 — look up crate_id; if it's not on the manifest, use 0.
    value = 0        # TODO: replace 0 with  manifest.get(crate_id, 0)

    return value
