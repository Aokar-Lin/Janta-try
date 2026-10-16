#!/usr/bin/env python3
"""
Janta static site generator.
Usage:  python3 _src/build.py      (writes the finished website into ./public)
"""
import html
import json
import os
import shutil
import sys
from datetime import date
from urllib.parse import quote

sys.path.insert(0, os.path.dirname(__file__))
from data import STORE as S, PRODUCTS, PHONE_BRANDS, WATCH_BRANDS, ACCESSORY_TYPES  # noqa: E402
import svgart  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "public"))


def asset_ver(rel):
    """Short content hash used as ?v= so browsers always fetch the latest CSS/JS."""
    import hashlib
    with open(os.path.join(ROOT, rel), "rb") as f:
        return hashlib.md5(f.read()).hexdigest()[:8]
TODAY = date.today().isoformat()
esc = html.escape
CUR = ' aria-current="page"'

CATS = {
    "phones": {"label": "Phones", "page": "phones.html", "icon": "phone-device",
               "title": "Smartphones in Nepal – Apple, Samsung, Xiaomi & More",
               "desc": "Shop the latest smartphones in Nepal at the best prices. Genuine Apple iPhone, Samsung Galaxy, Xiaomi, OnePlus, Vivo, Oppo and Realme phones with warranty.",
               "lead": "Genuine smartphones from Apple, Samsung, Xiaomi, OnePlus, Vivo, Oppo and Realme — with official warranty."},
    "watches": {"label": "Watches", "page": "watches.html", "icon": "watch",
                "title": "Smartwatches in Nepal – Apple Watch, Galaxy & More",
                "desc": "Buy original smartwatches in Nepal: Apple Watch, Samsung Galaxy Watch, Huawei, Amazfit, Noise and boAt at the best prices with fast support.",
                "lead": "Track your health, fitness and notifications with smartwatches from the world's top brands."},
    "accessories": {"label": "Accessories", "page": "accessories.html", "icon": "plug",
                    "title": "Phone Accessories in Nepal – Chargers, Cases & More",
                    "desc": "Original phone accessories in Nepal: fast chargers, wireless earphones, cases, power banks and tempered-glass screen protectors at great prices.",
                    "lead": "Chargers, earphones, cases, power banks and screen protectors — everything to complete your setup."},
}
LABELS = dict(PHONE_BRANDS + WATCH_BRANDS + ACCESSORY_TYPES)

# ------------------------------------------------------------------ icons (inline SVG, Lucide-style)
_I = {
    "whatsapp": '<path fill="currentColor" stroke="none" d="M17.47 14.38c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.16-.17.2-.35.22-.64.07-.3-.15-1.26-.46-2.39-1.47-.88-.79-1.48-1.76-1.65-2.06-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.18.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.61-.92-2.2-.24-.58-.49-.5-.67-.51l-.57-.01c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48s1.07 2.88 1.21 3.07c.15.2 2.1 3.2 5.08 4.49.71.31 1.26.49 1.7.63.71.22 1.36.19 1.87.12.57-.09 1.76-.72 2-1.41.25-.7.25-1.29.18-1.41-.08-.13-.27-.2-.57-.35m-5.42 7.4h-.01a9.87 9.87 0 0 1-5.03-1.38l-.36-.21-3.74.98 1-3.65-.24-.37a9.86 9.86 0 0 1-1.51-5.26c0-5.45 4.44-9.88 9.89-9.88 2.64 0 5.12 1.03 6.99 2.9a9.83 9.83 0 0 1 2.89 6.99c0 5.45-4.44 9.88-9.88 9.88m8.41-18.3A11.82 11.82 0 0 0 12.05 0C5.5 0 .16 5.34.16 11.89c0 2.1.55 4.14 1.59 5.95L.06 24l6.3-1.65a11.88 11.88 0 0 0 5.68 1.45h.01c6.55 0 11.89-5.34 11.89-11.89a11.82 11.82 0 0 0-3.48-8.41Z"/>',
    "bag": '<path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/>',
    "minus": '<path d="M5 12h14"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "menu": '<path d="M4 6h16M4 12h16M4 18h16"/>',
    "x": '<path d="M18 6 6 18M6 6l12 12"/>',
    "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
    "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10"/><path d="m9 12 2 2 4-4"/>',
    "tag": '<path d="M12.59 2.59A2 2 0 0 0 11.17 2H4a2 2 0 0 0-2 2v7.17a2 2 0 0 0 .59 1.42l8.7 8.7a2.43 2.43 0 0 0 3.42 0l6.58-6.58a2.43 2.43 0 0 0 0-3.42z"/><circle cx="7.5" cy="7.5" r="1.5" fill="currentColor"/>',
    "headset": '<path d="M3 14h3a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-7a9 9 0 0 1 18 0v7a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3"/>',
    "arrow": '<path d="M5 12h14M12 5l7 7-7 7"/>',
    "search": '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
    "filter": '<path d="M22 3H2l8 9.46V19l4 2v-8.54L22 3z"/>',
    "phone-device": '<rect x="5" y="2" width="14" height="20" rx="2"/><path d="M12 18h.01"/>',
    "watch": '<circle cx="12" cy="12" r="6"/><path d="M12 10v2l1 1"/><path d="m16.13 7.66-.81-4.05a2 2 0 0 0-2-1.61h-2.68a2 2 0 0 0-2 1.61l-.78 4.05M7.88 16.36l.8 4a2 2 0 0 0 2 1.61h2.72a2 2 0 0 0 2-1.61l.81-4.05"/>',
    "plug": '<path d="M12 22v-5M9 8V2M15 8V2M18 8v5a4 4 0 0 1-4 4h-4a4 4 0 0 1-4-4V8Z"/>',
    "grid": '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/>',
    "truck": '<path d="M14 18V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v11a1 1 0 0 0 1 1h2M15 18H9M19 18h2a1 1 0 0 0 1-1v-3.65a1 1 0 0 0-.22-.62l-3.48-4.35A1 1 0 0 0 17.52 8H14"/><circle cx="17" cy="18" r="2"/><circle cx="7" cy="18" r="2"/>',
    "check": '<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><path d="m9 11 3 3L22 4"/>',
    "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>',
    "award": '<circle cx="12" cy="8" r="6"/><path d="M15.48 12.89 17 22l-5-3-5 3 1.52-9.11"/>',
    "heart": '<path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/>',
    "facebook": '<path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>',
    "instagram": '<rect x="2" y="2" width="20" height="20" rx="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><path d="M17.5 6.5h.01"/>',
    "youtube": '<path d="M2.5 17a24.12 24.12 0 0 1 0-10 2 2 0 0 1 1.4-1.4 49.56 49.56 0 0 1 16.2 0A2 2 0 0 1 21.5 7a24.12 24.12 0 0 1 0 10 2 2 0 0 1-1.4 1.4 49.55 49.55 0 0 1-16.2 0A2 2 0 0 1 2.5 17"/><path d="m10 15 5-3-5-3z"/>',
    "tiktok": '<path fill="currentColor" stroke="none" d="M12.53.02C13.84 0 15.14.01 16.44 0c.08 1.53.63 3.09 1.75 4.17 1.12 1.11 2.7 1.62 4.24 1.79v4.03c-1.44-.05-2.89-.35-4.2-.97-.57-.26-1.1-.59-1.62-.93-.01 2.92.01 5.84-.02 8.75-.08 1.4-.54 2.79-1.35 3.94-1.31 1.92-3.58 3.17-5.91 3.21-1.43.08-2.86-.31-4.08-1.03-2.02-1.19-3.44-3.37-3.65-5.71-.02-.5-.03-1-.01-1.49.18-1.9 1.12-3.72 2.58-4.96 1.66-1.44 3.98-2.13 6.15-1.72.02 1.48-.04 2.96-.04 4.44-.99-.32-2.15-.23-3.02.37-.63.41-1.11 1.04-1.36 1.75-.21.51-.15 1.07-.14 1.61.24 1.64 1.82 3.02 3.5 2.87 1.12-.01 2.19-.66 2.77-1.61.19-.33.4-.67.41-1.06.1-1.79.06-3.57.07-5.36.01-4.03-.01-8.05.02-12.07z"/>',
}


