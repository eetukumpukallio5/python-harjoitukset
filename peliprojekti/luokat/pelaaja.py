from .esine import Esine

class Pelaaja:
    def __init__(self, nimi, inventaario, x, y):
        self.nimi = nimi
        self.inventaario = inventaario
        self.x = x
        self.y = y
        self.sijainti = str(x) + str(y)
        self.raha = 0
        #pelajaan tiedot. missä pelaaja on, tavaraluettelo, raha ja nimi

    def tulosta_inventaario(self):
        if len(self.inventaario) == 0:
            print(f"Sinulla ei ole yhtään esinettä.\nRahaa sinulla on {self.raha} euroa.")
        else:
            print("Alla on tavaraluettelosi:")
            for tavara in self.inventaario:
                print(tavara.nimi)
            print(f"Rahaa sinulla on {self.raha} euroa.")

    def liiku(self, suunta):
        pass

    def keraa_esine(self, esine):
        self.inventaario.append(esine)
        print(esine.hanki)