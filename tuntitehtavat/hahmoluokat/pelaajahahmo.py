from .hahmo import Hahmo

class Pelaajahahmo(Hahmo):
    def __init__(self, nimi, hp, inventaario):
        self.inventaario = inventaario
        super().__init__(nimi, hp)

    def tulosta(self):
        super().tulosta_tiedot()
        print(f"Sankarimme tavaraluettelo: {self.inventaario}")