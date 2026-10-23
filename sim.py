#!/usr/bin/env python3
"""Cedar Shipping — live voyage view.

Runs YOUR mission code and draws a harbour that reflects what it does — and what
it gets WRONG: your captain on the flag, a plotted course + ETA, cargo loading,
an overloaded boat listing and sinking, your fleet sailing. Re-run it (or let
`python play.py --watch` do it on save) and the picture updates.

Writes voyage.html. Open it with VS Code's Live Preview and it refreshes as you
code — no terminal needed after the watcher is running.
"""
from __future__ import annotations
import html

BG, SEA, SEA2 = "#06070f", "#0a1430", "#102a4a"
CYAN, MAG, GREEN, YELL, TEXT, DIM = "#18e0ff", "#ff2e97", "#00ff9c", "#fcee0a", "#ccd6f0", "#6e79a8"
RED, AMBER = "#ff3b5c", "#ff8c00"
FONT = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"


def _call(fn, *a):
    try:
        return fn(*a), True
    except Exception:
        return None, False


def gather() -> dict:
    """Run each mission; record done / attempted-wrong / untouched + failure signals."""
    s = {"status": {}, "captain": None, "captain_bad": None, "eta": None, "eta_bad": None,
         "cargo": 0, "overload": False, "value": None, "profit": None,
         "fleet": None, "available": None, "routes": None, "berth": None,
         "container": None, "total": 11}
    st = s["status"]

    # M01 — captain name
    try:
        from missions.m01_signon import captain
        v, ok = _call(captain)
        if ok and isinstance(v, str):
            if v.strip() == "":
                st[1] = "todo"
            elif v == v.lower() and " " not in v:
                st[1] = "done"; s["captain"] = v.strip()
            else:
                st[1] = "wrong"; s["captain_bad"] = v
        else:
            st[1] = "todo"
    except Exception:
        st[1] = "todo"

    # M02 — ETA
    try:
        from missions.m02_course import eta_hours
        v, ok = _call(eta_hours, 120, 20)      # expect 6
        if ok and v == 6:
            st[2] = "done"; s["eta"] = v
        elif ok and v not in (0, None):
            st[2] = "wrong"; s["eta_bad"] = v
        else:
            st[2] = "todo"
    except Exception:
        st[2] = "todo"

    # M03 — decide (overload if it would load a too-heavy crate)
    try:
        from missions.m03_weigh import decide
        a, ok1 = _call(decide, 40, 100)        # LOAD
        b, ok2 = _call(decide, 150, 100)       # LEAVE BEHIND
        if ok1 and ok2 and a == "LOAD" and b == "LEAVE BEHIND":
            st[3] = "done"
        elif (ok1 and a not in ("", None)) or (ok2 and b not in ("", None)):
            st[3] = "wrong"
        else:
            st[3] = "todo"
        if ok2 and b == "LOAD":                # loading something over capacity
            s["overload"] = True
        if st.get(3) == "done" and not s["overload"]:
            s["cargo"] = max(s["cargo"], 1)
    except Exception:
        st[3] = "todo"

    # M04 — load_hold (overload if a crate exceeds the limit)
    try:
        from missions.m04_load import load_hold
        v, ok = _call(load_hold, [10, 50, 30, 80], 50)
        if ok and isinstance(v, list):
            if v == [10, 50, 30]:
                st[4] = "done"; s["cargo"] = 3
            elif v:
                st[4] = "wrong"; s["cargo"] = min(len(v), 4)
                if any(c > 50 for c in v):
                    s["overload"] = True
            else:
                st[4] = "todo"
        else:
            st[4] = "todo"
    except Exception:
        st[4] = "todo"

    # M05 / M06 — value, profit
    for n, mod, fn, args, exp, bad in [
        (5, "m05_manifest", "value_of", ({"c1": 250}, "c1"), 250, 0),
        (6, "m06_logistics", "profit", (300, 50), 200, 0),
    ]:
        try:
            m = __import__(f"missions.{mod}", fromlist=[fn])
            v, ok = _call(getattr(m, fn), *args)
            if ok and v == exp:
                st[n] = "done"; s["value" if n == 5 else "profit"] = exp
            elif ok and v != bad:
                st[n] = "wrong"
            else:
                st[n] = "todo"
        except Exception:
            st[n] = "todo"

    # M07 / M08 — class + fleet dispatch
    try:
        from missions.m07_boat import Boat
        b = Boat("Nimbus", 100)
        if getattr(b, "name", None) == "Nimbus" and b.capacity == 100 \
                and b.can_carry(50) and not b.can_carry(150):
            st[7] = "done"; s["fleet"] = ["Nimbus", "Tug", "Hauler"]
            try:
                from missions.m08_dispatch import available
                fleet = [Boat("Nimbus", 100), Boat("Tug", 30), Boat("Hauler", 500)]
                v, ok = _call(available, fleet, 50)
                if ok and v == ["Nimbus", "Hauler"]:
                    st[8] = "done"; s["available"] = v
                elif ok and v:
                    st[8] = "wrong"
                else:
                    st[8] = "todo"
            except Exception:
                st[8] = "todo"
        else:
            st[7] = "todo"
    except Exception:
        st[7] = "todo"

    # M09 — route network (dict of lists)
    try:
        from missions.m09_routes import neighbours, has_lane
        net = {"A": ["B", "C"], "B": ["A"], "C": []}
        nb, ok1 = _call(neighbours, net, "A")
        hl, ok2 = _call(has_lane, net, "A", "B")
        if ok1 and ok2 and nb == ["B", "C"] and hl is True:
            st[9] = "done"; s["routes"] = net
        elif (ok1 and nb) or (ok2 and hl):
            st[9] = "wrong"
        else:
            st[9] = "todo"
    except Exception:
        st[9] = "todo"

    # M10 — berth assignment (nested dict)
    try:
        from missions.m10_harbour import berth_for
        resp = {"status": "ok", "assignments": {"Nimbus": "B12"}}
        v, ok = _call(berth_for, resp, "Nimbus")
        if ok and v == "B12":
            st[10] = "done"; s["berth"] = "B12"
        elif ok and v not in ("NONE", None, ""):
            st[10] = "wrong"
        else:
            st[10] = "todo"
    except Exception:
        st[10] = "todo"

    # M11 — pack a container
    try:
        from missions.m11_container import pack
        v, ok = _call(pack, [{"weight": 10}, {"weight": 5}])
        if ok and v == {"units": 2, "weight": 15}:
            st[11] = "done"; s["container"] = v
        elif ok and v not in ({"units": 0, "weight": 0}, None):
            st[11] = "wrong"
        else:
            st[11] = "todo"
    except Exception:
        st[11] = "todo"

    s["cleared"] = [i for i in range(1, 12) if st.get(i) == "done"]
    return s


