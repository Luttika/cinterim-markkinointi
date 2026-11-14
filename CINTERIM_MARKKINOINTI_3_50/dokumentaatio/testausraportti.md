# Testausraportti

Ajettu 9.10.2026 hiekkalaatikkodemolla (Mallikonepaja, keksitty data) ja paikallisella staattisella palvelimella.

## Tehty ja läpäisty
- **Faktantarkistus:** tekstit tarkistettu `ohjeet/tuotanto.md`, `ohjeet/huoltokirja.md`, `taso.py` ja toimintopuun (3.50.0, uusi PDF dokumentaatiossa) perusteella. Kuvissa ja teksteissä ei ole asiakastuloksia tai parannusprosentteja.
- **Kuvat:** kahdeksan kuvaa tehty oikean ohjelman (3.50.0) kaappauksista, katsottu silmin. Seisonta-, aamupalaveri-, taulu-, kuormitus-, lean-, kannattavuus-, raportti- ja huoltonäkymä toimivat ilman JS-virheitä.
- **Linkit:** kaikki sisäiset href/src/srcset-viittaukset kaikilla html-sivuilla tarkistettu. Ainoa "puuttuva" on `/lataa/Cinterim_Asennus.exe`, joka on tarkoituksella gitignoressa ja tulee deployssa erikseen.
- **Metatiedot** (8 sivua): title, description, canonical, og:image ja JSON-LD jäsentyvät; yksi H1 per sivu; ei otsikkotason hyppyjä; ei kuvia ilman alt-tekstiä; ei rikkinäisiä kuvia; ei JS-virheitä. Uusien sivujen kuvaukset 152 ja 157 merkkiä, tuotanto 130.
- **Responsiivisuus:** ei vaakavieritystä leveyksillä 375, 768 ja 1280 px (8 sivua). Mobiilinäkymä katsottu kuvakaappauksesta.
- **Julkaisun esitarkistus:** `tarkista_ennen_julkaisua.py website`: OK (217 tiedostoa).

## Ei tehty / puutteet
- **PageSpeed Insights ei mitattu** (vaatii julkaistun sivun tai erillisen mittauksen). Uudet kuvat ovat webp-muodossa ja lazy-loadattuja, mutta lukuja ei väitetä.
- **Lomakkeita ja latauspainikkeita ei testattu** (Netlify Forms toimii vain deployssa; lomakekoodiin ei koskettu).
- **LinkedIn Post Inspector / Open Graph livenä** testattavissa vasta julkaisun jälkeen.
- **Ohjelman testisarjoja ei ajettu**, koska ohjelmakoodia ei muutettu.
- **Havainto (ei korjattu, ei kuulu tähän työhön):** Tuotanto → Vaiheiden toteuma -näkymässä poikkeama ja h/kpl näkyvät merkinnällä "€ %" ja yksikkö €:na tunneille. Tämän vuoksi kuvaa ei käytetty julkaisuissa. Korjattu erillisessä PR:ssä `claude/vaiheanalyysi-yksikot` (fmtL + regressiotesti, savu 219/219).
- LEAN- ja Koontinäyttö-moduulien Stripe-hintoja ei ole luotu (hinnat päätetty, myynti käsin).