def icon(name, cls=""):
    c = f' class="{cls}"' if cls else ""
    return (f'<svg{c} viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{_I[name]}</svg>')


# ------------------------------------------------------------------ helpers
def npr(n):
    """Nepali/Indian digit grouping: 219900 -> Rs. 2,19,900"""
    s = str(int(n))
    if len(s) > 3:
        head, tail = s[:-3], s[-3:]
        parts = []
        while len(head) > 2:
            parts.insert(0, head[-2:])
            head = head[:-2]
        if head:
            parts.insert(0, head)
        s = ",".join(parts) + "," + tail
    return "Rs. " + s


PAGE_ITEMS = {}   # products shown on the page currently being built (for the Buy Now window)


def type_label(p):
    return {"phones": "Smartphone", "watches": "Smartwatch"}.get(p["cat"]) or LABELS[p["key"]].rstrip("s")


def slugify(t):
    return "".join(ch if ch.isalnum() else "-" for ch in t.lower()).strip("-").replace("--", "-")


def prepare_variants():
    """Default image = first colour; each extra colour gets its own recoloured illustration."""
    for p in PRODUCTS:
        for g in p["options"]:
            if g["kind"] != "colour":
                continue
            for i, v in enumerate(g["values"]):
                if p.get("photo") or not g.get("param"):
                    v["img"] = v.get("img") or img_path(p)
                    continue
                over = {g["param"]: v["hex"]}
                if p["img"]["type"] == "phone" and _colourful(v["hex"]):
                    over["accent"] = v["hex"]          # matching wallpaper on the phone screen
                if i == 0:
                    base_accent = p["img"].get("accent")
                    p["img"] = dict(p["img"], **over)
                    v["img"] = img_path(p)
                else:
                    v["img"] = f"assets/img/products/{p['slug']}--{slugify(v['label'])}.svg"
                    v["spec"] = dict(p["img"], **over)
                    if "accent" not in over and p["img"]["type"] == "phone" and base_accent:
                        v["spec"]["accent"] = base_accent


def _colourful(h):
    r, g, b = (int(h.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))
    return max(r, g, b) - min(r, g, b) > 45 and max(r, g, b) > 60


def price_range(p):
    lo = p["price"] + sum(min(v["add"] for v in g["values"]) for g in p["options"])
    hi = p["price"] + sum(max(v["add"] for v in g["values"]) for g in p["options"])
    return lo, hi


def default_price(p):
    return p["price"] + sum(g["values"][0]["add"] for g in p["options"])


def wa(msg):
    return f"https://wa.me/{S['whatsapp']}?text={quote(msg)}"


WA_GENERAL = wa("Hello Janta! I'd like to know more about your phones and watches.")


def abs_url(path):
    return S["domain"] + "/" + ("" if path == "index.html" else path)


def img_path(p):
    return p.get("photo") or f"assets/img/products/{p['slug']}.svg"


def address_str():
    return f"{S['street']}, {S['city']} {S['postcode']}, {S['country']}"


def jsonld(obj):
    return f'<script type="application/ld+json">{json.dumps(obj, ensure_ascii=False, separators=(",", ":"))}</script>'


def org_schema():
    return {
        "@context": "https://schema.org", "@type": "ElectronicsStore", "@id": S["domain"] + "/#store",
        "name": S["name"], "url": S["domain"] + "/", "logo": S["domain"] + "/favicon.svg",
        "image": S["domain"] + "/assets/img/hero-og.jpg", "telephone": S["phone_tel"], "email": S["email"],
        "priceRange": "Rs. 799 – Rs. 2,19,900", "currenciesAccepted": S["currency"],
        "address": {"@type": "PostalAddress", "streetAddress": S["street"], "addressLocality": S["city"],
                    "postalCode": S["postcode"], "addressRegion": S["region"], "addressCountry": S["country_code"]},
        "geo": {"@type": "GeoCoordinates", "latitude": S["geo"][0], "longitude": S["geo"][1]},
        "openingHours": S["hours_schema"], "sameAs": list(S["socials"].values()),
    }


def breadcrumb_schema(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": abs_url(u)}
                                for i, (n, u) in enumerate(items)]}


