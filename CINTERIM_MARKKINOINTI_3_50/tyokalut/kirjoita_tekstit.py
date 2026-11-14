# -*- coding: utf-8 -*-
"""Kirjoittaa LinkedIn-yritysjulkaisut (linkedin/) ja henkilökohtaiset jakosaatteet (jakotekstit/) markdown-tiedostoiksi."""
import pathlib
P = pathlib.Path(__file__).resolve().parents[1]
U = "?utm_source=linkedin&utm_medium=social&utm_campaign=kannattavuus_kaytannossa&utm_content="

POSTS = [
("01_lean", "Koneet käyvät, mutta tilaukset eivät valmistu ajallaan. Miksi?", "Tuotanto → Lean-mittarit", "cinterim.fi/lean", "01_lean.png", "#Lean #Konepaja #Tuotanto #Toimitusvarmuus",
"""Koneet käyvät, mutta tilaukset eivät valmistu ajallaan. Miksi?

Korkea käyttöaste näyttää hyvältä. Se ei kuitenkaan kerro, saako asiakas tilauksensa sovittuna päivänä.

Tuotannon sujuvuutta kertovat muut mittarit:
• toimitusvarmuus: kuinka suuri osa valmistuneista tilauksista valmistui toimituspäivään mennessä
• läpimenoaika: kauanko tilaus on tuotannossa
• jonotus: kuinka kauan työ odottaa ennen seuraavaa vaihetta
• pullonkaulat ja hylkäysten syyt Pareto-järjestyksessä

Cinterimin Lean-mittarit laskevat nämä valmistuneista tilauksista ja kirjatuista työtunneista. Mukana ovat myös virtaustehokkuuden arvio, koneiden OEE-arvio ja Andon-tilastot. Luvut ovat arvioita, ja ohjelma varoittaa, jos otos on liian pieni.

Pitkä jonotus tarkoittaa, että työ odottaa eikä etene. Siihen kannattaa puuttua ennen kuin lisää koneaikaa ostetaan.

Lean-mittarit kuuluvat Cinterimin LEAN-lisämoduuliin. Tutustu: {L}"""),
("02_aamupalaveri", "Kuinka paljon aamupalaverista kuluu sen selvittämiseen, missä tuotannossa mennään?", "Tuotanto → Aamupalaveri", "cinterim.fi/tuotanto#aamupalaveri", "02_aamupalaveri.png", "#Tuotanto #Konepaja #Tuotannonohjaus #Johtaminen",
"""Kuinka paljon aamupalaverista kuluu sen selvittämiseen, missä tuotannossa mennään?

Hyvä aamupalaveri tukee päätöksiä. Huono palaveri kuluu tiedon etsimiseen eri taulukoista, viesteistä ja ihmisten muistista.

Cinterimin Aamupalaveri kokoaa yhdelle sivulle:
• myöhässä olevat tilaukset
• toimitukset seuraavan seitsemän päivän aikana
• esteet ja avoimet apukutsut
• käynnissä olevat työt
• edellisenä työpäivänä valmistuneet vaiheet ja hylätyt kappaleet

Maanantaina edellinen työpäivä on perjantai. Sivun voi tulostaa A4:lle, jossa on tilaa sovituille toimenpiteille.

Tiedot tulevat samoista kirjauksista, joita työpisteissä tehdään työn aikana. Mitään ei tarvitse kirjata erikseen palaveria varten.

Aamupalaveri kuuluu Cinterimin Tuotanto-lisämoduuliin (Työaika ja kohdistusaste). Lue lisää: {L}"""),
("03_tuotantotaulu", "Tilaus on työn alla. Mutta mitä se käytännössä tarkoittaa?", "Tuotanto → Taulu", "cinterim.fi/tuotanto#taulu", "03_tuotantotaulu.png", "#Tuotanto #Konepaja #Tuotannonohjaus #Kanban",
"""Tilaus on työn alla. Mutta mitä se käytännössä tarkoittaa?

Se voi tarkoittaa, että työ on käynnissä koneella. Se voi tarkoittaa myös, että työ odottaa materiaalia tai piirustusta. Päällepäin ne näyttävät samalta.

Cinterimin Tuotantotaulu näyttää tilausten työvaiheet neljässä sarakkeessa: avoin, kesken, este ja valmis.

• Kesken-tila syntyy, kun työntekijä aloittaa vaiheen työlistalla.
• Este-tila syntyy, kun työtä ei voi tehdä. Syy näkyy kortissa.
• Kortissa näkyvät työpiste, toimituspäivä ja jäljellä oleva työ.
• Punainen reuna kertoo, että toimituspäivä on ohi.

Taulu on näkymä, ei erillinen kirjauspaikka. Tila syntyy työlistan kirjauksista, joten tunnit ja tila pysyvät samassa totuudessa.

Tuotantotaulu kuuluu Cinterimin Tuotanto-lisämoduuliin. Lue lisää: {L}"""),
("04_tyoaikakirjaukset", "Paljonko yksi tuottava työtunti yrityksessä oikeasti maksaa?", "Tuotanto → Työlista ja Työaikaraportti", "cinterim.fi/tuotanto#tyoaika", "04_tyoaikaraportti.png", "#Kustannuslaskenta #Konepaja #Tuotanto #Jälkilaskenta",
"""Paljonko yksi tuottava työtunti yrityksessä oikeasti maksaa?

Maksettu työtunti ja asiakkaan tilaukselle kohdistunut tuottava työtunti eivät ole sama asia. Ero syntyy asetuksista, odotuksesta ja muusta yleisajasta.

Cinterimissä työntekijä kirjaa työn työpisteessä PIN-koodilla: aloitus, lopetus, valmistuneet kappaleet ja tarvittaessa este. Samat kirjaukset ovat jälkilaskennan työtunteja.

Työaikaraportti näyttää jaksolta:
• kirjatut tunnit henkilöittäin, kuormitusryhmittäin, vaiheittain tai tilauksittain
• tilaukselle kirjatun työn osuuden
• käyttöasteen ja vapaan kapasiteetin
• nelikentän käyttöasteesta ja tilaustyön osuudesta

Kohdistusaste ja €/tuottava tunti syntyvät, kun kirjattuja tunteja verrataan maksettuihin tunteihin ja kirjanpidon kustannuksiin. Tulokseen vaikuttaa se, miten kustannukset on jaettu resursseille.

Työaikakirjaukset kuuluvat Cinterimin Tuotanto-lisämoduuliin. Lue lisää: {L}"""),
("05_huollot", "Milloin kone huollettiin viimeksi – ja mistä tieto löytyy?", "Asiakkaat → Huollot", "cinterim.fi/huolto", "05_huollot.png", "#Huolto #Kunnossapito #Konepaja #Huoltokirja",
"""Milloin kone huollettiin viimeksi – ja mistä tieto löytyy?

Jos vastaus on "kysy huoltomieheltä", huoltohistoria on yhden ihmisen muistin varassa. Silloin tieto katoaa lomien, vuoronvaihdon tai eläköitymisen mukana.

Cinterimin Huollot-osiossa kullekin kohteelle kirjataan huoltoväli ja seuraava huolto. Koneelle voi liittää huoltokohteita. Huoltokirjaan syntyy historia, kun huolto kuitataan tehdyksi.

• huoltokohteet ja koneet asiakaskohtaisesti
• seuraava huolto näkyy listassa, erääntynyt huolto punaisella
• Dashboardin kortti ja Huollot-välilehti näyttävät erääntyvät huollot
• kuittaus ja historia kohteittain
• arkistointi ja palautus, kun kohde poistuu käytöstä

Huoltokirja kuuluu Cinterimin Pro-lisenssiin. Erillinen Huolto ja asennus -lisämoduuli tuo lisäksi työmääräimet, aikataulun ja asentajan puhelinnäkymän.

Lue lisää: {L}"""),
("06_seisonta", "Kone seisoo tunnin. Paljonko se maksaa?", "Tuotanto → Seisonta", "cinterim.fi/tuotanto#seisonta", "06_seisonta.png", "#Tuotanto #Konepaja #Seisonta #Lean",
"""Kone seisoo tunnin. Paljonko se maksaa?

Ensin pitää tietää, kuinka usein koneet seisovat ja miksi. Ilman syytä seisonta on vain tunne, että "taas jotain odotettiin".

Cinterimissä seisonta kirjataan syykoodilla työlistalla, koneen kioskilla tai jälkikäteen käsin: konevika, asetus, materiaali puuttuu, odottaa työtä, ohjelmaa tai työkalua, laatuongelma, henkilöstö tai muu.

Yhteenvedosta näkee syyt, resurssit ja avoimet seisonnat. Euroarvio on seisonnan tunnit kerrottuna resurssin €/h. Se on kirjattu resurssikustannus, ei yrityksen todellinen menetys. Seisonnan aikana kate ei välttämättä olisi syntynyt.

Andon-apukutsulla työpiste hälyttää työnjohdon paikalle. Tilastosta näkee syyt ja kuittausnopeuden.

Seisonta ja Andon kuuluvat Cinterimin Tuotanto-lisämoduuliin. Lue lisää: {L}"""),
("07_kuormitus", "Kalenteri on täynnä töitä. Mutta onko tuotanto oikeasti täynnä?", "Tuotanto → Kuormitus", "cinterim.fi/tuotanto#kuormitus", "07_kuormitus.png", "#Kapasiteetti #Tuotannonohjaus #Konepaja #Tuotanto",
"""Kalenteri on täynnä töitä. Mutta onko tuotanto oikeasti täynnä?

Kokonaiskuormitus voi näyttää kohtuulliselta, vaikka yksi kone on ruuhkassa ja toinen seisoo vajaana. Silloin tilausta ei kannata luvata pelkän summan perusteella.

Cinterimin Kuormitus-näkymä jakaa jäljellä olevan työn viikoille toimitukseen asti ja näyttää sen resursseittain:
• viikkolämpökartta: vihreä alle 85 %, keltainen yli 85 %, punainen yli 100 %
• kokonaiskaavio ja resurssikohtainen kaavio
• lomat ja poissaolot pienentävät kapasiteettia
• vapaa kapasiteetti seuraaville viikoille ja ruuhkaisin resurssi

Näkymä ei ole aikataulutus. Se on arvio siitä, milloin kuorma nousee, ja se perustuu tilausten suunniteltuihin tunteihin.

Kuormitus kuuluu Cinterimin Tuotanto-lisämoduuliin. Lue lisää: {L}"""),
("08_kannattavuus", "Miksi työn kannattavuus selvitetään usein vasta sen valmistuttua?", "Tuotanto → Kannattavuus nyt", "cinterim.fi/tuotanto#kannattavuus", "08_kannattavuus_nyt.png", "#Kannattavuus #Kustannuslaskenta #Konepaja #Jälkilaskenta",
"""Miksi työn kannattavuus selvitetään usein vasta sen valmistuttua?

Silloin tieto tulee liian myöhään vaikuttamaan mihinkään. Tilaus on toimitettu, lasku lähtenyt ja seuraava tarjous jo laadittu samoilla oletuksilla.

Cinterim jäädyttää tilauksen arvion, kun tarjous muuttuu tilaukseksi: työ, kone, materiaalit ja odotettu kate. Sitä verrataan toteutuneisiin työvaiheisiin ja tunteihin, kun työ etenee.

Kannattavuus nyt -kortti näyttää:
• ennustetun katteen ja eron arvioon
• arvioidun valmiusasteen
• huomiota vaativat työt liikennevalolla
• luottamuksen: kun tietoa on vähän, ohjelma ei ekstrapoloi vaan näyttää vain jo kirjatun ylityksen

Luvut ovat arvioita. Ne kertovat suunnan ajoissa, ei tarkkaa lopputulosta. Vaiheiden toteuma kertoo, missä arvio ja todellisuus erosivat.

Kannattavuus nyt kuuluu Cinterimin Tuotanto-lisämoduuliin. Lue lisää: {L}"""),
]

