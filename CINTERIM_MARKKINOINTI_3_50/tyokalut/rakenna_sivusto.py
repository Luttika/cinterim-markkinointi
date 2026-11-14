# -*- coding: utf-8 -*-
"""Rakentaa sivustopäivityksen website/-kansioon: uudet sivut /lean ja /huolto, tuotanto.html:n laajennus,
lisämoduuli- ja hintatiedot (index, ominaisuudet), navigaatio/alatunniste, sitemap, redirects, llms.txt.
AJETAAN KERRAN puhtaalle website/-kansiolle (git checkout website/ ennen uusintaa)."""
import pathlib, re, datetime
R = pathlib.Path(__file__).resolve().parents[2]; W = R / "website"
PVM = "2026-10-09"
import sys; sys.path.insert(0, str(R))
import taso as _taso   # hinnat luetaan taso.py:stä: ne muuttuvat, joten niitä ei kirjoiteta käsin


def hinta(nimi):
    """'59 €/kk tai 590 €/vuosi' taso.LISAMODUULIT-tiedoista. Ei hintaa -> 'hinta ei ole vielä julkinen'."""
    m = _taso.LISAMODUULIT[nimi]
    if m.get("hinta_kk") is None:
        return "hinta ei ole vielä julkinen"
    return "%s €/kk tai %s €/vuosi" % (m["hinta_kk"], m["hinta_vuosi"])

def rd(n): return (W / n).read_text(encoding="utf-8")
def wr(n, s):
    s = re.sub(r"\{\{H:(\w+)\}\}", lambda m: hinta(m.group(1)), s)
    (W / n).write_text(s, encoding="utf-8", newline="\n")
def ersata(s, a, b, kerrat=1):
    assert a in s, "EI LÖYDY: " + a[:80]
    return s.replace(a, b, kerrat)

def img(nimi, alt, w, h, lazy=True, sizes="(max-width: 760px) 92vw, 570px"):
    ss = ", ".join("/esimerkkikuvat/%s-%d.webp %dw" % (nimi, x, x) for x in (480, 800, 1200) if x < 1600) + ", /esimerkkikuvat/%s.webp 1600w" % nimi
    return ('<img src="/esimerkkikuvat/%s-800.webp" alt="%s" width="%d" height="%d" decoding="async" %s srcset="%s" sizes="%s">'
            % (nimi, alt, w, h, 'loading="lazy"' if lazy else 'loading="eager" fetchpriority="high"', ss, sizes))

def kortit(rivit):
    return '<div class="feature-grid">' + "".join('<div class="card feature-card"><small>%s</small><h3>%s</h3><p>%s</p></div>' % r for r in rivit) + '</div>'

def faq(kk):
    return "".join("<details><summary>%s</summary><p>%s</p></details>" % k for k in kk)

def ldjson(url, otsikko, kuvaus, nimi_krumbs, kk):
    import json
    g = [{"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": otsikko, "description": kuvaus, "inLanguage": "fi-FI",
          "isPartOf": {"@id": "https://cinterim.fi/#website"}, "about": {"@id": "https://cinterim.fi/#software"}, "dateModified": PVM},
         {"@type": "BreadcrumbList", "itemListElement": [
             {"@type": "ListItem", "position": 1, "name": "Cinterim", "item": "https://cinterim.fi/"},
             {"@type": "ListItem", "position": 2, "name": nimi_krumbs, "item": url}]}]
    if kk:
        g.append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in kk]})
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": g}, ensure_ascii=False, separators=(",", ":")) + "</script>"

def uusi_sivu(pohja, polku, title, desc, og_kuva, main_html, ld):
    """Pohjana tuotanto.html: otsikko/metat/ld vaihdetaan, <main> korvataan, latausosio ja alatunniste säilyvät."""
    url = "https://cinterim.fi/" + polku
    a = pohja.index("<title>"); b = pohja.index('<link rel="preconnect" href="https://gateway.umami.is"')
    head = ('<title>%s</title><meta name="description" content="%s"><link rel="canonical" href="%s"><meta property="og:type" content="website">'
            '<meta property="og:site_name" content="Cinterim"><meta property="og:locale" content="fi_FI"><meta property="og:url" content="%s">'
            '<meta property="og:title" content="%s"><meta property="og:description" content="%s"><meta property="og:image" content="https://cinterim.fi/%s">'
            '<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="%s"><meta name="twitter:description" content="%s">'
            '<meta name="twitter:image" content="https://cinterim.fi/%s">%s') % (title, desc, url, url, title, desc, og_kuva, title, desc, og_kuva, ld)
    s = pohja[:a] + head + pohja[b:]
    m0 = s.index("<main>") + len("<main>"); m1 = s.index('<section class="download5"')
    return s[:m0] + main_html + s[m1:]

