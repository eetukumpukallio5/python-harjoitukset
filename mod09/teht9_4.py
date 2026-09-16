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
#tallennetaan autojen tiedot olioihin 1-10, ja lisätään ne kaikki sanakirjaan. 
#siirrytään silmukkaan, jossa kaikki autot kiihtyvät satunnaisen määrän -10 - 15 välillä. toistetaan silmukkaa kunnes yksi autoista saavuttaa 10000 km.
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

autot = []

for i in range(1, 11):
    "auto{i}" = Auto(f"ABC-{i}", random.randint(100, 200))

print(autot)
    
    
