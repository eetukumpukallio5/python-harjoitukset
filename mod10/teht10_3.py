#Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys, joka käskee kaikki hissit pohjakerrokseen. 
#Jatka pääohjelmaa siten, että talossasi tulee palohälytys.

class Talo:
    def __init__(self, alakerros, ylakerros):
        self.hissit = []
        self.alakerros = alakerros
        self.ylakerros = ylakerros

    def lisaa_hissi(self, hissi):
        self.hissit.append(hissi)

    def aja_hissia(self, hissi, kerros):
        hissi.siirry_kerrokseen(kerros)

    def palohalytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alakerros)

class Hissi:
    def __init__(self, alakerros, ylakerros):
        self.alakerros = alakerros
        self.ylakerros = ylakerros
        self.kerros = alakerros

    def siirry_kerrokseen(self, maali):
        while self.kerros != maali:
            if self.kerros < maali:
                self.kerros_ylos()
            elif self.kerros > maali:
                self.kerros_alas()
        print(f"Kerros {maali} saavutettu.")
        
    def kerros_ylos(self):
        self.kerros += 1
        if self.kerros > self.ylakerros:
            self.kerros = self.ylakerros
        print(f"Hissin kerros on nyt {self.kerros}.")

    def kerros_alas(self):
        self.kerros -= 1
        if self.kerros < self.alakerros:
            self.kerros = self.alakerros
        print(f"Hissin kerros on nyt {self.kerros}.")

print("Tervetuloa hissiohjelmaan. Luodaan hissit uuteen taloon.")
yla = int(input("Anna talon ylin kerros: "))
ala = int(input("Anna talon alin kerros: "))
talo = Talo(ala, yla)
hissit = int(input("Montako hissiä luodaan taloon?"))
for hissi in range(hissit):
    hissi = Hissi(ala, yla)
    talo.lisaa_hissi(hissi)

komento = "0"
while komento != "3":
    komento = input("1) Aja hissiä\n2) Palohälytys\n3) Lopeta ohjelma")
    if komento == "1":
        hissi = int(input("Anna hissin numero:"))
        hissi -= 1
        kerros = int(input("Mihin kerrokseen siirrytään?"))
        talo.aja_hissia(talo.hissit[hissi], kerros)
    if komento == "2":
        print("Palohälytys! Palohälytys! Kaikki hissit pohjakerrokseen!")
        talo.palohalytys()