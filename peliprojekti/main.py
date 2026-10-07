#tuodaan luokat niiden paketista
from luokat import Esine, Huone, Pelaaja, Auto
import sys
import json

#luodaan esineet
lompakko = Esine("lompakko", "Otit lompakon pöydältä mukaasi. Lompakossa on 30 euroa, hienoa!")
ampari = Esine("ämpäri", "Poimit ämpärin. Tällä voisi ehkä kuljettaa vettä joesta...")
onki = Esine("onki", "")
kala = Esine("kala", "Sait kalan!")
mustikka = Esine("mustikka", "Poimit mustikoita. Sait niitä litran!")
puolukka = Esine("puolukka", "Poimit puolukoita. Sait niitä litran!")
lakka = Esine("lakka", "Poimit lakkaa. Sait sitä litran!")
vesi = Esine("vesi", "Poimit ämpäriisi vettä.")
tynnyri = Esine("tynnyri", "Mies ottaa marjasi. Hän on tyytyväinen niihin! Saat ison tynnyrin vettä vaihdossa.")
vesipumppu = Esine("vesipumppu", "")

esineet = [lompakko, ampari, onki, kala, mustikka, puolukka, lakka, vesi, tynnyri, vesipumppu]

#luodaan huoneet ja lisätään ne listaan
huone1111 = Huone("1111", "Olet makuuhuoneessasi. Huoneen kiinnostavin asia lienee sänky, mutta sinua ei väsytä. Pohjoisessa on olohuoneesi.", "Olet makuuhuoneessasi. Huoneen kiinnostavin asia lienee sänky, mutta sinua ei väsytä. Pohjoisessa on olohuoneesi.")
huone1112 = Huone("1112", "Olet olohuoneessasi. Pöydällä on lompakkosi. Sinun kannattanee ottaa se mukaan. Pohjoisessa on autotie, idässä autotallisi ja etelässä makuuhuoneesi.", "Olet olohuoneessasi. Vielä ei ole aika levätä sohvalla. Pohjoisessa on autotie, idässä autotallisi ja etelässä makuuhuoneesi.", [lompakko])
huone1113 = Huone("1113", "Olet talosi ulkopuolella. Taloja lukuunottamatta täällä ei ole paljon nähtävää. Pohjoisessa on maatila ja etelässä talosi.", "Olet talosi ulkopuolella. Taloja lukuunottamatta täällä ei ole paljon nähtävää. Pohjoisessa on maatila ja etelässä talosi.")
huone1114 = Huone("1114", "Olet maatilalla. Tehtäväsi on hankkia tänne vettä. Sinulla on vielä töitä tämän suhteen. Etelässä on autotie.", "Olet maatilalla. Tehtäväsi on hankkia tänne vettä. Sinulla on vielä töitä tämän suhteen. Etelässä on autotie.", [], ["vesi", "tynnyri", "vesipumppu"])
huone1212 = Huone("1212", "Olet autotallissasi. Upea pakettiautosi on täällä. Lattialla on myös ämpäri. Lännessä on olohuoneesi.", "Olet autotallissasi. Upea pakettiautosi on täällä. Lännessä on olohuoneesi.", [ampari])

huone2111 = Huone("2111", "Olet lähikaupan parkkipaikalla. Täällä on jonkin verran ihmisiä ostoksilla ja tankilla. Pakusi on täällä. Pohjoisessa on lähikaupan sisäänkäynti.", "Olet lähikaupan parkkipaikalla. Täällä on jonkin verran ihmisiä ostoksilla ja tankilla. Pakusi on täällä. Pohjoisessa on lähikaupan sisäänkäynti.")
huone2112 = Huone("2112", "Olet kaupan sisällä. Onget on asetettu esille tarjoushintaan 25€. Kyltin mukaan tänne voi myydä kalaa. Tankin saa täyteen hinnalla 40€. Etelässä on parkkipaikka.", "Olet kaupan sisällä. Onget on asetettu esille tarjoushintaan 25€. Kyltin mukaan tänne voi myydä kalaa. Tankin saa täyteen hinnalla 40€. Etelässä on parkkipaikka.", [], {"onki": {"nimi": "onki", "hinta": 25, "saa_teksti": "Maksoit 25€ ongesta. Aika mennä kalastamaan!", "ei_saa_teksti": "Sinulla ei ole varaa onkeen."}, "kala": {"nimi": "kala", "hinta": 0, "saa_teksti": "Myyt kalan. Saat kalasta 25€!", "ei_saa_teksti": "Sinulla ei ole kalaa jota voisit myydä."}, "diesel": {"nimi": "diesel", "hinta": 40, "saa_teksti": "Täytät tankkisi dieselillä.", "ei_saa_teksti": "Sinulla ei ole tankkaukseen riittävästi rahaa."}})

