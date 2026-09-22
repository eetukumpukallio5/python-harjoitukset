#Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. 
#Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun nimi, pituus kilometreinä ja osallistuvien autojen lista. 

#Luokassa on alustaja, joka saa parametreinaan nimen, kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:
#tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.
#tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
#kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.

#Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä “Suuri romuralli”. 
#Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä. 
#Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa tunti_kuluu-metodia, jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi. 
#Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt.

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):
        self.tamanhetkinen_nopeus += muutos
        if self.tamanhetkinen_nopeus < 0:
            self.tamanhetkinen_nopeus = 0
        elif self.tamanhetkinen_nopeus >= self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus

    def kulje(self, aika):
        self.kuljettu_matka += (aika * self.tamanhetkinen_nopeus)

class Kilpailu:
    tunti = 0

    def __init__(self, nimi, km, autot):
        self.nimi = nimi
        self.km = km
        self.autot = autot

    def tunti_kuluu(self):
        pass

    def tulosta_tilanne(self):
        pass

    def kilpailu_ohi(self):
        pass

import random

autot = []

for auto in range(10):
    auto = Auto(f"ABC-{auto + 1}", random.randint(100, 200))
    autot.append(auto)

kisa = Kilpailu("Suuri romuralli", 8000, autot)
input(f"{kisa.nimi} alkakoon! {kisa.km} kilometriä maaliin, paras kuski voittakoon!\n(paina enter) ")