#Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi. 
#Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta. 
#Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. 
#Rekisteritunnus luodaan seuraavasti “ABC-1”, “ABC-2” jne. 
#Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

#Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä. Tämä tehdään kutsumalla kiihdytä-metodia.
#Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
#Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä. 
#Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.


#käytetään ohjelmassa tehtävän 9_3 auto luokkaa. arvotaan for loopilla kymmenelle autolle satunnainen huippunopeus 100-200 km/h.
#tallennetaan autojen tiedot listan paikkoihin 1-10, joita voidaan verrata tarvittaessa
#siirrytään silmukkaan, jossa kaikki autot kiihtyvät satunnaisen määrän -10 - 15 välillä. siirrytään sitten 1 tunnin verran.
#tulostetaan 3 tunnin välein johtaja ja jäljellä oleva matka, lisää hieman vuorovaikutteisuutta
#toistetaan silmukkaa kunnes yksi autoista saavuttaa 10000 km.
#tulostetaan autot kuljettujen matkojen mukaan.

import random

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



autot = ["auto1", "auto2", "auto3", "auto4", "auto5", "auto6", "auto7", "auto8", "auto9", "auto10"]
tunti = 0
karkimatka = 0


for i in range(10):
    autot[i] = Auto(f"ABC-{i + 1}", random.randint(100, 200))

print("Kilpa-ajot alkakoot!")

while karkimatka < 10000:
    karkimatka = 0
    for i in range(10):
        autot[i].kiihdyta(random.randint(-10, 15))
        autot[i].kulje(1)
        if autot[i].kuljettu_matka >= karkimatka:
            karkimatka = autot[i].kuljettu_matka
            pisin = autot[i]
    tunti += 1
    if tunti % 3 == 0:
        print(f"Tunteja on kulunut {tunti}! Kärjessä on auto {(pisin).rekisteritunnus}. Vielä {10000 - karkimatka} kilometria maaliin!")
        input("paina enter jatkaaksesi...")
else:
    lopputulos = []
    for i in range(10):
        