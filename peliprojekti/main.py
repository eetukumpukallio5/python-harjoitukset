#funktiot on funktiot paketissa. tuodaan ne
from funktiot import juo_vetta, katso_lista, lisaa_listaan, rakenna
from luokat import Esine, Huone, Pelaaja

#luodaan esineet
lompakko = Esine("lompakko", "Otit lompakon pöydältä mukaasi. Lompakossa on 30 euroa, hienoa!")
ampari = Esine("ämpäri", "Poimit ämpärin. Tällä voisi ehkä kuljettaa vettä joesta...")

#luodaan huoneet
huone1111 = Huone(1111, "Olet makuuhuoneessasi. Huoneen kiinnostavin asia lienee sänky, mutta sinua ei väsytä. Pohjoisessa on olohuoneesi.")
huone1112 = Huone(1112, "Olet olohuoneessasi. Pöydällä on lompakkosi. Sinun kannattanee ottaa se mukaan. Idässä on autotallisi ja etelässä makuuhuoneesi.", [lompakko])
huone1212 = Huone(1212, "Olet autotallissasi. Upea pakettiautosi on täällä. Lattialla on myös ämpäri. Lännessä on olohuoneesi.", [ampari])

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

print(pelaaja.sijainti)
huone = pelaaja.sijainti
print(huone.intro)

#yksinkertainen silmukka päävalikolle
while komento != "lopeta":
    komento = input("Valitse ja syötä komento.\n1) Lisää esine inventaarioon\n2) Katso inventaarion sisältö\n3) Juo vettä (tarvitsee vesipullon)\n4) Rakenna tornia (tarvitsee tiilin)\nlopeta) Sammuta ohjelma\n")
    if komento == "1":
        lisaa_listaan(inventaario)
    elif komento == "2":
        katso_lista(inventaario)
    elif komento == "3":
        juo_vetta(inventaario)
    elif komento == "4":
        if "tiili" in inventaario:
            kerrokset = kerrokset + 1
        rakenna(inventaario, kerrokset)
    elif komento != "lopeta":
        print("Virheellinen komento!")