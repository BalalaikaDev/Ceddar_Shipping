#!/usr/bin/env python3
"""Cedar Shipping — progress console.

    python play.py            show the dispatch log once
    python play.py --watch    live mode: re-checks automatically every time you
                              save a mission file (no commands to re-type)
"""
import os
import subprocess
import sys
import time
from pathlib import Path

CYAN, GREEN, DIM, MAG, YELL, RESET = (
    "\033[36m", "\033[92m", "\033[90m", "\033[95m", "\033[93m", "\033[0m")

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
    # run via "-m pytest" so the project root is importable no matter what
    r = subprocess.run([sys.executable, "-m", "pytest", str(test)],
                       capture_output=True)
    return r.returncode == 0


def render() -> int:
    results = [(n, t, c, mission_passes(n)) for n, t, c in MISSIONS]
    cleared = sum(1 for _, _, _, ok in results if ok)
    total = len(results)

    print(f"{CYAN}╔═══════════════════════════════════════════╗{RESET}")
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
              f"{CYAN}missions/m{nxt}_*.py{RESET}\n")
    return cleared


def _clear():
    os.system("cls" if os.name == "nt" else "clear")


def _fingerprint() -> float:
    """Latest change time across mission + test files — cheap change detector."""
    latest = 0.0
    for folder in ("missions", "tests"):
        for p in Path(folder).glob("*.py"):
            latest = max(latest, p.stat().st_mtime)
    return latest


def watch():
    last = -1.0
    print(f"{YELL}watch mode — edit a mission, hit save, and this updates itself. "
          f"Ctrl+C to stop.{RESET}")
    time.sleep(1.0)
    try:
        while True:
            fp = _fingerprint()
            if fp != last:
                last = fp
                _clear()
                render()
                print(f"  {DIM}watching for changes… (Ctrl+C to stop){RESET}")
            time.sleep(1.0)
    except KeyboardInterrupt:
        print(f"\n{DIM}stopped watching. fair winds, captain.{RESET}")


if __name__ == "__main__":
    if "--watch" in sys.argv or "-w" in sys.argv:
        watch()
    else:
        render()