LESSONS = {
    1: ("M01 · Sign the logbook", "functions, return, strings",
        ["A <b>variable</b> is a name for a value: <code>name = \"darius\"</code>.",
         "A <b>string</b> (type <code>str</code>) is text in quotes.",
         "<code>return</code> hands a value back."],
        "a captain name is lowercase, one word, in quotes."),
    2: ("M02 · Plot a course", "numbers & division",
        ["Whole numbers are <code>int</code>; decimals are <code>float</code>.",
         "<code>/</code> divides: <code>120 / 20</code> → <code>6.0</code>.",
         "Store it in a variable, then <code>return</code> it."],
        "time = distance / speed — check your maths."),
    3: ("M03 · Weigh the cargo", "booleans & if/else",
        ["<code>weight &lt;= capacity</code> gives a <b>bool</b>: <code>True</code>/<code>False</code>.",
         "<code>if</code>/<code>else</code> picks the label from that bool.",
         "Caps matter: <code>\"LOAD\"</code> ≠ <code>\"Load\"</code>."],
        "over capacity must be LEFT BEHIND — check &lt;= not &gt;=."),
    4: ("M04 · Load the hold", "lists & loops",
        ["A <b>list</b> holds items in order; build one with <code>.append()</code>.",
         "A <code>for</code> loop runs once per crate.",
         "Only keep crates within the limit."],
        "you loaded a crate heavier than the limit."),
    5: ("M05 · Read the manifest", "dictionaries",
        ["A <b>dict</b> maps keys→values: <code>{\"c1\": 250}</code>.",
         "<code>d.get(key, 0)</code> avoids a crash on a missing key."],
        "use manifest.get(crate_id, 0)."),
    6: ("M06 · Count the cost", "variables & reuse",
        ["A <b>constant</b> is a variable you don't change: <code>FUEL_PRICE = 2</code>.",
         "One function can <b>call another</b> — reuse <code>fuel_cost()</code>."],
        "profit = cargo_value − fuel_cost(distance)."),
    7: ("M07 · Build a boat", "classes & objects",
        ["A <b>class</b> is a blueprint; an <b>object</b> is one boat.",
         "<code>self</code> means <i>this</i> boat; attributes hold its data.",
         "A <b>method</b> is a function on the object."],
        "store name and capacity on self; compare weight to self.capacity."),
    8: ("M08 · Dispatch the fleet", "looping over objects",
        ["Loop over a list of <b>objects</b> and call each one's method.",
         "Collect the names that pass into a new list."],
        "keep a boat's name only when boat.can_carry(weight)."),
    9: ("M09 · The route network", "graphs (the Neo4j idea)",
        ["A <b>dict of lists</b> is a graph: each port → the ports it links to."],
        "neighbours = lanes.get(port, [])."),
    10: ("M10 · Radio the harbour", "nested data / APIs",
         ["Reach into a dict inside a dict — the shape an API returns as JSON."],
         "response.get('assignments', {}).get(boat_name, 'NONE')."),
    11: ("M11 · Pack a container", "the Docker idea",
         ["Sum over a list of dicts; return a new dict."],
         "count the items and add up their 'weight'."),
}