CTA = '<div class="actions"><a class="btn btn-primary" href="/#lataa">Kokeile 30 päivää</a><a class="btn btn-outline" href="/varaa">Varaa 30 min esittely</a></div>'
def hero(krumb, eyebrow, h1, lead, kuva_html):
    return ('<section class="page-hero"><div class="container"><div class="crumb"><a href="/">Cinterim</a> / %s</div><span class="eyebrow">%s</span>'
            '<h1>%s</h1><p>%s</p>%s<div class="page-shot">%s</div></div></section>' % (krumb, eyebrow, h1, lead, CTA, kuva_html))
def jatko(otsikko, teksti, linkit):
    return ('<section class="section"><div class="container center"><span class="badge">Jatka</span><h2>%s</h2><p class="lead">%s</p><p style="margin-top:22px">%s</p></div></section>'
            % (otsikko, teksti, " ".join('<a class="btn %s" href="%s">%s</a>' % x for x in linkit)))

# ───────────────────────── LEAN ─────────────────────────
LEAN_FAQ = [
 ("Mitä Lean-mittarit laskevat?", "Toimitusvarmuuden, läpimenoajan, virtaustehokkuuden arvion, jonotuksen ennen vaihetta, pullonkaulat, hylkäysten Pareton, koneiden OEE-arvion ja Andon-tilastot. Luvut lasketaan valmistuneista tilauksista ja kirjatuista työtunneista."),
 ("Optimoiko Cinterim tuotantoa automaattisesti?", "Ei. Lean-mittarit näyttävät mitä tuotannossa tapahtuu ja missä aika odottaa. Aikataulutusta tai automaattista optimointia ohjelmassa ei ole."),
 ("Kuinka monta valmista tilausta mittarit tarvitsevat?", "Mittarit toimivat heti, mutta alle viiden valmistuneen tilauksen otos on pieni. Ohjelma varoittaa siitä, jotta yksittäinen tilaus ei näytä trendiltä."),
 ("Tarvitaanko LEAN-moduuli erikseen?", "Kyllä. LEAN on lisämoduuli, joka vaatii Pro- tai Business-lisenssin ja Tuotanto-lisämoduulin (Työaika ja kohdistusaste). LEAN-moduulin hinta on {{H:lean}} (alv 0 %), kysy tarjous esittelyssä."),
]
lean_main = (
 hero("LEAN", "LEAN-mittarit konepajalle",
      "Koneet käyvät. Valmistuvatko tilaukset ajallaan?",
      "Korkea käyttöaste ei kerro, saako asiakas tilauksensa sovittuna päivänä. Cinterimin Lean-mittarit laskevat toimitusvarmuuden, läpimenoajan, jonotuksen ja pullonkaulat valmistuneista tilauksista ja kirjatuista työtunneista.",
      img("35_lean_mittarit", "Cinterimin Lean-mittarit: toimitusvarmuus, läpimenoaika, virtaustehokkuus ja työtä per tilaus (esimerkkiaineisto)", 1600, 441, lazy=False))
 + '<section class="section"><div class="container center"><span class="badge">Mittarit</span><h2>Mittarit ja työkalut, jotka katsovat tuotantoa asiakkaan päästä.</h2>'
 + kortit([
   ("TOIMITUS", "Toimitusvarmuus", "Valmistuneista tilauksista se osuus, joka valmistui toimituspäivään mennessä. Näkyy kuukausittain ja keskimääräisenä myöhästymisenä."),
   ("AIKA", "Läpimenoaika", "Kauanko tilaus on tuotannossa ensimmäisestä kirjauksesta viimeiseen valmistuneeseen vaiheeseen."),
   ("VIRTAUS", "Virtaustehokkuus (arvio)", "Kirjattu työ suhteessa arkipäiviin, työpäivän pituuteen ja tilauksella mukana olleisiin resursseihin. Arvio, ei mittaus."),
   ("JONO", "Jonotus ennen vaihetta", "Montako päivää työ odottaa edellisen vaiheen valmistumisesta seuraavan ensimmäiseen kirjaukseen. Pitkä jonotus on hukkaa."),
   ("PULLONKAULA", "Pullonkaulat", "Avoin työ suhteessa viikkokapasiteettiin. Näet, missä resurssissa työ kasautuu."),
   ("HUKKA", "Hylkäys-Pareto", "Hylätyt kappaleet syineen suuruusjärjestyksessä, jotta korjaus kohdistuu merkittävimpään syyhyn."),
   ("TRENDIT", "Lean-trendit, FPY ja WIP", "Toimitusvarmuus, läpimeno ja ensikertalaatu (FPY) kuukausittain sekä keskeneräinen työ (WIP) resurssia kohden, ylitys merkitään asetetusta rajasta."),
   ("KAIZEN", "Kaizen-lista", "Kehitysehdotukset hukkalajeineen, vastuuhenkilöineen, tiloineen ja tuloksineen. Valmistumispäivä kirjautuu kun ehdotus tehdään."),
   ("5S", "5S-tarkastukset", "Alueittainen pisteytys 0–5 viidelle S:lle, tulos prosentteina ja muutos edelliseen tarkastukseen. Heikoin alue ensin."),
   ("OEE", "OEE-arvio ja Andon-tilastot", "Koneille käytettävyys, suorituskyky ja laatu. Andon-kutsujen syyt ja keskimääräinen vasteaika."),
 ]) + '</div></section>'
 + '<section class="section alt"><div class="container split"><div><span class="kicker">Mistä luvut tulevat</span><h2>Ei erillistä kirjaamista Lean-raportteja varten.</h2>'
   '<p class="lead" style="margin:0">Mittarit johdetaan tilausten vaiheista ja työpisteissä tehdyistä kirjauksista: aloitus, lopetus, valmistuneet ja hylätyt kappaleet sekä esteet. Samat kirjaukset ovat jälkilaskennan työtunteja.</p>'
   '<ul class="checklist"><li>Mittarit lasketaan valmistuneista tilauksista (kaikki vaiheet valmiit)</li><li>Alle viiden valmiin tilauksen otoksesta ohjelma varoittaa</li><li>Esteen syy on vain nykytilaa, joten esteistä ei voi tehdä jaksovertailua</li><li>Päivätarkkuus: osa tiedoista perustuu kirjauspäivään, ei kellonaikaan</li></ul></div>'
   '<div class="visual">' + img("31_tuotantotaulu", "Cinterimin tuotantotaulu: avoin, kesken, este ja valmis (esimerkkiaineisto)", 1600, 754) + '</div></div></section>'
 + '<section class="section"><div class="container split reverse"><div><span class="kicker">Rajaukset</span><h2>Mitä Lean-mittarit eivät tee.</h2>'
   '<ul class="checklist"><li>Ei optimoi tuotantoa tai aikatauluta töitä automaattisesti</li><li>Kaizen-lista ja 5S-tarkastukset kirjaavat parannustyön, mutta eivät tee sitä puolestasi</li><li>Virtaustehokkuus ja OEE ovat arvioita kirjausten perusteella</li><li>Luvut ovat niin hyviä kuin kirjaukset: jos työ ei kirjaudu, mittarikaan ei näe sitä</li></ul></div>'
   '<div><span class="badge">Lisämoduuli</span><h3 style="margin-top:12px">LEAN-lisämoduuli</h3><p class="lead" style="margin:0">Vaatii Pro- tai Business-lisenssin sekä Tuotanto-lisämoduulin (Työaika ja kohdistusaste, {{H:tyoaika}}, alv 0 %). LEAN-moduulin hinta on {{H:lean}} (alv 0 %). Pro-kokeilun ensimmäisten 14 päivän aikana lisämoduulit ovat kokeiltavissa.</p>'
   '<p style="margin-top:18px"><a class="text-link" href="/tuotanto">Katso koko tuotannonohjaus →</a></p></div></div></section>'
 + '<section class="section alt"><div class="container"><span class="badge">Usein kysyttyä</span><h2>LEAN-mittarit käytännössä</h2>' + faq(LEAN_FAQ) + '</div></section>'
 + jatko("Kokeile omilla tilauksillasi.", "Asenna Cinterim ja katso, mitä toimitusvarmuutesi ja läpimenoaikasi kertovat.",
         [("btn-primary", "/#lataa", "Kokeile 30 päivää"), ("btn-navy", "/tuotanto", "Tuotannonohjaus"), ("btn-outline", "/varaa", "Varaa esittely")])
)

