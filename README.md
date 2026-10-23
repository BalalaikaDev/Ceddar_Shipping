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

**Act II — The Fleet.** Hire more boats and stop doing every run by hand. These
rungs climb into the exact stack that powers real systems like
[runi-os](https://github.com/BalalaikaDev/runi-os):

| # | Mission | You learn |
|---|---------|-----------|
| 06 | Count the cost | functions calling functions |
| 07 | Build a boat | your first **class** (objects) |
| 08 | Dispatch the fleet | looping over objects |
| 09 | The route network | **graphs** — the idea behind **Neo4j** |
| 10 | Radio the harbour | nested data / **APIs** — the idea behind **FastAPI** |
| 11 | Pack a container | standard units — the idea behind **Docker** 🚢 |

*More acts to come: a real FastAPI + Neo4j + Docker capstone that turns the game
into a working mini-platform.*

## Set sail
```
pip install -r requirements.txt
python play.py
```
Then follow `HOW_TO_PLAY.md`. Fair winds, captain.
