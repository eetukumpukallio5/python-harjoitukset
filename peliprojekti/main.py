#tuodaan luokat niiden paketista
from luokat import Esine, Huone, Pelaaja

#luodaan esineet
lompakko = Esine("lompakko", "Otit lompakon pöydältä mukaasi. Lompakossa on 30 euroa, hienoa!")
ampari = Esine("ämpäri", "Poimit ämpärin. Tällä voisi ehkä kuljettaa vettä joesta...")

#luodaan huoneet ja lisätään ne listaan
huone1111 = Huone("1111", "Olet makuuhuoneessasi. Huoneen kiinnostavin asia lienee sänky, mutta sinua ei väsytä. Pohjoisessa on olohuoneesi.")
huone1112 = Huone("1112", "Olet olohuoneessasi. Pöydällä on lompakkosi. Sinun kannattanee ottaa se mukaan. Idässä on autotallisi ja etelässä makuuhuoneesi.", [lompakko])
huone1212 = Huone("1212", "Olet autotallissasi. Upea pakettiautosi on täällä. Lattialla on myös ämpäri. Lännessä on olohuoneesi.", [ampari])
huoneet = [huone1111, huone1112, huone1212]

#otetaan tarvittavat muuttujat käyttäjältä, ja alustetaan komento muuttuja sekä inventaario.
komento = "n/a"
inventaario = []
kerrokset = 0
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
    komento = "lopeta"

#luodaan pelaaja. x y koordinaatit vastaavat ensimmäistä huonetta pelissä, pelaajan makuuhuonetta
#tilapäisesti staattinen. myöhemmin lisää pelin tallennus
x, y = 11, 11
pelaaja = Pelaaja(nimi, inventaario, x, y)
akt_huone = huone1111

#päävalikon silmukka
while komento != "lopeta":
    print(akt_huone.intro)
    komento = input("Valitse ja syötä komento.\n1) Poimi esine\n2) Liiku\n3) Katso tavaraluettelon sisältö\nlopeta) Sammuta ohjelma\n")
    if komento == "1":
        nosto = (input("Mitä tahdot poimia? ")).lower()
        loytyiko = False #tarkistetaan lista yksi esine kerrallaan. jos löytyy, muokkaamme listoja ja tulostaminen vaikuttuu
        for esine in akt_huone.esineet:
            if esine.nimi == nosto:
                print("kyl")
                loytyiko = True
                pelaaja.keraa_esine(esine)
                akt_huone.esineet.remove(esine)
        if loytyiko:
            pass
        else:
            print("Esinettä ei löytynyt yrityksestä huolimatta.")
    elif komento == "2": #tee vielä liike ennen palauttamista
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
    elif komento != "lopeta":
        print("Virheellinen komento!")