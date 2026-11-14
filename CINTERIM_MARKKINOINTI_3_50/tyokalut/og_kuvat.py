# -*- coding: utf-8 -*-
"""Tekee og-lean.png ja og-huolto.png (1200x630) og-tuotanto.png:n ilmeellä."""
import pathlib
from PIL import Image, ImageDraw, ImageFont
R = pathlib.Path(__file__).resolve().parents[2]; W = R / "website"
BG = Image.open(W / "og-tuotanto.png").convert("RGB")
FB = "C:/Windows/Fonts/segoeuib.ttf"; FR = "C:/Windows/Fonts/segoeui.ttf"
def tee(nimi, kicker, otsikko_rivit, ala):
    im = BG.copy(); d = ImageDraw.Draw(im)
    d.rectangle((60, 170, 860, 440), fill=(16, 36, 74))       # peittää vanhan tekstialueen
    d.text((82, 192), kicker, font=ImageFont.truetype(FB, 26), fill=(128, 224, 230))
    y = 232
    for r in otsikko_rivit: d.text((80, y), r, font=ImageFont.truetype(FB, 62), fill=(255, 255, 255)); y += 76
    d.text((82, 392), ala, font=ImageFont.truetype(FR, 28), fill=(220, 230, 245))
    im.save(W / nimi, optimize=True); print(nimi)
tee("og-lean.png", "LEAN", ["Valmistuvatko tilaukset", "ajallaan?"], "Toimitusvarmuus · läpimenoaika · pullonkaulat")
tee("og-huolto.png", "HUOLLOT", ["Huoltohistoria ei ole", "yhden ihmisen muistissa."], "Huoltokirja · koneet · muistutukset · kuittaus")
