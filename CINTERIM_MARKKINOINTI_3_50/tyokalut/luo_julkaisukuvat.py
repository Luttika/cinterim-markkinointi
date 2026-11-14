# -*- coding: utf-8 -*-
"""Kokoaa 8 LinkedIn-kuvaa (1200x1200) oikeista ohjelmakaappauksista (kuvat/raaka). Kaappaukset: kaappaa_nakymat.py."""
import pathlib
from PIL import Image, ImageDraw, ImageFont
R = pathlib.Path(__file__).resolve().parents[2]; RAW = R / "CINTERIM_MARKKINOINTI_3_50/kuvat/raaka"; OUT = R / "CINTERIM_MARKKINOINTI_3_50/kuvat"
LOGO = R / "static/logo/cinterim-logo-valkoinen.png"
NAVY, BG, TXT, SUB = (16, 36, 74), (238, 242, 248), (255, 255, 255), (170, 195, 235)
FB, FR = "C:/Windows/Fonts/segoeuib.ttf", "C:/Windows/Fonts/segoeui.ttf"
def font(p, s): return ImageFont.truetype(p, s)
def wrap(d, t, f, w):
    rows, cur = [], ""
    for sana in t.split():
        k = (cur + " " + sana).strip()
        if d.textlength(k, font=f) <= w: cur = k
        else: rows.append(cur); cur = sana
    return rows + [cur]
KUVAT = [  # (tiedosto, otsikko, polku ohjelmassa, [(raakakuva, (x0,y0,x1,y1) tai None)])
 ("01_lean", "Koneet käyvät. Miksi tilaukset myöhästyvät?", "Tuotanto → Lean-mittarit", [("01_lean", (0, 130, 1800, 9999))]),
 ("02_aamupalaveri", "Aamupalaveri ilman tiedon etsimistä", "Tuotanto → Aamupalaveri", [("02_aamupalaveri", (0, 100, 1440, 1000))]),
 ("03_tuotantotaulu", "”Työn alla”. Mutta missä vaiheessa?", "Tuotanto → Taulu", [("03_taulu", (0, 100, 2416, 1130))]),
 ("04_tyoaikaraportti", "Paljonko tuottava työtunti maksaa?", "Tuotanto → Työaikaraportti", [("04a_tyoaikaraportti", (0, 100, 2416, 1260))]),
 ("05_huollot", "Milloin kone huollettiin viimeksi?", "Asiakkaat → Huollot", [("05_huollot", (0, 0, 1800, 560))]),
 ("06_seisonta", "Kone seisoo tunnin. Paljonko se maksaa?", "Tuotanto → Seisonta", [("06_seisonta", (0, 180, 2416, 1180))]),
 ("07_kuormitus", "Kalenteri täynnä. Entä tuotanto?", "Tuotanto → Kuormitus", [("07_kuormitus", (0, 190, 2416, 1640))]),
 ("08_kannattavuus_nyt", "Kannattavuus näkyy jo työn aikana", "Tuotanto → Kannattavuus nyt", [("08a_kannattavuus_nyt", None)]),
]

KUVATEKSTIT = {
 1: "Korkea käyttöaste ei kerro, valmistuuko tilaus ajallaan. Toimitusvarmuus, läpimenoaika ja jonotus kertovat.",
 2: "Myöhässä olevat tilaukset, 7 päivän toimitukset, esteet ja käynnissä olevat työt yhdellä sivulla.",
 3: "Avoin, kesken, este, valmis: tilauksen todellinen eteneminen vaihe vaiheelta.",
 4: "Maksettu työtunti ja tilaukselle kohdistunut tuottava työtunti eivät ole sama asia.",
 5: "Huoltokohteet, huoltokirja ja muistutukset yhdessä paikassa, ei yhden ihmisen muistin varassa.",
 6: "Seisonnan syy ja kirjattu resurssikustannus näkyvät. Euroarvo ei ole menetetty kate.",
 7: "Kokonaiskuorma ja resurssikohtainen kuorma: näet missä on kapasiteettia ja missä ruuhka.",
 8: "Ennustettu kate ja valmiusaste näkyvät jo työn aikana, eivät vasta jälkilaskennassa.",
}
for i, (nimi, otsikko, polku, osat) in enumerate(KUVAT, 1):
    im = Image.new("RGB", (1200, 1200), BG); d = ImageDraw.Draw(im)
    d.rectangle((0, 0, 1200, 360), fill=NAVY)
    lg = Image.open(LOGO).convert("RGBA"); lg = lg.resize((int(lg.width * 46 / lg.height), 46)); im.paste(lg, (60, 48), lg)
    f = font(FB, 20); t = "TEOLLISUUDEN KANNATTAVUUS KÄYTÄNNÖSSÄ  %d/8" % i; d.text((1140 - d.textlength(t, font=f), 60), t, font=f, fill=SUB)
    ft = font(FB, 64); y = 140
    for r in wrap(d, otsikko, ft, 1080): d.text((60, y), r, font=ft, fill=TXT); y += 78
    d.text((60, 300), polku, font=font(FR, 30), fill=SUB)
    kuvat = []
    for raaka, box in osat:
        s = Image.open(RAW / (raaka + ".png")).convert("RGB")
        if box: s = s.crop((box[0], box[1], min(box[2], s.width), min(box[3], s.height)))
        kuvat.append(s)
    kuvat_s = []
    for s in kuvat:
        h = 1080 / s.width; s = s.resize((1080, max(1, int(s.height * h))), Image.LANCZOS)
        if s.height > 560: k = 560 / s.height; s = s.resize((int(s.width * k), 560), Image.LANCZOS)
        kuvat_s.append(s)
    kork = sum(s.height for s in kuvat_s); alku = 385 + min(110, max(0, (700 - kork - 140) // 2))
    for s in kuvat_s:
        x = 60 + (1080 - s.width) // 2
        d.rounded_rectangle((x - 6, alku - 6, x + s.width + 6, alku + s.height + 6), 10, fill=(255, 255, 255), outline=(205, 215, 232), width=2)
        im.paste(s, (x, alku)); alku += s.height + 16
    fc = font(FB, 34); yy = alku + 14
    for r in wrap(d, KUVATEKSTIT[i], fc, 1080): d.text((60, yy), r, font=fc, fill=NAVY); yy += 46
    d.text((60, 1128), "Esimerkkiaineisto (testidata) · Cinterim 3.50.0", font=font(FR, 24), fill=(70, 90, 125))
    t = "cinterim.fi"; d.text((1140 - d.textlength(t, font=font(FB, 28)), 1124), t, font=font(FB, 28), fill=NAVY)
    im.save(OUT / (nimi + ".png"), optimize=True); print(nimi, "OK")
