# -*- coding: utf-8 -*-
"""Lisää hiekkalaatikkodemoon (Mallikonepaja) koneet ja huoltokohteet Huollot-kuvaa varten. Keksittyä dataa.
Aja: CINTERIN_PORT=5301 python seed_huolto_mk.py  (seed_demo_2026.py ajettu ensin)"""
import datetime, json, os, urllib.request, urllib.error, http.cookiejar
B = "http://127.0.0.1:%s" % os.environ.get("CINTERIN_PORT", "5301")
op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
def a(p, d=None):
    r = urllib.request.Request(B + "/api" + p, data=json.dumps(d).encode() if d is not None else None, headers={"Content-Type": "application/json"})
    return json.loads(op.open(r).read())
a("/kirjaudu", {"email": "kari.luttinen@mallikonepaja.fi", "salasana": "demo1234"})
as_ = a("/asiakkaat"); as_ = as_.get("asiakkaat", as_) if isinstance(as_, dict) else as_
aid = next(x["id"] for x in as_ if "Pohjola" in (x.get("yritys") or x.get("nimi") or ""))
pv = lambda n: (datetime.date.today() + datetime.timedelta(days=n)).isoformat()
k = a("/koneet", {"asiakas_id": aid, "nimi": "Paineilmakompressori K2", "valmistaja": "Esimerkki", "malli": "KP-55", "sarjanumero": "DEMO-0001", "hankintapvm": pv(-900)})
kid = k.get("id")
for nimi, tyyp, vali, asen in [("Kompressorin vuosihuolto", "Kompressori", 12, pv(-400)), ("Imuilmasuodattimen vaihto", "Kompressori", 6, pv(-170)),
                               ("Hydrauliikan öljynvaihto", "Puristin", 12, pv(-120)), ("Nostolaitteen määräaikaistarkastus", "Nosturi", 12, pv(-330))]:
    h = a("/huoltokohteet", {"asiakas_id": aid, "nimi": nimi, "laitetyyppi": tyyp, "huoltovali_kk": vali, "asennuspvm": asen, "kone_id": kid if "Komp" in nimi or "Imu" in nimi else None, "huomiot": "Demo-aineisto"})
    print(nimi, h.get("seuraava_huolto") or h.get("ok"))