# ------------------------------------------------------------------ layout
def head(title, desc, path, root="", og_image="assets/img/hero-og.jpg", og_type="website", schemas=(), preload=""):
    full_title = title if "Janta" in title or len(title) > 57 else f"{title} | Janta"
    if len(desc) > 160:  # keep meta descriptions inside the ~160-char snippet limit
        desc = desc[:157].rsplit(" ", 1)[0].rstrip(",.;–- ") + "…"
    return f"""<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{abs_url(path)}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#ffffff">
<meta property="og:site_name" content="Janta">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{esc(full_title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{abs_url(path)}">
<meta property="og:image" content="{S['domain']}/{og_image}">
<meta property="og:locale" content="en_NP">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{root}favicon.svg" type="image/svg+xml">
<link rel="manifest" href="{root}site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap">
{preload}<link rel="stylesheet" href="{root}assets/css/style.css?v={asset_ver('assets/css/style.css')}">
<script>document.documentElement.classList.remove('no-js')</script>
<script src="{root}assets/js/main.js?v={asset_ver('assets/js/main.js')}" defer></script>
{"".join(jsonld(s) for s in schemas)}
</head>
"""


NAV = [("Home", "index.html"), ("Shop", "shop.html"), ("About Us", "about.html"), ("Contact Us", "contact.html")]


def logo(root):
    return (f'<a href="{root}index.html" class="logo" aria-label="Janta – home">'
            f'<span class="logo-mark" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M15 4v10a5 5 0 0 1-10 0"/><circle cx="19" cy="4" r="1.2" fill="currentColor"/></svg></span>'
            f'<span>Jant<em>a</em></span></a>')


def header(active, root=""):
    links = "".join(
        f'<li><a href="{root}{u}"{CUR if n == active else ""}>{n}</a></li>' for n, u in NAV)
    mlinks = "".join(
        f'<a class="m-link" href="{root}{u}"{CUR if n == active else ""}>{n}</a>' for n, u in NAV)
    return f"""<body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header" id="top">
  <div class="container header-inner">
    {logo(root)}
    <nav class="main-nav" aria-label="Main"><ul>{links}</ul></nav>
    <div class="header-actions">
      <a class="btn btn-wa" href="{WA_GENERAL}" target="_blank" rel="noopener">{icon("whatsapp")}WhatsApp Us</a>
      <button class="nav-toggle" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-nav">{icon("menu", "icon-menu")}{icon("x", "icon-close")}</button>
    </div>
  </div>
  <nav class="mobile-nav" id="mobile-nav" aria-label="Mobile">
    {mlinks}
    <a class="btn btn-wa" href="{WA_GENERAL}" target="_blank" rel="noopener">{icon("whatsapp")}Chat on WhatsApp</a>
  </nav>
</header>
"""


