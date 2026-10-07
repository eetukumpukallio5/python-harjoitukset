#tuodaan luokat niiden paketista
from luokat import Esine, Huone, Pelaaja, Auto
import sys
import json

#luodaan esineet
lompakko = Esine("lompakko", "Otit lompakon pöydältä mukaasi. Lompakossa on 30 euroa, hienoa!")
ampari = Esine("ämpäri", "Poimit ämpärin. Tällä voisi ehkä kuljettaa vettä joesta...")
onki = Esine("onki", "")
kala = Esine("kala", "Sait kalan!")

esineet = [lompakko, ampari, onki, kala]

#luodaan huoneet ja lisätään ne listaan
huone1111 = Huone("1111", "Olet makuuhuoneessasi. Huoneen kiinnostavin asia lienee sänky, mutta sinua ei väsytä. Pohjoisessa on olohuoneesi.", "Olet makuuhuoneessasi. Huoneen kiinnostavin asia lienee sänky, mutta sinua ei väsytä. Pohjoisessa on olohuoneesi.")
huone1112 = Huone("1112", "Olet olohuoneessasi. Pöydällä on lompakkosi. Sinun kannattanee ottaa se mukaan. Pohjoisessa on autotie, idässä autotallisi ja etelässä makuuhuoneesi.", "Olet olohuoneessasi. Vielä ei ole aika levätä sohvalla. Pohjoisessa on autotie, idässä autotallisi ja etelässä makuuhuoneesi.", [lompakko])
huone1113 = Huone("1113", "Olet talosi ulkopuolella. Taloja lukuunottamatta täällä ei ole paljon nähtävää. Pohjoisessa on maatila ja etelässä talosi.", "Olet talosi ulkopuolella. Taloja lukuunottamatta täällä ei ole paljon nähtävää. Pohjoisessa on maatila ja etelässä talosi.")
huone1114 = Huone("1114", "Olet maatilalla. Tehtäväsi on hankkia tänne vettä. Sinulla on vielä töitä tämän suhteen. Etelässä on autotie.", "Olet maatilalla. Tehtäväsi on hankkia tänne vettä. Sinulla on vielä töitä tämän suhteen. Etelässä on autotie.")
huone1212 = Huone("1212", "Olet autotallissasi. Upea pakettiautosi on täällä. Lattialla on myös ämpäri. Lännessä on olohuoneesi.", "Olet autotallissasi. Upea pakettiautosi on täällä. Lännessä on olohuoneesi.", [ampari])
huone2111 = Huone("2111", "Olet lähikaupan parkkipaikalla. Täällä on jonkin verran ihmisiä ostoksilla ja tankilla. Pakusi on täällä. Pohjoisessa on lähikaupan sisäänkäynti.", "Olet lähikaupan parkkipaikalla. Täällä on jonkin verran ihmisiä ostoksilla ja tankilla. Pakusi on täällä. Pohjoisessa on lähikaupan sisäänkäynti.")
huone2112 = Huone("2112", "Olet kaupan sisällä. Onget on asetettu esille tarjoushintaan 25€. Kyltin mukaan tänne voi myydä kalaa. Tankin saa täyteen hinnalla 40€. Etelässä on parkkipaikka.", "Olet kaupan sisällä. Onget on asetettu esille tarjoushintaan 25€. Kyltin mukaan tänne voi myydä kalaa. Tankin saa täyteen hinnalla 40€. Etelässä on parkkipaikka.", [], {"onki": {"nimi": "onki", "hinta": 25, "saa_teksti": "Maksoit 25€ ongesta. Aika mennä kalastamaan!", "ei_saa_teksti": "Sinulla ei ole varaa onkeen."}, "kala": {"nimi": "kala", "hinta": 0, "saa_teksti": "Myyt kalan. Saat kalasta 25€!", "ei_saa_teksti": "Sinulla ei ole kalaa jota voisit myydä."}, "diesel": {"nimi": "diesel", "hinta": 40, "saa_teksti": "Täytät tankkisi dieselillä.", "ei_saa_teksti": "Sinulla ei ole tankkaukseen riittävästi rahaa."}})