def _next(s):
    return next((i for i in range(1, 12) if s["status"].get(i) != "done"), 11)


def _crate(x, y, c=YELL, w=20):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{w*0.7:.0f}" rx="3" '
            f'fill="{c}" fill-opacity="0.9" stroke="{BG}"/>')


def scene(s) -> str:
    W, H, sea_y = 560, 380, 250
    over = s["overload"]
    o = [f'<svg viewBox="0 0 {W} {H}" width="100%" font-family="{FONT}">']
    o.append(f'<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">'
             f'<stop offset="0" stop-color="{BG}"/><stop offset="1" stop-color="{SEA}"/></linearGradient>'
             f'<filter id="g"><feGaussianBlur stdDeviation="2.4" result="b"/>'
             f'<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>')
    o.append(f'<rect width="{W}" height="{H}" rx="12" fill="url(#sky)"/>')
    o.append(f'<rect y="{sea_y}" width="{W}" height="{H-sea_y}" fill="{SEA2}"/>')
    for i, wy in enumerate((sea_y, sea_y+18, sea_y+36)):
        o.append(f'<path d="M0,{wy} q35,-8 70,0 t70,0 t70,0 t70,0 t70,0 t70,0 t70,0 t70,0" '
                 f'fill="none" stroke="{CYAN}" stroke-opacity="{0.22-i*0.05:.2f}">'
                 f'<animateTransform attributeName="transform" type="translate" '
                 f'values="0 0;-70 0;0 0" dur="{3+i}s" repeatCount="indefinite"/></path>')
    for px, lab in ((40, "PORT A"), (W-90, "PORT B")):
        o.append(f'<rect x="{px}" y="{sea_y-34}" width="50" height="34" fill="{DIM}" fill-opacity="0.35"/>'
                 f'<text x="{px+25}" y="{sea_y-42}" text-anchor="middle" font-size="10" fill="{DIM}">{lab}</text>')

    # course + ETA (M02): cyan when right, red when wrong
    if s["eta"] is not None or s["eta_bad"] is not None:
        col = CYAN if s["eta"] is not None else RED
        val = s["eta"] if s["eta"] is not None else s["eta_bad"]
        mark = "" if s["eta"] is not None else " ✗"
        o.append(f'<line x1="95" y1="{sea_y-6}" x2="{W-95}" y2="{sea_y-6}" stroke="{col}" '
                 f'stroke-dasharray="6 6" stroke-opacity="0.7"/>'
                 f'<text x="{W/2}" y="{sea_y-14}" text-anchor="middle" font-size="12" fill="{col}">'
                 f'ETA {val:g} h{mark}</text>')

    # boat
    tilt = 14 if over else 0
    sink = 16 if over else 0
    boat = []
    hull_stroke = RED if over else (CYAN if s["captain"] else DIM)
    boat.append(f'<path d="M-34,8 L34,8 L26,26 L-26,26 Z" fill="#20314f" stroke="{hull_stroke}" stroke-opacity="0.8"/>')
    boat.append(f'<line x1="0" y1="8" x2="0" y2="-34" stroke="{DIM}"/>')
    cap = s["captain"] or (s["captain_bad"] or "unsigned")
    flagcol = GREEN if s["captain"] else (AMBER if s["captain_bad"] else DIM)
    boat.append(f'<path d="M0,-34 L46,-27 L0,-20 Z" fill="{flagcol}" fill-opacity="0.9">'
                f'<animateTransform attributeName="transform" type="skewX" values="0;8;0;-6;0" '
                f'dur="2.5s" repeatCount="indefinite"/></path>')
    boat.append(f'<text x="6" y="-25" font-size="10" fill="{BG}" font-weight="700">{html.escape(cap)[:10]}</text>')
    # cargo on deck
    ncr = min(s["cargo"], 4)
    for i in range(ncr):
        boat.append(_crate(-26 + i*17, -6, RED if over else YELL, 15))
    if over:
        boat.append(_crate(-10, -24, RED, 24))  # the oversized crate that broke it
    boat = (f'<g transform="translate(240,{sea_y+sink}) rotate({tilt})">'
            f'<animateTransform attributeName="transform" type="translate" additive="sum" '
            f'values="0 0;0 -3;0 0" dur="2.5s" repeatCount="indefinite"/>' + "".join(boat) + '</g>')
    o.append(f'<g filter="url(#g)">{boat}</g>')
    if over:
        o.append(f'<text x="240" y="{sea_y-54}" text-anchor="middle" font-size="13" fill="{RED}" '
                 f'font-weight="700">⚠ OVERLOADED</text>')
    elif ncr == 0:
        o.append(_crate(150, sea_y-22, DIM, 20))
        o.append(f'<text x="160" y="{sea_y-28}" text-anchor="middle" font-size="9" fill="{DIM}">cargo waits</text>')

    # HUD
    hud = []
    if s["value"] is not None:
        hud.append(f'◈ manifest {s["value"]}')
    if s["profit"] is not None:
        hud.append(f'▲ profit {s["profit"]}')
    if hud:
        o.append(f'<text x="16" y="28" font-size="12" fill="{YELL}">{"   ".join(hud)}</text>')

    # fleet (M07/M08)
    if s["fleet"]:
        o.append(f'<text x="16" y="{H-44}" font-size="10" fill="{DIM}">FLEET</text>')
        for i, name in enumerate(s["fleet"]):
            fx = 20 + i*110
            lit = s["available"] is not None and name in s["available"]
            col = GREEN if lit else DIM
            o.append(f'<path d="M{fx},{H-20} l44,0 l-6,12 l-32,0 z" fill="#20314f" stroke="{col}"/>'
                     f'<text x="{fx+22}" y="{H-24}" text-anchor="middle" font-size="9" fill="{col}">{name}</text>')
        if s["available"] is not None:
            o.append(f'<text x="{W-16}" y="{H-44}" text-anchor="end" font-size="9" fill="{GREEN}">can carry 50t ✓</text>')

    # ---- Act II overlays ----
    # M09 — route network (dict of lists drawn as a little graph)
    if s["routes"]:
        nodes = {"A": (46, 70), "B": (118, 52), "C": (104, 116)}
        for a, links in s["routes"].items():
            for b in links:
                if a in nodes and b in nodes:
                    x1, y1 = nodes[a]; x2, y2 = nodes[b]
                    o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{CYAN}" stroke-opacity="0.55"/>')
        for name, (x, y) in nodes.items():
            o.append(f'<circle cx="{x}" cy="{y}" r="10" fill="#11132b" stroke="{CYAN}" filter="url(#g)"/>'
                     f'<text x="{x}" y="{y+4}" text-anchor="middle" font-size="10" fill="{CYAN}">{name}</text>')
        o.append(f'<text x="46" y="38" font-size="9" fill="{DIM}" letter-spacing="1">ROUTE NET</text>')

    # M10 — berth assignment at Port B (nested dict → where you dock)
    if s["berth"]:
        o.append(f'<text x="{W-65}" y="{sea_y-50}" text-anchor="middle" font-size="11" fill="{GREEN}" '
                 f'filter="url(#g)">⚓ {html.escape(str(s["berth"]))}</text>')

    # M11 — a packed container on the dock (standard unit)
    if s["container"]:
        c = s["container"]
        cx, cy = 128, sea_y - 20
        for i in range(2):
            o.append(f'<rect x="{cx}" y="{cy-i*13}" width="34" height="12" rx="1" fill="{GREEN}" '
                     f'fill-opacity="0.85" stroke="{BG}"/>')
            for gx in (cx+11, cx+23):
                o.append(f'<line x1="{gx}" y1="{cy-i*13}" x2="{gx}" y2="{cy-i*13+12}" stroke="{BG}" stroke-opacity="0.4"/>')
        o.append(f'<text x="{cx+17}" y="{cy-32}" text-anchor="middle" font-size="9" fill="{GREEN}">'
                 f'{c["units"]}u · {c["weight"]}t</text>')

    o.append('</svg>')
    return "".join(o)


