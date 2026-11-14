# -*- coding: utf-8 -*-
"""Kaappaa Cinterim 3.50.0 -näkymät markkinointikuvien pohjiksi (oikea ohjelma, Mallikonepaja-DEMO-data).
Ajo: CINTERIN_PORT=5301 python kaappaa_nakymat.py   (demopalvelin + seedit ajettu)"""
import os, pathlib, time
from playwright.sync_api import sync_playwright
B = "http://127.0.0.1:%s" % os.environ.get("CINTERIN_PORT", "5301")
OUT = pathlib.Path(__file__).resolve().parents[1] / "kuvat" / "raaka"; OUT.mkdir(parents=True, exist_ok=True)
N = [("01_lean", "nayta('tuotanto');tuotantoTabi('lean')", "#tu-pane-lean"),
     ("02_aamupalaveri", "nayta('tuotanto');tuotantoTabi('paiva')", "#tu-pane-paiva"),
     ("03_taulu", "nayta('tuotanto');tuotantoTabi('taulu')", "#tu-pane-taulu"),
     ("04a_tyoaikaraportti", "nayta('tuotanto');tuotantoTabi('raportti')", "#tu-pane-raportti"),
     ("04b_tyolista", "nayta('tuotanto');tuotantoTabi('tyolista')", "#tu-pane-tyolista"),
     ("06_seisonta", "nayta('tuotanto');tuotantoTabi('seisonta')", "#tu-pane-seisonta"),
     ("07_kuormitus", "nayta('tuotanto');tuotantoTabi('kuormitus')", "#tu-pane-kuormitus"),
     ("08a_kannattavuus_nyt", "nayta('tuotanto');tuotantoTabi('tilaukset')", "#tu-kannattavuus"),
     ("08b_vaiheiden_toteuma", "nayta('tuotanto');tuotantoTabi('toteuma')", "#tu-pane-toteuma")]
with sync_playwright() as p:
    try: br = p.chromium.launch(channel="msedge", headless=True)
    except Exception: br = p.chromium.launch(headless=True)
    ctx = br.new_context(viewport={"width": 1500, "height": 950}, device_scale_factor=2)
    ctx.add_init_script("try{localStorage.setItem('cinterin_tervetuloa_v1','1');}catch(e){}")
    pg = ctx.new_page(); errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.goto(B, wait_until="networkidle"); time.sleep(2)
    if pg.query_selector("#login-salasana"):
        pg.fill("#login-email", "kari.luttinen@mallikonepaja.fi"); pg.fill("#login-salasana", "demo1234")
        pg.press("#login-salasana","Enter"); pg.wait_for_selector("#login-salasana", state="detached"); pg.wait_for_load_state("networkidle"); time.sleep(2.5)
    pg.evaluate("document.getElementById('tervetuloa-modal')?.remove()")
    def kaappaa(nimi, js, sel, odota=3.5, maxh=None):
        pg.evaluate("var m=document.getElementById('modal');if(m){m.classList.add('hidden');}")
        pg.evaluate(js); time.sleep(odota)
        pg.evaluate("var n=document.getElementById('nav');if(n){n.style.visibility='hidden'}; var t=document.getElementById('topbar'); if(t){t.style.visibility='hidden'}; window.scrollTo(0,0)")
        el = pg.query_selector(sel); bb = el.bounding_box() if el else None
        if not bb or bb["height"] < 40: print(nimi, "TYHJÄ/EI LÖYDY", bb); return
        if maxh and bb["height"] > maxh:
            pg.screenshot(path=str(OUT / (nimi + ".png")), clip={"x": bb["x"], "y": bb["y"], "width": bb["width"], "height": maxh})
        else: el.screenshot(path=str(OUT / (nimi + ".png")))
        print(nimi, "OK", int(bb["width"]), int(bb["height"]))
    for n, js, sel in N: kaappaa(n, js, sel, maxh=900)
    # Huollot: asiakaskortti
    aid = pg.evaluate("fetch('/api/asiakkaat').then(r=>r.json()).then(d=>{d=d.asiakkaat||d;return (d.find(x=>(x.yritys||x.nimi||'').includes('Pohjola'))||{}).id})")
    kaappaa("05_huollot", "nayta('asiakkaat');avaaAsiakaskortti('%s');setTimeout(function(){var e=document.getElementById('asiakas-huollot-%s');if(e){var s=e.closest('div[style*=border]')||e.parentElement.parentElement;s.id='huolto-kaappaus';s.scrollIntoView();}},3000)" % (aid,aid), "#huolto-kaappaus", odota=6)
    br.close(); print("JS-virheet:", errs[:5])
