# -*- coding: utf-8 -*-
"""Sivuston laadunvarmistus: sisäiset linkit, kuvat, metatiedot, otsikkorakenne, vaakavieritys (375/768/1280 px).
Vaatii paikallisen palvelimen: cd website && python -m http.server 8090"""
import json, pathlib, re, sys, urllib.parse
from playwright.sync_api import sync_playwright
R = pathlib.Path(__file__).resolve().parents[2]; W = R / "website"
SIVUT = ["index", "tuotanto", "lean", "huolto", "ominaisuudet", "palvelu", "teollisuus", "jalkilaskenta"]
tulos = {"linkit": [], "meta": [], "asettelu": [], "kuvat": []}

# ── Sisäiset linkit (kaikki html-sivut) ──
rew = {}
for rivi in (W / "_redirects").read_text(encoding="utf-8").splitlines():
    o = rivi.split()
    if len(o) >= 3 and o[0].startswith("/") and o[2].startswith("200"): rew[o[0]] = o[1]
    if len(o) >= 3 and o[0].startswith("/") and o[2].startswith("30"): rew.setdefault(o[0], "REDIR")
def ok_polku(p):
    p = p.split("#")[0].split("?")[0]
    if p in ("", "/"): return True
    if p in rew: return True
    f = W / p.lstrip("/")
    if f.is_file(): return True
    if p.endswith("/") and (W / p.lstrip("/") / "index.html").is_file(): return True
    # /oppaat/<slug> -> opas-<slug>.html tai wildcard-sääntö
    return any(p.startswith(k.rstrip("*").rstrip("/")) for k in rew if k.endswith("*"))
rikki = set()
for f in sorted(W.glob("*.html")):
    s = f.read_text(encoding="utf-8")
    for h in re.findall(r'(?:href|src)="(/[^"]*)"', s):
        if not ok_polku(h): rikki.add((f.name, h))
    for h in re.findall(r'srcset="([^"]*)"', s):
        for u in re.findall(r"(/[^\s,]+)\s+\d+w", h):
            if not ok_polku(u): rikki.add((f.name, u))
tulos["linkit"] = sorted(rikki)

with sync_playwright() as p:
    try: br = p.chromium.launch(channel="msedge", headless=True)
    except Exception: br = p.chromium.launch(headless=True)
    for sivu in SIVUT:
        url = "http://127.0.0.1:8090/%s.html" % sivu
        # metatiedot ja otsikkorakenne
        ctx = br.new_context(viewport={"width": 1280, "height": 900}); pg = ctx.new_page(); virheet = []
        pg.on("pageerror", lambda e: virheet.append(str(e)))
        pg.goto(url, wait_until="networkidle")
        m = pg.evaluate("""()=>({title:document.title,
          desc:(document.querySelector('meta[name=description]')||{}).content||'',
          canon:(document.querySelector('link[rel=canonical]')||{}).href||'',
          ogt:(document.querySelector('meta[property="og:title"]')||{}).content||'',
          ogi:(document.querySelector('meta[property="og:image"]')||{}).content||'',
          h1:document.querySelectorAll('h1').length,
          h:[...document.querySelectorAll('h1,h2,h3')].map(e=>+e.tagName[1]),
          ld:[...document.querySelectorAll('script[type="application/ld+json"]')].map(s=>{try{JSON.parse(s.textContent);return 1}catch(e){return 0}}),
          imgsAlt:[...document.querySelectorAll('img')].filter(i=>!i.hasAttribute('alt')).length,
          rikkiKuva:[...document.querySelectorAll('img')].filter(i=>i.complete&&i.naturalWidth===0).map(i=>i.src)})""")
        hyppy = sum(1 for a, b in zip(m["h"], m["h"][1:]) if b - a > 1)
        tulos["meta"].append({"sivu": sivu, "title_pituus": len(m["title"]), "desc_pituus": len(m["desc"]), "canonical": m["canon"], "og_image": m["ogi"],
                              "h1": m["h1"], "otsikkotason_hypyt": hyppy, "ld_json_ok": m["ld"], "img_ilman_alt": m["imgsAlt"], "rikkinaiset_kuvat": m["rikkiKuva"], "js_virheet": virheet})
        ctx.close()
        for lev in (375, 768, 1280):
            c = br.new_context(viewport={"width": lev, "height": 900}); g = c.new_page(); g.goto(url, wait_until="networkidle")
            r = g.evaluate("()=>({sw:document.documentElement.scrollWidth,cw:document.documentElement.clientWidth})")
            tulos["asettelu"].append({"sivu": sivu, "leveys": lev, "scrollWidth": r["sw"], "clientWidth": r["cw"], "vaakavieritys": r["sw"] > r["cw"] + 1})
            if lev == 375 and sivu in ("lean", "huolto", "tuotanto"):
                g.screenshot(path=str(R / ("CINTERIM_MARKKINOINTI_3_50/dokumentaatio/qa_%s_375.png" % sivu)), full_page=True)
            c.close()
    br.close()
json.dump(tulos, open(R / "CINTERIM_MARKKINOINTI_3_50/dokumentaatio/qa_tulos.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("rikkinäiset linkit:", tulos["linkit"][:20], len(tulos["linkit"]))
for m in tulos["meta"]: print(m["sivu"], "title", m["title_pituus"], "desc", m["desc_pituus"], "h1", m["h1"], "hypyt", m["otsikkotason_hypyt"], "ld", m["ld_json_ok"], "altpuute", m["img_ilman_alt"], "rikkikuvat", m["rikkinaiset_kuvat"], "js", m["js_virheet"], m["og_image"])
print("vaakavieritys:", [(a["sivu"], a["leveys"]) for a in tulos["asettelu"] if a["vaakavieritys"]])