JAKO = {
"01_lean": """Kone voi olla koko ajan käynnissä ja asiakas silti odottaa tilaustaan. Käyttöaste kertoo koneesta, toimitusvarmuus kertoo asiakkaasta.

Lähes 15 vuotta valmistavassa teollisuudessa yrittäjänä ja myöhemmin tuotannon johtajana on opettanut katsomaan molempia. Cinterimin Lean-mittarit auttavat siinä. Yritysjulkaisu aiheesta alla.""",
"02_aamupalaveri": """Aamupalaverin arvo on päätöksissä, ei tilannekuvan keräämisessä. Jos ensimmäiset minuutit menevät sen selvittämiseen, missä mennään, tieto on väärässä paikassa.

Siksi Cinterimiin tehtiin yksi sivu: myöhässä olevat, tulevat toimitukset ja esteet. Lisää yritysjulkaisussa.""",
"03_tuotantotaulu": """"Työn alla" on tuotannossa yllättävän epämääräinen tila. Se voi olla käynnissä, odottaa materiaalia tai seistä jonossa.

Siksi Cinterimin tuotantotaulussa tilat on eroteltu: avoin, kesken, este ja valmis. Katso yritysjulkaisu.""",
"04_tyoaikakirjaukset": """Maksettu tunti ei ole sama asia kuin myytävä tunti. Ero on siinä, kuinka suuri osa työajasta päätyy asiakkaan tilaukselle.

Tuo luku tarvitaan sekä tarjouksen hinnoitteluun että jälkilaskentaan. Cinterimissä sen pohjana ovat työpisteiden kirjaukset. Lisää yritysjulkaisussa.""",
"05_huollot": """Huoltohistorian pitäminen yhden ihmisen muistissa toimii vain niin kauan kuin hän on paikalla.

Cinterimin huoltokirjassa kone, huoltoväli ja kuittaukset ovat yhdessä paikassa. Lisää yritysjulkaisussa.""",
"06_seisonta": """Seisonnasta puhutaan tuotannossa helposti tunteella. Kun syy kirjataan joka kerta, keskustelu muuttuu faktoiksi: mikä seisoo, miksi ja kuinka usein.

Euroarvion kanssa kannattaa olla tarkka. Cinterim kertoo suoraan, että se on resurssikustannus eikä menetetty kate. Katso yritysjulkaisu.""",
"07_kuormitus": """Tilauksen lupaaminen pelkän kokonaiskuorman perusteella on riski. Ratkaisevaa on, onko kapasiteettia juuri sillä koneella tai työvaiheessa, jota tilaus tarvitsee.

Cinterimin kuormitusnäkymä näyttää molemmat. Lisää yritysjulkaisussa.""",
"08_kannattavuus": """Jälkilaskenta kertoo, mitä tapahtui. Se on hyödyllistä, mutta usein myöhäistä.

Siksi Cinterimiin tehtiin näkymä, joka vertaa arviota toteumaan jo työn aikana ja kertoo myös, kuinka paljon lukuun voi luottaa. Yritysjulkaisu aiheesta alla.""",
}


