# Operator Training

> Learn to actually write **Python** — not vibe-code it — by clearing missions
> in an OSINT console. Each mission is a small, failing test you make pass.

Built as a from-scratch learning track to go with
[runi-os](https://github.com/BalalaikaDev/runi-os): the missions are themed as
investigation drills, and the concepts you learn here (safe lookups, scanning,
records, later graphs and API calls) are the exact building blocks that platform
is made of.

## Why this format
No lectures. You learn by doing the smallest useful thing and getting instant,
honest feedback from tests — the same way real engineers work (test-driven
development). Clearing a mission means your code provably does what was asked.

## The ladder
| # | Mission | You learn |
|---|---------|-----------|
| 01 | Identify | functions, `return`, strings |
| 02 | Triangulate | numbers & arithmetic |
| 03 | Threat check | `if` / `else`, comparisons |
| 04 | Port scan | lists, `for` loops, modulo |
| 05 | Pull a record | dictionaries, safe lookup |

_More drops coming: functions calling functions, your first class (`Entity`),
a tiny connections graph (the idea behind Neo4j), reading JSON, and calling a
mock enrichment source (the idea behind an API)._

## Start
```
pip install -r requirements.txt
python play.py
```
Then follow `HOW_TO_PLAY.md`. Good hunting, operator.