def buy_window(root):
    """Product-details window opened by every Buy Now button (filled in by main.js)."""
    if not PAGE_ITEMS:
        return ""
    items = {}
    for slug, p in PAGE_ITEMS.items():
        items[slug] = {"name": p["name"], "brand": p["brand"], "type": type_label(p), "price": p["price"],
                       "old": p["old_price"], "badge": p["badge"], "desc": p["desc"], "specs": p["specs"],
                       "img": img_path(p), "page": f"products/{slug}.html", "url": abs_url(f"products/{slug}.html"),
                       "options": [{"name": g["name"], "kind": g["kind"],
                                    "values": [{k: v[k] for k in ("label", "add", "hex", "img") if k in v} for v in g["values"]]}
                                   for g in p["options"]]}
    PAGE_ITEMS.clear()
    data = json.dumps({"wa": S["whatsapp"], "root": root, "items": items}, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return f"""<dialog class="qv" id="buy-now" aria-labelledby="qv-title">
  <button class="icon-btn qv-close" type="button" data-qv-close aria-label="Close">{icon("x")}</button>
  <div class="qv-grid">
    <div class="qv-media"><span class="badge" data-qv="badge" hidden></span><img data-qv="img" alt="" width="400" height="400"></div>
    <div class="qv-info">
      <span class="pc-brand" data-qv="brand"></span>
      <h2 id="qv-title" data-qv="name"></h2>
      <div class="pd-price"><span class="price" data-qv="price"></span><span class="price-old" data-qv="old"></span><span class="save-tag" data-qv="save"></span></div>
      <div class="stock">In stock · Ready for pickup or delivery</div>
      <div class="qv-options" data-qv="options"></div>
      <h3 class="qv-sub">About this product</h3>
      <p class="pd-desc" data-qv="desc"></p>
      <h3 class="qv-sub">Specifications</h3>
      <dl class="spec-list" data-qv="specs"></dl>
      <div class="qv-perks">
        <span>{icon("shield")}100% Genuine</span><span>{icon("truck")}Fast Delivery</span><span>{icon("headset")}Quick Support</span>
      </div>
      <div class="qv-buy">
        <div class="qv-qty-row">
          <span class="qv-label">Quantity</span>
          <div class="qty"><button type="button" data-qty="-1" aria-label="Decrease quantity">{icon("minus")}</button><output data-qv="qty" aria-live="polite">1</output><button type="button" data-qty="1" aria-label="Increase quantity">{icon("plus")}</button></div>
          <span class="qv-total">Total: <b data-qv="total"></b></span>
        </div>
        <a class="btn btn-wa btn-lg btn-block" data-qv="wa" href="#" target="_blank" rel="noopener">{icon("whatsapp")}Contact on WhatsApp</a>
        <div class="qv-links">
          <a href="tel:{S['phone_tel']}">{icon("phone")}Call {S['phone_display']}</a>
          <a data-qv="page" href="#">View full details {icon("arrow")}</a>
        </div>
      </div>
    </div>
  </div>
</dialog>
<script type="application/json" id="product-data">{data}</script>
"""


def footer(root=""):
    soc = "".join(f'<a href="{u}" target="_blank" rel="noopener" aria-label="Janta on {k.title()}">{icon(k)}</a>'
                  for k, u in S["socials"].items())
    cats = "".join(f'<li><a href="{root}{c["page"]}">{c["label"]}</a></li>' for c in CATS.values())
    hours = "<br>".join(f"{d}: {t}" for d, t in S["hours"])
    return f"""<footer class="site-footer">
  <div class="container footer-grid">
    <div class="footer-about">
      {logo(root)}
      <p>Your trusted destination in Nepal for genuine smartphones, smartwatches and accessories, at prices you'll love.</p>
      <div class="socials">{soc}</div>
    </div>
    <div>
      <h2 class="f-title">Shop</h2>
      <ul class="footer-links">{cats}<li><a href="{root}shop.html">All Products</a></li></ul>
    </div>
    <div>
      <h2 class="f-title">Company</h2>
      <ul class="footer-links">
        <li><a href="{root}index.html">Home</a></li>
        <li><a href="{root}about.html">About Us</a></li>
        <li><a href="{root}contact.html">Contact Us</a></li>
        <li><a href="{WA_GENERAL}" target="_blank" rel="noopener">WhatsApp Support</a></li>
      </ul>
    </div>
    <div>
      <h2 class="f-title">Get in touch</h2>
      <ul class="footer-contact">
        <li>{icon("pin")}<span>{esc(address_str())}</span></li>
        <li>{icon("phone")}<a href="tel:{S['phone_tel']}">{S['phone_display']}</a></li>
        <li>{icon("mail")}<a href="mailto:{S['email']}">{S['email']}</a></li>
        <li>{icon("clock")}<span>{hours}</span></li>
      </ul>
    </div>
  </div>
  <div class="container footer-bottom">
    <span>&copy; {date.today().year} Janta Phones &amp; Watches. All rights reserved.</span>
    <span>Genuine products · Best prices · Fast support</span>
  </div>
</footer>
{buy_window(root)}<aside aria-label="WhatsApp chat"><a class="wa-float" href="{WA_GENERAL}" target="_blank" rel="noopener" aria-label="Chat with Janta on WhatsApp">{icon("whatsapp")}</a></aside>
</body>
</html>
"""


def product_wa(p):
    return wa(f"Hello Janta! I'm interested in the {p['name']} ({npr(p['price'])}). Is it available?\n{abs_url('products/' + p['slug'] + '.html')}")


def badge(p):
    if not p["badge"]:
        return ""
    cls = {"Sale": " sale", "Hot": " hot"}.get(p["badge"], "")
    return f'<span class="badge{cls}">{p["badge"]}</span>'


def card(p, root="", order=0, lazy=True):
    url = f"{root}products/{p['slug']}.html"
    lo, hi = price_range(p)
    off = lo - p["price"]
    old = f'<span class="price-old">{npr(p["old_price"] + off)}</span>' if p["old_price"] else ""
    from_ = '<span class="price-from">From</span>' if hi != lo else ""
    sw = ""
    for g in p["options"]:
        if g["kind"] == "colour":
            dots = "".join(f'<i style="background:{v["hex"]}" title="{esc(v["label"])}"></i>' for v in g["values"][:5])
            sw = f'<div class="pc-swatches" aria-label="{len(g["values"])} colours">{dots}<span>{len(g["values"])} {g["name"].lower()}{"s" if len(g["values"]) > 1 else ""}</span></div>'
            break
        else:
            sw = sw or f'<div class="pc-swatches"><span>{len(g["values"])} {esc(g["name"].lower())} options</span></div>'
    PAGE_ITEMS[p["slug"]] = p
    load = 'loading="lazy" decoding="async"' if lazy else 'decoding="async"'
    return f"""<article class="product-card" data-cat="{p['cat']}" data-key="{p['key']}" data-price="{lo}" data-order="{order}" data-name="{esc(p['name'].lower() + ' ' + p['brand'].lower() + ' ' + LABELS[p['key']].lower())}">
  <a class="pc-media" href="{url}" tabindex="-1" aria-hidden="true">{badge(p)}<img src="{root}{img_path(p)}" alt="{esc(p['name'])}" width="400" height="400" {load}></a>
  <div class="pc-body">
    <span class="pc-brand">{esc(p['brand'])}</span>
    <h3 class="pc-title"><a href="{url}">{esc(p['name'])}</a></h3>
    <p class="pc-desc">{esc(p['short'])}</p>
    {sw}
    <div class="pc-price">{from_}<span class="price">{npr(lo)}</span>{old}</div>
    <div class="pc-actions"><a class="btn btn-primary" href="{url}" data-buy="{p['slug']}" aria-label="Buy now: {esc(p['name'])}">{icon("bag")}Buy Now</a></div>
  </div>
</article>"""


def write(rel, content):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def benefits_html():
    items = [("shield", "Genuine Products", "100% original devices sourced from authorised distributors, with official warranty and sealed boxes."),
             ("tag", "Best Prices", "Competitive, transparent pricing on every phone, watch and accessory. No hidden charges, ever."),
             ("headset", "Fast Support", "Quick replies on WhatsApp and phone, before and after your purchase. We're here to help.")]
    return "".join(f'<div class="benefit reveal"><div class="ic">{icon(i)}</div><h3>{t}</h3><p>{d}</p></div>' for i, t, d in items)


# ------------------------------------------------------------------ pages
def page_home():
    featured = [p for p in PRODUCTS if p["featured"]][:8]
    cards = "\n".join(card(p, "", i, lazy=i > 3) for i, p in enumerate(featured))
    by = {p["slug"]: p for p in PRODUCTS}
    cat_img = {"phones": "iphone-17-pro-max", "watches": "apple-watch-series-11", "accessories": "apple-airpods-4"}
    cat_cards = "".join(
        f'<a class="cat-card reveal" href="{c["page"]}"><div><h3>{c["label"]}</h3><p>{n} products</p>'
        f'<span class="link-arrow">Shop {c["label"].lower()} {icon("arrow")}</span></div>'
        f'<img class="cat-img" src="{img_path(by[cat_img[k]])}" alt="" width="400" height="400" loading="lazy"></a>'
        for k, c in CATS.items() for n in [sum(1 for p in PRODUCTS if p["cat"] == k)])
    brands = ([(l if k != "galaxy-watch" else "Galaxy Watch", "Phones", f"phones.html?filter={k}") for k, l in PHONE_BRANDS]
              + [(l if k != "galaxy-watch" else "Galaxy Watch", "Watches", f"watches.html?filter={k}") for k, l in WATCH_BRANDS if k != "apple-watch"])
    brands = [b for b in brands][:12]
    brand_html = "".join(f'<a class="brand-tile" href="{u}"><span class="bn">{esc(n)}</span><span class="bt">{t}</span></a>' for n, t, u in brands)
    preload = ('<link rel="preload" as="image" href="assets/img/hero-mobile.webp" media="(max-width: 767px)">'
               '<link rel="preload" as="image" href="assets/img/hero-1920.webp" imagesrcset="assets/img/hero-768.webp 768w, assets/img/hero-1200.webp 1200w, assets/img/hero-1920.webp 1920w" imagesizes="100vw" media="(min-width: 768px)">\n')
    site_schema = {"@context": "https://schema.org", "@type": "WebSite", "name": "Janta", "url": S["domain"] + "/",
                   "potentialAction": {"@type": "SearchAction", "target": S["domain"] + "/shop.html?q={search_term_string}",
                                       "query-input": "required name=search_term_string"}}
    out = head("Janta – Latest Phones & Watches at the Best Prices in Nepal",
               "Janta is your trusted store for genuine smartphones, smartwatches and accessories in Kathmandu, Nepal. Apple, Samsung, Xiaomi, OnePlus & more at the best prices.",
               "index.html", schemas=[org_schema(), site_schema], preload=preload)
    out += header("Home")
    out += f"""<main id="main">
<section class="hero" aria-labelledby="hero-title">
  <picture class="hero-media">
    <source media="(min-width: 768px)" srcset="assets/img/hero-768.webp 768w, assets/img/hero-1200.webp 1200w, assets/img/hero-1920.webp 1920w" sizes="100vw">
    <img src="assets/img/hero-mobile.webp" alt="Latest smartphones and smartwatches from top brands" width="720" height="450" fetchpriority="high">
  </picture>
  <div class="container">
    <div class="hero-content">
      <span class="eyebrow"><span class="dot"></span>New arrivals every week</span>
      <h1 id="hero-title">Latest <span class="accent">Phones &amp; Watches</span> at the Best Prices</h1>
      <p class="lead">Shop 100% genuine smartphones, smartwatches and accessories from the brands you love, with official warranty, honest prices and friendly support.</p>
      <div class="hero-ctas">
        <a class="btn btn-primary btn-lg" href="shop.html">Shop Now {icon("arrow")}</a>
        <a class="btn btn-wa btn-lg" href="{WA_GENERAL}" target="_blank" rel="noopener">{icon("whatsapp")}WhatsApp Us</a>
      </div>
      <div class="hero-trust">
        <div>{icon("shield")}<span><strong>100%</strong> Genuine</span></div>
        <div>{icon("truck")}<span><strong>Fast</strong> Delivery</span></div>
        <div>{icon("headset")}<span><strong>Quick</strong> Support</span></div>
      </div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="feat-title">
  <div class="container">
    <div class="section-head">
      <div><span class="kicker">Handpicked for you</span><h2 id="feat-title">Featured Products</h2>
      <p>Our best-selling phones, watches and accessories, chosen for performance and value.</p></div>
      <a class="link-arrow" href="shop.html">View all products {icon("arrow")}</a>
    </div>
    <div class="product-grid">
{cards}
    </div>
  </div>
</section>

<section class="section section-alt" aria-labelledby="cat-title">
  <div class="container">
    <div class="section-head"><div><span class="kicker">Browse</span><h2 id="cat-title">Shop by Category</h2></div></div>
    <div class="cat-grid">{cat_cards}</div>
  </div>
</section>

<section class="section" aria-labelledby="brand-title">
  <div class="container">
    <div class="section-head"><div><span class="kicker">Top names</span><h2 id="brand-title">Popular Brands</h2>
    <p>Authorised products from the world's most trusted phone and watch makers.</p></div></div>
    <div class="brand-grid">{brand_html}</div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="container">
    <div class="cta-band reveal">
      <div><h2>Can't find what you're looking for?</h2><p>Message us on WhatsApp. We'll check stock, compare models and get you the best deal within minutes.</p></div>
      <div class="btns"><a class="btn btn-wa btn-lg" href="{WA_GENERAL}" target="_blank" rel="noopener">{icon("whatsapp")}Chat on WhatsApp</a>
      <a class="btn btn-ghost btn-lg" href="tel:{S['phone_tel']}">{icon("phone")}Call Us</a></div>
    </div>
  </div>
</section>
</main>
"""
    out += footer()
    write("index.html", out)


def filter_group(gid, title, items, counts, hidden=False):
    rows = "".join(
        f'<label class="check"><input type="checkbox" name="filter" value="{k}"><span>{esc(l)}</span><span class="n">{counts.get(k, 0)}</span></label>'
        for k, l in items)
    return f'<div class="filter-group" data-group="{gid}"{" hidden" if hidden else ""}><h3>{title}</h3>{rows}</div>'


def page_shop(cat=None):
    items = [p for p in PRODUCTS if cat is None or p["cat"] == cat]
    counts = {}
    for p in PRODUCTS:
        counts[p["key"]] = counts.get(p["key"], 0) + 1
    path = "shop.html" if cat is None else CATS[cat]["page"]
    if cat is None:
        title = "Shop Phones, Smartwatches & Accessories Online in Nepal"
        desc = "Browse genuine smartphones, smartwatches and phone accessories at Janta. Filter by Apple, Samsung, Xiaomi, OnePlus, Vivo, Oppo, Realme, Amazfit, Huawei and more."
        h1, lead = "Shop All Products", "Phones, smartwatches and accessories from the brands you trust, all 100% genuine and at the best prices."
        crumbs = [("Home", "index.html"), ("Shop", "shop.html")]
    else:
        c = CATS[cat]
        title, desc, h1, lead = c["title"], c["desc"], c["label"], c["lead"]
        crumbs = [("Home", "index.html"), ("Shop", "shop.html"), (c["label"], path)]

    tabs = [("All Products", "shop.html", "grid", len(PRODUCTS), cat is None)] + [
        (c["label"], c["page"], c["icon"], sum(1 for p in PRODUCTS if p["cat"] == k), cat == k) for k, c in CATS.items()]
    tab_html = "".join(
        f'<a class="cat-tab" href="{u}"{CUR if a else ""}>{icon(i)}{l}<span class="count">{n}</span></a>'
        for l, u, i, n, a in tabs)

    groups = ""
    if cat in (None, "phones"):
        groups += filter_group("phones", "Phone Brands", PHONE_BRANDS, counts)
    if cat in (None, "watches"):
        groups += filter_group("watches", "Watch Brands", WATCH_BRANDS, counts)
    if cat in (None, "accessories"):
        groups += filter_group("accessories", "Phone Accessories", ACCESSORY_TYPES, counts)

    cards = "\n".join(card(p, "", i, lazy=i > 5) for i, p in enumerate(items))
    crumb_html = "".join(
        f'<li><a href="{u}">{n}</a></li>' if i < len(crumbs) - 1 else f'<li aria-current="page">{n}</li>'
        for i, (n, u) in enumerate(crumbs))
    item_list = {"@context": "https://schema.org", "@type": "ItemList", "name": h1,
                 "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": abs_url(f"products/{p['slug']}.html"), "name": p["name"]}
                                     for i, p in enumerate(items)]}
    out = head(title, desc, path, schemas=[breadcrumb_schema(crumbs), item_list])
    out += header("Shop")
    out += f"""<main id="main" class="shop">
<section class="page-hero">
  <div class="container">
    <nav class="breadcrumb" aria-label="Breadcrumb"><ol>{crumb_html}</ol></nav>
    <h1>{esc(h1)}</h1>
    <p>{esc(lead)}</p>
  </div>
</section>
<section class="section" style="padding-top:2rem">
  <div class="container">
    <nav class="cat-tabs" aria-label="Product categories">{tab_html}</nav>
    <div class="shop-layout" id="shop">
      <div class="filters-backdrop" data-close-filters></div>
      <aside class="filters" id="filters" aria-label="Product filters">
        <div class="filters-head"><h2>Filters</h2><button class="icon-btn" type="button" data-close-filters aria-label="Close filters">{icon("x")}</button></div>
        {groups}
        <button class="btn btn-outline clear-btn" type="button" data-clear>Clear all filters</button>
        <button class="btn btn-primary filters-apply" type="button" data-close-filters>Show results</button>
      </aside>
      <div>
        <div class="shop-toolbar">
          <div class="search-box">{icon("search")}<label class="visually-hidden" for="q">Search products</label><input id="q" type="search" placeholder="Search {'products' if cat is None else CATS[cat]['label'].lower()}…" autocomplete="off"></div>
          <button class="filter-toggle" type="button" aria-controls="filters" aria-expanded="false">{icon("filter")}Filters <span class="fcount"></span></button>
          <label class="visually-hidden" for="sort">Sort products</label>
          <select class="sort-select" id="sort">
            <option value="featured">Sort: Featured</option>
            <option value="price-asc">Price: Low to High</option>
            <option value="price-desc">Price: High to Low</option>
            <option value="name">Name: A–Z</option>
          </select>
          <p class="result-count" aria-live="polite">Showing <strong data-count>{len(items)}</strong> of {len(items)} products</p>
        </div>
        <div class="active-chips" aria-label="Active filters"></div>
        <div class="product-grid" data-grid>
{cards}
        </div>
        <div class="empty-state" hidden>
          <h3>No products found</h3>
          <p>Try a different search or clear your filters. Or ask us on WhatsApp, we may have it in stock!</p>
          <div style="display:flex;gap:.75rem;justify-content:center;flex-wrap:wrap">
            <button class="btn btn-outline" type="button" data-clear>Clear filters</button>
            <a class="btn btn-wa" href="{WA_GENERAL}" target="_blank" rel="noopener">{icon("whatsapp")}Ask on WhatsApp</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
</main>
"""
    out += footer()
    write(path, out)


