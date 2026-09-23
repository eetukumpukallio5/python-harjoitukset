#Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto. 
#Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina. 
#Polttomoottoriauton ominaisuutena on bensatankin koko litroina. 
#Kirjoita aliluokille alustajat. 
#Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin. 
#Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa. 
#Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l). 
#Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.

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

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akku_kapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akku_kapasiteetti = akku_kapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, polttoaine_kapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.polttoaine_kapasiteetti = polttoaine_kapasiteetti

sahko = Sahkoauto("ABC-15", 180, 52.5)
poltto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahko.kiihdyta(int(input("Anna sähköautolle nopeus: ")))
poltto.kiihdyta(int(input("Anna polttomoottoriautolle nopeus: ")))

sahko.kulje(3)
poltto.kulje(3)

print(f"Auton {sahko.rekisteritunnus} kuljettu matka on {sahko.kuljettu_matka}")
print(f"Auton {poltto.rekisteritunnus} kuljettu matka on {poltto.kuljettu_matka}")