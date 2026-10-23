#!/usr/bin/env python3
"""Cedar Shipping — live voyage view.

Runs YOUR mission code and draws a harbour scene that reflects what it does:
your captain name on the flag, a plotted course with an ETA, cargo that loads
or stays on the dock, the hold filling, your fleet sailing. Re-run it (or let
`python play.py --watch` do it on every save) and the picture updates.

Writes voyage.html. Open that with VS Code's Live Preview and it refreshes as
you code — no terminal needed after the watcher is running.
"""
from __future__ import annotations
import html

# ---- palette (matches the radar/profile theme) ----
BG, SEA, SEA2 = "#06070f", "#0a1430", "#102a4a"
CYAN, MAG, GREEN, YELL, TEXT, DIM = "#18e0ff", "#ff2e97", "#00ff9c", "#fcee0a", "#ccd6f0", "#6e79a8"
FONT = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"


def _try(fn, *a, **k):
    """Call a student function; return (value, True) or (None, False) if it isn't done."""
    try:
        return fn(*a, **k), True
    except Exception:
        return None, False


def gather() -> dict:
    """Run each mission's code with sample inputs; record what works so far."""
    s = {"captain": None, "eta": None, "decide": None, "loaded": None,
         "value": None, "profit": None, "fleet": None, "available": None,
         "cleared": [], "total": 11}

    try:
        from missions.m01_signon import captain
        v, ok = _try(captain)
        if ok and isinstance(v, str) and v.strip():
            s["captain"] = v.strip(); s["cleared"].append(1)
    except Exception:
        pass
    try:
        from missions.m02_course import eta_hours
        v, ok = _try(eta_hours, 120, 20)     # expect 6.0
        if ok and v == 6:
            s["eta"] = v; s["cleared"].append(2)
    except Exception:
        pass
    try:
        from missions.m03_weigh import decide
        a, ok1 = _try(decide, 40, 100)       # LOAD
        b, ok2 = _try(decide, 150, 100)      # LEAVE BEHIND
        if ok1 and ok2 and a == "LOAD" and b == "LEAVE BEHIND":
            s["decide"] = True; s["cleared"].append(3)
    except Exception:
        pass
    try:
        from missions.m04_load import load_hold
        v, ok = _try(load_hold, [10, 50, 30, 80], 50)   # [10,50,30]
        if ok and v == [10, 50, 30]:
            s["loaded"] = v; s["cleared"].append(4)
    except Exception:
        pass
    try:
        from missions.m05_manifest import value_of
        v, ok = _try(value_of, {"c1": 250}, "c1")
        if ok and v == 250:
            s["value"] = v; s["cleared"].append(5)
    except Exception:
        pass
    try:
        from missions.m06_logistics import profit
        v, ok = _try(profit, 300, 50)        # 300 - 100 = 200
        if ok and v == 200:
            s["profit"] = v; s["cleared"].append(6)
    except Exception:
        pass
    try:
        from missions.m07_boat import Boat
        b = Boat("Nimbus", 100)
        if getattr(b, "name", None) == "Nimbus" and b.can_carry(50) and not b.can_carry(150):
            s["fleet"] = ["Nimbus", "Tug", "Hauler"]; s["cleared"].append(7)
            try:
                from missions.m08_dispatch import available
                fleet = [Boat("Nimbus", 100), Boat("Tug", 30), Boat("Hauler", 500)]
                v, ok = _try(available, fleet, 50)
                if ok and v == ["Nimbus", "Hauler"]:
                    s["available"] = v; s["cleared"].append(8)
            except Exception:
                pass
    except Exception:
        pass
    # m09-m11: counted for progress but not drawn yet
    for mod, fn, args, exp in [
        ("m09_routes", "neighbours", ({"A": ["B"]}, "A"), ["B"]),
        ("m10_harbour", "berth_for", ({"assignments": {"N": "B12"}}, "N"), "B12"),
        ("m11_container", "pack", ([{"weight": 10}, {"weight": 5}],), {"units": 2, "weight": 15}),
    ]:
        try:
            m = __import__(f"missions.{mod}", fromlist=[fn])
            v, ok = _try(getattr(m, fn), *args)
            if ok and v == exp:
                s["cleared"].append(int(mod[1:3]))
        except Exception:
            pass
    return s