def page_product(p):
    root = "../"
    c = CATS[p["cat"]]
    crumbs = [("Home", "index.html"), ("Shop", "shop.html"), (c["label"], c["page"]), (p["name"], f"products/{p['slug']}.html")]
    crumb_html = "".join(
        f'<li><a href="{root}{u}">{esc(n)}</a></li>' if i < len(crumbs) - 1 else f'<li aria-current="page">{esc(n)}</li>'
        for i, (n, u) in enumerate(crumbs))
    specs = "".join(f"<div><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>" for k, v in p["specs"])
    PAGE_ITEMS[p["slug"]] = p
    lo, hi = price_range(p)
    old = ""
    if p["old_price"]:
        save = p["old_price"] - p["price"]
        old = f'<span class="price-old">{npr(p["old_price"] + lo - p["price"])}</span><span class="save-tag">Save {npr(save)}</span>'
    from_ = '<span class="price-from">From</span>' if hi != lo else ""
    opts = ""
    for g in p["options"]:
        vals = ""
        for v in g["values"]:
            extra = f' <small>{"+" if v["add"] > 0 else "−"}{npr(abs(v["add"]))[4:]}</small>' if v["add"] else ""
            dot = f'<i style="background:{v["hex"]}"></i>' if g["kind"] == "colour" else ""
            vals += f'<span class="pd-opt-val">{dot}{esc(v["label"])}{extra}</span>'
        opts += f'<div class="pd-opt"><span class="pd-opt-name">{esc(g["name"])}</span><div class="pd-opt-vals">{vals}</div></div>'
    if opts:
        opts = f'<h2 class="pd-opts-title">Available options</h2><div class="pd-opts">{opts}</div>'
    related = [q for q in PRODUCTS if q["cat"] == p["cat"] and q["slug"] != p["slug"]]
    related = sorted(related, key=lambda q: (q["key"] != p["key"], abs(q["price"] - p["price"])))[:4]
    rel_cards = "\n".join(card(q, root, i) for i, q in enumerate(related))
    url = abs_url(f"products/{p['slug']}.html")
    schema = {
        "@context": "https://schema.org", "@type": "Product", "name": p["name"], "sku": p["slug"],
        "image": [S["domain"] + "/" + img_path(p)], "description": p["desc"],
        "brand": {"@type": "Brand", "name": p["brand"]}, "category": c["label"] if p["cat"] != "accessories" else "Phone Accessories > " + LABELS[p["key"]],
        "offers": ({"@type": "Offer", "url": url, "priceCurrency": S["currency"], "price": str(lo),
                    "availability": "https://schema.org/InStock", "itemCondition": "https://schema.org/NewCondition",
                    "seller": {"@type": "Organization", "name": "Janta"}} if lo == hi else
                   {"@type": "AggregateOffer", "url": url, "priceCurrency": S["currency"], "lowPrice": str(lo), "highPrice": str(hi),
                    "availability": "https://schema.org/InStock", "itemCondition": "https://schema.org/NewCondition",
                    "seller": {"@type": "Organization", "name": "Janta"}}),
    }
    kind = c["label"].rstrip("s").lower() if p["cat"] != "accessories" else LABELS[p["key"]].lower().rstrip("s")
    title = f"{p['name']} Price in Nepal – {'From ' if lo != hi else ''}{npr(lo)}"
    desc = f"Buy the {p['brand']} {p['name'].replace(p['brand'] + ' ', '')} in Nepal {'from' if lo != hi else 'for'} {npr(lo)} at Janta. {p['short']} Genuine {kind} with warranty."
    desc = desc.replace("Apple Apple", "Apple")
    out = head(title, desc[:300], f"products/{p['slug']}.html", root, og_type="product",
               schemas=[schema, breadcrumb_schema(crumbs)])
    out += header("Shop", root)
    out += f"""<main id="main">
<section class="pd">
  <div class="container">
    <nav class="breadcrumb dark" aria-label="Breadcrumb"><ol>{crumb_html}</ol></nav>
    <div class="pd-grid">
      <div class="pd-media">{badge(p)}<img src="{root}{img_path(p)}" alt="{esc(p['name'])} by {esc(p['brand'])}" width="400" height="400" fetchpriority="high"></div>
      <div class="pd-info">
        <span class="pc-brand">{esc(p['brand'])} · {esc(type_label(p))}</span>
        <h1>{esc(p['name'])}</h1>
        <div class="pd-price">{from_}<span class="price">{npr(lo)}</span>{old}</div>
        <div class="stock">In stock · Ready for pickup or delivery</div>
        <p class="pd-desc">{esc(p['desc'])}</p>
        {opts}
        <h2 class="visually-hidden">Key specifications</h2>
        <dl class="spec-list">{specs}</dl>
        <div class="pd-ctas">
          <a class="btn btn-primary btn-lg" href="{product_wa(p)}" data-buy="{p['slug']}" target="_blank" rel="noopener">{icon("bag")}Buy Now</a>
          <a class="btn btn-outline btn-lg" href="tel:{S['phone_tel']}">{icon("phone")}Call {S['phone_display']}</a>
        </div>
        <div class="pd-perks">
          <div>{icon("shield")}<p style="margin:0"><strong>100% Genuine</strong><span>Official warranty</span></p></div>
          <div>{icon("truck")}<p style="margin:0"><strong>Fast Delivery</strong><span>Across Nepal</span></p></div>
          <div>{icon("headset")}<p style="margin:0"><strong>Quick Support</strong><span>Before &amp; after sale</span></p></div>
        </div>
      </div>
    </div>
  </div>
</section>
<section class="section section-alt" aria-labelledby="rel-title">
  <div class="container">
    <div class="section-head"><div><span class="kicker">You may also like</span><h2 id="rel-title">Related {c['label']}</h2></div>
    <a class="link-arrow" href="{root}{c['page']}">View all {c['label'].lower()} {icon("arrow")}</a></div>
    <div class="product-grid">
{rel_cards}
    </div>
  </div>
</section>
</main>
"""
    out += footer(root)
    write(f"products/{p['slug']}.html", out)