huone3112 = Huone("3112", "Olet metsässä. Puut ovat tiheästi asetteilla. Polku jatkuu pohjoiseen syvemmälle metsään. Idässä on metsän sisäänkäynti.", "Olet metsässä. Puut ovat tiheästi asetteilla. Polku jatkuu pohjoiseen syvemmälle metsään. Idässä on metsän sisäänkäynti.")
huone3113 = Huone("3113", "Olet metsässä. Kiviä on täällä paljon. Voit mennä pohjoiseen tai etelään polkua.", "Olet metsässä. Kiviä on täällä paljon. Voit mennä pohjoiseen tai etelään polkua.")
huone3114 = Huone("3114", "Olet metsässä. Tien varrella on puskia mustikoita. Idässä näkyy mökki. Polku vie myös etelään.", "Olet metsässä. Idässä näkyy mökki. Polku vie myös etelään.", [mustikka])
huone3211 = Huone("3211", "Olet metsän ulkopuolisella kentällä. Kenties täältä löytyy keino hankkia vettä. Pakusi on täällä. Pohjoisessa on metsän sisäänkäynti.", "Olet metsän ulkopuolisella kentällä. Kenties täältä löytyy keino hankkia vettä. Pohjoisessa on metsän sisäänkäynti.")
huone3212 = Huone("3212", "Olet metsän sisäänkäynnillä. Metsä haarautuu tästä. Läntinen polku vie syvemmälle metsään, idästä kuuluu veden juoksua ja etelässä on parkkipaikka.", "Olet metsän sisäänkäynnillä. Metsä haarautuu tästä. Läntinen polku vie syvemmälle metsään, idästä kuuluu veden juoksua ja etelässä on parkkipaikka.")
huone3214 = Huone("3214", "Olet mökissä. Täällä asustaa mies. Hän tarjoaa sinulle tynnyrillistä vettä, jos tuot hänelle kolme litraa marjoja. Metsä jatkuu länteen ja itään.", "Olet mökissä. Mies on kiitollinen marjoista. Metsä jatkuu länteen ja itään.", ["."], ["marjat"]) #tavaraluettelo sisältää yhden alkion. jos pelaaja saa tynnyrin, lista tyhjenee ja samalla myös huoneen intro.
huone3312 = Huone("3312", "Olet metsässä. Täällä on joki. Joessa näkyy kaloja. Pohjoisessa on lisää metsää ja lännessä on metsän sisäänkäynti.", "Olet metsässä. Täällä on joki. Joessa näkyy kaloja. Pohjoisessa on lisää metsää ja lännessä on metsän sisäänkäynti.", [kala, vesi])
huone3313 = Huone("3313", "Olet metsässä. Tien varrella on puskia puolukoita. Voit mennä pohjoiseen tai etelään polkua.", "Olet metsässä. Voit mennä pohjoiseen tai etelään polkua.", [puolukka])
huone3314 = Huone("3314", "Olet metsässä. Tie haarautuu kaikkiin suuntiin. Voit jatkaa pohjoiseen, länteen, itään tai etelään.", "Olet metsässä. Tie haarautuu kaikkiin suuntiin. Voit jatkaa pohjoiseen, länteen, itään tai etelään.")
huone3315 = Huone("3315", "Olet metsässä. Tie ei jatku tästä, mutta näköalat täältä ovat upeat. Voit jatkaa polkua etelään.", "Olet metsässä. Tie ei jatku tästä, mutta näköalat täältä ovat upeat. Voit jatkaa polkua etelään.")
huone3414 = Huone("3414", "Olet metsässä. Tien varrella on puskia lakkaa. Voit mennä länteen polkua.", "Olet metsässä. Voit mennä länteen polkua.", [lakka])

