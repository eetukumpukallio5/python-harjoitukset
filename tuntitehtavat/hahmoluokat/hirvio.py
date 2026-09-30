from .hahmo import Hahmo

class Hirvio(Hahmo):
    def __init__(self, nimi, hp, repliikki):
        self.repliikki = repliikki
        super().__init__(nimi, hp)

    def tulosta(self):
        super().tulosta_tiedot()
        print(f"{self.nimi} sanoo: {self.repliikki}")