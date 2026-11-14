# Muutosraportti: Cinterim 3.50.0 markkinointipäivitys

Pohja: main e3c8569 (versio 3.50.0 + kuormitusryhmä P2/P3 + moduuliaktivointi). Haara `claude/markkinointi-3-50` (työpuu `AI-mk`), ei pushattu. Ohjelman toiminnallisuutta ei muutettu.

## Uudet sivut
- `/lean` (`lean.html`): LEAN-mittarit konepajalle: 7 mittaria, mistä luvut tulevat, rajaukset, lisenssi, UKK (FAQPage-JSON-LD).
- `/huolto` (`huolto.html`): huoltojen hallinta: huoltokirja (Pro), Huolto ja asennus -lisämoduuli (59 €/kk, 590 €/v), UKK.
- OG-kuvat `og-lean.png`, `og-huolto.png`.

## Päivitetyt sivut
- `tuotanto.html`: uusi osio "Päivittäinen johtaminen" (ankkurit #aamupalaveri, #taulu, #tyoaika, #kuormitus, #kannattavuus, uudet kuvat), uusi lisämoduulit-osio (Tuotanto 59/590, LEAN, Huolto ja asennus 59/590, Koontinäyttö), title/description, JSON-LD-tarjous.
- `index.html`: lisämoduulikortin teksti ja hinta (Lean ei enää kuulu Työaika-moduuliin, koska se on nykyään oma LEAN-moduulinsa).
- Navigaatio ja alatunniste kaikilla sivuilla: LEAN ja Huollot.
- `sitemap.xml` (+/lean, /huolto, tuotanto lastmod), `_redirects` (siistit URLit + .html-ohjaukset), `llms.txt`.
- Uudet kuvat `esimerkkikuvat/30–36_*` (ohjelman 3.50.0 -näkymät, esimerkkiaineisto, webp 480/800/1200/1600).

## Päätökset ja huomiot
1. **Lisämoduulirakenne.** Toimintopuun PDF listaa Lean-mittarit Tuotanto-moduulin alle, mutta `taso.py` ja ohjeet erottavat LEANin omaksi lisämoduulikseen (vaatii Tuotanto-moduulin). Sivusto seuraa koodia. Toimintopuun generaattori on korjattu vastaamaan tätä (PR `claude/vaiheanalyysi-yksikot`); dokumentaation PDF on uusi versio.
2. **Hinnat.** Julkaistu: Free 0, Starter 19, Pro 49, Business 99 €/kk, Tuotanto-lisämoduuli 59 €/kk tai 590 €/v (alv 0 %). Huolto ja asennus 59/590 (`taso.py`): hinta vahvistettu käyttäjältä 9.10. LEAN 29 €/kk tai 290 €/v ja Koontinäyttö 19 €/kk tai 190 €/v (päätetty 9.10., vaativat Tuotanto-moduulin). **Hinnat eivät ole kovakoodattuja:** ne luetaan `taso.py`:n `LISAMODUULIT`-tiedoista (sivuston rakennusskripti, ohjekirjasto, toimintopuu ja sovelluksen lukkoviesti). Hinnanmuutos = muuta `taso.py` ja aja `rakenna_sivusto.py`, `rakenna_ohjeet.py` ja `tee_toimintopuu.py` uudelleen. Stripe-hintoja LEANille ja Koontinäytölle ei ole vielä luotu (toimitus käsin).
3. **Huolto.** Esitelty omana kokonaisuutenaan: huoltokirja kuuluu Pro-tasoon, lisämoduuli vain työmääräimiin, aikatauluun ja asentajan puhelinnäkymään.
4. **Kaizen/5S/FPY/WIP/trendit** ovat vielä kesken toisessa haarassa (`claude/lean-kaizen`), eikä niitä ole mainittu missään. Kun ne mergataan, lisää ne /lean-sivulle ja toimintopuuhun.
5. **Ei muutettu:** lomakkeet, latauspainikkeet, oppaat (vain nav/alatunniste), ohjelmakoodi.

## Julkaisuhuomio (viesti toiselta sessiolta 9.10.)
Mainissa ja tuotannossa on Huolto ja asennus -moduuli, Kaizen ja 5S, mutta **asentajanäkymän offline-jono ja valokuvat eivät ole vielä asiakaspaketeissa**. Sivustolta on siksi jätetty pois maininnat offline-jonosta ja kuvista /huolto-sivulla. Ennen Netlify-deployta varmista, että julkaistavat ominaisuudet ovat asiakkaiden saatavilla (paketit ja version.json), ja lisää maininnat vasta sitten. Kaizen-lista, 5S, FPY, WIP ja trendit on lisätty /lean-sivulle ja toimintopuuhun (LEAN-moduuli).