huoneet = [huone1111, huone1112, huone1113, huone1114, huone1212, huone2111, huone2112]
paku_huoneet = {huone1212: 0, huone2111: 3} #huoneet joissa paku on. jokaisella huoneella lukuarvo. käytetään laskemaan ajomatkoihin tarvittavat dieselit

#otetaan tarvittavat muuttujat käyttäjältä, ja alustetaan komento muuttuja sekä inventaario.
komento = "n/a"
nimi = input("Anna nimesi.\n")
while True:
    ika =  input("Anna ikäsi.\n")
    try:
        ika = float(ika)
    except ValueError:
        print("Iän täytyy olla numero.")
        continue
    break

#tarkistetaan ikä, ja jos alle 12 while loopin argumentti epäonnistuu ja päättää ohjelman
if ika >= 12:
    print(f"Tervetuloa, {nimi}!")
else:
    print("Sinun täytyy olla vähintään 12-vuotias pelataksesi.")
    sys.exit() #lopettaa suoraan ohjelman.

#peliä edeltävä päävalikko. voidaan aloittaa uusi peli, ladata aiempi sessio, tulostaa ohjeet tai esittely ja päättää ohjelma
while True:
    komento = input("Valitse ja syötä komento.\n1) Aloita uusi peli\n2) Lataa tallennettu peli\n3) Lue pelin esittely\n4) Lue pelin ohjeet\n5) Sammuta ohjelma\n")
    if komento == "1":
        print("Uusi peli alkaa. Onnea tehtävääsi.")
        pelaaja = Pelaaja(nimi, 0, [], 11, 11) #luodaan pelaaja. x y koordinaatit vastaavat ensimmäistä huonetta pelissä, pelaajan makuuhuonetta
        auto = Auto(70)
        akt_huone = huone1111
        break

    elif komento == "2":
        try:
            with open("peliprojekti/tekstitallenteet/tallennus.json", "r") as tiedosto:
                data = json.load(tiedosto) #ladataan json tiedostosta sanakirja jossa data. täytetään näillä arvoilla oliot ja muuttujat
        except FileNotFoundError:
            print("Tallennusta ei löydy. Aloita uusi peli tai yritä uudelleen.")
            continue
        except IOError:
            print("Tallennusten käsittelyssä tapahtui virhe. Aloita uusi peli tai yritä uudelleen.")
            continue
        pelaaja = Pelaaja(nimi, data["raha"], [], data["x"], data["y"])
        for tall_esine in data["inventaario"]: #tallennuksessa on vain esineiden nimet. jos nimi vastaa ohjelman oliota, lisätään se tavaraluetteloon
            for esine in esineet:
                if tall_esine == esine.nimi:
                    pelaaja.inventaario.append(esine)
        auto = Auto(data["tankki"])
        for huone in huoneet:
            if huone.koordinaatit == data["sijainti"]:
                akt_huone = huone
        huone1112.esineet = []
        for tall_esine in data["1112"]:
            for esine in esineet:
                if tall_esine == esine.nimi:
                    huone1112.esineet.append(esine)
        huone1212.esineet = []
        for tall_esine in data["1212"]:
            for esine in esineet:
                if tall_esine == esine.nimi:
                    huone1212.esineet.append(esine)
        print("Lataus onnistui! Peli jatkuu...")
        break

    elif komento == "3":
        with open("peliprojekti/tekstitallenteet/intro.txt", "r", encoding="utf-8") as tiedosto:
            data = tiedosto.read()
            print(data)

    elif komento == "4":
        with open("peliprojekti/tekstitallenteet/ohjeet.txt", "r", encoding="utf-8") as tiedosto:
            data = tiedosto.read()
            print(data)

    elif komento == "5":
        sys.exit()

    else:
        print("Virheellinen komento!")

