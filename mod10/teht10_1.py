#Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron. 
#Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa. 
#Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen. 
#Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on. 
#Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.

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

print("Tervetuloa hissiohjelmaan. Luodaan uusi hissi.")
yla = int(input("Anna hissin ylin kerros: "))
ala = int(input("Anna hissin alin kerros: "))
hissi = Hissi(ala, yla)

hissi.kerros_ylos()
hissi.siirry_kerrokseen(6)
hissi.siirry_kerrokseen(hissi.alakerros)