huone4111 = Huone("4111", "Olet huoltoasemalla. Saat tankattua pakusi hintaan 40€. Pohjoisessa on katu.", "Olet huoltoasemalla. Saat tankattua pakusi hintaan 40€. Pohjoisessa on katu.", [], {"diesel": {"nimi": "diesel", "hinta": 40, "saa_teksti": "Täytät tankkisi dieselillä.", "ei_saa_teksti": "Sinulla ei ole tankkaukseen riittävästi rahaa."}})
huone4112 = Huone("4112", "Olet kaupungissa. Lähelläsi on rautakauppa. Pakusi on täällä. Pohjoisessa on rautakauppa ja etelässä huoltoasema.", "Olet kaupungissa. Lähelläsi on rautakauppa. Pakusi on täällä. Pohjoisessa on rautakauppa ja etelässä huoltoasema.")
huone4113 = Huone("4113", "Olet rautakaupassa. Vesipumpun saa ostettua hinnalla 100€. Etelessä on katu.", "Olet rautakaupassa. Vesipumpun saa ostettua hinnalla 100€. Etelessä on katu.", [], {"vesipumppu": {"nimi": "vesipumppu", "hinta": 100, "saa_teksti": "Maksoit 100€ vesipumpusta. Tällä riittää vettä erittäin pitkäksi aikaa!", "ei_saa_teksti": "Sinulla ei ole varaa vesipumppuun."}})