# ───────────────────────── HUOLTO ─────────────────────────
HUOLTO_FAQ = [
 ("Kuuluuko huoltokirja Pro-lisenssiin?", "Kyllä. Huoltokohteet, koneet, huoltokirja, muistutukset ja kuittaukset kuuluvat Pro-lisenssiin (49 €/kk, alv 0 %). Erillistä lisämoduulia ei tarvita."),
 ("Mikä on Huolto ja asennus -lisämoduuli?", "Lisämoduuli tuo huolto- ja asennustyölle työmääräimet (tunnit, tarvikkeet, matkat, työraportti, lasku ja kate), aikataulun ja asentajan puhelinnäkymän. Hinta on {{H:huolto}} (alv 0 %) Pro- tai Business-lisenssin päälle. Huoltokirja toimii ilman sitä."),
 ("Miten seuraava huolto lasketaan?", "Seuraava huolto on edellinen huolto, tai asennuspäivä jos huoltoa ei ole vielä tehty, plus huoltoväli. Oletus on 12 kuukautta. Kun huolto kuitataan tehdyksi, seuraava huolto siirtyy eteenpäin."),
 ("Menevätkö huoltotiedot hukkaan, jos kohde poistetaan?", "Ei. Poistopainike arkistoi kohteen. Se katoaa listasta, luvuista ja muistutuksista, mutta huoltohistoria säilyy ja kohteen voi palauttaa asiakaskortin arkistoidut kohteet -listasta."),
]
huolto_main = (
 hero("Huolto", "Huoltojen hallinta",
      "Huoltohistoria ei saa olla yhden ihmisen muistin varassa.",
      "Cinterimin huoltokirja kokoaa asiakkaiden koneet, huoltokohteet, huoltovälit ja kuittaukset yhteen paikkaan. Seuraava huolto lasketaan automaattisesti ja erääntyvät huollot näkyvät listassa.",
      img("34_huoltokohteet", "Cinterimin huoltokohteet: seuraava huolto, erääntynyt huolto punaisella, kuittaus, historia ja työmääräin (esimerkkiaineisto)", 1600, 497, lazy=False))
 + '<section class="section"><div class="container center"><span class="badge">Pro-lisenssi</span><h2>Huoltokirja, koneet ja muistutukset.</h2>'
 + kortit([
   ("KOHTEET", "Huoltokohteet", "Kullekin kohteelle nimi, laitetyyppi, asennuspäivä ja huoltoväli. Seuraava huolto lasketaan itse."),
   ("KONEET", "Konerekisteri", "Valmistaja, malli, sarjanumero ja hankintapäivä. Koneelle voi liittää liitteitä ja useita huoltokohteita."),
   ("HUOLTOKIRJA", "Kuittaus ja historia", "Kuittaa huolto päivämäärällä ja kuvauksella. Käynti kirjautuu historiaan ja seuraava huolto siirtyy eteenpäin."),
   ("MUISTUTUS", "Erääntyvät huollot", "Huollot-välilehti ja Dashboardin Huoltokirja-kortti näyttävät erääntyvät ja erääntyneet kohteet. Suodata 30 päivän sisällä erääntyviin."),
   ("LASKUTUS", "Laskutustapa kohteelle", "Erikseen laskutettava huolto tarjoaa kuittauksen jälkeen pikanapin tarjoukseen. Huoltosopimukseen kuuluvaa käyntiä ei laskuteta erikseen."),
   ("ARKISTO", "Arkistointi ja palautus", "Poistopainike arkistoi kohteen. Historia säilyy ja kohteen voi palauttaa."),
 ]) + '</div></section>'
 + '<section class="section alt"><div class="container split"><div><span class="kicker">Huolto ja asennus -lisämoduuli</span><h2>Kun huoltotyö pitää tehdä, raportoida ja laskuttaa.</h2>'
   '<p class="lead" style="margin:0">Lisämoduuli tuo huolto- ja asennustyölle työmääräimen: yksi työ asiakkaan kohteessa, tunnit, tarvikkeet, matkat, työraportti, lasku ja kate.</p>'
   '<ul class="checklist"><li>Työmääräimet tunneilla, tarvikkeilla ja matkoilla</li><li>Hinnaton työraportti asiakkaalle</li><li>Aikataulu vastuuhenkilöittäin ja päivittäin</li><li>Asentajan puhelinnäkymä PIN-koodilla, ei hintoja</li><li>Valmis huoltotyö kirjautuu huoltohistoriaan</li></ul>'
   '<p style="margin-top:14px"><b>{{H:huolto}}</b> (alv 0 %) Pro- tai Business-lisenssin päälle. Ei vaadi Tuotanto-lisämoduulia.</p></div>'
   '<div class="visual">' + img("33_tyoaikaraportti", "Cinterimin työaikaraportti, jonka tunnit syntyvät työ- ja huoltokirjauksista (esimerkkiaineisto)", 1600, 790) + '</div></div></section>'
 + '<section class="section"><div class="container"><span class="badge">Usein kysyttyä</span><h2>Huoltojen hallinta käytännössä</h2>' + faq(HUOLTO_FAQ) + '</div></section>'
 + jatko("Ota huoltohistoria pois muistista.", "Kokeile huoltokirjaa omilla koneillasi ja asiakkaillasi Pro-kokeilussa.",
         [("btn-primary", "/#lataa", "Kokeile 30 päivää"), ("btn-navy", "/palvelu", "Huolto ja asennus"), ("btn-outline", "/varaa", "Varaa esittely")])
)