def page_about():
    crumbs = [("Home", "index.html"), ("About Us", "about.html")]
    values = [("award", "Quality First", "Every device we sell is 100% genuine, sourced from authorised distributors and backed by official warranty."),
              ("tag", "Honest Affordability", "We keep our margins fair and our prices transparent, so you always get real value for your money."),
              ("heart", "Customer Happiness", "From choosing the right model to after-sales help, we treat every customer like family.")]
    vals = "".join(f'<div class="benefit reveal"><div class="ic">{icon(i)}</div><h3>{t}</h3><p>{d}</p></div>' for i, t, d in values)
    out = head("About Janta – Trusted Phone & Watch Store in Kathmandu",
               "Learn about Janta, a trusted destination in Nepal for genuine smartphones, smartwatches and accessories, focused on quality, affordability and customer satisfaction.",
               "about.html", og_image="assets/img/about-og.jpg", schemas=[org_schema(), breadcrumb_schema(crumbs)])
    out += header("About Us")
    out += f"""<main id="main">
<section class="page-hero">
  <div class="container">
    <nav class="breadcrumb" aria-label="Breadcrumb"><ol><li><a href="index.html">Home</a></li><li aria-current="page">About Us</li></ol></nav>
    <h1>About Janta</h1>
    <p>Your trusted destination for phones, watches and accessories.</p>
  </div>
</section>
<section class="section">
  <div class="container about-grid">
    <div class="about-img reveal">
      <picture><source srcset="assets/img/about-700.webp 700w, assets/img/about-1200.webp 1200w" sizes="(min-width:1024px) 600px, 100vw" type="image/webp">
      <img src="assets/img/about-og.jpg" alt="Inside the Janta phone and watch store" width="1200" height="655" loading="lazy"></picture>
    </div>
    <div class="about-copy">
      <span class="kicker" style="color:var(--blue-600);font-weight:700;font-size:.8rem;letter-spacing:.12em;text-transform:uppercase">Our story</span>
      <h2>Technology for everyone, at a fair price</h2>
      <p>Janta (जनता), which means “the people”, was founded with one simple idea: everyone deserves access to genuine, high-quality technology without paying too much for it.</p>
      <p>Today, Janta is a trusted destination for the latest smartphones, smartwatches and accessories from brands like Apple, Samsung, Xiaomi, OnePlus, Vivo, Oppo, Realme, Huawei, Amazfit, Noise and boAt. Every product we sell is 100% original and comes with official warranty.</p>
      <p>Whether you're upgrading to a flagship phone, buying your first smartwatch or just need a reliable charger, our team will help you find the right product at the best price, and stay with you long after your purchase.</p>
      <div class="stats">
        <div class="stat"><b>10K+</b><span>Happy customers</span></div>
        <div class="stat"><b>13+</b><span>Top brands</span></div>
        <div class="stat"><b>100%</b><span>Genuine products</span></div>
        <div class="stat"><b>7 Days</b><span>Open every week</span></div>
      </div>
    </div>
  </div>
</section>
<section class="section section-alt" aria-labelledby="val-title">
  <div class="container">
    <div class="section-head"><div><span class="kicker">What we stand for</span><h2 id="val-title">Our Promise to You</h2>
    <p>Quality products, affordable prices and customer satisfaction are at the heart of everything we do.</p></div></div>
    <div class="values-grid">{vals}</div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="cta-band reveal">
      <div><h2>Visit us or shop from home</h2><p>Drop by our store on {S['street']}, {S['city']}, or browse online and order on WhatsApp.</p></div>
      <div class="btns"><a class="btn btn-white btn-lg" href="shop.html">Browse Products {icon("arrow")}</a>
      <a class="btn btn-wa btn-lg" href="{WA_GENERAL}" target="_blank" rel="noopener">{icon("whatsapp")}WhatsApp Us</a></div>
    </div>
  </div>
</section>
</main>
"""
    out += footer()
    write("about.html", out)


