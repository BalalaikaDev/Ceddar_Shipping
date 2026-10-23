# Graph Report - operator-training  (2026-10-23)

## Corpus Check
- 33 files · ~3,236 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 2, .ini 1)

## Summary
- 154 nodes · 181 edges · 20 communities (17 shown, 3 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 3 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `a1fad125`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Boat
- captain
- play.py
- m06_logistics.py
- m09_routes.py
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

## God Nodes (most connected - your core abstractions)
1. `Boat` - 10 edges
2. `Setup on a fresh PC` - 9 edges
3. `captain()` - 7 edges
4. `eta_hours()` - 5 edges
5. `decide()` - 5 edges
6. `load_hold()` - 5 edges
7. `value_of()` - 5 edges
8. `available()` - 5 edges
9. `berth_for()` - 5 edges
10. `watch()` - 5 edges

## Surprising Connections (you probably didn't know these)
- `Your task` --references--> `captain()`  [INFERRED]
  briefs/m01.md → missions/m01_signon.py
- `test_not_empty()` --calls--> `captain()`  [EXTRACTED]
  tests/test_m01.py → missions/m01_signon.py
- `test_returns_a_string()` --calls--> `captain()`  [EXTRACTED]
  tests/test_m01.py → missions/m01_signon.py
- `test_single_lowercase_word()` --calls--> `captain()`  [EXTRACTED]
  tests/test_m01.py → missions/m01_signon.py
- `test_basic()` --calls--> `eta_hours()`  [EXTRACTED]
  tests/test_m02.py → missions/m02_course.py

## Import Cycles
- None detected.

## Communities (20 total, 3 thin omitted)

### Community 0 - "Boat"
Cohesion: 0.20
Nodes (5): Boat, available(), test_attributes(), test_can_carry(), test_available()

### Community 1 - "captain"
Cohesion: 0.19
Nodes (8): Clear it, M01 — Sign the logbook, What you're learning, Your task, captain(), test_not_empty(), test_returns_a_string(), test_single_lowercase_word()

### Community 2 - "play.py"
Cohesion: 0.24
Nodes (5): _clear(), _fingerprint(), mission_passes(), render(), watch()

### Community 3 - "m06_logistics.py"
Cohesion: 0.25
Nodes (4): fuel_cost(), profit(), test_fuel_cost(), test_profit_uses_fuel_cost()

### Community 4 - "m09_routes.py"
Cohesion: 0.25
Nodes (4): has_lane(), neighbours(), test_has_lane(), test_neighbours()

### Community 5 - "Setup on a fresh PC"
Cohesion: 0.20
Nodes (9): 1. Install Python (the language), 2. Install Git (to download the game and get updates), 3. Install VS Code (your editor + terminal in one window), 4. Get the game, 5. Open it and play — one window, Getting updates later, macOS / Linux, Setup on a fresh PC (+1 more)

### Community 6 - "eta_hours"
Cohesion: 0.36
Nodes (3): eta_hours(), test_basic(), test_fractional()

### Community 7 - "decide"
Cohesion: 0.36
Nodes (3): decide(), test_leave_when_too_heavy(), test_load_when_it_fits()

### Community 8 - "load_hold"
Cohesion: 0.36
Nodes (3): load_hold(), test_filters_by_limit(), test_order_and_empty()

### Community 9 - "value_of"
Cohesion: 0.36
Nodes (3): value_of(), test_found(), test_missing_returns_zero()

### Community 10 - "berth_for"
Cohesion: 0.36
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
Cohesion: 0.40
Nodes (4): How to play, One-time setup, The loop (repeat per mission), Tips

### Community 17 - "Cedar Shipping"
Cohesion: 0.50
Nodes (3): Cedar Shipping, Set sail, The story

## Knowledge Gaps
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Not enough signal to generate questions. This usually means the corpus has no AMBIGUOUS edges, no bridge nodes, no INFERRED relationships, and all communities are tightly cohesive. Add more files or run with --mode deep to extract richer edges._