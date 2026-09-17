class Lentokone:
    def __init__(self, id, btmax, btnyky):
        self.id = id
        self.btmax = btmax
        self.btnyky = btnyky

    def tankkaa(self):
        print(f"Lentokone {self.id} tankattu onnistuneesti. Bensaa tankattiin {self.btmax - self.btnyky} litraa.")
        self.btnyky = self.btmax

    def tulosta_tiedot(self):
        print("Lentokoneen tunnus: {self.id}\nLentokoneen bensan nykyinen taso: {self.btmax}\nLentokoneeseen mahtuvan bensan maksimimäärä: {self.btnyky}")




valinta = input("Anna komento:\n1) Luo uusi lentokone\n2) Tankkaa lentokone\n3) Tulosta koneen tiedot\n0) Lopeta ohjelma")

while valinta != 0:
    if input == 1:
        id = input("Anna koneen ID: ")
        btmax = int(input(("Anna koneen tankin koko: ")))
        btnyky = int(input(("Anna koneen tankin koko: ")))
        