# ---- teaching: the concept for the mission you're on now ----
LESSONS = {
    1: ("M01 · Sign the logbook", "functions, return, strings",
        [("A <b>function</b> is a named block of code you can run again and again.",),
         ("<code>return</code> hands a value back to whoever called the function.",),
         ("A <b>string</b> (type <code>str</code>) is text in quotes: <code>\"darius\"</code>.",)]),
    2: ("M02 · Plot a course", "numbers & division",
        [("Whole numbers are <code>int</code>; decimals are <code>float</code>.",),
         ("<code>/</code> divides. <code>120 / 20</code> is <code>6.0</code> (a float).",),
         ("You can <code>return</code> a calculation directly.",)]),
    3: ("M03 · Weigh the cargo", "booleans & if/else",
        [("A comparison like <code>weight &lt;= capacity</code> gives a <b>bool</b>: <code>True</code> or <code>False</code>.",),
         ("<code>if</code> / <code>else</code> picks what to do based on that bool.",),
         ("Strings are case-sensitive: <code>\"LOAD\"</code> ≠ <code>\"Load\"</code>.",)]),
    4: ("M04 · Load the hold", "lists & loops",
        [("A <b>list</b> holds many items in order: <code>[10, 50, 30]</code>.",),
         ("A <code>for</code> loop runs once per item.",),
         ("Build a new list with <code>.append(x)</code> as you go.",)]),
    5: ("M05 · Read the manifest", "dictionaries",
        [("A <b>dict</b> maps keys to values: <code>{\"c1\": 250}</code>.",),
         ("<code>d.get(key, 0)</code> returns a default instead of crashing on a missing key.",)]),
    6: ("M06 · Count the cost", "variables & reuse",
        [("A <b>variable</b> is a name for a value: <code>FUEL_PRICE = 2</code>.",),
         ("One function can <b>call another</b> — reuse <code>fuel_cost()</code>, don't repeat it.",)]),
    7: ("M07 · Build a boat", "classes & objects",
        [("A <b>class</b> is a blueprint; an <b>object</b> is one boat made from it.",),
         ("<code>__init__</code> stores its data; <code>self</code> means <i>this</i> boat.",),
         ("A <b>method</b> is a function that belongs to the object.",)]),
    8: ("M08 · Dispatch the fleet", "looping over objects",
        [("Loop over a list of <b>objects</b> and call each one's method.",),
         ("Collect the ones that pass into a new list.",)]),
    9: ("M09 · The route network", "graphs (the Neo4j idea)",
        [("A <b>dict of lists</b> is a graph: each port → the ports it links to.",)]),
    10: ("M10 · Radio the harbour", "nested data / APIs",
         [("Reach into a dict inside a dict — the shape an API returns as JSON.",)]),
    11: ("M11 · Pack a container", "the Docker idea",
         [("Sum over a list of dicts; return a new dict. One standard unit.",)]),
}


def _lesson(cleared):
    nxt = next((i for i in range(1, 12) if i not in cleared), 11)
    return nxt, LESSONS[nxt]


def _crate(x, y, c=YELL, w=26):
    return (f'<g><rect x="{x}" y="{y}" width="{w}" height="{w*0.7:.0f}" rx="3" '
            f'fill="{c}" fill-opacity="0.85" stroke="{BG}"/>'
            f'<line x1="{x}" y1="{y}" x2="{x+w}" y2="{y+w*0.7:.0f}" stroke="{BG}" stroke-opacity="0.4"/></g>')