#päävalikon silmukka
while komento != "lopeta":
    akt_huone.esittely()
    komento = input("Valitse ja syötä komento.\n1) Poimi\n2) Liiku\n3) Katso tavaraluettelon sisältö\n4) Osta/Myy/Anna\nx) Aja\nlopeta) Tallenna ja sammuta ohjelma\n")
    if komento == "1":
        nosto = (input("Mitä tahdot poimia? ")).lower()
        loytyiko = False #tarkistetaan lista yksi esine kerrallaan. jos löytyy, muokkaamme listoja ja tulostaminen vaikuttuu
        for esine in akt_huone.esineet:
            if esine.nimi == nosto:
                loytyiko = True
                pelaaja.keraa_esine(esine)
                akt_huone.poista_esine(esine)
        if loytyiko:
            pass
        else:
            print("Esinettä ei löytynyt yrityksestä huolimatta.")

    elif komento == "2":
        suunta = (input("Mihin suuntaan liikutaan? (p, e, l, i) ")).lower()
        if suunta == "p" or suunta == "e" or suunta == "l" or suunta == "i":
            alku_x, alku_y = pelaaja.x, pelaaja.y
            pelaaja.liiku(suunta)
            print(pelaaja.sijainti)
            validi_huone = False #tarkistetaan onko uudet koordinaatit luodussa huoneessa vertaamalla koordinaatteja. jos on, vaihdetaan aktiivista huonetta. muutoin palautetaan koordinaatit alkuperäisiin
            for huone in huoneet:
                if huone.koordinaatit == pelaaja.sijainti:
                    validi_huone = True
                    akt_huone = huone
            if validi_huone:
                print("Sirryt uuteen tilaan...")
            else:
                print("Virheellinen ilmansuunta.")
                pelaaja.sijainti = akt_huone.koordinaatit
                pelaaja.x, pelaaja.y = alku_x, alku_y #palauttaa pelaajan alkuperäiset x y koordinaatit joilla lasketaan sisäisesti koordinaatit
        else:
            print("Virheellinen ilmansuunta.")
        print(pelaaja.sijainti)

    elif komento == "3":
        pelaaja.tulosta_inventaario()

    elif komento == "4":
        tuote = (input("Mitä haluat ostaa/myydä/antaa? ")).lower()
        for esine in esineet:
            if esine.nimi == tuote:
                tuote_esine = esine
        if tuote in akt_huone.kauppa: #kala diesel onki
            if pelaaja.raha >= akt_huone.kauppa[tuote]["hinta"]:
                if tuote == "kala": #rajatapaukset käsitellään. 
                    if kala in pelaaja.inventaario:
                        pelaaja.poista_esine(kala)
                        print(akt_huone.kauppa[tuote]["saa_teksti"])
                        continue
                    else:
                        print(akt_huone.kauppa[tuote]["ei_saa_teksti"])
                        continue
                if tuote == "diesel":
                    pelaaja.raha -= akt_huone.kauppa[tuote]["hinta"]
                    print(akt_huone.kauppa[tuote]["saa_teksti"])
                    auto.tankki = 70
                pelaaja.raha -= akt_huone.kauppa[tuote]["hinta"]
                print(akt_huone.kauppa[tuote]["saa_teksti"])
                pelaaja.inventaario.append(tuote_esine)
            else:
                print(akt_huone.kauppa[tuote]["ei_saa_teksti"])
        else:
            print("Vikasyöttö.")
    elif komento != "lopeta":
        print("Virheellinen komento!")

else: #jos lopetetaan ja tallennetaan, päästään tähän ja tallennetaan tarvitut tiedot tiedostoon
    listapelaaja = [] #ottaa nimet olioiden listojen esineistä, ja tallentaa ne listoihin
    for esine in pelaaja.inventaario:
        listapelaaja.append(esine.nimi)
    lista1112 = []
    for esine in huone1112.esineet:
        lista1112.append(esine.nimi)
    lista1212 = []
    for esine in huone1212.esineet:
        lista1212.append(esine.nimi)
    tallennus_data = {
        "x": pelaaja.x,
        "y": pelaaja.y,
        "sijainti": pelaaja.sijainti,
        "raha": pelaaja.raha,
        "inventaario": listapelaaja,
        "tankki": auto.tankki,
        "1112": lista1112,
        "1212": lista1212
    }
    print(tallennus_data)
    with open("peliprojekti/tekstitallenteet/tallennus.json", "w") as tiedosto:
        json.dump(tallennus_data, tiedosto)