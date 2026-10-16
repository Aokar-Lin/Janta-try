"""Lightweight, crisp SVG product renders for Janta (no external images needed)."""
import math


def _hex(c):
    c = c.lstrip("#")
    return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4))


def _mix(c1, c2, t):
    a, b = _hex(c1), _hex(c2)
    return "#%02x%02x%02x" % tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))


def light(c, t=.35):
    return _mix(c, "#ffffff", t)


def dark(c, t=.35):
    return _mix(c, "#000000", t)


def _wrap(uid, defs, body, title):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" role="img" aria-labelledby="t-{uid}">'
        f'<title id="t-{uid}">{title}</title><defs>{defs}'
        f'<radialGradient id="sh-{uid}" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#0a1f44" stop-opacity=".28"/>'
        f'<stop offset="1" stop-color="#0a1f44" stop-opacity="0"/></radialGradient></defs>'
        f'<ellipse cx="200" cy="372" rx="150" ry="14" fill="url(#sh-{uid})"/>{body}</svg>'
    )


def _lens(cx, cy, r, uid, ring="#2a2f3a"):
    return (
        f'<circle cx="{cx}" cy="{cy}" r="{r + 3}" fill="{ring}" opacity=".9"/>'
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#lens-{uid})"/>'
        f'<circle cx="{cx}" cy="{cy}" r="{r * .45:.1f}" fill="#0b1020"/>'
        f'<circle cx="{cx - r * .35:.1f}" cy="{cy - r * .35:.1f}" r="{r * .18:.1f}" fill="#9fb6ff" opacity=".55"/>'
    )