def scene(s) -> str:
    """The animated harbour SVG, reflecting state s."""
    W, H = 560, 380
    o = [f'<svg viewBox="0 0 {W} {H}" width="100%" font-family="{FONT}">']
    o.append(f'<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">'
             f'<stop offset="0" stop-color="{BG}"/><stop offset="1" stop-color="{SEA}"/></linearGradient>'
             f'<filter id="g"><feGaussianBlur stdDeviation="2.4" result="b"/>'
             f'<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>')
    o.append(f'<rect width="{W}" height="{H}" rx="12" fill="url(#sky)"/>')
    sea_y = 250
    o.append(f'<rect y="{sea_y}" width="{W}" height="{H-sea_y}" fill="{SEA2}"/>')
    # waves
    for i, wy in enumerate((sea_y, sea_y+18, sea_y+36)):
        o.append(f'<path d="M0,{wy} q35,-8 70,0 t70,0 t70,0 t70,0 t70,0 t70,0 t70,0 t70,0" '
                 f'fill="none" stroke="{CYAN}" stroke-opacity="{0.22-i*0.05:.2f}">'
                 f'<animateTransform attributeName="transform" type="translate" '
                 f'values="0 0;-70 0;0 0" dur="{3+i}s" repeatCount="indefinite"/></path>')
    # ports A and B
    for px, lab in ((40, "PORT A"), (W-90, "PORT B")):
        o.append(f'<rect x="{px}" y="{sea_y-34}" width="50" height="34" fill="{DIM}" fill-opacity="0.35"/>'
                 f'<text x="{px+25}" y="{sea_y-42}" text-anchor="middle" font-size="10" fill="{DIM}">{lab}</text>')

    # course line + ETA (M02)
    if s["eta"] is not None:
        o.append(f'<line x1="95" y1="{sea_y-6}" x2="{W-95}" y2="{sea_y-6}" stroke="{CYAN}" '
                 f'stroke-dasharray="6 6" stroke-opacity="0.7"/>'
                 f'<text x="{W/2}" y="{sea_y-14}" text-anchor="middle" font-size="12" fill="{CYAN}">'
                 f'ETA {s["eta"]:.0f} h</text>')

    # the boat (sails across once a course is plotted)
    bx = 240
    boat = [f'<g filter="url(#g)">']
    # hull
    boat.append(f'<path d="M-34,8 L34,8 L26,26 L-26,26 Z" fill="#20314f" stroke="{CYAN}" stroke-opacity="0.6"/>')
    # mast + flag with captain name (M01)
    cap = s["captain"] or "unsigned"
    flagcol = GREEN if s["captain"] else DIM
    boat.append(f'<line x1="0" y1="8" x2="0" y2="-34" stroke="{DIM}"/>')
    boat.append(f'<path d="M0,-34 L46,-27 L0,-20 Z" fill="{flagcol}" fill-opacity="0.85">'
                f'<animateTransform attributeName="transform" type="skewX" values="0;8;0;-6;0" '
                f'dur="2.5s" repeatCount="indefinite"/></path>')
    boat.append(f'<text x="6" y="-25" font-size="10" fill="{BG}" font-weight="700">{html.escape(cap)[:10]}</text>')
    # cargo on deck: crates that loaded (M03 gates one; M04 fills the hold)
    n_crates = 0
    if s["loaded"] is not None:
        n_crates = len(s["loaded"])
    elif s["decide"]:
        n_crates = 1
    for i in range(min(n_crates, 3)):
        boat.append(_crate(-24 + i*22, -4, YELL, 18))
    boat.append('</g>')
    # bobbing boat group, optionally sailing
    anim = ''
    if s["eta"] is not None:
        anim = (f'<animateTransform attributeName="transform" type="translate" additive="sum" '
                f'values="-120 0;120 0;-120 0" dur="10s" repeatCount="indefinite"/>')
    o.append(f'<g transform="translate({bx},{sea_y})">'
             f'<animateTransform attributeName="transform" type="translate" additive="sum" '
             f'values="0 0;0 -4;0 0" dur="2.5s" repeatCount="indefinite"/>{anim}'
             + "".join(boat) + '</g>')

    # a crate left on the dock when nothing loads yet
    if n_crates == 0:
        o.append(_crate(150, sea_y-24, DIM, 22))
        o.append(f'<text x="161" y="{sea_y-28}" text-anchor="middle" font-size="9" fill="{DIM}">cargo waits</text>')

    # coins / value (M05) + profit (M06)
    hud = []
    if s["value"] is not None:
        hud.append(f'◈ manifest {s["value"]}')
    if s["profit"] is not None:
        hud.append(f'▲ profit {s["profit"]}')
    if hud:
        o.append(f'<text x="16" y="28" font-size="12" fill="{YELL}">{"   ".join(hud)}</text>')

    # the fleet (M07/M08)
    if s["fleet"]:
        o.append(f'<text x="16" y="{H-44}" font-size="10" fill="{DIM}">FLEET</text>')
        for i, name in enumerate(s["fleet"]):
            fx = 20 + i*110
            lit = s["available"] is not None and name in s["available"]
            col = GREEN if lit else DIM
            o.append(f'<path d="M{fx},{H-20} l44,0 l-6,12 l-32,0 z" fill="#20314f" stroke="{col}"/>'
                     f'<text x="{fx+22}" y="{H-24}" text-anchor="middle" font-size="9" fill="{col}">{name}</text>')
        if s["available"] is not None:
            o.append(f'<text x="{W-16}" y="{H-44}" text-anchor="end" font-size="9" fill="{GREEN}">'
                     f'can carry 50t ✓</text>')

    o.append('</svg>')
    return "".join(o)


