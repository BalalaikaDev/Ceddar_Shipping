# How to play

You learn by writing a little code and **watching your harbour react** — one
small mission at a time. No prior experience needed.

## One-time setup
1. Install **Python 3.10+** from https://www.python.org/downloads/ (tick "Add
   Python to PATH" on Windows).
2. Install **VS Code** from https://code.visualstudio.com/ and, inside it, the
   **"Live Preview"** extension by Microsoft (Extensions panel → search
   "Live Preview" → Install). This is what shows the live harbour *inside* VS Code.
3. In a terminal, from this folder:
   ```
   pip install -r requirements.txt
   ```

## Set up the one-window view (do this once per session)
1. Open this folder in VS Code: `code .`
2. Open the built-in terminal (**Ctrl + `**) and start watch mode:
   ```
   python play.py --watch
   ```
   This creates **`voyage.html`** and keeps it updated every time you save.
3. In the Explorer, right-click **`voyage.html`** → **"Show Preview"**
   (Live Preview). A harbour pane opens *inside VS Code*.
4. Drag a mission file and the preview side by side. That's your cockpit.

## The loop (this is the whole game)
1. The **harbour panel** tells you the mission you're on and teaches the idea
   (what a variable is, the types, etc.).
2. Read the matching brief, e.g. `briefs/m01.md`, for the detail.
3. Edit the mission file, e.g. `missions/m01_signon.py` — replace the
   `raise NotImplementedError(...)` line with your code.
4. **Save (Ctrl + S).** Within a second the harbour redraws: your captain name
   appears on the flag, a course gets plotted, cargo loads, boats sail. The
   terminal's progress bar ticks up too.

No commands to retype, no switching windows — edit, save, watch.

## If you prefer plain tests
Everything still works the old way:
```
python play.py            # text progress
pytest tests/test_m01.py  # run one mission's checks
pytest                    # run all
```

## Tips
- **Type the answers yourself** rather than pasting — that's the point.
- Work missions **in order** (07 → 08 build on each other).
- You can't break anything. Experiment freely.
- If the preview doesn't move, check the `python play.py --watch` terminal is
  still running and that you **saved** the file.