# ───────────────────────── TUOTANTO-sivun laajennus ─────────────────────────
TUOTANTO_LISA = (
 '<section class="section" id="paivittainen"><div class="container"><div class="center"><span class="badge">Päivittäinen johtaminen</span><h2>Kuusi näkymää tilauksen todelliseen tilanteeseen.</h2>'
 '<p class="lead">Kaikki näkymät johdetaan samoista tilauksen vaiheista ja työpisteiden kirjauksista. Mitään ei kirjata erikseen raportointia varten.</p></div>'
 '<div id="aamupalaveri" class="split" style="margin-top:36px"><div><span class="kicker">Aamupalaveri</span><h3>Palaveri päätöksiin, ei tiedon etsimiseen.</h3><p>Myöhässä olevat tilaukset, toimitukset seuraavan 7 päivän aikana, esteet, avoimet apukutsut, käynnissä olevat työt sekä edellisen työpäivän valmistuneet vaiheet ja hylätyt kappaleet yhdellä sivulla. Tulostettavassa A4:ssä on tilaa sovituille toimenpiteille.</p></div>'
 '<div class="visual">' + img("30_aamupalaveri", "Cinterimin aamupalaveri: myöhässä olevat tilaukset, esteet, apukutsut ja käynnissä olevat työt (esimerkkiaineisto)", 1600, 827) + '</div></div>'
 '<div id="taulu" class="split reverse" style="margin-top:44px"><div><span class="kicker">Tuotantotaulu</span><h3>Avoin, kesken, este, valmis.</h3><p>Taulu näyttää tilausten työvaiheet neljässä sarakkeessa työpisteen, toimituspäivän ja jäljellä olevan työn kanssa. Kesken-tila syntyy, kun työntekijä aloittaa vaiheen, ja este kun työtä ei voi tehdä. Taulu on näkymä: tilaa ei muuteta vetämällä, jotta tunnit ja tila pysyvät yhdessä totuudessa.</p></div>'
 '<div class="visual">' + img("31_tuotantotaulu", "Cinterimin tuotantotaulu: avoin, kesken, este ja valmis (esimerkkiaineisto)", 1600, 754) + '</div></div>'
 '<div id="tyoaika" class="split" style="margin-top:44px"><div><span class="kicker">Työajan kirjaus</span><h3>Maksettu tunti ja tuottava tunti eivät ole sama asia.</h3><p>Työntekijä kirjaa työn työpisteessä PIN-koodilla: aloitus, lopetus, valmistuneet kappaleet ja este. Työaikaraportti näyttää kirjatut tunnit henkilöittäin, kuormitusryhmittäin, vaiheittain tai tilauksittain sekä käyttöasteen, vapaan kapasiteetin ja tilaustyön osuuden. Raportin voi viedä CSV:nä Exceliin.</p>'
 '<p>Samat kirjaukset ovat jälkilaskennan työtunteja, joten tuotannon kirjaus ja kannattavuuden seuranta käyttävät samaa dataa.</p></div>'
 '<div class="visual">' + img("33_tyoaikaraportti", "Cinterimin työaikaraportti ja nelikenttä käyttöasteesta ja tilaustyön osuudesta (esimerkkiaineisto)", 1600, 790) + '</div></div>'
 '<div id="kuormitus" class="split reverse" style="margin-top:44px"><div><span class="kicker">Kuormitus</span><h3>Kalenteri täynnä ei tarkoita, että tuotanto on täynnä.</h3><p>Jäljellä oleva työ jaetaan viikoille toimitukseen asti ja näytetään resursseittain lämpökarttana (vihreä alle 85 %, keltainen yli 85 %, punainen yli 100 %). Lomat ja poissaolot pienentävät kapasiteettia. Näet vapaan kapasiteetin ja ruuhkaisimman resurssin. Näkymä on arvio tilausten suunnitelluista tunneista, ei aikataulutus.</p></div>'
 '<div class="visual">' + img("32_kuormitus", "Cinterimin kuormitus: viikkolämpökartta ja resurssikohtainen kuormitus (esimerkkiaineisto)", 1600, 1066) + '</div></div>'
 '<div id="kannattavuus" class="split" style="margin-top:44px"><div><span class="kicker">Kannattavuus nyt</span><h3>Poikkeama näkyy jo työn aikana.</h3><p>Tilauksen arvio jäädytetään, kun tarjous muuttuu tilaukseksi. Kannattavuus nyt vertaa sitä toteutuneisiin tunteihin ja näyttää ennustetun katteen, arvioidun valmiusasteen ja huomiota vaativat työt. Kun tietoa on vähän, ohjelma ei ekstrapoloi vaan näyttää vain jo kirjatun ylityksen. Luvut ovat arvioita.</p></div>'
 '<div class="visual">' + img("36_kannattavuus_nyt", "Cinterimin Kannattavuus nyt: ennustettu kate, arvioitu valmiusaste ja huomiota vaativat työt (esimerkkiaineisto)", 1600, 443) + '</div></div>'
 '<p class="center" style="margin-top:34px"><a class="text-link" href="/lean">LEAN-mittarit: toimitusvarmuus, läpimenoaika ja pullonkaulat →</a> &nbsp; <a class="text-link" href="/huolto">Huoltojen hallinta →</a> &nbsp; <a class="text-link" href="/jalkilaskenta">Jälkilaskenta →</a></p>'
 '</div></section>')

