# How to play

You learn by making failing tests pass — one small mission at a time. No prior
experience needed.

## One-time setup
1. Install **Python 3.10+** from https://www.python.org/downloads/ (tick "Add
   Python to PATH" on Windows).
2. In a terminal, from this folder, install the test runner:
   ```
   pip install -r requirements.txt
   ```

## The loop (repeat per mission)
1. See where you are:
   ```
   python play.py
   ```
2. Read the next brief, e.g. `briefs/m01.md` (Sign the logbook).
3. Open the matching file, e.g. `missions/m01_identify.py`, and replace the
   `TODO` / `raise NotImplementedError` line with your code.
4. Run that mission's test:
   ```
   pytest tests/test_m01.py
   ```
   - **Red** (a failure) tells you what's expected — read the message, adjust.
   - **Green** = cleared. Move to the next mission.

## Tips
- Run **all** tests with just `pytest`.
- Stuck? The brief for each mission shows the shape of the answer. Type it out
  yourself rather than pasting — that's the point.
- You can't break anything. Experiment freely.
