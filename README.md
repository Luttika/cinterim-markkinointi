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
| `Mainokset/Tehtaan mies/` | LinkedIn-mainos "Tehtaan mies – tehtaan työkalu": neljä versiota (oma kuva + historiallinen valokuva), mainoskuvat 1:1, 4:5, 1.91:1 ja yrityssivun banneri, UTM-linkit ja kuvien lähde- ja lisenssitiedot |
| `Esimerkkikuvat_raaka/` | Ohjelman kuvakaappausten raakaversiot (demodata) |

## Työkalut
`tyokalut/`-skriptit on tehty ajettaviksi Cinterin-repon juuresta (ne lukevat ja kirjoittavat polkuja kuten
`website/esimerkkikuvat` ja `CINTERIM_MARKKINOINTI_3_50/kuvat/raaka`). Jos ajat niitä uudelleen, kopioi
`CINTERIM_MARKKINOINTI_3_50/` hetkeksi Cinterin-repon juureen, aja skripti siellä, ja tuo muuttuneet kuvat takaisin tänne.
Älä commitoi kansiota Cinterin-repoon.

Tarjouslaskennan Excel-pohjan rakentaja (`rakenna_excel_pohja.py`) jäi Cinterin-repoon kansioon `tyokalut/`, koska se tuottaa
sivuston ladattavan tiedoston ja savutesti tarkistaa sen.

Huom: tiedostot ovat edelleen Cinterin-repon historiassa; tämä siirto ei pienennä sen kokoa.

## Kuvien lisenssit ja lähdemerkinnät
Mainosten historialliset valokuvat ovat Vapriikin kuva-arkiston (Tampereen historialliset museot) kuvia, lisenssi **CC BY 4.0**. Lähdemerkintä on pakollinen kaikissa käytöissä, myös julkaisun tekstissä: *Kuva: Vapriikin kuva-arkisto / valokuvaaja, CC BY 4.0*. Valokuvaaja, otsikko ja lähde on kirjattu kunkin mainoskansion `KUVAN_LAHDE_JA_LISENSSI.txt`-tiedostoon. Kuvia on muokattu (rajattu, seepia, liitetty mainoskuvaan), mikä CC BY 4.0 sallii.

Vapriikin käyttöehtojen mukaan tunnistettavien henkilökuvien käyttö markkinoinnissa vaatii kuvassa olevan suostumuksen. Versiot `mainos_tehtaan_mies_vapriikki` (veturi) ja `mainos_tehtaan_mies_ihmiseton_halli` (ei ihmisiä) eivät sisällä tunnistettavia henkilöitä. Versiossa `mainos_tehtaan_mies_konepajahalli` hallissa on kaukana pieniä työntekijöitä; mainoskoossa kasvot eivät erotu, mutta varmista Vapriikilta (kuva-arkisto@tampere.fi) ennen maksettua käyttöä. Mainosten mies on tekijän oma kuva.