LISAMODUULIT = (
 '<section class="section" id="lisamoduulit"><div class="container center"><span class="badge">Lisämoduulit</span><h2>Lisää vain se, mitä tarvitset.</h2>'
 '<p class="lead">Lisämoduulit edellyttävät Pro- tai Business-lisenssin. Hinnat alv 0 %, vuosilaskutus vastaa 10 kuukauden hintaa.</p>'
 + kortit([
   ("TUOTANTO", "Työaika ja kohdistusaste", "Työlista ja kioski, työaikakirjaukset, tuotantotaulu, aamupalaveri, kuormitus, vaiheiden toteuma, seisonta, Andon, työaikaraportti ja Kannattavuus nyt. <b>{{H:tyoaika}}.</b>"),
   ("LEAN", "LEAN", "Toimitusvarmuus, läpimenoaika, virtaustehokkuus, jonotus, pullonkaulat, hylkäys-Pareto, OEE-arvio, trendit, Kaizen-lista ja 5S-tarkastukset. Vaatii Tuotanto-moduulin. <b>{{H:lean}}.</b> <a class=\"text-link\" href=\"/lean\">Lue lisää →</a>"),
   ("HUOLTO", "Huolto ja asennus", "Työmääräimet, huoltoaikataulu ja asentajan puhelinnäkymä. Huoltokirja kuuluu Prohon ilman moduulia. <b>{{H:huolto}}.</b> <a class=\"text-link\" href=\"/huolto\">Lue lisää →</a>"),
   ("KOONTINÄYTTÖ", "Koontinäyttö", "Tuotannon mittarit isolle näytölle tai TV:lle hallissa. Vaatii Tuotanto-moduulin. <b>{{H:koontinaytto}}.</b>"),
 ])
 + '<p class="fine" style="margin-top:20px">Pro-kokeilun ensimmäisten 14 päivän aikana lisämoduulit ovat kokeiltavissa.</p>'
 '</div></section>')

