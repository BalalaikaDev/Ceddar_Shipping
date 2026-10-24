# Graph Report - operator-training  (2026-10-24)

## Corpus Check
- 35 files · ~5,728 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 2, .ini 1)

## Summary
- 144 nodes · 198 edges · 21 communities (17 shown, 4 thin omitted)
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 12 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `dc19fe05`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Boat
- captain
- play.py
- m06_logistics.py
- sim.py
- Setup on a fresh PC
- eta_hours
- decide
- load_hold
- value_of
- berth_for
- m11_container.py
- M02 — Plot a course
- M03 — Weigh the cargo
- M04 — Load the hold
- M05 — Read the manifest
- How to play
- Cedar Shipping
- AGENTS.md

## God Nodes (most connected - your core abstractions)
1. `gather()` - 13 edges
2. `Boat` - 12 edges
3. `Setup on a fresh PC` - 9 edges
4. `captain()` - 8 edges
5. `eta_hours()` - 6 edges
6. `decide()` - 6 edges
7. `load_hold()` - 6 edges
8. `available()` - 6 edges
9. `berth_for()` - 6 edges
10. `watch()` - 6 edges

## Surprising Connections (you probably didn't know these)
- `Your task` --references--> `captain()`  [INFERRED]
  briefs/m01.md → missions/m01_signon.py
- `gather()` --indirect_call--> `captain()`  [INFERRED]
  sim.py → missions/m01_signon.py
- `gather()` --indirect_call--> `eta_hours()`  [INFERRED]
  sim.py → missions/m02_course.py
- `gather()` --indirect_call--> `decide()`  [INFERRED]
  sim.py → missions/m03_weigh.py
- `gather()` --indirect_call--> `load_hold()`  [INFERRED]
  sim.py → missions/m04_load.py

## Import Cycles
- None detected.

## Communities (21 total, 4 thin omitted)

### Community 0 - "Boat"
Cohesion: 0.29
Nodes (5): Boat, available(), test_attributes(), test_can_carry(), test_available()

### Community 1 - "captain"
Cohesion: 0.23
Nodes (8): Clear it, M01 — Sign the logbook, What you're learning, Your task, captain(), test_not_empty(), test_returns_a_string(), test_single_lowercase_word()

### Community 2 - "play.py"
Cohesion: 0.24
Nodes (6): _clear(), _fingerprint(), mission_passes(), _redraw_voyage(), render(), watch()

### Community 3 - "m06_logistics.py"
Cohesion: 0.48
Nodes (4): fuel_cost(), profit(), test_fuel_cost(), test_profit_uses_fuel_cost()

### Community 4 - "sim.py"
Cohesion: 0.20
Nodes (10): has_lane(), neighbours(), _call(), _crate(), gather(), _next(), render(), scene() (+2 more)

### Community 5 - "Setup on a fresh PC"
Cohesion: 0.20
Nodes (9): 1. Install Python (the language), 2. Install Git (to download the game and get updates), 3. Install VS Code (your editor + terminal in one window), 4. Get the game, 5. Open it and play — one window, Getting updates later, macOS / Linux, Setup on a fresh PC (+1 more)

### Community 6 - "eta_hours"
Cohesion: 0.53
Nodes (3): eta_hours(), test_basic(), test_fractional()

### Community 7 - "decide"
Cohesion: 0.53
Nodes (3): decide(), test_leave_when_too_heavy(), test_load_when_it_fits()

### Community 8 - "load_hold"
Cohesion: 0.53
Nodes (3): load_hold(), test_filters_by_limit(), test_order_and_empty()

### Community 9 - "value_of"
Cohesion: 0.53
Nodes (3): value_of(), test_found(), test_missing_returns_zero()

### Community 10 - "berth_for"
Cohesion: 0.53
Nodes (3): berth_for(), test_found(), test_missing_and_empty()

### Community 12 - "M02 — Plot a course"
Cohesion: 0.40
Nodes (4): Clear it, M02 — Plot a course, What you're learning, Your task

### Community 13 - "M03 — Weigh the cargo"
Cohesion: 0.40
Nodes (4): Clear it, M03 — Weigh the cargo, What you're learning, Your task

### Community 14 - "M04 — Load the hold"
Cohesion: 0.40
Nodes (4): Clear it, M04 — Load the hold, What you're learning, Your task

### Community 15 - "M05 — Read the manifest"
Cohesion: 0.40
Nodes (4): Clear it, M05 — Read the manifest, What you're learning, Your task

### Community 16 - "How to play"
Cohesion: 0.29
Nodes (6): How to play, If you prefer plain tests, One-time setup, Set up the one-window view (do this once per session), The loop (this is the whole game), Tips

### Community 17 - "Cedar Shipping"
Cohesion: 0.50
Nodes (3): Cedar Shipping, Set sail, The story

## Knowledge Gaps
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `gather()` connect `sim.py` to `Boat`, `captain`, `eta_hours`, `decide`, `load_hold`, `berth_for`, `m11_container.py`?**
  _High betweenness centrality (0.090) - this node is a cross-community bridge._
- **Are the 9 inferred relationships involving `gather()` (e.g. with `captain()` and `eta_hours()`) actually correct?**
  _`gather()` has 9 INFERRED edges - model-reasoned connections that need verification._
- **Why does `captain()` connect `captain` to `sim.py`?**
  _High betweenness centrality (0.084) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `captain()` (e.g. with `Your task` and `gather()`) actually correct?**
  _`captain()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Why does `Boat` connect `Boat` to `sim.py`?**
  _High betweenness centrality (0.068) - this node is a cross-community bridge._