# Cedar Shipping

> Learn to actually write **Python** — not vibe-code it — by running a shipping
> empire. You start as one boat hauling crates from port to port. You end up
> commanding an automated fleet. Every mission teaches a real concept.

Each mission is a small, **failing test** you make pass. No lectures, no prior
experience needed — you learn the way engineers actually work (test-driven),
and clearing a mission means your code provably does the job.

## The story

**Act I — Deckhand.** One boat, one captain, one run at a time.

| # | Mission | You learn |
|---|---------|-----------|
| 01 | Sign the logbook | functions, `return`, strings |
| 02 | Plot a course | numbers & division |
| 03 | Weigh the cargo | `if` / `else`, comparisons |
| 04 | Load the hold | lists, `for` loops |
| 05 | Read the manifest | dictionaries, safe lookup |

**Act II — The Fleet** *(coming next).* Hire more boats and stop doing every run
by hand:

- **reuse your work** — one `deliver()` routine many boats can run *(functions)*
- **a boat with a name, capacity and position** — your first **class** *(objects)*
- **dispatch the whole fleet at once** — loop over your boats *(iteration)*
- **the route network** — ports linked by shipping lanes: a **graph** — the idea
  behind **Neo4j**
- **radio the harbour for orders** — calling an **API**, the idea behind **FastAPI**
- **🚢 containers** — pack each cargo so it runs anywhere: the idea behind **Docker**

By the end you'll have met — in a game — the exact stack that powers real
systems like [runi-os](https://github.com/BalalaikaDev/runi-os).

## Set sail
```
pip install -r requirements.txt
python play.py
```
Then follow `HOW_TO_PLAY.md`. Fair winds, captain.