def render(s) -> str:
    nxt, (title, concept, points) = _lesson(s["cleared"])
    cleared = sorted(set(s["cleared"]))
    bar = "".join(f'<span class="pip {"on" if i in cleared else ""}"></span>' for i in range(1, 12))
    pts = "".join(f"<li>{p[0]}</li>" for p in points)
    done = len(cleared) == s["total"]
    headline = ("Every mission cleared — the fleet is yours." if done
                else f"Now: <b>{title}</b>")
    return f"""<!doctype html><html><head><meta charset="utf-8"><title>Cedar Shipping</title>
<style>
  :root {{ color-scheme: dark; }}
  body {{ margin:0; background:{BG}; color:{TEXT}; font-family:{FONT};
         display:flex; gap:16px; padding:16px; flex-wrap:wrap; }}
  .scene {{ flex:1 1 440px; min-width:320px; }}
  .panel {{ flex:1 1 300px; min-width:260px; background:#0a0b1a; border:1px solid #1b2348;
           border-radius:12px; padding:16px 18px; }}
  h1 {{ font-size:15px; letter-spacing:1px; color:{CYAN}; margin:0 0 2px; }}
  .sub {{ color:{DIM}; font-size:11px; margin-bottom:14px; }}
  .now {{ font-size:13px; margin:0 0 4px; }}
  .concept {{ color:{MAG}; font-size:11px; text-transform:uppercase; letter-spacing:1px; margin-bottom:8px; }}
  ul {{ padding-left:18px; margin:6px 0 14px; }}
  li {{ margin:7px 0; font-size:13px; line-height:1.45; }}
  code {{ background:#11132b; color:{GREEN}; padding:1px 5px; border-radius:4px; font-size:12px; }}
  .steps {{ font-size:11px; color:{DIM}; border-top:1px solid #1b2348; padding-top:10px; line-height:1.6; }}
  .bar {{ display:flex; gap:5px; margin:10px 0; }}
  .pip {{ width:16px; height:7px; border-radius:2px; background:#1b2348; }}
  .pip.on {{ background:{GREEN}; }}
  b {{ color:{TEXT}; }} i {{ color:{CYAN}; }}
</style></head>
<body>
  <div class="scene">{scene(s)}</div>
  <div class="panel">
    <h1>CEDAR SHIPPING</h1>
    <div class="sub">live voyage — updates when you save a mission file</div>
    <div class="bar">{bar}</div>
    <div class="now">{headline}</div>
    <div class="concept">{html.escape(concept)}</div>
    <ul>{pts}</ul>
    <div class="steps">
      1 · read <code>briefs/m{nxt:02d}.md</code><br>
      2 · edit <code>missions/m{nxt:02d}_*.py</code> — replace the TODO line<br>
      3 · <b>save</b> — watch this picture update<br>
      cleared {len(cleared)}/{s['total']}
    </div>
  </div>
</body></html>"""


if __name__ == "__main__":
    import sys
    out = sys.argv[1] if len(sys.argv) > 1 else "voyage.html"
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(render(gather()))
    print(f"wrote {out}")
