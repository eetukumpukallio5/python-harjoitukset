'''
1. Lue koodi läpi, suorita se, varmista että ymmärrät, miten se toimii nyt.
2. Luo luokat Hirvio ja Pelaajahahmo. Ne molemmat perivät luokan Hahmo.
3. Muokkaa koodia niin, että lisäät Pelaajahahmo-luokalle ominaisuuden tavaralista. 
Kun pelaajahahmo-olio luodaan, se saa parametrinä listan tavaroita, jotka tallennetaan olion listaan.
4. Ylikirjoita Hahmo-luokan tulosta-metodi Pelaajahahmolle niin, että se tulostaa mukaan myös tavaralistan.
5. Muokkaa niin, että vain hirviöillä on repliikki, ei kaikilla Hahmo-olioilla.
6. Ylikirjoita Hirvio-luokan tulosta-metodi niin, että se tulostaa myös repliikin.
7. Jos ehdit: Luo peliin useampi hirviö, ja laita pelaajahahmo taistelemaan myös niiden kanssa. 
Taistelu-metodia ei tarvita sekä hahmolle että hirviölle. 
Siirrä se sille luokalle, jossa se on sinusta looginen. 
Testaa, että peli toimii järkevästi.
'''

class Hahmo:
    def __init__(self, nimi, hp):
        self.nimi = nimi        
        self.hp = hp

    def tulosta_tiedot(self):
        print(f"Hahmon nimi: {self.nimi}")
        print(f"Hahmon hp: {self.hp}")

    def taistelu(self, vastustaja):
        print("Tulee suuri taistelu.")
        input()
        if vastustaja.hp > self.hp:
            print(f"{self.nimi} hävisi taistelun :<")
            self.hp = 0
        else:
            print(f"{self.nimi} voitti taistelun!")
            self.tulosta_tiedot()

class Hirvio(Hahmo):
    def __init__(self, nimi, hp, repliikki):
        self.repliikki = repliikki
        super().__init__(nimi, hp)

    def tulosta(self):
        super().tulosta_tiedot()
        print(f"{self.nimi} sanoo: {self.repliikki}")

class Pelaajahahmo(Hahmo):
    def __init__(self, nimi, hp, inventaario):
        self.inventaario = inventaario
        super().__init__(nimi, hp)

    def tulosta(self):
        super().tulosta_tiedot()
        print(f"Sankarimme tavaraluettelo: {self.inventaario}")

inventaario = ["Miekka", "Kilpi", "Amuletti"]

merihirvio = Hirvio("Merihirviö", 80, "Lits läts, aion syödä sinut!")
pelaajahahmo = Pelaajahahmo(input("Anna hahmon nimi: "), 150, inventaario)

print("Peli alkaa.")
pelaajahahmo.tulosta()
input()

print(f"{pelaajahahmo.nimi} kohtaa ensimmäiseksi kauhean hirviön.")
merihirvio.tulosta()

input()
pelaajahahmo.taistelu(merihirvio)
input()
print(f"Peli ohi.")