def page_contact():
    crumbs = [("Home", "index.html"), ("Contact Us", "contact.html")]
    hours = "".join(f"<li><span>{d}</span><b>{t}</b></li>" for d, t in S["hours"])
    maps_link = "https://www.google.com/maps/search/?api=1&query=" + quote(S["map_query"])
    embed = "https://www.google.com/maps?q=" + quote(S["map_query"]) + "&output=embed"
    out = head("Contact Janta – WhatsApp, Phone, Email & Store Location",
               f"Contact Janta – WhatsApp {S['whatsapp_display']}, call {S['phone_display']}, email {S['email']}, or visit our store at {address_str()}.",
               "contact.html", schemas=[org_schema(), breadcrumb_schema(crumbs)])
    out += header("Contact Us")
    out += f"""<main id="main">
<section class="page-hero">
  <div class="container">
    <nav class="breadcrumb" aria-label="Breadcrumb"><ol><li><a href="index.html">Home</a></li><li aria-current="page">Contact Us</li></ol></nav>
    <h1>Contact Us</h1>
    <p>Questions about a product, price or stock? We usually reply within minutes on WhatsApp.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="contact-grid">
      <div class="contact-card wa reveal">
        <div class="ic">{icon("whatsapp")}</div>
        <h2>WhatsApp</h2><p>Fastest way to reach us</p>
        <span class="val">{S['whatsapp_display']}</span>
        <a class="btn btn-wa" href="{WA_GENERAL}" target="_blank" rel="noopener">{icon("whatsapp")}Chat Now</a>
      </div>
      <div class="contact-card reveal">
        <div class="ic">{icon("phone")}</div>
        <h2>Phone</h2><p>Call us during store hours</p>
        <a class="val" href="tel:{S['phone_tel']}">{S['phone_display']}</a>
        <a class="btn btn-outline" href="tel:{S['phone_tel']}">{icon("phone")}Call Us</a>
      </div>
      <div class="contact-card reveal">
        <div class="ic">{icon("mail")}</div>
        <h2>Email</h2><p>We reply within 24 hours</p>
        <a class="val" href="mailto:{S['email']}">{S['email']}</a>
        <a class="btn btn-outline" href="mailto:{S['email']}">{icon("mail")}Send Email</a>
      </div>
      <div class="contact-card reveal">
        <div class="ic">{icon("pin")}</div>
        <h2>Store Address</h2><p>Come visit our showroom</p>
        <address class="val" style="font-style:normal">{S['street']}, {S['city']} {S['postcode']}<br>{S['region']}, {S['country']}</address>
        <a class="btn btn-outline" href="{maps_link}" target="_blank" rel="noopener">{icon("pin")}Get Directions</a>
      </div>
    </div>
    <div class="map-wrap">
      <div class="map-frame">
        <iframe src="{embed}" title="Janta store location on Google Maps" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
      </div>
      <div class="hours-card">
        <h2>Store Hours</h2>
        <ul>{hours}</ul>
        <a class="btn btn-wa" href="{WA_GENERAL}" target="_blank" rel="noopener">{icon("whatsapp")}Message us anytime</a>
      </div>
    </div>
  </div>
</section>
</main>
"""
    out += footer()
    write("contact.html", out)


