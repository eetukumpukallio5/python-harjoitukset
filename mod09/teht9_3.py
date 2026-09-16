#Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän. 
#Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt. 
#Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h. 
#Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

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
        
            

auto1 = Auto("ABC-123", 142)
print(f"Rekisteritunnus {auto1.rekisteritunnus} nopeus {auto1.huippunopeus} tämänhetkinen nopeus {auto1.tamanhetkinen_nopeus} kuljettu matka {auto1.kuljettu_matka}")

auto1.kiihdyta(30)
auto1.kulje(0.5)
print(f"Auton nopeus nyt: {auto1.tamanhetkinen_nopeus} Matka nyt: {auto1.kuljettu_matka}")
auto1.kiihdyta(70)
auto1.kulje(1)
print(f"Auton nopeus nyt: {auto1.tamanhetkinen_nopeus} Matka nyt: {auto1.kuljettu_matka}")
auto1.kiihdyta(50)
auto1.kulje(0.25)
print(f"Auton nopeus nyt: {auto1.tamanhetkinen_nopeus} Matka nyt: {auto1.kuljettu_matka}")
auto1.kiihdyta(-200)
auto1.kulje(2)
print(f"Auton nopeus nyt: {auto1.tamanhetkinen_nopeus} Matka nyt: {auto1.kuljettu_matka}")