EXTRA = {
"01_lean": "Aloita kolmesta luvusta: kuinka moni tilaus valmistui ajallaan, kauanko tilaus oli tuotannossa ja missä vaiheessa se odotti pisimpään. Ne kertovat enemmän kuin yksittäinen käyttöasteprosentti.",
"02_aamupalaveri": "Näin palaverin aika jää siihen, mitä tehdään: kuka siirtyy minnekin, mikä tilaus priorisoidaan ja mitä esteelle tehdään tänään.",
"03_tuotantotaulu": "Rajaa taulu yhteen työpisteeseen, niin jokainen näkee oman jononsa. Kortista pääsee suoraan tilauksen vaiheisiin.",
"04_tyoaikakirjaukset": "Näin tarjouksen tuntihinta voidaan peilata siihen, mitä tuottava tunti on todellisuudessa maksanut, eikä pelkkään arvioon.",
"05_huollot": "Muistutus ei korvaa huoltoa, mutta se estää unohtamasta sen. Ja kun joku kysyy, mitä koneelle on tehty, vastaus löytyy historiasta.",
"06_seisonta": "Kun syyt on kirjattu, voi katsoa mikä syy toistuu. Silloin korjaus kohdistuu oikeaan paikkaan, ei arvaukseen.",
"07_kuormitus": "Jos ruuhka on yhdellä koneella, ratkaisu on usein toinen kuin silloin, kun koko tuotanto on täynnä. Siksi molemmat näkymät ovat rinnakkain.",
"08_kannattavuus": "Jos poikkeama näkyy kolmantena työpäivänä eikä kolmantena viikkona, hintaan, aikatauluun tai asiakkaaseen ehtii vielä reagoida.",
}
JAKO_EXTRA = {
"01_lean": "Mittarit ovat arvioita, mutta ne osoittavat oikeaan suuntaan.",
"02_aamupalaveri": "Tulosta sivu, ja palaverissa on heti pohja sovituille toimenpiteille.",
"03_tuotantotaulu": "Näkymä päivittyy työlistan kirjauksista, joten kenenkään ei tarvitse päivittää sitä erikseen.",
"04_tyoaikakirjaukset": "Luvut ovat todellisia vain, jos kirjaukset tehdään työpisteessä helposti. Siksi työlista toimii puhelimella ja tabletilla.",
"05_huollot": "Pelkkä muistutus ei huoltoa tee, mutta se estää unohtamasta. Ja kun joku kysyy, mitä koneelle on tehty, vastaus löytyy historiasta eikä kenenkään päästä.",
"06_seisonta": "Kerro ensin syy, sitten vasta euroarvio. Toinen ilman toista johtaa harhaan.",
"07_kuormitus": "Näkymä ei aikatauluta, mutta se kertoo, milloin kannattaa miettiä toimituspäivää uudelleen ja missä kapasiteettia vielä on, ennen kuin uusi tilaus luvataan.",
"08_kannattavuus": "Ei kymmenien raporttien selaamista, vaan yksi kortti, jossa huomiota vaativat työt ovat ylimpänä.",
}