def page_404():
    out = head("Page Not Found", "Sorry, the page you are looking for could not be found. Browse genuine phones, smartwatches and accessories at Janta.", "404.html")
    out = out.replace('content="index, follow, max-image-preview:large"', 'content="noindex"')
    out += header("")
    out += f"""<main id="main"><section class="section"><div class="container" style="text-align:center;max-width:620px">
<p style="font-size:5rem;font-weight:800;color:var(--blue-600);margin:0;line-height:1">404</p>
<h1>Page not found</h1><p style="color:var(--muted)">Sorry, we couldn't find that page. It may have moved, or the product may be sold out.</p>
<div style="display:flex;gap:.75rem;justify-content:center;flex-wrap:wrap;margin-top:1.5rem"><a class="btn btn-primary" href="/index.html">Go Home</a><a class="btn btn-outline" href="/shop.html">Browse Shop</a></div>
</div></section></main>
"""
    out += footer("/")
    write("404.html", out)


def extras():
    urls = [("", "1.0", "weekly"), ("shop.html", "0.9", "daily")] + [(c["page"], "0.9", "daily") for c in CATS.values()] + \
           [("about.html", "0.6", "monthly"), ("contact.html", "0.7", "monthly")] + \
           [(f"products/{p['slug']}.html", "0.8", "weekly") for p in PRODUCTS]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sm += "".join(f"  <url><loc>{S['domain']}/{u}</loc><lastmod>{TODAY}</lastmod><changefreq>{f}</changefreq><priority>{pr}</priority></url>\n" for u, pr, f in urls)
    sm += "</urlset>\n"
    write("sitemap.xml", sm)
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {S['domain']}/sitemap.xml\n")
    write("favicon.svg", '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#3f3f46"/><stop offset="1" stop-color="#09090b"/></linearGradient></defs>'
          '<rect width="64" height="64" rx="16" fill="url(#g)"/><path d="M38 14v22a11 11 0 0 1-22 0" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round"/><circle cx="48" cy="14" r="3.5" fill="#fff"/></svg>')
    write("site.webmanifest", json.dumps({"name": "Janta – Phones & Watches", "short_name": "Janta", "start_url": "/index.html",
                                          "display": "standalone", "background_color": "#ffffff", "theme_color": "#09090b",
                                          "icons": [{"src": "/favicon.svg", "sizes": "any", "type": "image/svg+xml"}]}, indent=2))


def product_images():
    d = os.path.join(ROOT, "assets", "img", "products")
    os.makedirs(d, exist_ok=True)
    for p in PRODUCTS:
        if p.get("photo"):
            continue
        with open(os.path.join(d, p["slug"] + ".svg"), "w", encoding="utf-8") as f:
            f.write(svgart.render(p["slug"][:12].replace("-", ""), esc(p["name"]), p["img"]))
        for g in p["options"]:
            for v in g["values"]:
                if v.get("spec"):
                    with open(os.path.join(ROOT, v["img"]), "w", encoding="utf-8") as f:
                        f.write(svgart.render(p["slug"][:12].replace("-", ""), esc(f'{p["name"]} – {v["label"]}'), v["spec"]))


def main():
    prepare_variants()
    img_dir = os.path.join(ROOT, "assets", "img", "products")
    if os.path.isdir(img_dir):
        shutil.rmtree(img_dir)
    prod_dir = os.path.join(ROOT, "products")
    if os.path.isdir(prod_dir):
        shutil.rmtree(prod_dir)
    product_images()
    page_home()
    page_shop()
    for k in CATS:
        page_shop(k)
    for p in PRODUCTS:
        page_product(p)
    page_about()
    page_contact()
    page_404()
    extras()
    print(f"Built {len(PRODUCTS)} products + 8 pages into {ROOT}")


if __name__ == "__main__":
    main()