# ---------------------------------------------------------------- phones
def phone(uid, title, body="#3b4a6b", accent="#2f6bff", cam="pro"):
    bx, by, bw, bh = 82, 38, 150, 312
    defs = (
        f'<linearGradient id="bd-{uid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{light(body, .28)}"/>'
        f'<stop offset=".55" stop-color="{body}"/><stop offset="1" stop-color="{dark(body, .25)}"/></linearGradient>'
        f'<linearGradient id="fr-{uid}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{dark(body, .35)}"/>'
        f'<stop offset=".5" stop-color="{light(body, .15)}"/><stop offset="1" stop-color="{dark(body, .35)}"/></linearGradient>'
        f'<linearGradient id="sc-{uid}" x1="0" y1="0" x2=".4" y2="1"><stop offset="0" stop-color="{light(accent, .25)}"/>'
        f'<stop offset=".6" stop-color="{accent}"/><stop offset="1" stop-color="{dark(accent, .55)}"/></linearGradient>'
        f'<radialGradient id="lens-{uid}" cx=".4" cy=".35" r=".7"><stop offset="0" stop-color="#3b4a7a"/>'
        f'<stop offset="1" stop-color="#05070f"/></radialGradient>'
        f'<linearGradient id="gl-{uid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".35"/>'
        f'<stop offset=".4" stop-color="#fff" stop-opacity="0"/></linearGradient>'
    )
    # back phone
    back = (
        f'<g transform="rotate(-9 {bx + bw / 2} {by + bh / 2})">'
        f'<rect x="{bx - 3}" y="{by - 3}" width="{bw + 6}" height="{bh + 6}" rx="30" fill="url(#fr-{uid})"/>'
        f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="27" fill="url(#bd-{uid})"/>'
        f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="27" fill="url(#gl-{uid})"/>'
    )
    mx, my = bx + 14, by + 14
    if cam == "pro":
        back += (f'<rect x="{mx}" y="{my}" width="74" height="78" rx="20" fill="{light(body, .12)}" stroke="{dark(body, .2)}" stroke-width="1.5"/>'
                 + _lens(mx + 21, my + 21, 12, uid) + _lens(mx + 21, my + 57, 12, uid) + _lens(mx + 53, my + 39, 12, uid)
                 + f'<circle cx="{mx + 55}" cy="{my + 12}" r="4" fill="#f5e6c8"/>')
    elif cam == "duo":
        back += (f'<rect x="{mx}" y="{my}" width="62" height="66" rx="18" fill="{light(body, .12)}" stroke="{dark(body, .15)}" stroke-width="1.5"/>'
                 + _lens(mx + 19, my + 19, 11, uid) + _lens(mx + 43, my + 47, 11, uid)
                 + f'<circle cx="{mx + 47}" cy="{my + 15}" r="4" fill="#f5e6c8"/>')
    elif cam == "vertical":
        back += (_lens(mx + 16, my + 16, 12, uid) + _lens(mx + 16, my + 50, 12, uid) + _lens(mx + 16, my + 84, 12, uid)
                 + f'<circle cx="{mx + 46}" cy="{my + 16}" r="4" fill="#f5e6c8"/>')
    elif cam == "circle":
        cx, cy = bx + bw / 2, by + 70
        back += (f'<circle cx="{cx}" cy="{cy}" r="46" fill="{dark(body, .18)}" stroke="{light(body, .3)}" stroke-width="3"/>'
                 + _lens(cx - 18, cy - 18, 11, uid) + _lens(cx + 18, cy - 18, 11, uid) + _lens(cx - 18, cy + 18, 11, uid)
                 + f'<circle cx="{cx + 18}" cy="{cy + 18}" r="6" fill="#f5e6c8"/>')
    elif cam == "rect":
        back += (f'<rect x="{mx}" y="{my}" width="46" height="104" rx="23" fill="{dark(body, .15)}" stroke="{light(body, .25)}" stroke-width="2"/>'
                 + _lens(mx + 23, my + 23, 12, uid) + _lens(mx + 23, my + 58, 12, uid)
                 + f'<circle cx="{mx + 23}" cy="{my + 88}" r="5" fill="#f5e6c8"/>')
    elif cam == "square":
        back += (f'<rect x="{mx}" y="{my}" width="84" height="84" rx="22" fill="{dark(body, .2)}" stroke="{light(body, .25)}" stroke-width="2"/>'
                 + _lens(mx + 23, my + 23, 12, uid) + _lens(mx + 61, my + 23, 12, uid) + _lens(mx + 23, my + 61, 12, uid)
                 + f'<circle cx="{mx + 61}" cy="{my + 61}" r="6" fill="#f5e6c8"/>')
    back += "</g>"

    fx, fy, fw, fh = 175, 58, 148, 308
    front = (
        f'<g transform="rotate(5 {fx + fw / 2} {fy + fh / 2})">'
        f'<rect x="{fx - 3}" y="{fy - 3}" width="{fw + 6}" height="{fh + 6}" rx="30" fill="url(#fr-{uid})"/>'
        f'<rect x="{fx}" y="{fy}" width="{fw}" height="{fh}" rx="27" fill="#0b0f1a"/>'
        f'<rect x="{fx + 6}" y="{fy + 6}" width="{fw - 12}" height="{fh - 12}" rx="22" fill="url(#sc-{uid})"/>'
        f'<path d="M{fx + 6} {fy + 200} C {fx + 50} {fy + 160}, {fx + 100} {fy + 250}, {fx + fw - 6} {fy + 190} L {fx + fw - 6} {fy + fh - 28} '
        f'Q {fx + fw - 6} {fy + fh - 6} {fx + fw - 28} {fy + fh - 6} L {fx + 28} {fy + fh - 6} Q {fx + 6} {fy + fh - 6} {fx + 6} {fy + fh - 28} Z" fill="#fff" opacity=".12"/>'
        f'<path d="M{fx + 6} {fy + 240} C {fx + 60} {fy + 200}, {fx + 90} {fy + 280}, {fx + fw - 6} {fy + 235} L {fx + fw - 6} {fy + fh - 28} '
        f'Q {fx + fw - 6} {fy + fh - 6} {fx + fw - 28} {fy + fh - 6} L {fx + 28} {fy + fh - 6} Q {fx + 6} {fy + fh - 6} {fx + 6} {fy + fh - 28} Z" fill="#fff" opacity=".12"/>'
        f'<text x="{fx + fw / 2}" y="{fy + 92}" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="40" font-weight="300" fill="#fff">9:41</text>'
        f'<text x="{fx + fw / 2}" y="{fy + 112}" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="10" fill="#fff" opacity=".8">Sunday, 15 October</text>'
    )
    if cam in ("pro", "duo"):
        front += f'<rect x="{fx + fw / 2 - 26}" y="{fy + 16}" width="52" height="15" rx="7.5" fill="#05070f"/>'
    else:
        front += f'<circle cx="{fx + fw / 2}" cy="{fy + 22}" r="6" fill="#05070f"/>'
    front += f'<rect x="{fx}" y="{fy}" width="{fw}" height="{fh}" rx="27" fill="url(#gl-{uid})" opacity=".5"/></g>'
    return _wrap(uid, defs, back + front, title)


