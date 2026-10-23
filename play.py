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
    ("01", "Identify", "variables & return"),
    ("02", "Triangulate", "numbers & arithmetic"),
    ("03", "Threat check", "if / else"),
    ("04", "Port scan", "loops & lists"),
    ("05", "Pull a record", "dictionaries"),
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
    print(f"{CYAN}║        OPERATOR TRAINING // CONSOLE        ║{RESET}")
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
        print(f"  {GREEN}All missions cleared. Stand by for the next drop.{RESET}\n")
    else:
        nxt = next(n for n, _, _, ok in results if not ok)
        print(f"  next up: {CYAN}briefs/m{nxt}.md{RESET}  →  edit "
              f"{CYAN}missions/m{nxt}_*.py{RESET}  →  "
              f"{CYAN}pytest tests/test_m{nxt}.py{RESET}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
