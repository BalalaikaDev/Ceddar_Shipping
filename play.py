#!/usr/bin/env python3
"""Operator Training — progress console.

Runs each mission's tests and shows how far you've cleared.
    python play.py
"""
import subprocess
import sys
from pathlib import Path

CYAN, GREEN, DIM, MAG, RESET = "\033[36m", "\033[92m", "\033[90m", "\033[95m", "\033[0m"

MISSIONS = [
    # Act I — Deckhand
    ("01", "Sign the logbook", "functions & return"),
    ("02", "Plot a course", "numbers & division"),
    ("03", "Weigh the cargo", "if / else"),
    ("04", "Load the hold", "loops & lists"),
    ("05", "Read the manifest", "dictionaries"),
    # Act II — The Fleet
    ("06", "Count the cost", "functions calling functions"),
    ("07", "Build a boat", "your first class"),
    ("08", "Dispatch the fleet", "looping over objects"),
    ("09", "The route network", "graphs (the Neo4j idea)"),
    ("10", "Radio the harbour", "nested data / APIs (FastAPI)"),
    ("11", "Pack a container", "the Docker idea"),
]


def mission_passes(num: str) -> bool:
    test = Path("tests") / f"test_m{num}.py"
    if not test.exists():
        return False
    r = subprocess.run([sys.executable, "-m", "pytest", str(test)],
                       capture_output=True)
    return r.returncode == 0


def main() -> int:
    results = [(n, t, c, mission_passes(n)) for n, t, c in MISSIONS]
    cleared = sum(1 for _, _, _, ok in results if ok)
    total = len(results)

    print(f"\n{CYAN}╔═══════════════════════════════════════════╗{RESET}")
    print(f"{CYAN}║       HARBOUR MASTER // DISPATCH LOG       ║{RESET}")
    print(f"{CYAN}╚═══════════════════════════════════════════╝{RESET}\n")
    for n, title, concept, ok in results:
        mark = f"{GREEN}● CLEARED{RESET}" if ok else f"{DIM}○ locked {RESET}"
        name = f"{GREEN}{title}{RESET}" if ok else f"{title}"
        print(f"  {mark}  M{n}  {name}  {DIM}— {concept}{RESET}")

    bar_len = 30
    filled = int(bar_len * cleared / total) if total else 0
    bar = f"{GREEN}{'█' * filled}{DIM}{'░' * (bar_len - filled)}{RESET}"
    print(f"\n  progress  {bar}  {MAG}{cleared}/{total}{RESET}\n")
    if cleared == total:
        print(f"  {GREEN}Every mission cleared, admiral. The fleet is yours.{RESET}\n")
    else:
        nxt = next(n for n, _, _, ok in results if not ok)
        print(f"  next up: {CYAN}briefs/m{nxt}.md{RESET}  →  edit "
              f"{CYAN}missions/m{nxt}_*.py{RESET}  →  "
              f"{CYAN}pytest tests/test_m{nxt}.py{RESET}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
