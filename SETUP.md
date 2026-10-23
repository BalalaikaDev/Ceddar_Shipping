# Setup on a fresh PC

Zero to playing in ~10 minutes. Steps are for **Windows**; macOS/Linux notes at the end.

## 1. Install Python (the language)
- Download Python **3.11 or newer**: https://www.python.org/downloads/
- Run the installer. **Tick "Add python.exe to PATH"** on the first screen (important!), then "Install Now".
- Check it worked — open a new terminal (PowerShell) and run:
  ```
  python --version
  ```
  You should see `Python 3.11.x` (or newer).

## 2. Install Git (to download the game and get updates)
- Download: https://git-scm.com/download/win
- Run the installer; the default options are fine.
- Check:
  ```
  git --version
  ```

## 3. Install VS Code (your editor + terminal in one window)
- Download: https://code.visualstudio.com/
- During install, tick **"Add to PATH"** and **"Open with Code"** (both boxes).
- Open VS Code once, go to the Extensions panel (the squares icon on the left),
  search **"Python"** (by Microsoft) and install it.

## 4. Get the game
In a terminal, pick a folder you like (e.g. your `dev` folder) and run:
```
git clone https://github.com/BalalaikaDev/Ceddar_Shipping.git
cd Ceddar_Shipping
pip install -r requirements.txt
```

## 5. Open it and play — one window
```
code .
```
That opens the whole project in VS Code. Then:
- Open the built-in terminal: **Ctrl + `** (the key above Tab).
- Start live mode:
  ```
  python play.py --watch
  ```
- Now just **edit a mission file and save (Ctrl+S)** — the terminal redraws your
  progress automatically. No commands to retype.

The loop: read `briefs/m01.md` → edit `missions/m01_signon.py` → save → watch it
clear → next mission.

## Getting updates later
New missions and fixes land in the repo. To pull them in:
```
git pull
```
(Your own edits to mission files are kept.)

## macOS / Linux
- Python: `brew install python` (mac) or your package manager; or python.org.
- Git and VS Code: same sites as above, or your package manager.
- Everything else is identical, except the VS Code terminal shortcut may be
  **Cmd + `** on macOS, and use `python3` if `python` isn't found.

## Troubleshooting
- **`python` not found** → you missed "Add to PATH" in step 1. Re-run the Python
  installer and tick it, or reinstall.
- **`ModuleNotFoundError: No module named 'missions'`** → run commands from inside
  the `Ceddar_Shipping` folder (where `play.py` is).
- **You end up at a `>>>` prompt** → that's Python's interactive shell. Type
  `exit()` and press Enter to get back to the normal terminal.