def main():
    t = rd("tuotanto.html")
    # uudet sivut ennen tuotanto.html:n muokkausta (pohjana alkuperäinen)
    ld_lean = ldjson("https://cinterim.fi/lean", "LEAN-mittarit konepajalle", "Cinterimin LEAN-lisämoduuli laskee toimitusvarmuuden, läpimenoajan, jonotuksen, pullonkaulat ja hylkäysten Pareton valmistuneista tilauksista.", "LEAN", LEAN_FAQ)
    wr("lean.html", uusi_sivu(t, "lean", "LEAN-mittarit konepajalle: toimitusvarmuus ja läpimenoaika | Cinterim",
        "Cinterimin LEAN-lisämoduuli laskee konepajan toimitusvarmuuden, läpimenoajan, jonotuksen, pullonkaulat ja hylkäysten Pareton valmistuneista tilauksista.",
        "og-lean.png", lean_main, ld_lean))
    ld_h = ldjson("https://cinterim.fi/huolto", "Huoltojen hallinta", "Cinterimin huoltokirja kokoaa koneet, huoltokohteet, huoltovälit ja kuittaukset yhteen paikkaan.", "Huolto", HUOLTO_FAQ)
    wr("huolto.html", uusi_sivu(t, "huolto", "Koneiden huoltokirja ja huoltomuistutukset | Cinterim",
        "Cinterimin huoltokirja kokoaa asiakkaiden koneet, huoltokohteet, huoltovälit, muistutukset ja kuittaukset yhteen paikkaan. Huoltokirja kuuluu Pro-lisenssiin.",
        "og-huolto.png", huolto_main, ld_h))

    # tuotanto.html: uudet osiot + oikeat lisämoduulitiedot + otsikko/meta
    t = ersata(t, '<section class="section alt"><div class="container split"><div><span class="kicker">Poikkeamat</span>', TUOTANTO_LISA + '<section class="section alt" id="seisonta"><div class="container split"><div><span class="kicker">Poikkeamat</span>')
    a = t.index('<section class="section"><div class="container center"><span class="badge">Lisämoduuli</span><h2>Työaika ja kohdistusaste</h2>'); b = t.index("</section>", a) + len("</section>")
    t = t[:a] + LISAMODUULIT + t[b:]
    t = t.replace("Konepajan tuotannonohjaus: työlista ja kuormitus | Cinterim", "Konepajan tuotannonohjaus: työlista, kuormitus ja kate | Cinterim")
    t = t.replace('Konepajan kevyt tuotannonohjaus: työlista, työvaiheet, kuormitus, Kanban, seisonta ja ennustettu kate yhdistettynä tilauksen kustannusarvioon.',
                  'Konepajan kevyt tuotannonohjaus: työlista, tuotantotaulu, aamupalaveri, kuormitus, työaikakirjaukset, seisonta ja ennustettu kate.')
    lisat = "".join(',{"@type":"Offer","name":"%s","price":"%s","priceCurrency":"EUR"}' % (m["nimi"], m["hinta_kk"]) for m in _taso.LISAMODUULIT.values() if m.get("hinta_kk") is not None)
    t = ersata(t, '{"@type":"Offer","name":"Business","price":"99","priceCurrency":"EUR"}]', '{"@type":"Offer","name":"Business","price":"99","priceCurrency":"EUR"}' + lisat + ']')
    t = t.replace("Toimitusvarmuus ja Lean-mittarit</li>", 'Toimitusvarmuus ja <a href="/lean">Lean-mittarit</a></li>')
    wr("tuotanto.html", t)

    # index.html: lisämoduulikortti hinnoittelussa
    s = rd("index.html")
    vanha = "<p>Työlista, työaika, tuotannon Kanban, kuormitus, aamupalaveri, vaiheiden toteuma, Andon, seisonta ja Lean-mittarit.</p>"
    uusi = ('<p>Työlista, työaikakirjaukset, tuotantotaulu, aamupalaveri, kuormitus, vaiheiden toteuma, Andon, seisonta ja Kannattavuus nyt. <b>{{H:tyoaika}}</b> (alv 0 %). '
            '<a href="/lean">LEAN-mittarit</a>, koontinäyttö sekä <a href="/huolto">Huolto ja asennus</a> ovat omia lisämoduulejaan.</p>')
    s = ersata(s, vanha, uusi)
    wr("index.html", s)
    print("index.html lisämoduulikortti päivitetty")

    # navigaatio ja alatunniste kaikille sivuille: Lean + Huolto
    for f in sorted(W.glob("*.html")):
        s = f.read_text(encoding="utf-8")
        if f.name.startswith("google"): continue
        o = s
        s = s.replace('<li><a href="/tuotanto">Tuotanto</a></li>\n<li><a href="/jalkilaskenta">Jälkilaskenta</a></li>\n<li><a href="/tietoturva">Tietoturva</a></li>',
                      '<li><a href="/tuotanto">Tuotanto</a></li>\n<li><a href="/lean">LEAN</a></li>\n<li><a href="/huolto">Huollot</a></li>\n<li><a href="/jalkilaskenta">Jälkilaskenta</a></li>\n<li><a href="/tietoturva">Tietoturva</a></li>')
        s = s.replace('<li><a href="/tuotanto">Tuotanto</a></li><li><a href="/jalkilaskenta">Jälkilaskenta</a></li></ul>',
                      '<li><a href="/tuotanto">Tuotanto</a></li><li><a href="/lean">LEAN-mittarit</a></li><li><a href="/huolto">Huoltojen hallinta</a></li><li><a href="/jalkilaskenta">Jälkilaskenta</a></li></ul>')
        if s != o: f.write_text(s, encoding="utf-8", newline="\n")
    # ominaisuudet: linkit Lean/Huolto
    # sitemap, redirects, llms.txt
    sm = rd("sitemap.xml")
    lisa = "".join('  <url><loc>https://cinterim.fi/%s</loc><lastmod>%s</lastmod><changefreq>monthly</changefreq><priority>%s</priority></url>\n' % (p, PVM, pr) for p, pr in (("lean", "0.9"), ("huolto", "0.9")))
    sm = sm.replace("  <url><loc>https://cinterim.fi/jalkilaskenta</loc>", lisa + "  <url><loc>https://cinterim.fi/jalkilaskenta</loc>", 1)
    sm = sm.replace("https://cinterim.fi/tuotanto</loc><lastmod>2026-09-25", "https://cinterim.fi/tuotanto</loc><lastmod>" + PVM)
    wr("sitemap.xml", sm)
    rr = rd("_redirects")
    rr = rr.replace("/tuotanto.html        /tuotanto           301!\n", "/tuotanto.html        /tuotanto           301!\n/lean.html            /lean               301!\n/huolto.html          /huolto             301!\n", 1)
    rw = "/tuotanto                   /tuotanto.html                   200\n"
    assert rw in rr
    rr = rr.replace(rw, rw + "/lean                       /lean.html                       200\n/huolto                     /huolto.html                     200\n", 1)
    wr("_redirects", rr)
    ll = rd("llms.txt")
    ll = ll.replace("- [Tuotanto](https://cinterim.fi/tuotanto)", "- [Tuotanto](https://cinterim.fi/tuotanto)\n- [LEAN-mittarit](https://cinterim.fi/lean)\n- [Huoltojen hallinta](https://cinterim.fi/huolto)", 1)
    wr("llms.txt", ll)
    print("valmis")

if __name__ == "__main__":
    main()
