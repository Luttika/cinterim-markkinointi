# Materiaalien käyttöohje

## Kansiot
- `linkedin/` kahdeksan yritysjulkaisua (kopioi teksti suoraan, hashtagit viimeisellä rivillä, laskeutumislinkki UTM-merkittynä).
- `jakotekstit/` kahdeksan henkilökohtaista jakosaatetta samalla numeroinnilla.
- `kuvat/` kahdeksan 1200 × 1200 px kuvaa. Alakansio `raaka/` sisältää alkuperäiset ohjelmakaappaukset (ei julkaisuun).
- `tyokalut/` skriptit, joilla kaikki voidaan tuottaa uudelleen.

## Julkaisu LinkedInissä
1. Julkaise sivun nimissä `linkedin/NN_*.md`:n teksti ja liitä kuva `kuvat/`-kansiosta. Alt-teksti: tiedoston ylärivit.
2. Jaa julkaisu omassa profiilissasi ja liitä `jakotekstit/NN_*.md`:n teksti.
3. Tarkista ennen julkaisua, että kuvan teksti "Esimerkkiaineisto (testidata)" näkyy. Kuvissa ei ole oikeita asiakkaita, vaan Mallikonepaja-demon keksittyä dataa.

## Jakosaatteet
Jakosaatteet on kirjoitettu yleisellä tasolla. Ne eivät sisällä keksittyjä tapahtumia tai lukuja. Ainoa henkilökohtainen taustalause (julkaisu 1) perustuu antamaasi taustaan (lähes 15 vuotta yrittäjänä valmistavassa teollisuudessa, myöhemmin tuotannon johtajana). Lisää omat kokemuksesi omin sanoin, jos haluat, mutta vain todellisia.

## Verkkosivuston julkaisu (vasta hyväksynnän jälkeen)
1. Käytä työpuun `website/`-kansiota (koko sivusto on versionhallinnassa).
2. `python tarkista_ennen_julkaisua.py website`
3. `netlify deploy --prod` kuten aiemmin (`julkaise-cinterim.cmd`). 
4. Tarkista livenä: /lean, /huolto, /tuotanto, /sitemap.xml, jakokuvat (LinkedIn Post Inspector).

## Kuvien ja sivujen uusintatuotanto
Käynnistä demo hiekkalaatikkokantaan, aja seedit (`markkinointi/esimerkkikuvat_lahteet/`, `tyokalut/seed_huolto_mk.py`), sitten `kaappaa_nakymat.py`, `luo_julkaisukuvat.py`, `sivuston_kuvat.py`, `rakenna_sivusto.py` (puhtaalle `website/`-kansiolle).
