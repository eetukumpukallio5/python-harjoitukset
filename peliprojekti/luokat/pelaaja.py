from .esine import Esine

class Pelaaja:
    def __init__(self, nimi, raha, inventaario, x, y):
        self.nimi = nimi
        self.inventaario = inventaario
        self.x = x
        self.y = y
        self.sijainti = str(self.x) + str(self.y)
        self.raha = raha
        #pelajaan tiedot. missä pelaaja on, tavaraluettelo, raha ja nimi

    def tulosta_inventaario(self):
        if len(self.inventaario) == 0:
            print(f"Sinulla ei ole yhtään esinettä.\nRahaa sinulla on {self.raha} euroa.")
        else:
            print("Sinulla on:")
            for tavara in self.inventaario:
                print(tavara.nimi)
            print(f"Rahaa sinulla on {self.raha} euroa.")

    def liiku(self, suunta):
        if suunta == "p":
            self.y += 1
        elif suunta == "e":
            self.y -= 1
        elif suunta == "i":
            self.x += 1
        else: #eli kun suunta on l
            self.x -= 1
        self.sijainti = str(self.x) + str(self.y) #päivittää uudet koordinaatit

    def keraa_esine(self, esine):
        self.inventaario.append(esine)
        print(esine.hanki)

        if esine.nimi == "lompakko":
            self.raha += 30

    def poista_esine(self, esine):
        self.inventaario.remove(esine)

        if esine.nimi == "kala":
            self.raha += 25