# ---------------------------------------------------------------- watches
def watch(uid, title, case="#c9ced8", strap="#1a3c7a", accent="#2f6bff", shape="square", sport=True):
    defs = (
        f'<linearGradient id="cs-{uid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{light(case, .45)}"/>'
        f'<stop offset=".5" stop-color="{case}"/><stop offset="1" stop-color="{dark(case, .35)}"/></linearGradient>'
        f'<linearGradient id="st-{uid}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{dark(strap, .25)}"/>'
        f'<stop offset=".5" stop-color="{light(strap, .12)}"/><stop offset="1" stop-color="{dark(strap, .25)}"/></linearGradient>'
        f'<radialGradient id="dl-{uid}" cx=".5" cy=".35" r=".8"><stop offset="0" stop-color="#1b2540"/>'
        f'<stop offset="1" stop-color="#03050b"/></radialGradient>'
    )
    straps = (f'<rect x="150" y="18" width="100" height="160" rx="{38 if sport else 14}" fill="url(#st-{uid})"/>'
              f'<rect x="150" y="222" width="100" height="160" rx="{38 if sport else 14}" fill="url(#st-{uid})"/>')
    if sport:
        straps += "".join(f'<circle cx="200" cy="{y}" r="4.5" fill="{dark(strap, .45)}"/>' for y in (300, 325, 350))
    else:
        straps += (f'<rect x="158" y="24" width="84" height="148" rx="10" fill="none" stroke="{light(strap, .3)}" stroke-width="1.5" stroke-dasharray="4 4"/>'
                   f'<rect x="158" y="228" width="84" height="148" rx="10" fill="none" stroke="{light(strap, .3)}" stroke-width="1.5" stroke-dasharray="4 4"/>')
    rings = ""
    if shape == "square":
        body = (f'<rect x="114" y="92" width="172" height="216" rx="50" fill="url(#cs-{uid})"/>'
                f'<rect x="284" y="150" width="14" height="40" rx="6" fill="{dark(case, .15)}"/>'
                f'<rect x="286" y="208" width="10" height="34" rx="4" fill="{dark(case, .2)}"/>'
                f'<rect x="124" y="102" width="152" height="196" rx="42" fill="url(#dl-{uid})"/>'
                f'<text x="200" y="196" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="50" font-weight="600" fill="#fff">10:09</text>'
                f'<text x="200" y="146" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="13" fill="{light(accent, .3)}" font-weight="700">SUN 15</text>')
        cx, cy = 200, 248
        for i, (r, col, p) in enumerate([(22, "#ff3b5c", .78), (16, "#9dff3b", .6), (10, "#2fd8ff", .85)]):
            circ = 2 * math.pi * r
            rings += (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-opacity=".22" stroke-width="5"/>'
                      f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="5" stroke-linecap="round" '
                      f'stroke-dasharray="{circ * p:.1f} {circ:.1f}" transform="rotate(-90 {cx} {cy})"/>')
    else:
        ticks = ""
        for i in range(60):
            a = math.radians(i * 6)
            r1, r2 = (78, 88) if i % 5 == 0 else (84, 88)
            w = 3 if i % 5 == 0 else 1.2
            ticks += (f'<line x1="{200 + r1 * math.sin(a):.1f}" y1="{200 - r1 * math.cos(a):.1f}" x2="{200 + r2 * math.sin(a):.1f}" '
                      f'y2="{200 - r2 * math.cos(a):.1f}" stroke="#fff" stroke-opacity="{.95 if i % 5 == 0 else .45}" stroke-width="{w}"/>')

        def hand(deg, length, width, col, back=12):
            a = math.radians(deg)
            return (f'<line x1="{200 - back * math.sin(a):.1f}" y1="{200 + back * math.cos(a):.1f}" x2="{200 + length * math.sin(a):.1f}" '
                    f'y2="{200 - length * math.cos(a):.1f}" stroke="{col}" stroke-width="{width}" stroke-linecap="round"/>')
        body = (f'<rect x="292" y="182" width="16" height="36" rx="6" fill="{dark(case, .15)}"/>'
                f'<circle cx="200" cy="200" r="110" fill="url(#cs-{uid})"/>'
                f'<circle cx="200" cy="200" r="100" fill="{dark(case, .55)}"/>'
                f'<circle cx="200" cy="200" r="94" fill="url(#dl-{uid})"/>{ticks}'
                f'<circle cx="200" cy="150" r="18" fill="none" stroke="{accent}" stroke-opacity=".35" stroke-width="4"/>'
                f'<circle cx="200" cy="150" r="18" fill="none" stroke="{accent}" stroke-width="4" stroke-linecap="round" stroke-dasharray="80 113" transform="rotate(-90 200 150)"/>'
                f'<text x="200" y="255" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="13" font-weight="700" fill="#fff" opacity=".85">8,432 steps</text>'
                + hand(304, 52, 6, "#fff") + hand(54, 74, 4.5, "#fff") + hand(190, 80, 2, accent, 18)
                + f'<circle cx="200" cy="200" r="6" fill="{accent}"/><circle cx="200" cy="200" r="2.5" fill="#fff"/>')
    return _wrap(uid, defs, straps + body + rings, title)


