class Normi:
    def sano(self):
        print("Olen normi!")

class Uus(Normi):
    def sano(self):
        print("Olen uusi!")

normi = Normi()
uus = Uus()

normi.sano()
uus.sano()