huoneet = [huone1111, huone1112, huone1113, huone1114, huone1212, huone2111, huone2112, huone3112, huone3113, huone3114, huone3211, huone3212, huone3214, huone3312, huone3313, huone3314, huone3315, huone3414, huone4111, huone4112, huone4113]
paku_huoneet = {huone1212: {1: 0, 2: 3, 3: 10, 4: 30}, huone2111: {1: 3, 2: 0, 3: 7, 4: 27}, huone3211: {1: 10, 2: 7, 3: 0, 4: 20}, huone4112: {1: 30, 2: 27, 3: 20, 4: 0}} #huoneet joissa paku on. jokaisella huoneella sanakirjassa etäisyys dieselin kulussa toisiin pakuhuoneisiin
aja_uusi_huone = {1: {"huone": huone1212, "x": 12, "y": 12}, 2: {"huone": huone2111, "x": 21, "y": 11}, 3: {"huone": huone3211, "x": 32, "y": 11}, 4: {"huone": huone4112, "x": 41, "y": 12}} #pakulla ajaessa syötteen perusteella asetetaan uusi huone pelaajalle

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
        auto = Auto(20)
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
        huone3114.esineet = []
        for tall_esine in data["3114"]:
            for esine in esineet:
                if tall_esine == esine.nimi:
                    huone3114.esineet.append(esine)
        huone3313.esineet = []
        for tall_esine in data["3313"]:
            for esine in esineet:
                if tall_esine == esine.nimi:
                    huone3313.esineet.append(esine)
        huone3414.esineet = []
        for tall_esine in data["3414"]:
            for esine in esineet:
                if tall_esine == esine.nimi:
                    huone3414.esineet.append(esine)
        huone3214.esineet = []
        for alkio in data["3214"]:
            huone3214.esineet.append(alkio)
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
    komento = input("Valitse ja syötä komento.\n1) Poimi\n2) Liiku\n3) Katso tavaraluettelon sisältö\n4) Osta/Myy/Anna\n5) Aja\nlopeta) Tallenna ja sammuta ohjelma\n")
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

    elif komento == "3":
        pelaaja.tulosta_inventaario()

    elif komento == "4":
        tuote = (input("Mitä haluat ostaa/myydä/antaa? ")).lower()
        if akt_huone == huone1114: #tulostetaan esineen mukaan lopputekstit
            if tuote == "vesi":
                if vesi in pelaaja.inventaario:
                    with open("peliprojekti/tekstitallenteet/loppu1.txt", "r", encoding="utf-8") as tiedosto:
                        data = tiedosto.read()
                        print(data)
                        sys.exit()
                continue
            elif tuote == "tynnyri":
                if tynnyri in pelaaja.inventaario:
                    with open("peliprojekti/tekstitallenteet/loppu2.txt", "r", encoding="utf-8") as tiedosto:
                        data = tiedosto.read()
                        print(data)
                        sys.exit()
                continue
            elif tuote == "vesipumppu":
                if vesipumppu in pelaaja.inventaario:
                    with open("peliprojekti/tekstitallenteet/loppu3.txt", "r", encoding="utf-8") as tiedosto:
                        data = tiedosto.read()
                        print(data)
                        sys.exit()
                continue
            else:
                print("Vikasyöttö.")
                continue
        for esine in esineet:
            if esine.nimi == tuote:
                tuote_esine = esine
        if tuote in akt_huone.kauppa: #alku kaikilla, vähitään tsekataan onko syöte listan sisällä. tästä haarautuu eteenpäin
            if tuote == "marjat":
                if mustikka in pelaaja.inventaario and puolukka in pelaaja.inventaario and lakka in pelaaja.inventaario:
                    pelaaja.keraa_esine(tynnyri)
                    huone3214.esineet.clear()
                    pelaaja.poista_esine(mustikka)
                    pelaaja.poista_esine(puolukka)
                    pelaaja.poista_esine(lakka)
                    continue
                else:
                    print("Sinulla ei ole tarpeeksi marjoja.")
                    continue
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
                    continue
                pelaaja.raha -= akt_huone.kauppa[tuote]["hinta"]
                print(akt_huone.kauppa[tuote]["saa_teksti"])
                pelaaja.inventaario.append(tuote_esine)
            else:
                print(akt_huone.kauppa[tuote]["ei_saa_teksti"])
        else:
            print("Vikasyöttö.")

    elif komento == "5":
        if akt_huone in paku_huoneet:
            maali = input(f"Pakussasi on {auto.tankki} litraa dieseliä jäljellä. Mihin tahdot ajaa?\n1) Koti ja maantila ({paku_huoneet[akt_huone][1]} litraa)\n2) Lähikauppa ({paku_huoneet[akt_huone][2]} litraa)\n3) Metsä ({paku_huoneet[akt_huone][3]} litraa)\n4) Kaupunki ({paku_huoneet[akt_huone][4]} litraa)\n")
            try:
                maali = int(maali)
            except ValueError:
                print("Syötteen täytyy olla numero.")
                continue
            if maali > 4:
                print("Syöte ei listalla.")
                continue
            if auto.tankki < paku_huoneet[akt_huone][maali]:
                print("Autossasi ei ole riittävästi dieseliä.")
                continue
            print("Ajetaan...")
            auto.tankki -= paku_huoneet[akt_huone][maali]
            akt_huone = aja_uusi_huone[maali]["huone"]
            pelaaja.saavu(aja_uusi_huone[maali]["x"], aja_uusi_huone[maali]["y"])
        else:
            print("Pakettiautosi ei ole täällä, täten et voi ajaa mihinkään.")
    
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
    lista3114 = []
    for esine in huone3114.esineet:
        lista3114.append(esine.nimi)
    lista3313 = []
    for esine in huone3313.esineet:
        lista3313.append(esine.nimi)
    lista3414 = []
    for esine in huone3414.esineet:
        lista3414.append(esine.nimi)
    lista3214 = huone3214.esineet #3214 ainoastaan tallentaa onko tynnyri otettu, ei tarvitse säätöä olioiden kanssa
    tallennus_data = {
        "x": pelaaja.x,
        "y": pelaaja.y,
        "sijainti": pelaaja.sijainti,
        "raha": pelaaja.raha,
        "inventaario": listapelaaja,
        "tankki": auto.tankki,
        "1112": lista1112,
        "1212": lista1212,
        "3114": lista3114,
        "3313": lista3313,
        "3414": lista3414,
        "3214": lista3214
    }
    with open("peliprojekti/tekstitallenteet/tallennus.json", "w") as tiedosto:
        json.dump(tallennus_data, tiedosto)