# ---------------------------------------------------------------- accessories
def charger(uid, title, color="#f4f6fa", cable="#ffffff"):
    defs = (f'<linearGradient id="c1-{uid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{light(color, .5)}"/>'
            f'<stop offset="1" stop-color="{dark(color, .12)}"/></linearGradient>')
    body = (
        f'<rect x="112" y="40" width="14" height="46" rx="4" fill="#b8bec9"/><rect x="152" y="40" width="14" height="46" rx="4" fill="#b8bec9"/>'
        f'<rect x="80" y="78" width="118" height="150" rx="26" fill="url(#c1-{uid})" stroke="{dark(color, .12)}" stroke-width="2"/>'
        f'<rect x="120" y="198" width="38" height="14" rx="7" fill="{dark(color, .55)}"/>'
        f'<path d="M139 228 C 139 300, 230 250, 250 300 S 300 330, 300 262" fill="none" stroke="{dark(cable, .12)}" stroke-width="12" stroke-linecap="round"/>'
        f'<path d="M139 228 C 139 300, 230 250, 250 300 S 300 330, 300 262" fill="none" stroke="{cable}" stroke-width="8" stroke-linecap="round"/>'
        f'<rect x="284" y="200" width="32" height="64" rx="10" fill="url(#c1-{uid})" stroke="{dark(color, .15)}" stroke-width="2"/>'
        f'<rect x="291" y="176" width="18" height="28" rx="6" fill="#c3c8d2"/><rect x="295" y="182" width="10" height="16" rx="3" fill="#7d8594"/>'
    )
    return _wrap(uid, defs, body, title)


def earbuds(uid, title, color="#ffffff", accent="#2f6bff", stem=True):
    defs = (f'<linearGradient id="e1-{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{light(color, .6)}"/>'
            f'<stop offset="1" stop-color="{dark(color, .14)}"/></linearGradient>')
    body = (
        f'<rect x="70" y="150" width="190" height="170" rx="70" fill="url(#e1-{uid})" stroke="{dark(color, .15)}" stroke-width="2"/>'
        f'<path d="M78 210 H252" stroke="{dark(color, .18)}" stroke-width="2"/>'
        f'<circle cx="165" cy="262" r="5" fill="{accent}"/>'
    )
    if stem:
        for x, rot in ((278, -12), (322, 10)):
            body += (f'<g transform="rotate({rot} {x} 220)"><rect x="{x - 9}" y="200" width="18" height="110" rx="9" fill="url(#e1-{uid})" stroke="{dark(color, .15)}" stroke-width="1.5"/>'
                     f'<ellipse cx="{x}" cy="190" rx="26" ry="30" fill="url(#e1-{uid})" stroke="{dark(color, .15)}" stroke-width="1.5"/>'
                     f'<ellipse cx="{x - 6}" cy="186" rx="10" ry="12" fill="{dark(color, .45)}"/></g>')
    else:
        for x, y in ((290, 120), (318, 210)):
            body += (f'<circle cx="{x}" cy="{y}" r="38" fill="url(#e1-{uid})" stroke="{dark(color, .15)}" stroke-width="1.5"/>'
                     f'<circle cx="{x}" cy="{y}" r="20" fill="{dark(color, .35)}"/><circle cx="{x + 14}" cy="{y - 18}" r="5" fill="{accent}"/>')
    return _wrap(uid, defs, body, title)


