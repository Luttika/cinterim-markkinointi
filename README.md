# Cinterim – markkinointiaineisto

Markkinointikuvat ja -tekstit, jotka siirrettiin pois ohjelman repostä (`Luttika/Cinterin`) 14.11.2026, jotta ohjelman repo
sisältää vain ohjelman, sivuston ja niiden työkalut.

| Kansio | Sisältö |
|---|---|
| `Linkedin kuvat/` | LinkedIn-kuvat, karusellit (PDF), bannerit ja yrityssivun logo |
| `CINTERIM_MARKKINOINTI_3_50/kuvat/` | Version 3.50 julkaisukuvat (`raaka/` = alkuperäiset kuvakaappaukset) |
| `CINTERIM_MARKKINOINTI_3_50/linkedin/`, `jakotekstit/` | Julkaisutekstit |
| `CINTERIM_MARKKINOINTI_3_50/dokumentaatio/` | Julkaisukalenteri, ohjeet, QA-kuvat ja -raportit |
| `CINTERIM_MARKKINOINTI_3_50/tyokalut/` | Kampanjan työkalut (kuvakaappaukset, julkaisukuvat, og-kuvat, sivuston QA) |

## Työkalut
`tyokalut/`-skriptit on tehty ajettaviksi Cinterin-repon juuresta (ne lukevat ja kirjoittavat polkuja kuten
`website/esimerkkikuvat` ja `CINTERIM_MARKKINOINTI_3_50/kuvat/raaka`). Jos ajat niitä uudelleen, kopioi
`CINTERIM_MARKKINOINTI_3_50/` hetkeksi Cinterin-repon juureen, aja skripti siellä, ja tuo muuttuneet kuvat takaisin tänne.
Älä commitoi kansiota Cinterin-repoon.

Tarjouslaskennan Excel-pohjan rakentaja (`rakenna_excel_pohja.py`) jäi Cinterin-repoon kansioon `tyokalut/`, koska se tuottaa
sivuston ladattavan tiedoston ja savutesti tarkistaa sen.

Huom: tiedostot ovat edelleen Cinterin-repon historiassa; tämä siirto ei pienennä sen kokoa.