def render(s) -> str:
    nxt = _next(s)
    title, concept, points, hint = LESSONS[nxt]
    cleared = s["cleared"]
    bar = "".join(f'<span class="pip {"on" if i in cleared else ""}"></span>' for i in range(1, 12))
    pts = "".join(f"<li>{p}</li>" for p in points)
    done = len(cleared) == s["total"]
    attempted_wrong = s["status"].get(nxt) == "wrong"
    nudge = (f'<div class="bad">✗ not quite — {hint}</div>' if attempted_wrong else "")
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
  .sub {{ color:{DIM}; font-size:11px; margin-bottom:12px; }}
  .now {{ font-size:13px; margin:2px 0 4px; }}
  .concept {{ color:{MAG}; font-size:11px; text-transform:uppercase; letter-spacing:1px; margin-bottom:8px; }}
  .bad {{ background:#2a0e18; color:{RED}; border:1px solid {RED}; border-radius:6px;
         padding:6px 9px; font-size:12px; margin:6px 0 10px; }}
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
    {nudge}
    <ul>{pts}</ul>
    <div class="steps">
      1 · read <code>briefs/m{nxt:02d}.md</code><br>
      2 · edit <code>missions/m{nxt:02d}_*.py</code> — fill the TODO step(s)<br>
      3 · <b>save</b> — watch the harbour react<br>
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