def case(uid, title, color="#2f6bff", second="#0a1f44", clear=False):
    def one(x, y, rot, col, op=1):
        return (f'<g transform="rotate({rot} {x + 75} {y + 155})" opacity="{op}">'
                f'<rect x="{x}" y="{y}" width="150" height="310" rx="30" fill="{col}" stroke="{dark(col, .25)}" stroke-width="3"/>'
                f'<rect x="{x + 6}" y="{y + 6}" width="138" height="298" rx="25" fill="none" stroke="{light(col, .3)}" stroke-width="2" opacity=".7"/>'
                f'<rect x="{x + 14}" y="{y + 14}" width="78" height="82" rx="20" fill="#fff" fill-opacity="{.35 if clear else .9}" stroke="{dark(col, .3)}" stroke-width="2"/>'
                f'<circle cx="{x + 75}" cy="{y + 175}" r="34" fill="none" stroke="{light(col, .35)}" stroke-width="4" opacity=".7"/>'
                f'<rect x="{x - 4}" y="{y + 90}" width="5" height="40" rx="2" fill="{dark(col, .3)}"/></g>')
    if clear:
        body = one(110, 40, -6, "#cfe0ff", .55) + one(150, 50, 7, "#dbe7ff", .75)
    else:
        body = one(90, 40, -8, second) + one(165, 55, 6, color)
    return _wrap(uid, "", body, title)


def _is_light(c):
    r, g, b = _hex(c)
    return (0.299 * r + 0.587 * g + 0.114 * b) > 170


def powerbank(uid, title, color="#1f2937", accent="#2f6bff", label="20000mAh"):
    ink = "#1e293b" if _is_light(color) else "#ffffff"
    acc = accent if accent.lower() != color.lower() else "#ffffff"
    defs = (f'<linearGradient id="p1-{uid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{light(color, .25)}"/>'
            f'<stop offset="1" stop-color="{dark(color, .25)}"/></linearGradient>')
    body = (
        f'<g transform="rotate(-8 200 200)">'
        f'<rect x="110" y="50" width="180" height="300" rx="34" fill="url(#p1-{uid})"/>'
        f'<rect x="110" y="50" width="180" height="300" rx="34" fill="none" stroke="#fff" stroke-opacity=".15" stroke-width="2"/>'
        f'<rect x="150" y="60" width="26" height="9" rx="4" fill="{dark(color, .6)}"/><rect x="190" y="60" width="40" height="9" rx="4" fill="{dark(color, .6)}"/>'
        + "".join(f'<circle cx="{172 + i * 19}" cy="300" r="5" fill="{acc if i < 3 else (dark(color, .2) if _is_light(color) else light(color, .3))}"/>' for i in range(4))
        + f'<text x="200" y="215" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="22" font-weight="700" fill="{ink}" opacity=".9">{label}</text>'
        f'<path d="M196 150 l-14 26 h14 l-6 22 l22 -30 h-14 l8 -18 z" fill="{acc}"/></g>'
    )
    return _wrap(uid, defs, body, title)


def glass(uid, title, tint="#9cc0ff"):
    defs = (f'<linearGradient id="g1-{uid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".9"/>'
            f'<stop offset=".5" stop-color="{tint}" stop-opacity=".35"/><stop offset="1" stop-color="#fff" stop-opacity=".7"/></linearGradient>')
    body = (
        f'<g transform="rotate(-8 200 200)"><rect x="100" y="40" width="160" height="320" rx="30" fill="#0b0f1a"/>'
        f'<rect x="107" y="47" width="146" height="306" rx="24" fill="#1a3c7a"/></g>'
        f'<g transform="rotate(6 220 200)"><rect x="150" y="42" width="160" height="320" rx="30" fill="url(#g1-{uid})" stroke="#fff" stroke-width="3"/>'
        f'<rect x="210" y="56" width="40" height="10" rx="5" fill="#0b0f1a" opacity=".25"/>'
        f'<path d="M170 300 L290 90" stroke="#fff" stroke-width="16" opacity=".55" stroke-linecap="round"/>'
        f'<path d="M200 320 L292 160" stroke="#fff" stroke-width="6" opacity=".45" stroke-linecap="round"/>'
        f'<text x="230" y="250" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="30" font-weight="800" fill="#1240a8" opacity=".55">9H</text></g>'
    )
    return _wrap(uid, defs, body, title)


RENDERERS = {"phone": phone, "watch": watch, "charger": charger, "earbuds": earbuds,
             "case": case, "powerbank": powerbank, "glass": glass}


def render(uid, title, spec):
    spec = dict(spec)
    kind = spec.pop("type")
    return RENDERERS[kind](uid, title, **spec)