for n, otsikko, polku, url, kuva, tagit, teksti in POSTS:
    base = url.split("#")
    full = "https://" + base[0] + U + n + ("#" + base[1] if len(base) > 1 else "")
    i = teksti.rfind('\n\n')
    teksti = teksti[:i] + '\n\n' + EXTRA[n] + teksti[i:]
    t = teksti.replace("{L}", full)
    (P / "linkedin" / (n + ".md")).write_text(
        "# Julkaisu %s: %s\n\n**Kanava:** C.Interimin yrityssivu\n**Kuva:** `kuvat/%s` (alt-teksti: Cinterim-ohjelman näkymä %s, esimerkkiaineisto)\n"
        "**Laskeutumissivu:** %s\n**Sanamäärä:** noin %d\n\n---\n\n%s\n\n%s\n" % (n[:2], otsikko, kuva, polku, full, len(t.split()), t, tagit), encoding="utf-8")
    j = JAKO[n] + '\n\n' + JAKO_EXTRA[n]
    (P / "jakotekstit" / (n + ".md")).write_text(
        "# Jakosaate %s: %s\n\nJulkaistaan omassa profiilissa, kun jaat C.Interimin yritysjulkaisun. **Sanamäärä:** noin %d\n\n---\n\n%s\n" % (n[:2], otsikko, len(j.split()), j), encoding="utf-8")
    print(n, len(t.split()), len(j.split()))
