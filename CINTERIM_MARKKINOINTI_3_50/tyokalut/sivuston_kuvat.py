# -*- coding: utf-8 -*-
"""Tekee sivuston kuvat (webp, 480/800/1200 + täysi) 3.50.0-kaappauksista (kuvat/raaka) -> website/esimerkkikuvat/."""
import pathlib
from PIL import Image
R = pathlib.Path(__file__).resolve().parents[2]
RAW = R / "CINTERIM_MARKKINOINTI_3_50/kuvat/raaka"; OUT = R / "website/esimerkkikuvat"
KUVAT = [("30_aamupalaveri", "02_aamupalaveri", (0, 40, 2416, 1290)),
         ("31_tuotantotaulu", "03_taulu", (0, 40, 2416, 1180)),
         ("32_kuormitus", "07_kuormitus", (0, 40, 2416, 1650)),
         ("33_tyoaikaraportti", "04a_tyoaikakirjaus" if False else "04a_tyoaikaraportti", (0, 40, 2416, 1250)),
         ("34_huoltokohteet", "05_huollot", (0, 0, 1800, 560)),
         ("35_lean_mittarit", "01_lean", (0, 40, 2416, 9999)),
         ("36_kannattavuus_nyt", "08a_kannattavuus_nyt", (0, 0, 2416, 9999))]
for nimi, raaka, box in KUVAT:
    im = Image.open(RAW / (raaka + ".png")).convert("RGB")
    im = im.crop((box[0], box[1], min(box[2], im.width), min(box[3], im.height)))
    w0 = min(im.width, 1600)
    if im.width > w0: im = im.resize((w0, int(im.height * w0 / im.width)), Image.LANCZOS)
    for w in (480, 800, 1200):
        if w < im.width:
            im.resize((w, int(im.height * w / im.width)), Image.LANCZOS).save(OUT / ("%s-%d.webp" % (nimi, w)), "WEBP", quality=82, method=6)
    im.save(OUT / (nimi + ".webp"), "WEBP", quality=82, method=6)
    print(nimi, im.width, im.height)
